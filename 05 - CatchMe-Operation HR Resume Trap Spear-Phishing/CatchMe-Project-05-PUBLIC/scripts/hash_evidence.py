#!/usr/bin/env python3
"""Calculate MD5 and SHA-256 hashes without modifying files."""
from pathlib import Path
import hashlib, sys

if len(sys.argv) < 2:
    raise SystemExit("Usage: python3 scripts/hash_evidence.py FILE [FILE ...]")

for item in sys.argv[1:]:
    path = Path(item)
    if not path.is_file():
        print(f"ERROR: not a file: {path}")
        continue
    md5, sha256, size = hashlib.md5(), hashlib.sha256(), 0
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            size += len(chunk)
            md5.update(chunk)
            sha256.update(chunk)
    print(f"File: {path}\nSize: {size} bytes\nMD5: {md5.hexdigest()}\nSHA256: {sha256.hexdigest()}\n")
