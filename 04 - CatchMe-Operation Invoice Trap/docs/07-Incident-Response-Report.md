# Phase 07 — Incident Response Report

## Executive summary

An invoice-themed email delivered a ZIP archive containing a Windows shortcut. Shortcut metadata shows hidden, encoded PowerShell that downloads remote content from `files.bpakcaging.xyz/update` and passes it to `Invoke-Expression`. PowerShell script-block logs and PCAP traffic corroborate the download and show recurring HTTP communications to `cdn.bpakcaging.xyz:8080`. An HTTP POST body contains Windows process-listing output, while endpoint logs show Seatbelt-related host-enumeration commands. The PCAP also contains repeated long hexadecimal-label DNS queries under `bpakcaging.xyz`; matching responses returned no answers, and partial POST output includes errors for those names.

**Assessment:** High confidence of suspicious PowerShell execution and command-and-control-like activity with attempted host reconnaissance. Successful data exfiltration, credential theft, DNS tunnelling, persistence, and full business impact are not established by the reviewed evidence.

## Scope and evidence

- Email: `dump.eml`
- Attachment: `Invoice.zip`, SHA-256 `b55ee53b18871f811f5a4ec405cd70de6b3f1f7cf28712ab5cb5186cbf551e87`
- LNK: `Invoice_20230103.lnk`, SHA-256 `86d5e0589fbd8c90604da954197344801f0579de157510e13492db0c712a0cc8`
- Endpoint: `powershell.json`, including event IDs 4104 and 4100
- Network: `capture.pcapng`
- Host/user context: `QL-WKSTN-5693\j.westcott`

## Key indicators

| Indicator | Context |
|---|---|
| `bpakcaging.xyz` | Observed sender/domain string; spelling differs from `bpackaging.xyz` |
| `files.bpakcaging.xyz/update` | URL embedded in the LNK's decoded PowerShell and observed in PCAP |
| `files.bpakcaging.xyz/sb.exe` | GET observed around 17:14:34 UTC; related to later Seatbelt commands in endpoint logs |
| `cdn.bpakcaging.xyz:8080` | Repeated HTTP command-polling-like traffic |
| `159.89.205.40:8080` | HTTP peer associated with repeated POSTs |
| `167.71.211.113` | DNS peer observed for long-label queries; role not independently confirmed |
| `/27fe2489` | Repeated HTTP POST URI |
| `/8cce49b0`, `/b86459bb` | Additional observed HTTP paths |

Treat these as incident-specific indicators; validate ownership and context before using them outside the lab.

## Impact assessment

**Observed:** suspicious PowerShell execution, remote content retrieval, recurring HTTP exchanges, process-listing output in an HTTP POST, attempted host enumeration, and repeated long-label DNS lookups.

**Not established:** credential access or theft, successful exfiltration, persistence, lateral movement, destructive actions, or the full scope of host compromise. HTTP `200` responses alone do not prove the server accepted or used submitted content.

## Containment and remediation recommendations

For an actual enterprise incident, under the organization's incident-response process:

1. Isolate the affected endpoint from untrusted networks while preserving forensic access and evidence.
2. Preserve the original email, archive, LNK, PowerShell event logs, PCAP, and relevant Windows logs. Record hashes and chain of custody.
3. Block or sinkhole the incident-specific domains, IPs, and URIs only after validating them against the organization's environment and threat-intelligence process.
4. Search enterprise telemetry for the domain strings, HTTP peer, URI paths, PowerShell download-and-execute patterns, and matching long-label DNS queries.
5. Review process creation, PowerShell, DNS, proxy, firewall, EDR, authentication, and cloud metadata logs for scope and impact.
6. Reset credentials only if evidence or response policy indicates possible exposure; revoke active sessions and tokens where warranted.
7. Reimage or restore the endpoint from a known-good baseline if compromise is confirmed; verify persistence mechanisms and patch the initial access path.
8. Validate recovery with EDR scans, monitoring, and documented business-owner sign-off.

These are recommendations, not actions claimed to have been performed in this lab.

## Detection opportunities

- Alert on Office/user-launched shortcut activity that starts hidden or encoded PowerShell and invokes `DownloadString` followed by `Invoke-Expression`.
- Detect repeated PowerShell-originated HTTP POSTs to rare destinations or unusual ports, particularly when preceded by remote script retrieval.
- Correlate DNS queries with unusually long high-entropy labels and repeated no-answer responses, but tune to reduce false positives.
- Alert on download of `sb.exe` or execution of host-enumeration tooling in an unexpected user context, while validating software inventory and administrative use.

## Lessons learned

- SPF/DKIM passing does not establish that a sender or message is benign.
- Password-protected archives and shortcut files warrant safe, metadata-first inspection.
- Endpoint and network evidence materially strengthen each other when correlated by timestamp, host, domain, and URI.
- Distinguish attempted commands and observed responses from confirmed successful outcomes.
- Preserve decoding limitations explicitly; do not call partial body decoding complete or label suspicious DNS activity as confirmed tunnelling without evidence.
