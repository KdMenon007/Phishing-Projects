# CatchMe Project 05 — Operation HR Resume Trap
## Incident Response Investigation Report

### 1. Executive Summary
A spear-phishing email delivered a malicious Word document targeting a
Junior IT Analyst applicant workflow. Static analysis identified an
AutoOpen macro that retrieves remote content, writes it to
C:\ProgramData\update.js, and launches it using wscript.exe.

Memory analysis identified the process chain Outlook.exe → WINWORD.exe
→ wscript.exe → updater.exe. A scheduled task named Updater was recovered.
Its action executes hidden PowerShell that retrieves a Base64-encoded
script from the current user's registry value named debug.

### 2. Severity Assessment
Assessment: HIGH, pending environment-specific impact validation.

Rationale:
- Malicious document execution chain identified.
- Script execution through Windows Script Host and PowerShell.
- Scheduled-task persistence identified.
- Suspicious outbound communication associated with updater.exe.
- Potential attempts to interfere with AMSI and PowerShell ETW logging.

This assessment is based on available artifacts, not a confirmed assessment
of business impact or successful defense-evasion techniques.

### 3. Email and Attachment Evidence
Email subject: Resume - Application for Junior IT Analyst Role
Sender: [REDACTED_SENDER_EMAIL]
Recipient: [REDACTED_RECIPIENT_EMAIL]

Email SHA-256:
88d7090d0a9f7115ce9f76a2c82f6d4843cdf655fba09e0f0c50e4eddd554fce

Attachment: Resume_WesleyTaylor.doc
Attachment SHA-256:
4db25ee3c46be38aa219fe2192711af65d55d5d7e25a889bb9990beb19f9b8b0

The document contains an AutoOpen macro using Microsoft.XMLHTTP and
ADODB.Stream to retrieve remote content, save it as update.js, and launch
it through wscript.exe.

### 4. Process and Execution Findings
Memory process-tree evidence identified:
- OUTLOOK.EXE, PID 1440
- WINWORD.EXE, PID 1124
- wscript.exe, PID 4260
- updater.exe, PID 6216
- conhost.exe, PID 4464

Observed updater image path:
C:\Windows\Tasks\updater.exe

The process relationship supports the suspected document-to-script-to-
payload execution chain.

### 5. Persistence Findings
Recovered scheduled task: \Updater
Author: [REDACTED_DOMAIN]\[REDACTED_USER]

The task executes:
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

Arguments retrieve the HKCU registry value named debug from:
HKCU\Software\Microsoft\Windows\CurrentVersion

The value is Base64-decoded as Unicode/UTF-16LE and passed to IEX.
The task XML indicates hidden, non-interactive PowerShell execution.

The registry value contents were not recovered during this investigation.
The complete payload therefore remains unknown.

### 6. Network and Script Indicators
Observed C2 candidate:
http://128.199.95.189:8080

Observed HTTP path:
 /news.php

Other URL recovered from the document macro:
https://files.boogeymanisback.lol/aa2a9c53cbb80416d3b47d85538d9971/update.png

Observed filenames:
- update.js
- updater.exe

Memory network records associate updater.exe with 128.199.95.189:8080.
The recovered socket records show CLOSED states; they do not prove an
active connection at the time of analysis.

A partially recovered PowerShell fragment contains code attempting to
modify AMSI-related state and PowerShell ETW logging state. This supports
an attempted defense-evasion interpretation, but successful bypass or
logging suppression has not been established.

### 7. Evidence Hashes
Original memory image WKSTN-2961.raw SHA-256:
c0daf36eac4d1d2ff1a328bec21bcf73a2b3c958735d127319a1552d75dc9266

Updater data-section dump SHA-256:
8e82c6c1a860383f3c79838b7979b18f74cd0b001894d8b75e2f6f581fe51a55

Updater image-section dump SHA-256:
ade8c752735e24b3dfa6e99e8f4324af2fb52316baf27e789f845f427952a077

### 8. MITRE ATT&CK Mapping
Potentially relevant techniques:
- T1566.001 — Spearphishing Attachment
- T1059.005 — Visual Basic
- T1059.007 — JavaScript/JScript
- T1059.001 — PowerShell
- T1053.005 — Scheduled Task/Job: Scheduled Task
- T1105 — Ingress Tool Transfer
- T1071.001 — Web Protocols
- T1562.001 — Impair Defenses

Mappings are based on observed artifacts and should be treated as
investigative classifications, not proof that every technique succeeded.

### 9. Response Recommendations
1. Isolate the affected endpoint if it is still operational and at risk.
2. Preserve memory, disk, email, attachment, task XML, and relevant logs.
3. Block or investigate the identified URLs and IP at appropriate controls.
4. Remove the malicious scheduled task and payload only after evidence
   preservation and authorization.
5. Investigate the registry debug value, task history, PowerShell logs,
   process creation logs, Prefetch, and endpoint telemetry.
6. Search the environment for the hashes, paths, task name, URLs, and IP.
7. Reset potentially exposed credentials and review account activity
   if evidence supports credential exposure.
8. Validate recovery with endpoint monitoring and follow-up hunts.

### 10. Limitations
- The registry debug value payload was not recovered.
- The recovered PowerShell fragment is truncated.
- The available network records show closed sockets.
- Successful AMSI/ETW tampering and the full C2 exchange are unconfirmed.
- No conclusion about data exfiltration or business impact is made
  from the currently available evidence.

### 11. Conclusion
Available artifacts support a malicious-document execution chain,
suspicious payload activity, scheduled-task persistence, and C2-related
indicators. The incident should be treated as high priority for response
and further validation. Unrecovered payload content and unconfirmed
behavior are explicitly retained as investigation limitations.
