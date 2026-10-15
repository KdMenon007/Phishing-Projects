# CatchMe SOC — Phishing Investigation & Incident Response

## 1. Project Overview

**CatchMe SOC — Phishing Investigation & Incident Response** is a cybersecurity investigation portfolio focused on analyzing phishing emails, identifying malicious indicators, investigating email-based attacks, and documenting incident response activities using a structured Security Operations Center (SOC) workflow.

This repository serves as a central collection of phishing investigation case files, forensic analysis, threat intelligence research, detection logic, and incident response documentation.

The objective is to demonstrate practical, evidence-driven investigation skills relevant to SOC Analyst L1/L2, Senior SOC Analyst, Threat Hunter, and Incident Responder roles.

Each investigation follows a repeatable workflow covering initial alert triage, email artifact collection, technical analysis, IOC extraction, threat attribution where evidence supports it, impact assessment, detection opportunities, and incident response recommendations.

## 2. Objectives

- Investigate suspicious and potentially malicious emails using a structured SOC workflow.
- Analyze email headers, sender identity, authentication results, and message routing.
- Identify phishing URLs, suspicious domains, malicious attachments, and embedded indicators.
- Investigate business email compromise (BEC), impersonation, credential phishing, and suspicious business requests.
- Extract and document indicators of compromise (IOCs).
- Use threat intelligence and OSINT to enrich investigation findings.
- Map observed attacker behavior to the MITRE ATT&CK framework.
- Develop detection opportunities for email security gateways, SIEM platforms, and endpoint telemetry.
- Document incident timelines, evidence, findings, and recommended containment actions.
- Produce professional incident reports suitable for technical review and a cybersecurity portfolio.

## 3. Investigation Scope

The repository may contain multiple investigation scenarios, each documented as an independent case.

| Investigation Area | Scope |
|---|---|
| Email header analysis | Received chain, sender identity, Reply-To, Return-Path, SPF, DKIM, and DMARC |
| Phishing investigation | Suspicious messages, social engineering, and credential theft attempts |
| URL analysis | Redirects, suspicious domains, URL reputation, and destination analysis |
| Attachment analysis | File metadata, hashes, static analysis, and safe sandbox results where available |
| Business Email Compromise | Executive impersonation, payment requests, invoice fraud, and trusted-sender abuse |
| Threat intelligence | Domain, IP, URL, file-hash enrichment, and OSINT |
| IOC extraction | Domains, URLs, IP addresses, email addresses, and file hashes |
| Detection engineering | Email rules, SIEM queries, correlation opportunities, and alert tuning |
| Incident response | Triage, containment, eradication, recovery, and lessons learned |

*The actual scope of each case depends on the available evidence. Unavailable telemetry or unperformed analysis must be documented rather than assumed.*

## 4. SOC Investigation Methodology

Each case follows a consistent investigation lifecycle.

### Phase 1 — Alert Triage

- Review the reported email or security alert.
- Identify the recipient, sender, subject, timestamp, and reported behavior.
- Determine the initial severity and investigation priority.
- Preserve the original message and associated artifacts when authorized.
- Establish the investigation scope and evidence sources.

### Phase 2 — Email Forensics

- Examine email headers and message structure.
- Review SPF, DKIM, and DMARC results.
- Compare the displayed sender address with the actual sending infrastructure and domain.
- Inspect Reply-To and Return-Path discrepancies.
- Review message routing, timestamps, and authentication anomalies.
- Identify suspicious language, urgency, impersonation, and unusual requests.

### Phase 3 — URL and Attachment Analysis

- Extract URLs, domains, filenames, and file hashes.
- Inspect URL structure, redirects, and domain characteristics.
- Enrich indicators using appropriate threat intelligence sources.
- Calculate cryptographic hashes for available files.
- Perform static analysis and use controlled sandbox environments when justified.
- Record analysis results and limitations.

Do not open suspicious links or execute attachments on a normal workstation.

### Phase 4 — Threat Intelligence and IOC Enrichment

- Search relevant threat intelligence sources for extracted indicators.
- Review domain registration and DNS information where appropriate.
- Check IP addresses, URLs, and file hashes against reputable intelligence services.
- Correlate findings with known malicious infrastructure or campaigns when evidence supports the relationship.
- Record source, lookup time, result, and confidence for each enrichment finding.

A reputation result alone does not prove that an artifact is malicious or benign.

### Phase 5 — Investigation and Correlation

Where telemetry is available:

- Search email gateway and mail server logs.
- Identify other recipients of the same or similar messages.
- Check for URL clicks and attachment delivery events.
- Review endpoint and authentication activity associated with affected users.
- Investigate possible credential submission, suspicious sign-ins, mailbox rule changes, or account compromise.
- Establish the incident timeline and assess the potential impact.

### Phase 6 — Detection and MITRE ATT&CK Mapping

- Identify observed attacker techniques and relevant detection opportunities.
- Map supported findings to applicable MITRE ATT&CK techniques.
- Develop detection logic using the available SIEM or email security platform.
- Document required log sources, query logic, expected results, and false-positive considerations.
- Validate detections against available test data or controlled simulations.

Technique mapping must be based on observed behavior or clearly stated investigative hypotheses.

### Phase 7 — Incident Response

- Recommend or perform authorized containment actions.
- Block confirmed malicious indicators where appropriate.
- Remove malicious emails from affected mailboxes when supported by organizational procedures.
- Reset credentials and revoke sessions if compromise is confirmed or reasonably suspected.
- Review and remediate persistence or unauthorized mailbox changes.
- Validate recovery and document residual risks.

### Phase 8 — Reporting and Lessons Learned

- Prepare a technical incident report.
- Maintain an evidence register and IOC register.
- Document the timeline, findings, impact, and confidence level.
- Record containment and remediation recommendations.
- Identify detection gaps and opportunities for prevention.
- Capture lessons learned and follow-up actions.

## 5. Repository Structure

```text
CatchMe-Phishing-Investigations/
│
├── README.md
│
├── Cases/
│   ├── Case-001-Phishing-Email/
│   │   ├── Incident-Report.md
│   │   ├── Email-Analysis.md
│   │   ├── Evidence-Register.md
│   │   ├── IOC-Register.md
│   │   ├── Investigation-Timeline.md
│   │   ├── MITRE-ATTACK-Mapping.md
│   │   ├── Detection-Logic.md
│   │   └── assets/
│   │
│   ├── Case-002-Business-Email-Compromise/
│   │   ├── Incident-Report.md
│   │   ├── Email-Analysis.md
│   │   ├── Evidence-Register.md
│   │   ├── IOC-Register.md
│   │   ├── Investigation-Timeline.md
│   │   ├── MITRE-ATTACK-Mapping.md
│   │   ├── Detection-Logic.md
│   │   └── assets/
│   │
│   └── Case-003-Suspicious-Attachment/
│       ├── Incident-Report.md
│       ├── Email-Analysis.md
│       ├── Evidence-Register.md
│       ├── IOC-Register.md
│       ├── Investigation-Timeline.md
│       ├── MITRE-ATTACK-Mapping.md
│       ├── Detection-Logic.md
│       └── assets/
│
├── Detections/
│   ├── SIEM-Queries/
│   ├── Email-Security-Rules/
│   └── Detection-Validation.md
│
├── Playbooks/
│   ├── Phishing-Triage.md
│   ├── Email-Compromise-Response.md
│   └── Malicious-Attachment-Response.md
│
├── References/
│   ├── Tools-and-Resources.md
│   └── MITRE-ATTACK-References.md
│
└── LICENSE
```

*This is a proposed structure. Create case folders and supporting files as the investigations are developed.*

## 6. Evidence Collection and Handling

Evidence must be handled consistently to support reproducible investigations.

For each artifact, record:

- Evidence ID
- Artifact name and type
- Collection source
- Collection timestamp and timezone
- SHA-256 hash, where applicable
- Storage location
- Analysis performed
- Observations and findings
- Evidence limitations

Preserve original artifacts where possible and conduct analysis on working copies. Redact credentials, personal information, confidential business data, and sensitive email content before publishing evidence.

Do not upload live credentials, session tokens, private customer information, or confidential corporate emails to a public repository.

## 7. Tools and Technologies

Tools may vary by case. The following are examples of tools suitable for the investigation workflow.

| Category | Example Tools |
|---|---|
| Email analysis | Microsoft Outlook message inspection, Google Admin email logs, Microsoft Defender for Office 365 |
| Header analysis | Google Admin Toolbox Messageheader, MXToolbox |
| URL analysis | urlscan.io, VirusTotal, URLhaus |
| File analysis | Detect It Easy, ExifTool, YARA, controlled malware-analysis sandboxes |
| Threat intelligence | VirusTotal, AbuseIPDB, URLhaus, WHOIS and DNS utilities |
| Network analysis | Wireshark, Zeek |
| SIEM and detection | Elastic Security, Splunk, Microsoft Sentinel |
| Incident response | Evidence registers, investigation timelines, endpoint and identity audit logs |
| Frameworks | MITRE ATT&CK |

*These are candidate tools, not a claim that every tool was used in every investigation. Public scanning services may retain or share submitted samples, URLs, or other data; review their policies before submitting sensitive artifacts.*

## 8. MITRE ATT&CK Coverage

Depending on the evidence, investigations may involve techniques such as:

| Technique | ID | Relevance |
|---|---|---|
| Phishing: Spearphishing Attachment | T1566.001 | Malicious email attachment |
| Phishing: Spearphishing Link | T1566.002 | Malicious link delivered through email |
| Phishing: Spearphishing via Service | T1566.003 | Phishing delivered through a third-party service |
| Phishing: Spearphishing Voice | T1566.004 | Voice-based phishing where relevant |
| User Execution: Malicious File | T1204.002 | User executes a malicious file |
| Steal Web Session Cookie | T1539 | Session-cookie theft, if supported by evidence |
| Email Collection | T1114 | Email collection activity, where observed |

Only techniques supported by the case evidence should be included in the final mapping. A phishing email alone does not establish that a user executed a file, disclosed credentials, or suffered account compromise.

Reference: [MITRE ATT&CK — Phishing (T1566)](https://attack.mitre.org/techniques/T1566/)

## 9. Incident Report Requirements

Every completed case should contain an incident report covering:

1. Executive summary
2. Incident classification and severity
3. Investigation scope
4. Affected users, systems, and services
5. Evidence sources
6. Technical email analysis
7. URL and attachment findings
8. Threat intelligence enrichment
9. IOC register
10. Investigation timeline
11. Impact assessment
12. MITRE ATT&CK mapping
13. Detection and correlation opportunities
14. Containment and remediation
15. Recovery and validation
16. Lessons learned
17. References and appendices

Clearly distinguish confirmed facts, analytical conclusions, and unverified hypotheses.

## 10. Security and Ethical Considerations

- Use authorized lab environments and approved investigation procedures.
- Do not interact with suspected malicious infrastructure unless explicitly authorized and necessary for the investigation.
- Do not send phishing emails to real users without formal authorization.
- Do not execute suspicious attachments on production systems.
- Protect personal data and confidential evidence.
- Use synthetic or sanitized examples for public demonstrations.
- Document tool limitations, evidence gaps, and uncertainty.
- Never claim that an incident was contained, remediated, or validated unless the action was actually completed and its outcome verified.

## 11. Project Deliverables

The repository is intended to demonstrate practical SOC capabilities through the following deliverables:

- Structured phishing investigation case files
- Technical email forensic analysis
- Evidence and IOC registers
- Investigation timelines
- Threat intelligence enrichment records
- MITRE ATT&CK technique mapping
- SIEM detection queries and validation notes
- Incident response playbooks
- Technical incident reports
- Remediation recommendations and lessons learned

## 12. Learning Outcomes

This project supports the development and demonstration of skills in:

- Phishing alert triage and investigation
- Email security and authentication analysis
- Digital evidence handling
- Threat intelligence and OSINT
- IOC extraction and enrichment
- SIEM investigations and detection engineering
- Identity and endpoint investigation
- MITRE ATT&CK mapping
- Incident response and technical reporting
- Evidence-based security decision-making

## 13. References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [Microsoft Learn — Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/defender-office-365/)
- [Google Admin Toolbox](https://toolbox.googleapps.com/)
- [VirusTotal](https://www.virustotal.com/)
- [URLhaus](https://urlhaus.abuse.ch/)
- [YARA](https://yara.readthedocs.io/)

