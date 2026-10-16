# MITRE ATT&CK Mapping

Mappings below describe observed behavior, not attribution. Technique mapping should be reviewed against the current ATT&CK version before publication.

| Observed behavior | Candidate technique | Evidence | Confidence / caveat |
|---|---|---|---|
| Invoice-themed email delivered a ZIP containing a Windows LNK | **T1566.001 — Phishing: Spearphishing Attachment** | `dump.eml`; `Invoice.zip`; LNK metadata | High for attachment-based lure in the lab scenario; exact delivery mechanics are based on supplied artefacts. |
| LNK invokes hidden, encoded PowerShell | **T1059.001 — Command and Scripting Interpreter: PowerShell** | `Invoice_20230103.lnk`; PowerShell event 4104 | High. |
| PowerShell downloads remote content and invokes it with `iex` | **T1105 — Ingress Tool Transfer** (candidate) and **T1059.001** | LNK command; event 4104; GET `/update` | High for remote retrieval/execution pattern; exact downloaded script contents not fully documented. |
| Recurring HTTP polling and POST result reporting | **T1071.001 — Application Layer Protocol: Web Protocols** (candidate) | Event 4104 record 501; repeated HTTP GET/POST traffic | High for HTTP-based C2-like behavior; label as candidate technique based on observed pattern. |
| Process-listing output and Seatbelt-related commands | **T1057 — Process Discovery** and **T1082 — System Information Discovery** (candidate) | TCP stream 150 decoded process list; PowerShell Seatbelt-related commands | Moderate to high for discovery behavior; do not infer all tool commands succeeded. |
| Repeated long hexadecimal-label DNS queries | **T1071.004 — Application Layer Protocol: DNS** (investigative hypothesis only) | 88 unique long-label queries; zero-answer responses; partial POST output contains lookup errors | Not confirmed as DNS C2/tunnelling. Retain as hypothesis, not a confirmed mapping. |

## Explicitly not established

- **T1041 — Exfiltration Over C2 Channel:** POSTs exist and some decoded output resembles command results, but successful exfiltration is not proven.
- Credential dumping or theft, persistence, lateral movement, and impact techniques are not mapped because current evidence does not establish them.
