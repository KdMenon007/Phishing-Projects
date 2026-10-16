# Phase 02 — Email Security Analysis

## 1. Evidence Record

- **Artefact:** `dump.eml`
- **Observed working location:** `~/Desktop/artefacts/dump.eml`
- **File identification:** RFC 822 mail, ASCII text, CRLF line terminators
- **Reported file size:** 14 KB
- **SHA-256:** `4cdd0a2f16a9e1578b5c3419eeac9c403f7dce86b12fb3b8219ce5f534c1fc`
- **Evidence source:** terminal output supplied during the investigation
- **Status:** Header review started; attachment contents not yet analyzed

## 2. Message Summary

| Field | Observed value |
|---|---|
| From | Arthur Griffin `<agriffin@bpakcaging.xyz>` |
| To | Julianne Westcott `<julianne.westcott@hotmail.com>` |
| Date | Fri, 13 Jan 2023 09:25:26 +0000 |
| Subject | `Collection for Quick Logistics LLC - Jan 2023` |
| Reply-To | Arthur Griffin `<agriffin@bpakcaging.xyz>` |
| Return-Path | `agriffin@bpakcaging.xyz` |
| Sender | `agriffin@bpakcaging.xyz` |
| Message-ID domain | `tracking.bpakcaging.xyz` |
| Sender IP reported by receiving infrastructure | `15.235.99.80` |
| HELO name | `pa80.mxout.mta1.net` |
| Attachment indicated by screenshots | `Invoice.zip` |

**Important spelling observation:** The email uses `bpakcaging.xyz` (with the characters in “packaging” apparently transposed/misspelled) rather than the expected-looking `bpackaging.xyz` shown in the scenario screenshot. Record this exact observed value and compare it against the scenario and other artefacts; do not silently normalize it.

## 3. Mail Routing Observations

The visible `Received` chain shows the message arriving from `pa80.mxout.mta1.net` at IP `15.235.99.80` into Microsoft 365/EOP infrastructure at approximately **2023-01-13 09:25:31 UTC**, then passing through Microsoft mail systems. The message date is **09:25:26 UTC**.

The timestamps and hostnames are observations from the supplied headers. They should be used as correlation pivots when reviewing endpoint and network artefacts.

## 4. Authentication Results

The supplied header output contains:

- `spf=pass`, with sender IP `15.235.99.80` and `smtp.mailfrom=bpakcaging.xyz`
- `dkim=pass`, with `header.d=bpakcaging.xyz`
- `dmarc=bestguesspass action=none`, with `header.from=bpakcaging.xyz`
- A second DKIM signature for `elasticemail.com`

### Interpretation

These results indicate that the receiving mail system reported SPF and DKIM passing for the domains shown in the message. The DMARC value is specifically `bestguesspass`, not a plain `dmarc=pass` result. Authentication success does **not** prove that the message is benign, that the named person is genuine, or that the domain is the legitimate business partner. The apparent domain spelling is a lead for further validation, not sufficient by itself to prove spoofing.

## 5. Social-Engineering Observations

The screenshots of the email body show an invoice/collections theme:

- It refers to document `#39586972`.
- It states that payment is due on January 20, 2023.
- It asks the recipient to confirm that payment is on track.
- It directs the recipient to an attached document.
- It provides the password `Invoice2023!` for an encrypted file.
- The attachment is shown as `Invoice.zip`.

This creates a plausible urgency/legitimacy lure for a finance employee. The attachment and password-protected archive require safe inspection before making a final malware determination.

## 6. Header Security Signals and Caveats

- `X-MS-Exchange-Organization-SCL: 5` is present in the captured headers. Record it as a mail-filtering signal; do not interpret it as definitive proof of maliciousness without understanding the environment's scoring policy.
- The `X-Microsoft-Antispam-Mailbox-Delivery` header includes `OFR:TrustedSenderList`. This is an observed delivery-processing field and may help explain mail handling, but should not be treated as a guarantee of safety.
- The message has a `List-Unsubscribe` field and tracking-style Message-ID/subdomain. These can occur in legitimate bulk-mail infrastructure as well as suspicious campaigns; context is required.
- The screenshots and pasted header output are secondary representations. Confirm exact details against the original `.eml` file and preserve the original hash.

## 7. Preliminary Indicators to Track

| Indicator | Value | Context |
|---|---|---|
| Sender domain | `bpakcaging.xyz` | Apparent sender domain; spelling needs validation |
| Sender IP | `15.235.99.80` | Reported by receiving mail infrastructure |
| HELO hostname | `pa80.mxout.mta1.net` | Observed in `Received-SPF` / `Received` headers |
| Message-ID domain | `tracking.bpakcaging.xyz` | Observed in Message-ID |
| Attachment filename | `Invoice.zip` | Shown in screenshot; validate in MIME content |
| Document reference | `39586972` | Included in email body |
| Archive password | `Invoice2023!` | Included in email body; treat as sensitive incident detail |

These are investigation leads, not automatically malicious IOCs. Validate each against endpoint and network evidence before assigning a verdict.

## 8. Current Assessment

**Assessment:** Suspicious invoice-themed email requiring continued investigation.

**Confidence:** Moderate that the message uses an invoice-themed social-engineering lure, based on the observed body and attachment. The available header output alone does not establish that the attachment executed or that the workstation was compromised.

**Not yet established:**
- The actual file type and contents of `Invoice.zip`
- Whether the attachment contains a malicious LNK, script, document, or other payload
- Whether Julianne opened the attachment
- Any PowerShell execution or network communication caused by the email
- The attacker's objective or impact

## 9. Next Commands — MIME and Attachment Inspection

Run these from `~/Desktop/artefacts` and share the output:

```bash
cd ~/Desktop/artefacts

# Find MIME part and attachment metadata
grep -inE 'Content-Type:|Content-Disposition:|filename=|Content-Transfer-Encoding:' dump.eml

# Show the email body and MIME structure around the attachment
grep -anE 'boundary=|Content-Type:|Content-Disposition:|filename=|Content-Transfer-Encoding:' dump.eml

# Confirm available artefacts
ls -lh
```

Do not execute the archive contents. We will extract the attachment safely in a controlled analysis directory, identify its true file type, and calculate its hash before inspecting it.

## 10. Phase Status

- [x] Record `dump.eml` size and SHA-256
- [x] Review visible message headers
- [x] Record sender, recipient, subject, timestamps, and authentication results
- [x] Record preliminary social-engineering observations
- [ ] Parse MIME parts and safely extract the attachment
- [ ] Identify and hash the attachment
- [ ] Review URLs and other body indicators
- [ ] Correlate email findings with endpoint and network telemetry


## 11. Attachment Extraction Results

The attachment was extracted from the original `dump.eml` using Python's email parser. The original email was not modified.

| Property | Observed value |
|---|---|
| Extracted path | `extracted/Invoice.zip` |
| Actual size | 908 bytes |
| Declared MIME type | `application/zip` |
| File identification | ZIP archive, created by version 6.3 |
| Uncompressed size reported by `file` | 2,344 bytes |
| SHA-256 | `b55ee53b18871f811f5a4ec405cd70de6b3f1f7cf28712ab5cb5186cbf551e87` |
| Archive entry | `Invoice_20230103.lnk` |
| Entry size | 2,344 bytes |
| Entry timestamp | 2023-01-13 16:51 (archive listing) |

The extracted attachment size matches the 908-byte size declared in the MIME `Content-Disposition` header. The ZIP listing identifies one Windows shortcut (`.lnk`) named `Invoice_20230103.lnk`. A shortcut can contain a target path, arguments, and other metadata; its presence is suspicious in this invoice context but does not alone prove malicious behavior.

## 12. Safe Next Step — Inspect the LNK Metadata

Do not double-click the shortcut or run it. First extract it into a dedicated analysis folder and inspect metadata only:

```bash
cd ~/Desktop/artefacts
mkdir -p extracted/lnk

# Extract the archive entry without executing it
unzip -o extracted/Invoice.zip -d extracted/lnk

# Verify the extracted file type and hash
file extracted/lnk/Invoice_20230103.lnk
sha256sum extracted/lnk/Invoice_20230103.lnk

# Check whether LNKParse3 is available
command -v lnkparse
python3 -m pip show LnkParse3
lnkparse --help
```

If `lnkparse` is installed and its help confirms the expected syntax, use its documented options to parse `extracted/lnk/Invoice_20230103.lnk`. If no CLI is available, share the help output and we will select the correct invocation for the installed version. Do not install packages or execute the LNK until we decide what is needed.

Useful metadata to record includes the shortcut target, arguments, working directory, relative path, icon path, timestamps, and any embedded command. Treat any extracted command or URL as untrusted data; do not run it.

## 13. Updated Phase Status

- [x] Record `dump.eml` size and SHA-256
- [x] Review visible message headers
- [x] Record sender, recipient, subject, timestamps, and authentication results
- [x] Identify MIME attachment metadata
- [x] Extract `Invoice.zip` from the email
- [x] Calculate SHA-256 of `Invoice.zip`
- [x] List archive contents
- [x] Extract and parse LNK metadata safely (see Phase 03 / attack-chain notes)
- [x] Review the LNK URL and command line
- [x] Correlate email findings with endpoint and network telemetry (see Phases 03–05)
