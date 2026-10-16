# CatchMe Project 05 — Detection and Response Playbook

## Objective
Detect and investigate suspicious resume-themed email attachments,
Office-to-script execution, scheduled-task persistence, hidden PowerShell,
and outbound communication associated with the investigated indicators.

## Detection 1 — Office Spawning Script Interpreters
Look for WINWORD.EXE spawning wscript.exe, cscript.exe, powershell.exe,
or other unexpected child processes.

Windows telemetry:
- Sysmon Event ID 1 — Process creation
- Security Event ID 4688 — Process creation, if enabled

Investigate parent process, child process, command line, user, file path,
timestamp, and related network activity.

## Detection 2 — Suspicious Scheduled Task
Hunt for a task named Updater and tasks that launch hidden PowerShell
or read encoded commands from user registry locations.

Windows telemetry:
- Security Event ID 4698 — Scheduled task created, if enabled
- Microsoft-Windows-TaskScheduler/Operational logs
- Sysmon process-creation events

Do not rely on task name alone; validate task action and execution history.

## Detection 3 — Suspicious Script and Payload Paths
Investigate these observed paths:
- C:\ProgramData\update.js
- C:\Windows\Tasks\updater.exe

Correlate file creation, process execution, Prefetch, antivirus detections,
and endpoint telemetry. Validate hashes before containment decisions.

## Detection 4 — Network Indicators
Investigate:
- 128.199.95.189:8080
- files.boogeymanisback.lol
- /news.php
- /aa2a9c53cbb80416d3b47d85538d9971/update.png

Search DNS, proxy, firewall, EDR, and network telemetry. These are
investigation indicators, not proof that every connection succeeded.
Check for other hosts communicating with the same infrastructure.

## Detection 5 — PowerShell Defense-Evasion Indicators
Review PowerShell script-block and process logs for suspicious access to
AMSI internals, PowerShell ETW provider fields, Base64 decoding, and IEX.

Relevant telemetry may include:
- PowerShell Operational Event ID 4104, if script-block logging is enabled
- Event ID 4103, if module logging is enabled
- Sysmon Event ID 1, if process creation is configured

Logging may be incomplete or absent; absence of an event does not prove
the behavior did not occur.

## Triage Procedure
1. Confirm the host, user, event time, and affected process.
2. Preserve volatile and non-volatile evidence according to policy.
3. Validate email and attachment hashes.
4. Reconstruct the process tree and correlate file and network activity.
5. Inspect scheduled tasks and relevant registry locations.
6. Search enterprise telemetry for the same indicators.
7. Determine scope, persistence, credential exposure, and potential impact.
8. Record confidence and distinguish confirmed findings from hypotheses.

## Containment
- Isolate the endpoint according to incident-response policy.
- Block confirmed malicious indicators at suitable network controls.
- Prevent further execution of the document and associated payloads.
- Protect potentially exposed accounts and credentials where warranted.
- Preserve evidence before deleting files or persistence artifacts.

## Eradication and Recovery
- Remove confirmed malicious tasks, scripts, binaries, and related artifacts
  after evidence collection and authorization.
- Investigate and remediate the initial email-delivery path.
- Restore from a trusted state if endpoint integrity cannot be established.
- Re-enable or validate security controls and logging.
- Monitor for recurring task creation, suspicious PowerShell, and C2 traffic.

## Closure Criteria
- Scope and affected assets documented.
- Evidence and hashes preserved.
- Persistence removed or otherwise remediated.
- Credentials and access reviewed where relevant.
- Detection coverage validated.
- Recovery confirmed and limitations documented.
