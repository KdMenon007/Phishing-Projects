# Phase 06 — MITRE ATT&CK & Detection Engineering

Technique mapping is based on the observed lab evidence. A technique is not marked confirmed merely because it is plausible in the scenario.

| Technique | Name | Evidence in this case | Confidence / caveat |
|---|---|---|---|
| T1566.001 | Phishing: Spearphishing Attachment | Invoice-themed email carried a password-protected ZIP containing an LNK | High for attachment-based lure; user interaction inferred from chain, validate exact execution telemetry |
| T1204.002 | User Execution: Malicious File | LNK appears in the delivery chain and leads to PowerShell execution evidence | Supported by correlated artefacts; preserve uncertainty if exact user-action event is unavailable |
| T1059.001 | Command and Scripting Interpreter: PowerShell | LNK command and PowerShell Event 4104 evidence show hidden/encoded PowerShell, remote retrieval, and dynamic execution | High |
| T1105 | Ingress Tool Transfer | Remote content retrieval and later `sb.exe` retrieval are observed in the evidence chain | Supported as a transfer behavior; exact payload contents and successful execution require separate validation |
| T1071.001 | Application Layer Protocol: Web Protocols | Repeated HTTP communications to `cdn.bpakcaging.xyz:8080` | High for HTTP usage; C2 interpretation supported by context |
| T1057 | Process Discovery | Process-listing output appears in a POST body | High for process-list output; do not infer that every listed process was malicious |
| T1082 | System Information Discovery | Host-enumeration activity is present; use only if specific system-information commands/results are preserved in endpoint logs | Conditional; confirm specific command evidence before final tagging |

## Explicitly not confirmed

- **T1071.004 — DNS:** long-label DNS activity is suspicious, but DNS-based C2/tunnelling has not been established.
- **T1041 — Exfiltration Over C2 Channel:** process-listing output in a POST indicates data was placed in an HTTP request, but the full body is not completely decoded and the server-side handling is unknown. Do not label successful exfiltration as confirmed.
- **Credential access:** no direct evidence in the reviewed artefacts proves credential theft.
- **Persistence / lateral movement:** not established by the artefacts summarized here.

## Detection engineering priorities

1. Correlate PowerShell Event 4104 with process creation and network activity on the same host.
2. Alert on remote retrieval plus dynamic PowerShell execution, especially when hidden/encoded.
3. Add threshold logic for repeated HTTP POSTs to rare destinations and URIs.
4. Use DNS uniqueness and label-length thresholds as anomaly signals, not a standalone DNS-tunnelling verdict.
5. Add process-discovery detections, tuned for authorized administration and security tooling.

See `detections/siem-queries.md` for Splunk SPL and Elastic KQL starter queries. These have not been run against a connected SIEM and should be validated before deployment.
