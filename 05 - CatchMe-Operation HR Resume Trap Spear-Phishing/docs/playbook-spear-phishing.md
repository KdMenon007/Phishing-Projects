# Playbook — Spear-Phishing Attachment Investigation

**Project:** CatchMe Project 05 — Operation Resume Trap  
**Purpose:** Standardize triage and response to a suspected spear-phishing email that delivers a macro-enabled Office document or other malicious attachment.  
**Audience:** SOC Analyst L1/L2, Incident Responder  
**Status:** Lab playbook; adapt to the organization's approved procedures before production use.

## 1. Trigger

Use this playbook when one or more of the following occur:
- A suspicious resume, invoice, HR, or job-application email is reported.
- An Office document contains suspicious VBA or auto-execution behavior.
- Office spawns a script interpreter such as `wscript.exe`, `cscript.exe`, PowerShell, or a command shell.
- A script or Office child process downloads or launches an unexpected executable.
- A host communicates with an untrusted or unexplained external endpoint after opening an attachment.

## 2. Initial triage

1. Record the alert source, detection time, affected user, hostname, and reporter.
2. Preserve the original email as `.eml`, including full headers.
3. Record sender, recipient, subject, timestamps, message ID, and authentication results.
4. Extract attachments to a controlled evidence directory without opening or executing them.
5. Calculate SHA-256 and MD5 hashes; record file size and detected file type.
6. Treat sender authentication results as one signal only; SPF/DKIM/DMARC pass does not prove the message is benign.
7. Assign severity using business impact, execution evidence, payload behavior, and confirmed communications.

## 3. Attachment analysis

1. Identify the actual file format; do not trust the extension alone.
2. For legacy Office files, use static analysis tools such as `oleid` and `olevba`.
3. Record macro names, auto-execution routines, suspicious APIs/keywords, URLs, filenames, paths, and commands.
4. Never enable macros or run the attachment on a normal workstation.
5. If dynamic analysis is required, use an isolated, disposable lab with controlled networking and a documented authorization.
6. Correlate extracted indicators with endpoint, proxy, DNS, firewall, and memory evidence.

## 4. Endpoint and memory investigation

Collect or review, as authorized:
- Process tree and parent/child relationships.
- Process command lines, creation times, PIDs, and image paths.
- Office spawning script interpreters or shells.
- Files created in user-writable or unusual paths, including `%ProgramData%` and task-related directories.
- Network connections attributed to suspicious processes.
- Scheduled-task creation and task definitions.
- Relevant event logs, EDR telemetry, and memory artifacts.

For memory evidence, record the tool/version and exact command used. A string match alone is a lead, not proof of execution. Correlate at least two independent evidence sources where possible.

## 5. Containment

Follow the organization's incident authority and approval process:
1. Isolate the affected endpoint using EDR or approved network controls if active compromise is suspected.
2. Preserve volatile evidence when feasible and authorized before shutdown or remediation.
3. Block confirmed malicious domains/IPs/URLs and file hashes at appropriate controls, after checking for shared infrastructure and business impact.
4. Quarantine the email and search for other recipients or matching messages.
5. Disable or reset affected credentials only when evidence or policy warrants it; prioritize suspected credential theft.
6. Record every action, approver, timestamp, and result.

## 6. Eradication and recovery

1. Identify and remove confirmed malicious files, scripts, scheduled tasks, and persistence mechanisms through approved response procedures.
2. Reimage or restore the host if integrity cannot be established.
3. Patch the exploited application or control weakness and update detections.
4. Validate endpoint health, persistence removal, and absence of renewed suspicious traffic.
5. Return the host to service only with incident-owner approval.

## 7. Closure criteria

Close only when:
- The email and attachment have been documented and hashed.
- Execution chain and relevant indicators have been assessed.
- Network and persistence findings are recorded, including unresolved limitations.
- Containment and recovery actions have been validated.
- Required stakeholders have been notified.
- Detection improvements and lessons learned have owners.

## 8. Required evidence fields

Email sender/recipient/subject/time; attachment name/type/size/hashes; host/user; process names/PIDs/PPIDs/paths/commands; URLs/IPs/ports/timestamps; persistence mechanism; containment actions; analyst; tool versions; evidence references; confidence and unresolved questions.

## 9. Current lab case note

For this case, Volatility output supports the observed chain:
`OUTLOOK.EXE` PID 1440 → `WINWORD.EXE` PID 1124 → `wscript.exe` PID 4260 running `C:\ProgramData\update.js` → `updater.exe` PID 6216 at `C:\Windows\Tasks\updater.exe`.

Repeated `windows.netscan` records attribute connections to `128.199.95.189:8080` to PID 6216, with the displayed state `CLOSED`. Treat this as a strong suspicious endpoint lead pending further corroboration. Do not mark the investigation complete until the attachment, download URL, persistence mechanism, and remaining requested findings have been validated or explicitly marked unresolved.
