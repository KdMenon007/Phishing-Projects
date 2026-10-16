# Phase 08 — Detection Validation Plan

## Purpose

Turn the case findings into reproducible detection tests without presenting unexecuted queries as production-validated.

## Validation matrix

| Test | Data source | Expected result | Result status |
|---|---|---|---|
| Remote retrieval + `iex` in PowerShell script block | PowerShell Operational Event 4104 | Find the script block containing remote retrieval and dynamic execution | Evidence observed in source logs; SIEM query not run |
| Encoded/hidden PowerShell process creation | Sysmon Event 1 or Security Event 4688 | Find command line with encoded/hidden options or suspicious API strings | Pending SIEM field mapping |
| Repeated HTTP POST to rare host/URI | PCAP-derived HTTP/Zeek/proxy events | Find repeated POSTs to `cdn.bpakcaging.xyz:8080` and `/27fe2489` | PCAP evidence observed; SIEM query not run |
| Long-label DNS anomaly | DNS logs | Identify unique long labels under `bpakcaging.xyz`, including zero-answer responses | 88 unique labels observed in PCAP filter; SIEM query not run |
| Process enumeration | HTTP POST body and PowerShell logs | Find process listing and Seatbelt-related commands | Process-list output observed; full stream 1076 body remains partially decoded |

## Lab validation workflow

1. Set the time range to 13 January 2023 around 17:00–17:40 UTC.
2. Confirm the source fields exist before using the supplied SPL/KQL.
3. Run each query independently and record the number of returned events.
4. Open representative events and compare them with the raw evidence.
5. Test the query against a benign time range or approved admin activity.
6. Tune thresholds to reduce false positives without losing the observed incident sequence.
7. Save a screenshot of the query, result count, selected event, and timestamp.
8. Update the status column only after the query has actually been executed and reviewed.

## What counts as validated

- **Evidence observed:** visible in original email, endpoint log, or PCAP.
- **Query tested:** query executed against the relevant SIEM dataset.
- **Detection validated:** expected events returned and reviewed; known benign cases checked.
- **Production-ready:** owner, severity, triage guidance, suppression logic, and change control are documented.

Do not promote a query directly from “starter” to “production-ready” without the last two validation stages.
