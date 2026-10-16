# Network Analysis Notes

## Capture observations

- Affected workstation: `10.10.182.255`
- HTTP peer: `159.89.205.40:8080`
- HTTP Host: `cdn.bpakcaging.xyz:8080`
- Observed DNS peer: `167.71.211.113` (role not independently validated)
- Domain string in suspicious activity: `bpakcaging.xyz` (preserve exact spelling)

## HTTP timeline

| Timestamp (UTC) | Observation | Evidence reference |
|---|---|---|
| 2023-01-13 17:10:09.751986 | GET `files.bpakcaging.xyz/update` | TShark output supplied during investigation |
| 2023-01-13 17:10:10.189504 | GET `/8cce49b0` to `cdn.bpakcaging.xyz:8080` | HTTP stream analysis |
| 2023-01-13 17:10:10.623363 | GET `/b86459bb` | HTTP stream analysis |
| 2023-01-13 17:10:11.392604 | POST `/27fe2489` | HTTP stream analysis |
| ~2023-01-13 17:14:34 | GET `files.bpakcaging.xyz/sb.exe` | TShark output supplied during investigation |
| 2023-01-13 17:34:39.953173 | POST `/27fe2489`, TCP stream 1076, Content-Length 78618 | TShark HTTP fields / stream 1076 |
| 2023-01-13 17:34:40.152293 | HTTP 200 response to stream 1076 POST | TShark HTTP fields / stream 1076 |

Repeated GETs and POSTs were observed over the period, with HTTP traffic continuing intermittently through at least 17:34 UTC. The request user-agent identifies Windows PowerShell 5.1.

## POST content

- TCP stream 150 contains partially decoded Windows process-listing output (e.g., process names and standard process-table columns).
- TCP stream 1076 declares a 78,618-byte POST body. The partial decode contains repeated DNS lookup errors for long hexadecimal labels beneath `bpakcaging.xyz`, as well as resolver output and a working-directory string `C:\Users\j.westcott\Documents`.
- The full stream 1076 body has not been fully validated as decoded text. Treat the decoded output as partial.

## DNS

- 88 unique queries matched the pattern `^[A-Fa-f0-9]{20,}\.bpakcaging\.xyz\.?$`.
- The matching queries originated from `10.10.182.255` and were sent to `167.71.211.113`.
- The matching responses had `NOERROR` (`dns.flags.rcode = 0`) and zero answers.
- Partial HTTP POST output includes “No address (A) records available” messages for matching labels.

Assessment: repeated changing long labels are suspicious in context and correlate with HTTP result reporting. DNS tunnelling and DNS-based exfiltration are not confirmed.

## Additional observation

A request to `169.254.169.254/latest/meta-data/iam/security-credentials/` at `17:17:19.666422 UTC` returned HTTP 404. This is a metadata-path probe; credential retrieval is not evidenced. Periodic `instance-action` metadata requests begin before the suspicious activity and should not be attributed to the incident without more evidence.

## Limitations

A server HTTP `200` response does not prove data was accepted or used. No claim of successful exfiltration, credential theft, or DNS tunnelling should be made from the evidence recorded here alone.
