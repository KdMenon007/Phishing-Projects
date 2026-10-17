# Detection: Ransomware Download Attempt

## Observed command
PowerShell attempted to retrieve `http://ff.sillytechninja.io/ransomboogey.exe` and save it as `C:\Users\evan.hutchinson\ransomboogey.exe` using a remote PowerShell command.

## KQL pivots
```kql
process.command_line : "*ransomboogey.exe*"
```
```kql
process.command_line : "*ff.sillytechninja.io*"
```

## Interpretation
This evidence confirms an attempted download command, not necessarily a successful download, binary execution, or encryption. Validate file creation, process start, file modifications, ransom notes, and backup/recovery state before assigning impact.
