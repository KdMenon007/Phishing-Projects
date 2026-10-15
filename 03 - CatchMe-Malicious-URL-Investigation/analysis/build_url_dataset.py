#!/usr/bin/env python3
import csv
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

source = Path("analysis/raw/openphish-feed.txt")
output = Path("analysis/working/url-investigation-sample.csv")
summary_path = Path("analysis/working/feed-summary.json")
output.parent.mkdir(parents=True, exist_ok=True)

raw = source.read_bytes()
lines = [line.strip() for line in raw.decode("utf-8").splitlines()
         if line.strip()]

valid = []
seen = set()
invalid = 0

for entry in lines:
    try:
        u = urlsplit(entry)
        if u.scheme not in ("http", "https") or not u.hostname:
            invalid += 1
            continue
        if entry in seen:
            continue
        seen.add(entry)
        valid.append((entry, u))
    except ValueError:
        invalid += 1

def defang(url):
    return url.replace("https://", "hxxps://", 1).replace(
        "http://", "hxxp://", 1
    ).replace(".", "[.]")

rows = []
for i, (entry, u) in enumerate(valid[:10], 1):
    rows.append({
        "sample_id": f"OPH-{i:03d}",
        "url_defanged": defang(entry),
        "scheme": u.scheme,
        "hostname_defanged": u.hostname.replace(".", "[.]"),
        "path": u.path or "/",
        "query_present": str(bool(u.query)).lower(),
        "source": "OpenPhish community feed",
        "classification": "Feed-listed; not independently verified",
    })

with output.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

summary = {
    "source": "OpenPhish community feed",
    "retrieved_utc": datetime.now(timezone.utc).isoformat(),
    "feed_sha256": hashlib.sha256(raw).hexdigest(),
    "nonempty_lines": len(lines),
    "valid_unique_urls": len(valid),
    "invalid_lines": invalid,
    "sample_size": len(rows),
    "sample_csv": str(output),
    "classification_note": (
        "Feed inclusion is a reported indicator, not independent proof "
        "of current malicious activity."
    ),
}
summary_path.write_text(json.dumps(summary, indent=2) + "\n")

print(json.dumps(summary, indent=2))
print("Sample CSV SHA-256:", hashlib.sha256(output.read_bytes()).hexdigest())
