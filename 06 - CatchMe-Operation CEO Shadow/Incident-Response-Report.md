# Incident Response Report — Operation CEO Shadow

## 1. Executive overview
- **Scenario organization:** Quick Logistics LLC
- **Target user:** CEO Evan Hutchinson
- **Primary host:** `WKSTN-0051.quicklogistics.org`
- **Secondary host:** `WKSTN-1327.quicklogistics.org`
- **Observed window:** 29–30 August 2023
- **Telemetry:** Elastic Discover, `winlogbeat-*`, process-creation and network events
- **Assessment:** Multi-stage intrusion evidence spanning phishing/HTA execution, file staging, suspicious DLL loading, network communications, credential access, remote execution, DCSync, and a ransomware-download attempt.
- **Impact status:** No supplied screenshot proves successful ransomware execution, encryption, or final business impact. Treat those as unconfirmed.

## 2. Initial access and stage-one execution
A financial-themed email titled **Urgent Financial Matter Requiring Immediate Attention** was displayed as sent to Evan Hutchinson. The attachment `ProjectFinancialSummary_Q3.pdf` appeared in Downloads as a disc-image file. After mounting, a same-named item was shown as an HTML Application.

Elastic process telemetry shows `mshta.exe` PID **6392** launched `D:\ProjectFinancialSummary_Q3.pdf.hta`. Shortly afterward, `xcopy.exe` PID **3832** copied `D:\review.dat` to `C:\Users\EVAN~1.HUT\AppData\Local\Temp\review.dat`:

```text
"C:\Windows\System32\xcopy.exe" /s /i /e /h D:\review.dat C:\Users\EVAN~1.HUT\AppData\Local\Temp\review.dat
```

This is direct evidence of file staging. The copy event alone does not prove that the copied file executed.

## 3. Suspected DLL execution, UAC bypass, and network activity
A visible parent-process command line references:

```text
"C:\Windows\System32\rundll32.exe" D:\review.dat,DllRegisterServer
```

Two `fodhelper.exe` process events were observed on `WKSTN-0051.quicklogistics.org`, with `rundll32.exe` listed as the parent. This is consistent with a suspected `fodhelper.exe` UAC-bypass chain. The supplied screenshots do not independently establish that elevation succeeded; confirm with expanded event JSON and token/elevation evidence.

Network telemetry shows repeated connections from `rundll32.exe` PID 4672 to **`165.232.170.151:80`**. This is a suspicious external endpoint associated with the implant's execution window. Label it a suspected C2 endpoint pending corroboration from DNS, proxy, firewall, or packet evidence.

## 4. Credential access and lateral movement
PowerShell on `WKSTN-0051` accessed `IT_Automation.ps1` from `\\WKSTN-1327.quicklogistics.org\ITFiles`. The screenshots show a PowerShell command downloading the Mimikatz ZIP from:

`https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip`

On `WKSTN-1327`, Mimikatz ran `sekurlsa::pth` targeting `itadmin`. A later PowerShell command created a `PSCredential` for `QUICKLOGISTICS\allan.smith` and used `Invoke-Command` against `WKSTN-1327`. On the second host, a malicious PowerShell process (PID 6708) had parent `wsmprovhost.exe`, consistent with a remote PowerShell session. Mimikatz later targeted `administrator` on the second host.

**Credential hygiene:** the public version intentionally redacts the plaintext password and complete NTLM hashes. Do not commit unredacted screenshots, passwords, tokens, or reusable credential material to a public repository.

## 5. Active Directory / DCSync
A Mimikatz command was observed using `lsadump::dcsync` against `quicklogistics.org` with `/user:backupda`. This supports reporting a DCSync attempt targeting **`backupda`**. Confirm the domain-controller audit events and whether directory secrets were successfully replicated before describing the operation as successful credential extraction.

## 6. Ransomware download attempt
A PowerShell `Invoke-Command` command attempted to download:

`http://ff.sillytechninja.io/ransomboogey.exe`

to:

`C:\Users\evan.hutchinson\ransomboogey.exe`

The evidence supports an attempted download command. Additional process events mention `ransomboogey.exe`, but the screenshots supplied so far do not conclusively establish successful execution or file encryption. Validate file creation, process start, file-system impact, ransom notes, and recovery artefacts before concluding ransomware impact.

## 7. Evidence-based answers
- Initial HTA process PID: **6392** (`mshta.exe`).
- File-copy process: **3832** (`xcopy.exe`).
- Implant-copy destination: `C:\Users\EVAN~1.HUT\AppData\Local\Temp\review.dat`.
- Suspected implant invocation: `rundll32.exe D:\review.dat,DllRegisterServer`.
- Network endpoint: **`165.232.170.151:80`**.
- UAC-bypass-associated process: **`fodhelper.exe`**; success not independently proven.
- Remote share file: **`IT_Automation.ps1`**.
- Second-host remote PowerShell parent: **`wsmprovhost.exe`**.
- DCSync account: **`backupda`**.
- Ransomware URL: **`http://ff.sillytechninja.io/ransomboogey.exe`**.
- Scheduled task name: **not yet established**.

## 8. Recommended response actions
1. Preserve original event JSON and validate timestamps/timezone; narrow the search range to 29–31 August 2023.
2. Isolate affected hosts if this were a live environment; preserve memory and disk artefacts before cleanup where feasible.
3. Block and investigate `165.232.170.151` and the ransomware-download domain/URL using approved controls.
4. Rotate affected credentials, invalidate sessions, and review privileged account usage; do not reuse lab credentials outside the exercise.
5. Review PowerShell, WinRM, SMB, scheduled-task, process-creation, and domain-controller audit logs.
6. Verify whether `ransomboogey.exe` was created or executed and whether files were modified or encrypted.
7. Restore only from verified clean backups if impact is confirmed.

## 9. Limitations
This report is based on screenshots rather than raw event exports. Some command-line fields are truncated in Discover. Hit counts are not proof of execution or impact. The scheduled-task name remains unresolved, UAC elevation is not proven, and ransomware execution/encryption is not established by the supplied evidence.
