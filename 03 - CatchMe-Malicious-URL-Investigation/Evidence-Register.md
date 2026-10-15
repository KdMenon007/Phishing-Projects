# Evidence Register

**Project:** CatchMe — Malicious URL & Phishing Infrastructure Investigation  
**Observation date:** 2026-10-15  
**Handling:** Defanged indicators; no suspicious websites visited.

| Evidence ID | Artifact | Description | Source / Method | SHA-256 / Status | Limitation |
|---|---|---|---|---|---|
| E-001 | `analysis/raw/openphish-feed.txt` | Raw OpenPhish community feed snapshot | Retrieved from public feed endpoint | `3ae958e9039cb2d88ab7a039726445ca08936c773820c8c4e4310477a29305f4` | Feed listing is an intelligence lead, not independent proof of maliciousness |
| E-002 | `analysis/working/url-investigation-sample.csv` | Ten defanged URLs selected from the feed | Local sample generation | `1fdd3620abae411ee3355581a6bbbd1e95923c50308cf15a0632a25179149277` | Sample of 10; not a complete analysis of all feed entries |
| E-003 | `analysis/working/rdap-results.json` | RDAP lookup results for ten sample domains | RDAP queries | `db3d3efe4fe02b30537f110eb9598ebe416844190e37a0f487640445b357d993` | HTTP 404/400 results are inconclusive; registration data does not prove maliciousness |
| E-004 | `analysis/working/dns-results.json` | A, AAAA, and MX lookup results | `dig` using system-configured resolver | `e6d4bd11537f3c06c081716e4903ae663db489473f765c5d65ef8ab38de52c4c` | Timeouts and no-answer results do not prove inactivity |
| E-005 | `assets/evidence/dns/resolver-comparison.md` | Comparison of system resolver with Cloudflare and Google DNS for one indicator, plus system resolver result for a second | `dig` queries | `a860d64149242f71e893a99114206b898accb01730f324cbb87c8b195f3adc06` | Strong evidence of differing resolver responses; exact filtering component not established |
| E-006 | `analysis/url-triage-results.json` | URL-structure triage output for four controlled test URLs | Local Python script | `2486d437888bd4d4f58d8602759a730ebe8a47b14fac2fe3e3d44df30f46f430` | Controlled test examples; not evidence about the ten feed-listed domains |

## Evidence Handling Notes

- Preserve raw intelligence separately from public sanitized artifacts.
- Do not visit feed-listed URLs directly.
- Record retrieval times, methods, and hashes when capturing new evidence.
- Keep observed facts separate from analyst hypotheses.
- Recalculate hashes if any artifact is modified.
