# Detection Coverage Matrix — Operation CEO Shadow

The rules below are analytic starting points for Elastic ECS/Winlogbeat data. Validate field mappings and test against benign baselines before deploying to production.

| Detection use case | Candidate signal | Evidence anchor | Priority | Validation status |
|---|---|---|---|---|
| HTA launched by `mshta.exe` | `process.name: mshta.exe` with `.hta` or suspicious document-like argument | Screenshot 05 | High | Screenshot-backed; tune against approved HTA use |
| Suspicious file copied from mounted drive | `xcopy.exe` command line copies a drive-root file into user Temp | Screenshot 06 | High | Command observed; validate broader baseline |
| `rundll32.exe` loading nonstandard DLL path | `rundll32.exe` with a path under user-writable locations or unusual export | Screenshots 07, 09 | High | Parent command context observed; direct event needed |
| Unusual `rundll32.exe` outbound connection | Process `rundll32.exe` plus destination `165.232.170.151:80` | Screenshot 10 | High | Endpoint observed; attribution needs corroboration |
| `fodhelper.exe` unusual parent | `fodhelper.exe` with unexpected parent/command-line ancestry | Screenshot 09 | High | Suspected UAC-bypass sequence; elevation unconfirmed |
| Mimikatz download from public GitHub release | PowerShell `iwr`/`Invoke-WebRequest` to Mimikatz release URL | Screenshot 12 | High | Download command observed |
| Pass-the-hash tooling | Mimikatz command includes `sekurlsa::pth` | Screenshots 13, 15 | High | Process command observed; authentication result separate |
| SMB script access followed by remoting | Access to `IT_Automation.ps1` followed by `Invoke-Command` / WinRM events | Screenshots 11, 17, 18 | High | Sequence observed; correlate authentication outcome |
| DCSync command | Process command line includes `lsadump::dcsync` | Screenshot 16 | Critical | Command observed; DC logs required to confirm success |
| Ransomware download attempt | PowerShell download URL or output path contains `ransomboogey.exe` | Screenshots 19–22 | Critical | Attempt observed; execution and encryption not established |
| Scheduled-task persistence | Task creation/modification events plus suspicious action/parent | Not yet evidenced | High | Pending; task name unresolved |

## KQL starter queries

```kql
process.name : "mshta.exe" and process.command_line : "*ProjectFinancialSummary_Q3.pdf.hta*"
```

```kql
process.name : "xcopy.exe" and process.command_line : "*review.dat*"
```

```kql
process.name : "rundll32.exe" and destination.ip : "165.232.170.151" and destination.port : 80
```

```kql
process.name : "fodhelper.exe" or process.parent.name : "fodhelper.exe"
```

```kql
process.command_line : "*sekurlsa::pth*" or process.command_line : "*lsadump::dcsync*"
```

```kql
process.command_line : "*ransomboogey.exe*" or process.args : "*ransomboogey.exe*"
```

## Detection engineering notes

- Use process GUIDs and host identity for correlation when available; PID alone is not globally unique and can be reused.
- Normalize hostnames and timestamp fields before building cross-host sequences.
- Avoid alerting on a single tool name alone; combine ancestry, path, command line, user context, network destination, and time proximity.
- Record false positives, expected administrative behavior, rule version, test data, and tuning changes.
