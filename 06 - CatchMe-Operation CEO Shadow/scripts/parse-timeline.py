#!/usr/bin/env python3
"""Print a CSV timeline sorted by timestamp/time column."""
import csv, sys
from pathlib import Path
source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("Attack-Timeline.csv")
if not source.exists():
    raise SystemExit(f"Timeline CSV not found: {source}")
with source.open(newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows, fields = list(reader), reader.fieldnames or []
key = next((x for x in ("timestamp", "time", "Time") if x in fields), None)
if not key:
    raise SystemExit("CSV needs timestamp, time, or Time column.")
for row in sorted(rows, key=lambda r: r.get(key, "")):
    print(" | ".join(f"{field}={row.get(field, '')}" for field in fields))
