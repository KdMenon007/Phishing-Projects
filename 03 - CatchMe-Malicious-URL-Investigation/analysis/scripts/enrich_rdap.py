import csv
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "analysis/working/domain-investigation.csv"
JSON_PATH = ROOT / "analysis/working/rdap-results.json"

session = requests.Session()
session.headers.update({"User-Agent": "CatchMe-SOC-Lab/1.0"})

with CSV_PATH.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

results = []

for row in rows:
    defanged = row["domain_defanged"]
    domain = defanged.replace("[.]", ".")
    item = {
        "domain_defanged": defanged,
        "queried_domain": domain,
        "lookup_utc": datetime.now(timezone.utc).isoformat(),
        "service": "https://rdap.org",
        "http_status": None,
        "domain_name": None,
        "status": [],
        "events": [],
        "error": None,
    }

    try:
        response = session.get(
            f"https://rdap.org/domain/{domain}",
            timeout=15,
            allow_redirects=True,
        )
        item["http_status"] = response.status_code
        item["service"] = response.url.split("/domain/")[0]

        if response.status_code == 200:
            data = response.json()
            item["domain_name"] = data.get("ldhName")
            item["status"] = data.get("status", [])
            item["events"] = [
                {
                    "action": event.get("eventAction"),
                    "date": event.get("eventDate"),
                }
                for event in data.get("events", [])
            ]
            row["registration_status"] = "RDAP record returned; see rdap-results.json"
            row["analyst_assessment"] = (
                "Feed-listed; RDAP metadata retrieved; maliciousness not established"
            )
        elif response.status_code == 404:
            row["registration_status"] = "RDAP returned 404; registration not established"
            row["analyst_assessment"] = (
                "Feed-listed; RDAP record not found at lookup time; further verification needed"
            )
        else:
            row["registration_status"] = f"RDAP HTTP {response.status_code}; inconclusive"
            row["analyst_assessment"] = "Feed-listed; registration status inconclusive"

    except (requests.RequestException, ValueError) as exc:
        item["error"] = f"{type(exc).__name__}: {exc}"
        row["registration_status"] = "Lookup failed; unknown"
        row["analyst_assessment"] = "Feed-listed; registration status unknown"

    results.append(item)
    print(
        f"{defanged}: HTTP {item['http_status']}"
        if item["http_status"] is not None
        else f"{defanged}: lookup failed"
    )
    time.sleep(0.5)

with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

JSON_PATH.write_text(
    json.dumps(
        {
            "generated_utc": datetime.now(timezone.utc).isoformat(),
            "lookup_type": "RDAP domain registration metadata",
            "caution": (
                "RDAP availability and registration metadata do not establish "
                "whether a domain is malicious. HTTP errors are not proof of non-registration."
            ),
            "results": results,
        },
        indent=2,
    ) + "\n",
    encoding="utf-8",
)

print("\nCSV SHA-256:", hashlib.sha256(CSV_PATH.read_bytes()).hexdigest())
print("JSON output:", JSON_PATH)
print("JSON SHA-256:", hashlib.sha256(JSON_PATH.read_bytes()).hexdigest())
