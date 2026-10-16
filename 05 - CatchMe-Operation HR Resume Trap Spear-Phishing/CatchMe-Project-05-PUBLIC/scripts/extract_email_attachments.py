#!/usr/bin/env python3
"""Extract MIME attachments and calculate hashes; never execute extracted files."""
from email import policy
from email.parser import BytesParser
from pathlib import Path
import hashlib, json, sys

if len(sys.argv) < 2:
    raise SystemExit('Usage: python3 scripts/extract_email_attachments.py EMAIL.eml [OUTPUT_DIR]')

source = Path(sys.argv[1])
output = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("evidence/extracted")
output.mkdir(parents=True, exist_ok=True)

with source.open("rb") as handle:
    msg = BytesParser(policy=policy.default).parse(handle)

for field in ("From", "To", "Subject", "Date"):
    print(f"{field}: {msg.get(field)}")

count = 0
for index, part in enumerate(msg.walk(), start=1):
    filename = part.get_filename()
    payload = part.get_payload(decode=True)
    if not filename or payload is None:
        continue
    safe_name = Path(filename).name
    destination = output / safe_name
    if destination.exists():
        destination = output / f"{index}_{safe_name}"
    destination.write_bytes(payload)
    record = {
        "filename": safe_name,
        "saved_path": str(destination),
        "content_type": part.get_content_type(),
        "size_bytes": len(payload),
        "md5": hashlib.md5(payload).hexdigest(),
        "sha256": hashlib.sha256(payload).hexdigest(),
    }
    print(json.dumps(record, indent=2))
    count += 1

if count == 0:
    print("No filename-bearing MIME attachments found.")
