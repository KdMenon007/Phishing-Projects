# Runbook — CatchMe Project 05 Evidence Collection

**Project:** Operation Resume Trap — Spear Phishing Against HR  
**Environment:** Kali Linux analyst workstation; authorized TryHackMe lab artifacts  
**Goal:** Repeatable, evidence-led investigation with commands and screenshots suitable for a portfolio report.

> Run these commands only against the authorized lab artifacts. Do not execute the suspicious attachment or publish raw memory/email evidence to a public repository.

## 1. Prepare a case workspace

```bash
mkdir -p ~/Desktop/CatchMe-Project-05/{evidence,outputs,screenshots}
cd ~/Desktop
```

Keep the original files unchanged. Store working copies separately and record hashes.

```bash
sha256sum "Junior IT Analyst Resume Application.eml" \
  "Resume_WesleyTaylor.doc" WKSTN-2961.raw
md5sum "Resume_WesleyTaylor.doc"
file "Junior IT Analyst Resume Application.eml" \
  "Resume_WesleyTaylor.doc" WKSTN-2961.raw
```

## 2. Static email and attachment analysis

If the project helper script is available in the extracted repository, run it from the repository root:

```bash
python3 scripts/extract_email_attachments.py \
  "Junior IT Analyst Resume Application.eml" evidence/extracted
```

If the helper is not in the current directory, change to the project repository first; do not assume `scripts/` exists on `~/Desktop`.

Analyze the extracted Office document statically:

```bash
oleid "Resume_WesleyTaylor.doc"
olevba -a "Resume_WesleyTaylor.doc" | tee outputs/olevba-analysis.txt
olevba "Resume_WesleyTaylor.doc" | tee outputs/olevba-source.txt
```

Record the attachment hash, macro names, URLs, file paths, and commands. Do not enable editing/content or run macros.

## 3. Validate and inspect the memory image

```bash
file WKSTN-2961.raw
sha256sum WKSTN-2961.raw
vol -f WKSTN-2961.raw windows.info | tee outputs/volatility-info.txt
```

If `windows.info` recognizes the image, run targeted plugins:

```bash
vol -f WKSTN-2961.raw windows.pstree | tee outputs/pstree.txt
vol -f WKSTN-2961.raw windows.cmdline | tee outputs/cmdline.txt
vol -f WKSTN-2961.raw windows.netscan | tee outputs/netscan.txt
```

Filter existing output files for review, avoiding unnecessary repeated full plugin runs:

```bash
grep -Ei -C 3 'winword|wscript|powershell|cmd\.exe|schtasks|updater\.exe' outputs/pstree.txt
grep -Ei -C 2 'update\.js|ProgramData|updater\.exe|schtasks|https?://' outputs/cmdline.txt
grep -Ei '128\.199\.95\.189|:8080' outputs/netscan.txt
```

If needed, perform a targeted file-object scan:

```bash
vol -f WKSTN-2961.raw windows.filescan |
grep -Ei 'update\.js|Resume_WesleyTaylor|updater\.exe|TaskCache|\.job' |
tee outputs/filescan-filtered.txt
```

## 4. Current observed leads

From the captured output:
- Outlook PID `1440` opened the `.eml`.
- Word PID `1124`, parent PID `1440`, opened the cached resume document.
- `wscript.exe` PID `4260`, parent PID `1124`, ran `C:\ProgramData\update.js`.
- `updater.exe` PID `6216`, parent PID `4260`, ran from `C:\Windows\Tasks\updater.exe`.
- Multiple network records associate PID `6216` with `128.199.95.189:8080`; the displayed connection states were `CLOSED`.

These are evidence-backed observations from the current screenshots. The download URL, scheduled-task command, and full attachment path from memory still require corroboration.

## 5. Evidence and screenshot naming

Save terminal output to text files with `tee` where possible. Capture screenshots showing the command and relevant output, without cropping out context needed to understand the result.

Suggested names:
- `16-volatility-process-tree.png`
- `17-volatility-command-lines.png`
- `18-volatility-network-connections.png`
- Continue sequentially for later findings.

Update `evidence/evidence-register.csv`, `docs/timeline.csv`, and the incident response report as findings are validated. Record UTC timestamps and tool versions.

## 6. Public GitHub safety checklist

Before publishing:
- Exclude raw memory images, original suspicious email, and attachment binaries unless you have explicit permission and a safe, intentional distribution plan.
- Check `.gitignore` and run `git status --short`.
- Remove personal data, secrets, tokens, credentials, and unrelated host information from screenshots and logs.
- Publish sanitized reports, detection logic, redacted screenshots, hashes, and lab methodology.
- Label unresolved values as `Pending` or `Not established`; never invent missing findings.
