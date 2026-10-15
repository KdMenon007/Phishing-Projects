# Incident Response Report — CatchMe Phishing Investigation

## 1. Executive Summary

This investigation analyzed two email artifacts and a separately supplied
Base64-encoded PDF attachment. Work included header review, email authentication
review, URL extraction, PDF metadata inspection, PDFiD scanning, and hash
verification.

The PDF contained the TryHackMe flag `THM{BENIGN_PDF_ATTACHMENT}`. The two email
samples use brand-themed display names with sending domains whose relationship
to those brands was not independently verified. The final destinations of the
tracking links were not investigated by visiting them.

**Assessment:** The PDF is classified as benign within the lab exercise. The
emails' legitimacy remains inconclusive based on the evidence collected here.

## 2. Scope and Method

- Parsed `email1.eml` and `email3.eml` headers.
- Reviewed SPF, DKIM, and DMARC results recorded in the messages.
- Extracted URL and image references without navigating to them.
- Decoded the PDF from `email2.txt`.
- Inspected PDF metadata and PDFiD indicators.
- Calculated SHA-256 hashes for source artifacts and the extracted PDF.

## 3. Evidence Integrity

### Original artifacts

| Artifact | SHA-256 |
|---|---|
| `email1.eml` | `2ed3d561ebc566b8bb131efb5db6fb227c6b6d9042b6ee835bbf8f61e6ec8a15` |
| `email2.txt` | `d905c328fa169f892e89f66dc34595e3d00db9c530e349400cb692d2b86c82b6` |
| `email3.eml` | `69f6d1ef0c1026e71c0268bda6e4a865176af9b5c105781868420555435e86a9` |

### Extracted PDF

- File: `analysis/pdf/zmqpalgh.pdf`
- Size: 35,277 bytes
- SHA-256: `7a8fbf5de792a20a2f3be994e041f34f9ca3f37e10d829f77bef94dfe7b77900`
- Decoded payload and extracted file matched byte-for-byte.

## 4. Email 1 — ADT-Themed Message

- From: `[redacted-sender]`
- Display name: `ADT Security Services`
- Reply-To: `[redacted-reply-address]`
- Originating IP: `43.255.56.161`
- Subject: `Help protect your budget by protecting your home`
- SPF: pass
- DKIM: pass for `ant.anki-tech.com`
- DMARC: pass, policy `p=NONE`

### URL observations

The HTML contains click, open, and unsubscribe tracking URLs on
`ant.anki-tech.com`, image resources on `blueoceanfresh.com`, and standard W3C
HTML references.

### Assessment

Authentication passed for the sender domain. The relationship between the
displayed ADT identity and the sending domain remains unverified. The external
image domain is an observation, not proof of maliciousness.

## 5. Email 3 — Home Depot-Themed Message

- From: `[redacted-sender]`
- Display name: `Thank you! Home Depot`
- Reply-To: `[redacted-sender]`
- Originating IP: `103.234.236.83`
- Subject: `Order Placed : Your Order ID [redacted-order-id] Placed Successfully`
- SPF: pass
- DKIM: pass for `teckbe.com`
- DMARC: pass, policy `p=NONE`

### URL observations

The HTML contains tracking-style URLs on `t.teckbe.com` and image resources on
`img.teckbe.com`. Visible text includes `CLICK HERE`, `Unsubscribe`, and
`Report Spam`.

### Assessment

Authentication passed for `teckbe.com`. The sender's authorization to represent
Home Depot and the final destinations of the tracking URLs remain unverified.
The available evidence does not establish a confirmed phishing destination.

## 6. PDF Attachment Analysis

- Filename: `zmqpalgh.pdf`
- MIME type: `application/pdf`
- PDF version: 1.6
- Pages: 1
- Author metadata: `Sam Iam`
- Creator metadata: Acrobat PDFMaker 21 for Word
- Creation metadata: July 1, 2021
- Extracted text: `THM{BENIGN_PDF_ATTACHMENT}`

PDFiD reported zero for `/JS`, `/JavaScript`, `/AA`, `/OpenAction`, `/AcroForm`,
`/Launch`, `/EmbeddedFile`, `/RichMedia`, and `/XFA`. `pdfdetach -list` reported
zero embedded files.

These checks support the benign classification used in the lab exercise.
They do not prove that the file is universally safe or that its metadata is
authentic.

## 7. Timeline

| Timestamp | Source | Observation |
|---|---|---|
| June 21, 2021 15:35:39 UTC | `email1.eml` | Timestamp in message Date header |
| July 1, 2021 08:31:50 UTC−04:00 | PDF metadata | Embedded creation timestamp |
| July 11, 2021 11:43:46 UTC | `email3.eml` | Timestamp in message Date header |

The PDF metadata timestamp falls between the email timestamps. This does not
establish that either email delivered the PDF.

## 8. Indicators

The generated inventory contains 15 URL indicators and one SHA-256 indicator.
The four URL domains observed are:

- `ant.anki-tech.com`
- `blueoceanfresh.com`
- `img.teckbe.com`
- `t.teckbe.com`

These are extracted indicators. Their reputation and maliciousness were not
independently verified.

## 9. Incident Response Recommendations

1. Preserve the original artifacts and their recorded hashes.
2. Validate the sender domains and claimed brand relationships using trusted,
   independent sources.
3. Investigate URL reputation and redirect destinations in an approved,
   isolated environment without exposing user credentials.
4. Correlate any future findings with mail gateway, DNS, proxy, and endpoint logs.
5. Avoid blocking domains solely because they appear in these samples; require
   additional evidence and operational context.
6. Document confidence, evidence source, and limitations for every conclusion.

## 10. Final Assessment

The attachment was classified as benign by the TryHackMe lab flag and showed no
obvious active-content indicators in the static checks performed. Both emails
passed SPF, DKIM, and DMARC for their respective sender domains, but those
results do not establish brand authorization. The emails' overall legitimacy
remains inconclusive because redirect destinations and external reputation
were not verified.

## 11. Evidence Screenshots

- `assets/screenshots/03-attachment-analysis/pdf-metadata.png`
- `assets/screenshots/03-attachment-analysis/pdfid-scan.png`
- `assets/screenshots/04-indicator-analysis/indicator-inventory.png`
- `assets/screenshots/05-integrity/sha256-verification.png`
