# Phase 04 — Network Traffic Analysis

## Scope and method

Analysed `capture.pcapng` with TShark filters and TCP-stream following. Findings below are based on terminal output recorded during the investigation. Where a full HTTP body was not reliably decoded, conclusions are limited to the visible content and transaction metadata.

## 1. Suspicious HTTP activity

| Observation | Evidence |
|---|---|
| Workstation | `10.10.182.255` |
| HTTP server | `159.89.205.40:8080` |
| HTTP Host header | `cdn.bpakcaging.xyz:8080` |
| Repeated URI | `/27fe2489` |
| Client user agent | `WindowsPowerShell/5.1.18362.145` within a Windows PowerShell user-agent string |
| Final reviewed transaction | TCP stream `1076`, 2023-01-13 17:34:39.953173 UTC |
| Declared request body | 78,618 bytes |
| Server response | HTTP `200` at 2023-01-13 17:34:40.152293 UTC |

The PCAP shows repeated GET and POST requests to the same endpoint, with recurring POSTs to `/27fe2489`. Earlier transactions include GET requests such as `/8cce49b0` and `/b86459bb`. The timing and HTTP headers align with PowerShell endpoint evidence that describes polling for commands and returning results. This is assessed as **command-and-control-like HTTP behavior** with high confidence in the suspicious nature of the activity.

An HTTP `200` confirms the server returned a successful HTTP status; it does not establish what the server did with the submitted data or prove that an operator received or used it.

## 2. Process-enumeration output in HTTP POST

A partially decoded body associated with TCP stream `150` begins with a Windows process table, including columns such as `Handles`, `NPM(K)`, `PM(K)`, `WS(K)`, `CPU(s)`, `Id`, `SI`, and `ProcessName`. Visible entries include ordinary Windows and environment processes such as `cmd`, `conhost`, `csrss`, `dllhost`, `dwm`, `Ec2Config`, and `amazon-ssm-agent`.

**Assessment:** process-listing output was present in the decoded POST content. In the context of the recurring HTTP exchange, this supports host reconnaissance and possible command-result reporting. The process names themselves are not inherently malicious.

## 3. DNS observations

The workstation `10.10.182.255` generated 88 unique DNS queries matching the filter for long hexadecimal labels directly beneath `bpakcaging.xyz`. The matching responses observed in the capture returned DNS response code `0` (NOERROR) with zero answer records. Queries were sent to `167.71.211.113`; this is the observed DNS peer in the capture and should not be assumed to be a public authoritative server without further validation.

A partially decoded HTTP POST body includes repeated errors such as `No address (A) records available for <long-label>.bpakcaging.xyz`. The matching labels and the overlap in timing suggest the DNS lookup activity and HTTP command-result reporting are related.

**Assessment:** repeated, changing, long hexadecimal labels are suspicious in the incident context. However, these observations alone do **not** prove DNS tunnelling or data exfiltration over DNS. The decoded POST body is partial and its full content has not been validated.

## 4. Payload retrieval and reconnaissance correlation

- At approximately `2023-01-13 17:10:09.751986 UTC`, the workstation made an HTTP GET for `files.bpakcaging.xyz/update`, consistent with the URL embedded in the LNK's decoded PowerShell command.
- At approximately `17:14:34 UTC`, the PCAP shows a GET for `files.bpakcaging.xyz/sb.exe`.
- Endpoint logs later show Seatbelt-related commands, consistent with host enumeration. Correlate exact event records before claiming that every downloaded tool executed successfully.
- A request to `169.254.169.254/latest/meta-data/iam/security-credentials/` at `17:17:19.666422 UTC` received HTTP `404`. This is consistent with a metadata-path probe, but does not show credential retrieval.
- Periodic requests to `169.254.169.254/latest/meta-data/instance-action` begin before the suspicious PowerShell activity. Do not automatically attribute those periodic requests to the malware without further process-level correlation.

## 5. Key indicators (lab-scoped)

| Indicator | Context | Handling |
|---|---|---|
| `bpakcaging.xyz` | Observed in email and suspicious DNS/HTTP names | Treat as a suspicious lab indicator; spelling differs from `bpackaging.xyz` |
| `files.bpakcaging.xyz` | LNK PowerShell download URL; GETs observed in PCAP | Correlate with endpoint events |
| `cdn.bpakcaging.xyz:8080` | Repeated HTTP GET/POST communications | Strong C2-like indicator in this case |
| `159.89.205.40:8080` | HTTP peer for recurring POSTs | Validate in environment before blocking outside lab |
| `167.71.211.113` | DNS peer in the capture | Observed resolver/peer; role not independently established |
| `/27fe2489` | Repeated POST path | Context-specific URI; use in network detection |
| `/b86459bb`, `/8cce49b0` | Other observed HTTP paths | Context-specific URI indicators |

Do not treat any single domain or IP as universally malicious without checking ownership, environment, and current context.

## 6. Reproducible TShark checks

```bash
# Requests from the affected workstation to the suspicious HTTP peer
 tshark -r capture.pcapng \
  -Y 'ip.src == 10.10.182.255 && ip.dst == 159.89.205.40 && http.request' \
  -T fields -e frame.time_utc -e tcp.stream -e http.request.method \
  -e http.host -e http.request.uri -e http.content_length

# Long hexadecimal DNS labels directly under the observed domain
 tshark -r capture.pcapng \
  -Y 'dns.flags.response == 0 && ip.src == 10.10.182.255 && dns.qry.name matches "^[A-Fa-f0-9]{20,}\.bpakcaging\.xyz\.?$"' \
  -T fields -e frame.time_utc -e dns.qry.name

# DNS response code and answer count for the same pattern
 tshark -r capture.pcapng \
  -Y 'dns.flags.response == 1 && dns.qry.name matches "^[A-Fa-f0-9]{20,}\.bpakcaging\.xyz\.?$"' \
  -T fields -e frame.time_utc -e dns.qry.name -e dns.flags.rcode -e dns.count.answers
```

## 7. Limitations

- The full HTTP POST body in stream `1076` has not been fully decoded into a validated complete text representation. The declared body length is 78,618 bytes; a previous partial decode contains DNS lookup errors and resolver output.
- A successful HTTP status does not establish successful exfiltration or operator use of the data.
- DNS tunnelling is not confirmed by the current evidence.
- The role of `167.71.211.113` as a resolver versus another DNS peer has not been independently established.
- The full downloaded payload and any resulting system changes are outside the findings documented here unless supported by additional artefacts.

## 8. Phase conclusion

The network evidence corroborates suspicious PowerShell-driven HTTP communications and recurring DNS lookups, and includes process-enumeration output in an HTTP POST. Combined with the endpoint logs and LNK metadata, the activity is consistent with a multi-stage intrusion involving payload retrieval, command polling, and host reconnaissance. Further analysis would be needed to establish the exact data transmitted, successful exfiltration, persistence, or credential access.
