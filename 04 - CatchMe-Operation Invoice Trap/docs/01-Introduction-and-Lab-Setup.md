# Phase 01 — Introduction & Lab Setup

## 1. Project Overview

**Project name:** CatchMe Project 01 — Operation Invoice Trap  
**Investigation type:** Multi-stage phishing investigation and attack-chain reconstruction  
**Target organization:** Quick Logistics LLC  
**Target employee:** Julianne Westcott, Finance  
**Apparent business partner:** B Packaging Inc.  
**Apparent sender:** Arthur Griffin (`agriffin@bpackaging.xyz`)  
**Investigation environment:** Authorized TryHackMe lab

Operation Invoice Trap investigates an invoice-themed email and its associated endpoint and network artefacts. The goal is to reconstruct what happened using evidence from the email, PowerShell event logs, and packet capture rather than assuming the attack chain from the scenario description.

## 2. Incident Scenario

Julianne Westcott, a finance employee at Quick Logistics LLC, receives an email with the subject **“Collection for Quick Logistics LLC - Jan 2023”**. The message refers to an unpaid invoice, gives a due date, and asks the recipient to open an attached ZIP archive named `Invoice.zip`. The message also provides a password for an encrypted file.

The sender display name is Arthur Griffin, identified in the message as a Collections Officer at B Packaging Inc. These details establish the scenario and provide leads for investigation; they do not, by themselves, prove sender impersonation or malicious execution.

## 3. Investigation Objectives

- Inspect the email's visible content and raw headers.
- Review sender, reply-to, return-path, SPF, DKIM, and DMARC information.
- Safely identify the attachment and record its metadata and cryptographic hash.
- Examine PowerShell telemetry for suspicious commands and execution evidence.
- Analyze packet-capture data for DNS lookups, network connections, and possible payload or command-and-control traffic.
- Correlate observations into a timestamped attack timeline.
- Map only evidence-supported behavior to MITRE ATT&CK.
- Document detection opportunities and incident-response recommendations.
- Produce a concise executive summary and a technically reproducible report.

## 4. Scope

### In scope

- The provided `dump.eml` email artefact.
- The provided `powershell.json` PowerShell event-log export.
- The provided `capture.pcapng` packet capture.
- Derived indicators, timestamps, analysis notes, screenshots, detection ideas, and recommendations based on those artefacts.

### Out of scope

- Contacting any external sender, domain, or IP address.
- Opening or executing the attachment on a normal workstation.
- Testing systems outside the authorized lab.
- Claiming a real-world compromise or business impact beyond what the evidence establishes.
- Publishing raw artefacts that contain sensitive information or are not authorized for redistribution.

## 5. Evidence Inventory

| Artefact | Description | Planned use |
|---|---|---|
| `dump.eml` | Email message with headers, body, and attachment representation/metadata | Email and attachment analysis |
| `powershell.json` | JSON-formatted PowerShell logs extracted from Windows event logs | Endpoint execution investigation |
| `capture.pcapng` | Packet capture from the affected workstation | Network traffic analysis |

Record the original file names, sizes, SHA-256 hashes, and collection location before analysis. Keep original artefacts unchanged and perform analysis on working copies where possible.

## 6. Tools

- **Thunderbird / text tools:** Inspect the email and MIME structure.
- **`file`, `sha256sum`, `grep`, `sed`:** Identify artefacts, calculate hashes, and inspect text.
- **`jq`:** Parse and filter `powershell.json`.
- **Wireshark:** Interactive packet inspection.
- **TShark:** Command-line packet filtering and extraction of metadata.
- **Python and archive utilities:** Inspect file metadata or archive structure safely when required.
- **MITRE ATT&CK:** Classify observed adversary behaviors.
- **SIEM query language:** Develop detection examples only after confirming the relevant schema and fields.

Tool availability and versions should be recorded during setup. Do not assume a particular SIEM data model until it is known.

## 7. Lab Architecture

The investigation uses three evidence sources associated with the same scenario:

1. **Email layer** — identifies the lure, sender information, links, and attachment.
2. **Endpoint layer** — provides PowerShell activity that may reveal execution or follow-on behavior.
3. **Network layer** — provides packet-level observations that may corroborate endpoint events.

The layers will be correlated by timestamps, host/user context, commands, URLs, domains, IP addresses, and file indicators when those values are actually present in the artefacts.

## 8. Investigation Methodology

1. Inventory artefacts and calculate SHA-256 hashes.
2. Analyze the email without opening suspicious links or executing the attachment.
3. Extract and review relevant PowerShell events.
4. Inspect the packet capture using Wireshark/TShark.
5. Correlate observations into a timeline.
6. Assess confidence and distinguish facts from hypotheses.
7. Map supported behaviors to ATT&CK and propose detections.
8. Write response recommendations and the final report.

For each finding, record the evidence source, exact timestamp (including timezone where known), relevant field or packet/event reference, interpretation, confidence, and limitations.

## 9. Reporting Standards

- **Confirmed:** Directly supported by the artefact(s).
- **Probable:** Multiple observations support the interpretation, but a material gap remains.
- **Possible:** A plausible hypothesis requiring further evidence.
- **Not established:** The available evidence does not support a conclusion.

Do not label an email malicious solely because it contains an attachment or uses an unfamiliar domain. Do not assign an ATT&CK technique, declare command-and-control, or state impact without supporting evidence.

## 10. Initial Observations

From the supplied email screenshots, the message appears to:

- Use an invoice/collection theme and a payment deadline.
- Name Arthur Griffin as the sender and B Packaging Inc. as the organization.
- Address Julianne Westcott.
- Include an attachment named `Invoice.zip`.
- Provide a password (`Invoice2023!`) to view an encrypted file.
- Show SPF pass and DKIM-related authentication information in the captured header view.

These are preliminary observations from screenshots. They must be checked against the original `dump.eml`. Authentication results should be interpreted carefully: SPF/DKIM passing can show authorization or message integrity for a domain, but does not by itself establish that the sender or message is trustworthy.

## 11. Phase Completion Checklist

- [ ] Confirm the three artefacts are present.
- [ ] Record file sizes and SHA-256 hashes.
- [ ] Record analysis VM and tool versions.
- [ ] Preserve originals and document working-copy locations.
- [ ] Complete this introduction with verified lab details.
- [ ] Proceed to Phase 02 — Email Security Analysis.

## 12. Next Phase

**Phase 02 — Email Security Analysis** will validate the sender and authentication headers, inspect the MIME structure, identify the attachment's actual file type, and document URLs and other indicators without executing the attachment.
