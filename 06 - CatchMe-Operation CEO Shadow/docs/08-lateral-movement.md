# 08 — Lateral Movement

**Status: remote share access and PowerShell remoting activity observed.**

PowerShell on `WKSTN-0051` accessed `IT_Automation.ps1` from `\\WKSTN-1327.quicklogistics.org\ITFiles`. A later command creates a credential for `QUICKLOGISTICS\allan.smith` and invokes remote PowerShell on `WKSTN-1327`. The plaintext password is redacted from public screenshots.

On the second host, the malicious PowerShell process has parent `wsmprovhost.exe`, consistent with a remote PowerShell session. Correlate SMB, WinRM/PowerShell Operational, authentication, and process-creation events to determine whether all remote actions completed successfully.
