# Project Status — Operation CEO Shadow

**Stage:** Multi-stage Elastic investigation documented from 23 supplied screenshots. Several findings are supported; a few scenario questions remain open.

## Confirmed from visible telemetry
- `mshta.exe` PID 6392 launched `D:\ProjectFinancialSummary_Q3.pdf.hta` on `WKSTN-0051`.
- `xcopy.exe` PID 3832 copied `D:\review.dat` to the CEO user's Temp directory.
- `rundll32.exe` PID 4672 connected repeatedly to `165.232.170.151:80`.
- `fodhelper.exe` process events are consistent with a suspected UAC-bypass sequence; successful elevation is not independently proven.
- PowerShell accessed `IT_Automation.ps1` on `\\WKSTN-1327\ITFiles` and later used remote PowerShell against `WKSTN-1327`.
- Mimikatz pass-the-hash activity targeted `itadmin` and later `administrator`; full credential material is redacted from this public release.
- Mimikatz DCSync command targeted `backupda`.
- PowerShell attempted to download `ransomboogey.exe` from `ff.sillytechninja.io` into the CEO profile.

## Still open / requires validation
- Exact scheduled-task name.
- Separate expanded process event proving the direct `rundll32.exe` execution command.
- Whether UAC elevation succeeded.
- Whether the ransomware binary was successfully downloaded, executed, or encrypted files.
- Whether `WKSTN-0051` is the scenario's expected answer for the specifically worded attacker-lab-host question.

## Release hygiene
- Included 23 screenshots with descriptive filenames.
- Redacted the plaintext lab password in the credentialed PowerShell screenshot. Full hashes/passwords should remain in private lab notes, not a public repository.
- The archive is a portfolio-ready evidence package, not a claim that every attack stage succeeded.
