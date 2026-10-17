#!/usr/bin/env python3
"""Calculate SHA-256 hashes for files under a supplied evidence directory."""
import hashlib, sys
from pathlib import Path

def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("evidence")
if not root.exists():
    raise SystemExit(f"Path does not exist: {root}")
for p in sorted(x for x in root.rglob("*") if x.is_file()):
    print(f"{sha256(p)}  {p}")
