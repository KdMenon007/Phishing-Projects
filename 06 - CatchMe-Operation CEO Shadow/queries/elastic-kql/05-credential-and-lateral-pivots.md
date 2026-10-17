# Search 05 — Credential and Lateral Pivots

```kql
process.name : "mimikatz.exe" and process.command_line : "*sekurlsa::pth*"
```

```kql
process.command_line : "*IT_Automation.ps1*" or process.command_line : "*Invoke-Command*"
```

```kql
process.parent.name : "wsmprovhost.exe"
```

```kql
process.name : "mimikatz.exe" and process.command_line : "*lsadump::dcsync*"
```

Correlate with authentication, SMB, WinRM/PowerShell Operational, and domain-controller events. Full hashes and passwords are intentionally omitted from the public package.
