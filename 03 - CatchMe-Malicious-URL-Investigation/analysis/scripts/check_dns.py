import csv
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "analysis/working/domain-investigation.csv"
OUT_PATH = ROOT / "analysis/working/dns-results.json"

with CSV_PATH.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

results = []

for row in rows:
    defanged = row["domain_defanged"]
    domain = defanged.replace("[.]", ".")
    result = {
        "domain_defanged": defanged,
        "queried_domain": domain,
        "observed_utc": datetime.now(timezone.utc).isoformat(),
        "records": {},
        "errors": {},
    }

    for record_type in ("A", "AAAA", "MX"):
        try:
            proc = subprocess.run(
                ["dig", "+time=3", "+tries=1", "+short", domain, record_type],
                capture_output=True, text=True, timeout=5, check=False,
            )
            values = [
                line.strip() for line in proc.stdout.splitlines()
                if line.strip()
            ]
            result["records"][record_type] = values
            if proc.returncode != 0:
                result["errors"][record_type] = (
                    proc.stderr.strip() or f"dig exit code {proc.returncode}"
                )
        except (subprocess.TimeoutExpired, OSError) as exc:
            result["records"][record_type] = []
            result["errors"][record_type] = str(exc)

    answers = sum(len(v) for v in result["records"].values())
    result["summary"] = (
        "DNS answers returned" if answers
        else "No answers returned; status requires further interpretation"
    )
    results.append(result)

    print(f"\n{defanged}")
    for rtype, values in result["records"].items():
        print(f"  {rtype}: {', '.join(values) if values else 'No answer'}")
    for rtype, error in result["errors"].items():
        print(f"  {rtype} error: {error}")

OUT_PATH.write_text(
    json.dumps({
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "method": "dig queries using the system-configured resolver",
        "caution": (
            "DNS responses are time-sensitive. No answer does not prove "
            "that a domain is unregistered or benign."
        ),
        "results": results,
    }, indent=2) + "\n",
    encoding="utf-8",
)

print("\nJSON:", OUT_PATH)
print("SHA-256:", hashlib.sha256(OUT_PATH.read_bytes()).hexdigest())
