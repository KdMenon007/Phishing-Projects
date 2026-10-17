# Detection: SMB Access and Remote PowerShell

## Observed activity
- `IT_Automation.ps1` was read from `\\WKSTN-1327.quicklogistics.org\ITFiles`.
- A PowerShell command created a credential for `QUICKLOGISTICS\allan.smith` and invoked a remote command against `WKSTN-1327`.
- On the second host, the malicious PowerShell process had parent `wsmprovhost.exe`, consistent with PowerShell remoting.

## KQL pivots
```kql
process.name : "powershell.exe" and process.command_line : "*Invoke-Command*"
```
```kql
process.parent.name : "wsmprovhost.exe"
```
```kql
process.command_line : "*IT_Automation.ps1*"
```

Correlate WinRM/PowerShell operational logs, process creation, authentication logs, and SMB share access. Passwords are redacted from public evidence.
