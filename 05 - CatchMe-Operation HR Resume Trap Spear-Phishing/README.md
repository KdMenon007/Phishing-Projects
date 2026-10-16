# CatchMe Project 05 --- Operation Resume Trap

**Scenario:** HR-themed spear-phishing investigation based on the
TryHackMe Boogeyman 2 room.\
**Status:** In progress. Findings must be validated against the supplied
artefacts.

## Executive Summary

Static analysis of the resume attachment identified an `AutoOpen` VBA macro that requests remote content, writes the response to `C:\ProgramData\update.js`, and launches it through Windows Script Host. Memory evidence shows `OUTLOOK.EXE` → `WINWORD.EXE` → `wscript.exe` → `updater.exe` and repeated closed socket records to `128.199.95.189:8080`. A recovered `\Updater` scheduled task runs hidden PowerShell that Base64-decodes and executes a registry value named `debug`. That value was not recovered, so its final payload remains unknown. See `outputs/confirmed-findings.txt` and `docs/incident-response-report.md` for evidence and limitations.
## Artefacts

  -----------------------------------------------------------------------------------------------------------------------------------------
  Artefact                                     Initial SHA-256                                                      Notes
  -------------------------------------------- -------------------------------------------------------------------- -----------------------
  `Junior IT Analyst Resume Application.eml`   `88d7090d0a9f7115ce9f76a2c82f6d4843cdf655fba09e0f0c50e4eddd554fce`   RFC 822 email

  `WKSTN-2961.raw`                             `c0daf36eac4d1d2ff1a328bec21bcf73a2b3c958735d127319a1552d75dc9266`   `file` identified it as
                                                                                                                    a Windows Event Trace
                                                                                                                    Log; validate format
                                                                                                                    before selecting tools
  -----------------------------------------------------------------------------------------------------------------------------------------

Recalculate hashes after copying to verify integrity.

## Confirmed Email Header Findings

-   **From:** `westaylor23@outlook.com`
-   **To:** `maxine.beck@quicklogisticsorg.onmicrosoft.com`
-   **Subject:** `Resume - Application for Junior IT Analyst Role`
-   **Date:** `Sun, 20 Aug 2023 18:19:20 +0000`

These are observed header values; they do not alone prove the sender's
identity or successful execution of an attachment.

## Workflow

1.  Preserve originals and record hashes.
2.  Parse email headers and MIME structure.
3.  Extract attachments to a separate directory; never execute
    suspicious files.
4.  Validate the workstation artefact format.
5.  Investigate process, payload, network, and persistence evidence with
    suitable tools.
6.  Record commands, timestamps, output, and screenshot references.
7.  Map confirmed findings to MITRE ATT&CK.
8.  Document limitations and distinguish facts from hypotheses.

## Evidence Handling

Keep originals unchanged. Store derived artefacts separately. Record
evidence source, hashes, collection method, and notes in
`evidence/evidence-register.csv`. Do not publish raw memory/email
artefacts or suspicious binaries unless redistribution is authorized.

## Project Structure

-   `evidence/` --- evidence register and local analysis logs
-   `scripts/` --- helper scripts
-   `screenshots/` --- screenshots
-   `docs/` --- question tracker, timeline, ATT&CK worksheet
-   `reports/` --- incident report

The core chain is documented from analyst-provided tool output. Do not publish original email/memory artefacts or suspicious binaries. Review `docs/incident-response-report.md` for unresolved limitations before presenting the case as closed.
