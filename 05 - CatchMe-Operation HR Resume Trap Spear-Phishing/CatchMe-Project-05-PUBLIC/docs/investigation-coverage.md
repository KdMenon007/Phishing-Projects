# Investigation Coverage --- Operation HR Resume Trap: Spear-Phishing Investigation

This document highlights the forensic areas investigated in this case.
It is not a question-and-answer worksheet; record validated findings in
the incident report, evidence register, and timeline.

## Email and Attachment Analysis

-   **Sender identity and email routing:** review `From`, `To`,
    `Reply-To`, `Return-Path`, `Received`, and authentication headers
    where present.
-   **Victim mailbox:** identify the intended recipient from the
    original message headers.
-   **Malicious attachment identification:** establish the exact
    attachment filename and MIME type.
-   **File integrity:** calculate and record MD5 and SHA-256 hashes of
    the extracted attachment.
-   **Macro behaviour:** inspect the document statically for download
    URLs, commands, and execution logic. Never execute the suspicious
    document.

## Stage 2 Payload and Process Execution

-   **Payload retrieval:** identify the URL used by the document or
    macro to retrieve the next stage.
-   **Execution process:** determine which process executed the stage 2
    payload.
-   **Process lineage:** record process name, full image path, PID, and
    parent PID.
-   **Payload path:** establish the full on-disk path of the stage 2
    payload using corroborating evidence.

## Secondary Payload and Command-and-Control

-   **Binary delivery:** identify the URL used to download the malicious
    binary.
-   **C2 process:** determine the process associated with the C2
    connection.
-   **Process identity:** record the relevant PID and full executable
    path.
-   **Network indicator:** record the observed C2 IP address and port in
    `IP:port` format.
-   **Correlation:** correlate process, memory, and network artefacts
    before attributing a connection to malware.

## Memory Forensics and Attachment Trace

-   **Artefact validation:** verify the actual format of
    `WKSTN-2961.raw` before choosing a forensic workflow.
-   **Attachment path:** determine the full path of the malicious email
    attachment as represented in the workstation artefacts.
-   **Process and memory evidence:** preserve relevant command lines,
    paths, process identifiers, and timestamps.

## Persistence

-   **Scheduled-task activity:** identify the task-related evidence
    associated with persistence.
-   **Full persistence command:** record the exact command used to
    create or execute the scheduled task.
-   **Timeline correlation:** compare task creation with the observed C2
    callback and other activity; do not infer timing without supporting
    timestamps.

## Evidence and Reporting Standards

-   Record exact values rather than paraphrasing paths, commands, PIDs,
    hashes, or URLs.
-   Cite a source file, command output, screenshot, or log for every
    material finding.
-   Label each finding as **Confirmed**, **Inferred**, or **Not
    established**.
-   Distinguish a command being present or attempted from proof that it
    completed successfully.
-   Include relevant screenshots in `screenshots/` and reference them in
    the incident report.
-   Map behaviours to MITRE ATT&CK only when supported by evidence.


## Static macro triage

- [x] Confirm the file is a legacy Word OLE document.
- [x] Record `oleid` flag indicating suspicious VBA macros.
- [x] Record `olevba -a` indicators and filenames shown.
- [ ] Review full VBA source statically to confirm exact URLs, commands, and payload behavior.
- [ ] Correlate any macro indicators with workstation telemetry before asserting execution or C2.


## Confirmed static macro chain

- [x] `AutoOpen` macro entry point present in `NewMacros.bas`.
- [x] HTTP GET URL recovered from the displayed macro source.
- [x] Macro source writes response body to `C:\ProgramData\update.js`.
- [x] Macro source invokes `wscript.exe C:\ProgramData\update.js`.
- [ ] Verify whether the URL was contacted and the file was created on the endpoint.
- [ ] Identify process IDs, parent process, execution timestamps, and network/C2 evidence from workstation telemetry.
- [ ] Do not infer successful execution from macro source alone.


## Workstation artefact format validation

- [x] Record initial `file` result and header/string inspection screenshots.
- [ ] Inspect partition table and filesystem offsets before selecting a parser.
- [ ] Determine whether the artefact is a disk image, event trace, or another container.
- [ ] Only then select appropriate forensic tooling and correlate endpoint activity.


## Targeted memory triage

- [x] Volatility `windows.info` recognizes the image as 64-bit Windows 10 build 18362.
- [x] Initial strings search surfaced a cached resume-document path and a candidate HTTP URL.
- [ ] Correlate the candidate URL with `windows.netscan` output.
- [ ] Identify relevant processes and parent/child relationships with `windows.pstree`.
- [ ] Inspect process command lines with `windows.cmdline`.
- [ ] Verify scheduled-task persistence and exact command from memory structures or other corroborating evidence.


## Correlated memory-forensics findings

- [x] Outlook PID 1440 launched/opened Word PID 1124 in the observed process tree.
- [x] Word PID 1124 is the parent of `wscript.exe` PID 4260.
- [x] `wscript.exe` command line references `C:\ProgramData\update.js`.
- [x] `updater.exe` PID 6216 is a child of `wscript.exe` and runs from `C:\Windows\Tasks\updater.exe`.
- [x] `windows.netscan` shows repeated connections attributed to PID 6216 to `128.199.95.189:8080`; displayed states are `CLOSED`.
- [ ] Extract and inspect the JavaScript from memory or recover it from the relevant evidence.
- [ ] Determine the exact scheduled-task creation command and persistence artefact.
- [ ] Confirm the stage-two download URL from the script content and correlate it to the process/network evidence.
- [ ] Identify the PID associated with any separate C2 process only if additional evidence supports one; current output attributes the candidate endpoint to PID 6216 (`updater.exe`).
