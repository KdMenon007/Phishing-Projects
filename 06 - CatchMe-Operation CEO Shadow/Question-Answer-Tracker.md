# Investigation Question Tracker — Operation CEO Shadow

> **Public-release hygiene:** passwords and complete pass-the-hash values are intentionally redacted. Keep any unredacted lab notes private. Do not publish reusable credentials.

| # | Question | Answer / status | Evidence |
|---:|---|---|---|
| 1 | PID of process executing the initial stage-one payload? | **6392 — `mshta.exe`**, launched with `D:\ProjectFinancialSummary_Q3.pdf.hta`. | Screenshot 05 |
| 2 | Full command line for the file-implant/copy attempt? | `"C:\Windows\System32\xcopy.exe" /s /i /e /h D:\review.dat C:\Users\EVAN~1.HUT\AppData\Local\Temp\review.dat` (PID 3832). | Screenshot 06 |
| 3 | Command line used to execute the implanted file? | Observed parent command line: `"C:\Windows\System32\rundll32.exe" D:\review.dat,DllRegisterServer`. Treat as strongly supported, but the visible screenshot is the parent-process field of `fodhelper.exe`, not a separate expanded `rundll32.exe` event. | Screenshots 08–09 |
| 4 | Name of scheduled task created by the malicious script? | **Pending.** The supplied screenshots do not expose the task name. | Query scheduled-task creation telemetry; retain as unresolved |
| 5 | C2 connection IP:port from implanted-file execution? | **`165.232.170.151:80`**; repeated `rundll32.exe` network events are visible on `WKSTN-0051.quicklogistics.org`. | Screenshot 10 |
| 6 | Process used for UAC bypass? | **`fodhelper.exe`** appears in the suspected UAC-bypass sequence; successful elevation is not independently proven by these screenshots alone. | Screenshots 08–09 |
| 7 | GitHub URL for credential-dumping tool? | `https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip` | Screenshot 12 |
| 8 | `username:hash` credential used to access another machine? | **`itadmin:<NTLM hash redacted>`**. The screenshot shows Mimikatz `sekurlsa::pth` targeting `itadmin`; full hash is omitted from this public copy. | Screenshots 12–13 |
| 9 | Name of remote-share file accessed? | **`IT_Automation.ps1`** from `\\WKSTN-1327.quicklogistics.org\ITFiles`. | Screenshot 11 |
| 10 | New `username:password` used for lateral movement? | **`QUICKLOGISTICS\allan.smith : [PASSWORD REDACTED]`**. The evidence shows a `PSCredential` used with `Invoke-Command -ComputerName WKSTN-1327`; the screenshot has been redacted for public release. | Screenshot 18 |
| 11 | Hostname involved in the lateral-movement attempt/source execution? | **`WKSTN-0051.quicklogistics.org`** is the observed source host initiating the remote command. If the room expects a separately named attacker lab host, verify against the scenario's full telemetry before treating this as final. | Screenshots 11, 18–19 |
| 12 | Parent process of the malicious command on the second host? | **`wsmprovhost.exe`** on `WKSTN-1327.quicklogistics.org`. | Screenshot 17 |
| 13 | `username:hash` of credentials used on the second host? | **`administrator:<NTLM hash redacted>`**. Mimikatz pass-the-hash activity is visible; full hash is omitted from this public copy. | Screenshot 15 |
| 14 | Account besides Administrator targeted in DCSync? | **`backupda`** via `lsadump::dcsync /domain:quicklogistics.org /user:backupda`. | Screenshot 16 |
| 15 | URL used to download the ransomware binary? | **`http://ff.sillytechninja.io/ransomboogey.exe`**. Evidence supports a download attempt to `C:\Users\evan.hutchinson\ransomboogey.exe`; do not infer successful execution or encryption from the download command alone. | Screenshot 19 |

## Important validation notes
- The date picker shown in several screenshots extends to 2026; the visible event timestamps are from 29–30 August 2023. Set the time picker narrowly before exporting or comparing events.
- Search hit counts are context, not proof of malicious execution or impact.
- Confirm the scheduled-task name from task-creation events before closing Q4.
