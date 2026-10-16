# Incident Response Report — Operation Resume Trap

## 1. Case information
- **Project:** CatchMe Project 05 — Operation Resume Trap: Spear-Phishing Against HR
- **Scenario:** HR-themed resume phishing / Boogeyman 2 investigation
- **Status:** Core attack chain and persistence mechanism identified; some payload and registry details remain unverified.
- **Analysis approach:** Static document analysis and offline memory-artifact examination. The suspicious document was not executed.

## 2. Executive summary
A resume-themed email was sent to an HR recipient at Quick Logistics. Static analysis of `Resume_WesleyTaylor.doc` identified an `AutoOpen` VBA macro that requests remote content from a URL ending in `/update.png`, writes the response body to `C:\ProgramData\update.js`, and invokes the script with Windows Script Host. Memory analysis independently showed `OUTLOOK.EXE` → `WINWORD.EXE` → `wscript.exe` (`C:\ProgramData\update.js`) → `updater.exe` (`C:\Windows\Tasks\updater.exe`) → `conhost.exe`. Network artifacts associated the updater process with repeated closed socket records to `128.199.95.189:8080`. A recovered `\Updater` scheduled-task definition runs hidden PowerShell that reads, Base64-decodes, and executes a registry value named `debug` under the current user's registry hive. The registry value's content was not recovered, so its decoded payload remains unknown.

## 3. Scope and evidence
See `../evidence/evidence-register.csv` and `../outputs/confirmed-findings.txt`. Original email SHA-256: `88d7090d0a9f7115ce9f76a2c82f6d4843cdf655fba09e0f0c50e4eddd554fce`. Original attachment MD5: `52c4384a0b9e248b95804352ebec6c5b`; SHA-256: `4db25ee3c46be38aa219fe2192711af65d55d5d7e25a889bb9990beb19f9b8b0`.

## 4. Initial email and document analysis
- Sender: `[REDACTED_SENDER_EMAIL]`
- Recipient: `[REDACTED_RECIPIENT_EMAIL]`
- Subject: `Resume - Application for Junior IT Analyst Role`
- Date: `Sun, 20 Aug 2023 18:19:20 +0000`
- Attachment: `Resume_WesleyTaylor.doc`
- Macro: `AutoOpen` uses `Microsoft.XMLHTTP` to GET `https://files.boogeymanisback.lol/aa2a9c53cbb80416d3b47d85538d9971/update.png`, writes `responseBody` to `C:\ProgramData\update.js` using `ADODB.Stream`, and executes `wscript.exe C:\ProgramData\update.js` via `WScript.Shell`.
- SPF/DKIM/DMARC reportedly passed for outlook.com. This does not establish that the message was benign or that the sender's intent was legitimate.

## 5. Execution chain
| Stage | Process / artifact | Evidence | Confidence |
|---|---|---|---|
| Delivery | Resume-themed `.eml` and `.doc` | Email headers and original attachment analysis | High |
| Macro behavior | `AutoOpen` → HTTP GET → write `update.js` → `wscript.exe` | `olevba -c -d` source output | High for intended code behavior |
| Document execution | `OUTLOOK.EXE` PID 1440; `WINWORD.EXE` PID 1124 | Memory process tree and cached attachment path | High |
| Script execution | `wscript.exe` PID 4260, `C:\ProgramData\update.js` | Memory process tree / command-line output | High |
| Follow-on payload | `updater.exe` PID 6216, `C:\Windows\Tasks\updater.exe` | Process tree, command line, file scan and dump | High |
| Console child | `conhost.exe` PID 4464 | Memory process tree | High |

## 6. Payload delivery and network
- **Macro URL:** `https://files.boogeymanisback.lol/aa2a9c53cbb80416d3b47d85538d9971/update.png`
- **Observed network destination:** `128.199.95.189:8080`
- **Associated process:** `updater.exe`, PID 6216
- **Network state:** Multiple `CLOSED` socket records in memory output, dated 2023-08-21 14:14:13–14:16:11 as reported by the tool; timezone not established.
- **Recovered strings:** `Invoke-Empire`, `EmpireStager`, `PowershellEmpire`, `DotNetEmpire`, `Sharpire`, `RunPowerShell`, `stage2Response`, `FromBase64String`, `CreateDecryptor`, `CreateEncryptor`, plus web paths.
- **Assessment:** Strongly suspicious payload and network indicators. Strings alone do not prove which framework was executed, which URL delivered the updater, or the full command-and-control protocol.

## 7. Persistence
Recovered scheduled-task XML identifies URI `\Updater`, author/user `[REDACTED_DOMAIN]\[REDACTED_USER]`, enabled daily trigger beginning `2023-08-21T09:00:00`, and registration time `2023-08-21T15:14:03` (timezone unverified). The task launches PowerShell with `-NonI -W hidden -c` and runs an expression that retrieves `HKCU:\Software\Microsoft\Windows\CurrentVersion` value `debug`, Base64-decodes it as Unicode, then invokes it using `IEX`. The task is configured with `InteractiveToken` and `LeastPrivilege`. The value contents were not recovered; the final payload is unknown.

## 8. Timeline
See `timeline.csv`. Timestamps are retained as reported and are not asserted to be UTC unless the source explicitly supplies a UTC offset.

## 9. MITRE ATT&CK mapping (supported behaviors)
- **T1566.001 — Spearphishing Attachment:** resume-themed email with malicious document.
- **T1204.002 — User Execution: Malicious File:** Word document execution is supported by memory process evidence; exact user interaction is inferred from the chain.
- **T1059.005 — Visual Basic:** VBA macro source contains the execution logic.
- **T1105 — Ingress Tool Transfer:** macro code downloads remote content; successful transfer is not independently verified from source code alone.
- **T1059.007 — JavaScript/JScript:** `wscript.exe` executes a `.js` path, supported by process evidence.
- **T1053.005 — Scheduled Task/Job: Scheduled Task:** recovered enabled `\Updater` task definition.
- **T1059.001 — PowerShell:** scheduled-task action invokes PowerShell with hidden execution of a registry-stored value.
- **T1027 — Obfuscated Files or Information:** Base64 decoding and suspicious encoded/obfuscated strings are present; use this as a behavior mapping, not proof of a particular obfuscator.

## 10. Response recommendations
1. Isolate the affected workstation and preserve memory/disk evidence under incident-response procedures.
2. Block and hunt for the observed URL, domain, IP:port, file paths, process names, and scheduled-task URI across relevant telemetry, subject to organizational policy.
3. Remove the malicious scheduled task and payload only after evidence preservation and approval.
4. Inspect the relevant user's registry hive for the `debug` value; export the key/value safely and decode offline in a controlled environment.
5. Review Office child processes, Windows Script Host, PowerShell, scheduled-task creation, and outbound connections around the incident window.
6. Reset potentially exposed credentials and review account activity if investigation supports possible credential access.
7. Improve controls for macro-enabled documents, script execution, application control, and attachment sandboxing.

## 11. Limitations
- Original document was statically analyzed and not executed.
- The remote URL's response was not independently retrieved or validated.
- The `HKCU` registry value `debug` was not recovered; its decoded command/payload is unknown.
- The SOFTWARE hive could not be parsed from the available artifact; the scheduled-task plugin failed, so task XML was recovered from file scan/dump artifacts.
- `WKSTN-2961.raw` was identified by `file` as a Windows Event Trace Log, although Volatility parsed it as a memory image. Preserve this format ambiguity in reporting.
- Memory network timestamps and task XML timestamps have not been normalized to UTC.
- Memory-dumped executable-section hashes are not asserted to be hashes of the original on-disk file.

## 12. Conclusion
Evidence supports a malicious resume-document chain using VBA to stage and launch `update.js`, followed by `updater.exe`, suspicious outbound socket records, and a scheduled-task persistence mechanism. The precise registry-stored persistence payload and the full remote payload delivery relationship remain unresolved. The investigation should be described as substantially evidenced but not fully closed until those gaps are either resolved or explicitly accepted as limitations.
