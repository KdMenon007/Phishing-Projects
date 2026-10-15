#!/usr/bin/env python3
import csv
import hashlib
from pathlib import Path
from datetime import datetime, timezone

source = Path("analysis/working/url-investigation-sample.csv")
output = Path("analysis/working/domain-investigation.csv")

with source.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

domains = sorted({
    row["hostname_defanged"]
    for row in rows
    if row.get("hostname_defanged")
})

with output.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "domain_defanged", "source", "observed_utc",
            "dns_status", "registration_status",
            "independent_reputation", "analyst_assessment"
        ]
    )
    writer.writeheader()
    for domain in domains:
        writer.writerow({
            "domain_defanged": domain,
            "source": "OpenPhish community feed",
            "observed_utc": datetime.now(timezone.utc).isoformat(),
            "dns_status": "Not checked",
            "registration_status": "Not checked",
            "independent_reputation": "Not checked",
            "analyst_assessment": "Pending enrichment",
        })

print("Sample URL records:", len(rows))
print("Unique domains:", len(domains))
print("Output:", output)
print("SHA-256:", hashlib.sha256(output.read_bytes()).hexdigest())
