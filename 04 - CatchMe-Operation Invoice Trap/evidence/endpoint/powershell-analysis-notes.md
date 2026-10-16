# Endpoint Analysis Notes

## Host and user context

- Host/user context observed: `QL-WKSTN-5693\j.westcott`
- Evidence source: `powershell.json`
- Event IDs reviewed: PowerShell 4104 (script block logging), 4100 (PowerShell errors)

## Key observations

| Time (UTC, approximate unless noted) | Event reference | Observation | Interpretation / caveat |
|---|---|---|---|
| 2023-01-13 17:10:07 | 4104, record 500 | Encoded/hidden PowerShell activity; decoded command downloads `http://files.bpakcaging.xyz/update` and passes returned content to `iex` | High-risk remote content execution pattern |
| 2023-01-13 17:10:11 | 4104, record 501 | References `cdn.bpakcaging.xyz:8080`, command polling, `iex`, and posting results | Strong C2-like behavior; corroborated by PCAP |
| 2023-01-13 17:10:24–17:10:54 | 4100 events | Invoke-WebRequest parsing errors involving IE parsing engine | Errors do not prove all requests failed |
| 2023-01-13 17:12:18 | 4100, record 554 | Invoke-Expression error involving HTML from GitHub | Suggests attempted interpretation of returned HTML; effect not established |
| Around 2023-01-13 17:15:49 | PowerShell logs | Seatbelt-related commands including `sb.exe` arguments `system`, `all`, `-group=all` | Consistent with host enumeration; successful completion not assumed |

## Correlation

The PCAP shows a GET to `files.bpakcaging.xyz/update` at `17:10:09.751986 UTC`, shortly after the script-block event, and recurring HTTP traffic to `cdn.bpakcaging.xyz:8080`. A GET for `files.bpakcaging.xyz/sb.exe` at about `17:14:34 UTC` precedes Seatbelt-related endpoint commands.

## Conclusion and limitations

The evidence supports suspicious PowerShell execution, remote retrieval, recurring command-polling behavior, and attempted host reconnaissance. It does not independently establish persistence, credential theft, or successful exfiltration. Retain raw event exports and exact record identifiers for reproducibility.
