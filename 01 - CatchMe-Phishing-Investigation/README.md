# CatchMe — Phishing Email Investigation

![Project Banner](assets/project-banner.png)

## Project Overview

A hands-on phishing investigation lab focused on email header analysis,
URL extraction, attachment triage, evidence integrity, and incident assessment.

**Role focus:** SOC Analyst L2  
**Environment:** Kali Linux  
**Source exercises:** TryHackMe — Phishing Analysis Fundamentals and Phishing Emails in Action

## Objectives

- Parse email headers and authentication results.
- Extract URLs and identify domains without visiting links.
- Decode and statically inspect a PDF attachment.
- Record SHA-256 hashes and preserve original evidence.
- Correlate observations and document investigation limitations.

## Evidence

| Artifact | Purpose |
|---|---|
| `assets/evidence/email/email1.eml` | ADT-themed email sample |
| `assets/evidence/email/email2.txt` | Base64-encoded PDF attachment content |
| `assets/evidence/email/email3.eml` | Home Depot-themed email sample |
| `analysis/pdf/zmqpalgh.pdf` | Decoded PDF for static inspection |
| `analysis/indicator-inventory.csv` | Extracted URL and hash inventory |
| `analysis/evidence-timeline.csv` | Header and metadata timestamps |
| `assets/evidence/integrity/SHA256-MANIFEST.txt` | File integrity record |

## Key Findings

- SPF, DKIM, and DMARC passed for the sender domains in both email samples.
- The visible brand names do not independently establish that the sending domains are authorized to represent those brands.
- The email HTML contains tracking-style links and image resources.
- The PDF text extraction produced `THM{BENIGN_PDF_ATTACHMENT}`.
- PDFiD reported zero for `/JS`, `/JavaScript`, `/AA`, `/OpenAction`, `/Launch`, and `/EmbeddedFile`.
- The extracted PDF was verified byte-for-byte against the decoded Base64 payload.

## Limitations

- Tracking URLs were not visited, so their final destinations were not verified.
- External domain reputation and brand authorization were not independently established.
- Static PDF checks do not prove absolute safety.
- The PDF's creation metadata does not prove which email, if any, delivered it.

## Screenshots

- `assets/screenshots/03-attachment-analysis/pdf-metadata.png`
- `assets/screenshots/03-attachment-analysis/pdfid-scan.png`
- `assets/screenshots/04-indicator-analysis/indicator-inventory.png`
- `assets/screenshots/05-integrity/sha256-verification.png`

## Safety

The investigation used static inspection. Do not open suspicious links or execute attachments outside an authorized, isolated analysis environment.
