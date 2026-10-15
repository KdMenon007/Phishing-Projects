# CatchMe — Phishing Email Investigation

**SOC Analyst L2 Portfolio Project | Phishing Analysis | Threat Investigation | Incident Response**

A practical cybersecurity investigation project focused on analyzing suspicious email samples, examining email headers, extracting indicators, performing static attachment triage, maintaining evidence integrity, and documenting investigation findings.

## Project Overview

| Detail | Description |
|---|---|
| Project | CatchMe — Phishing Email Investigation |
| Role Focus | SOC Analyst L2 |
| Analysis Environment | Kali Linux |
| Investigation Focus | Email header analysis, URL extraction, attachment triage, and evidence integrity |
| Core Activities | Indicator analysis, investigation timeline creation, incident reporting, and response recommendations |
| Deliverables | Incident response report, evidence register, IOC register, timeline, workflow diagram, and investigation documentation |
| Project Type | Practical cybersecurity investigation and portfolio project |

## Objectives

- Analyze email headers, sender domains, reply-to addresses, and authentication results.
- Identify discrepancies between displayed sender identities and sending domains.
- Extract URLs and domains from suspicious email content without visiting the links.
- Perform static analysis of a decoded PDF attachment.
- Record SHA-256 hashes and document evidence handling.
- Build an indicator inventory and investigation timeline.
- Document findings, limitations, and incident-response recommendations.
- Map relevant investigative observations to candidate MITRE ATT&CK techniques.
- Communicate conclusions accurately without treating unverified indicators as confirmed malicious infrastructure.

## Investigation Workflow

1. **Evidence intake:** Identify the supplied email samples and preserve the original artifacts.
2. **Email header analysis:** Review sender details, reply-to addresses, timestamps, originating IP information, and authentication results.
3. **Content analysis:** Examine message subjects, displayed brand identities, and email content for suspicious characteristics.
4. **URL and indicator extraction:** Identify URLs, domains, and other relevant indicators without opening suspicious links.
5. **Attachment triage:** Inspect the decoded PDF using static-analysis tools and review its metadata and selected structural indicators.
6. **Integrity verification:** Calculate SHA-256 hashes and compare the extracted attachment with the decoded payload.
7. **Timeline development:** Record message timestamps and attachment metadata while noting uncertainties.
8. **Investigation assessment:** Evaluate the available evidence, document limitations, and develop response recommendations.
9. **Reporting:** Maintain the evidence register, IOC register, investigation timeline, and incident-response report.

## Key Findings

### 1. Email Authentication and Sender Identity

The analyzed messages returned passing SPF, DKIM, and DMARC results for their respective sending domains.

These results establish authentication outcomes for those domains; they do not independently prove that the messages were authorized by the brands displayed in the sender names.

### 2. URL and Domain Observations

The messages contained tracking-style URLs and external image resources.

The extracted indicators were documented for investigation purposes. Their final destinations, current reputation, and maliciousness were not independently verified.

**Assessment:** An extracted URL or domain should not be classified as malicious solely because it appears in a suspicious-looking email.

### 3. PDF Attachment Analysis

The decoded PDF was examined using static-analysis methods.

Observed results included:

- Extracted text containing `THM{BENIGN_PDF_ATTACHMENT}`.
- No occurrences of selected PDF indicators such as `/JS`, `/JavaScript`, `/AA`, `/OpenAction`, `/Launch`, and `/EmbeddedFile` in the reported PDFiD results.
- PDF metadata containing document creation information.
- A byte-for-byte match between the decoded attachment payload and the extracted PDF.

These observations support the documented triage findings but do not prove that a PDF is completely safe.

### 4. Evidence Integrity

SHA-256 hashes were recorded for the original email artifacts and extracted PDF. The decoded attachment was verified against the extracted file.

The original evidence is retained separately from the sanitized files prepared for public presentation.

### Investigation Assessment

The available evidence supports documenting suspicious-message characteristics and performing further investigation. It does not, by itself, establish that every message, URL, or attachment is malicious.

## Public Evidence and Analysis

| Artifact | Purpose |
|---|---|
| `public-evidence/email/` | Sanitized email derivatives prepared for public review |
| `analysis/indicator-inventory.csv` | Extracted URL and hash indicator inventory |
| `analysis/evidence-timeline.csv` | Timeline of message-header and PDF-metadata observations |
| `IOC-Register.csv` | Indicator register |
| `Evidence-Register.md` | Evidence handling notes and integrity references |
| `Investigation-Timeline.md` | Human-readable investigation timeline |
| `Incident-Response-Report.md` | Investigation findings, technical analysis, limitations, and response recommendations |
| `MITRE-ATTACK-Mapping.md` | Candidate technique mappings and supporting rationale |
| `assets/diagrams/phishing-investigation-workflow.svg` | Investigation workflow diagram |
| `assets/screenshots/` | Selected screenshots of analysis activities |
| `lessons-learned.md` | Lessons learned and investigation improvements |
| `references/tools-and-resources.md` | Tools and reference material |
| `scripts/generate_report.py` | Report-generation script |

## Evidence Handling and Sanitization

Original email artifacts, the extracted PDF, and the original SHA-256 manifest are retained separately and are not included in this public repository.

The files in `public-evidence/email/` are sanitized derivatives prepared for public review. Email-routing details and web URLs were removed or redacted for publication.

Consequently:

- Sanitized files may differ from the original evidence in content, structure, and hash.
- Their hashes must not be used to verify the integrity of the original artifacts.
- The original evidence hashes refer to locally retained artifacts and do not imply that those files are downloadable from this repository.
- Sanitized derivatives are provided to demonstrate investigation documentation, not as substitutes for original forensic evidence.

## Investigation Timeline

The timeline records relevant message-header timestamps and PDF metadata.

PDF metadata is not necessarily reliable evidence of email delivery time or attachment provenance. A timestamp that falls between two email timestamps does not independently prove that the attachment was delivered with either message.

See [`Investigation-Timeline.md`](Investigation-Timeline.md) for the recorded timeline and confidence notes.

## Indicator Management

The IOC register records extracted indicators and their validation status.

Indicators should be distinguished by evidence source and verification status:

- **Extracted:** Observed directly in a supplied artifact.
- **Unverified:** Reputation or destination has not been independently established.
- **Confirmed malicious:** Requires sufficient supporting evidence; extraction alone is not enough.

See [`IOC-Register.csv`](IOC-Register.csv) and [`analysis/indicator-inventory.csv`](analysis/indicator-inventory.csv).

## MITRE ATT&CK Mapping

The project documents candidate mappings related to phishing and malicious attachments where appropriate.

These mappings are investigative hypotheses based on the available evidence, not confirmation that a particular technique was successfully executed.

See [`MITRE-ATTACK-Mapping.md`](MITRE-ATTACK-Mapping.md) for the rationale and evidence limitations.

## Incident Response Recommendations

For a suspected phishing incident, recommended actions include:

1. Preserve the original message and associated evidence.
2. Identify potentially affected users and endpoints.
3. Review email gateway, endpoint, proxy, DNS, and authentication logs where available.
4. Determine whether suspicious links were accessed or attachments were opened.
5. Investigate any associated credential submission, malware execution, or unauthorized activity.
6. Block confirmed malicious indicators using approved organizational procedures.
7. Remove malicious messages from affected mailboxes where appropriate.
8. Reset potentially compromised credentials and revoke sessions when supported by investigation findings.
9. Document containment, remediation, recovery, and lessons learned.

These are response recommendations, not claims that the actions were performed in this lab investigation.

## Limitations

- Suspicious links were not visited, and their final destinations were not verified.
- External domain reputation and authorization to represent the displayed brands were not independently established.
- Static PDF checks cannot prove that a document is completely safe.
- PDF creation metadata does not establish which email delivered the attachment.
- The public email derivatives have been sanitized and do not preserve the originals byte-for-byte.
- Original evidence and the original integrity manifest are retained separately.
- The available findings are insufficient to declare all observed indicators malicious.

## Safety and Evidence Handling

- Do not visit suspicious links or execute attachments outside an authorized, isolated analysis environment.
- Preserve original evidence and calculate hashes before analysis.
- Keep original artifacts separate from sanitized publication copies.
- Record tools, timestamps, and analysis results where relevant.
- Clearly label unverified indicators and investigative hypotheses.
- Do not claim a detection, containment action, or malware execution occurred unless supported by evidence.

## Project Structure

```text
Phishing-Projects/
├── analysis/
│   ├── evidence-timeline.csv
│   └── indicator-inventory.csv
├── assets/
│   ├── diagrams/
│   └── screenshots/
├── detections/
│   └── elastic-kql/
├── public-evidence/
│   ├── email/
│   └── README.md
├── references/
├── scripts/
├── Evidence-Register.md
├── Incident-Response-Report.md
├── Investigation-Timeline.md
├── IOC-Register.csv
├── MITRE-ATTACK-Mapping.md
├── lessons-learned.md
└── README.md
```

## Skills Demonstrated

- Email-header analysis and authentication-result interpretation
- Phishing content analysis
- URL and indicator extraction
- Static attachment analysis and PDF metadata inspection
- SHA-256 integrity verification
- Evidence handling and timeline development
- Incident-response reporting and risk assessment
- MITRE ATT&CK mapping
- Technical documentation and investigative communication
- Clear separation of observed evidence, hypotheses, and verified conclusions
