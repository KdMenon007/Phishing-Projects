# Evidence Register — CatchMe Business Email Investigation

## 1. Purpose

This register identifies the artifacts collected for the CatchMe business email investigation lab, their integrity hashes, their role in the investigation, and their evidentiary limitations.

## 2. Handling and Scope

- This is a controlled cybersecurity training project.
- `challenge.eml` is a **modified, payload-redacted training sample**, not an untouched original email.
- `SWT_09674321_synthetic.CAB` is a **synthetic replacement** created for safe analysis. It is not the original attachment.
- The extracted text file belongs to the synthetic CAB artifact.
- Email claims, sender identity, transaction details, and payment status are unverified.
- Text within edited headers, including SPF-related results, must not be represented as an independently performed live authentication check.
- SHA-256 hashes identify the exact files present when the hashes were calculated. They do not establish the authenticity of the original message.

## 3. Primary Evidence

| Evidence ID | File | SHA-256 | Description and limitations |
|---|---|---|---|
| E-01 | `assets/evidence/email/challenge.eml` | `8d9e777637f66fd45fedc7388ffd97c6a0a771f1c0c59e0a15514a8bc510232d` | Modified, payload-redacted email training sample. Header and body chronology contains deliberate edits. |
| E-02 | `assets/evidence/attachments/SWT_09674321_synthetic.CAB` | `dd04f62f7fb1a50850e1f76548a62d66d745ebf7bc207ac5930b031ee2b63d71` | Synthetic CAB archive for safe file-analysis practice; not the original attachment. |
| E-03 | `analysis/attachment-extracted/payment-receipt-lab.txt` | `21adb3bd7d3ca72fb4ae1371c69521e560a1ebb7969b39690aae6460dac4c66f` | Harmless text extracted from E-02. It explicitly identifies itself as synthetic lab material. |

## 4. Screenshots

All screenshots are stored in `assets/evidence/screenshots/`.

| Evidence ID | Screenshot | Purpose |
|---|---|---|
| S-01 | `01-catchme-email-rendered-view.png` | Rendered view of the email sample. |
| S-02 | `02-catchme-email-header-integrity.png` | Email header and integrity review. |
| S-03 | `03-synthetic-cab-analysis.png` | Synthetic CAB file identification and inspection. |
| S-04 | `04-synthetic-extracted-artifact.png` | Inspection of the extracted text artifact. |
| S-05 | `05-email-mime-validation.png` | MIME structure and attachment-payload validation. |
| S-06 | `06-catchme-evidence-integrity.png` | Evidence hash verification. |
| S-07 | `07-catchme-ioc-classification.png` | IOC review and classification. |
| S-08 | `08-catchme-evidence-inventory.png` | Evidence inventory. |
| S-09 | `09-catchme-email-timeline.png` | Timeline comparison and chronology review. |

Screenshots document the displayed state at capture time. They do not independently prove the authenticity of the underlying email or any claimed financial transaction. Review screenshots for sensitive data before publishing them.

## 5. Investigation Notes

- The email contains sender and Reply-To addresses using different mailbox addresses.
- The sample includes a claimed payment reference and financial details; these are claims in the message, not verified transactions.
- The sample's October 2026 Date header and transaction time conflict with older June 2020 Received-header timestamps and the timestamp embedded in the Message-ID.
- The sample's attachment payload was removed. The synthetic CAB is used only to demonstrate safe attachment-analysis procedures.
- The IP address `192.119.71.157` appears in the supplied header material. Its ownership, reputation, and relationship to malicious activity have not been independently established by this register.

## 6. Integrity Revalidation

Recalculate hashes before sharing or publishing the project:

```bash
sha256sum \
  assets/evidence/email/challenge.eml \
  assets/evidence/attachments/SWT_09674321_synthetic.CAB \
  analysis/attachment-extracted/payment-receipt-lab.txt
```

If a file changes, update this register with the new hash and document the reason for the change. Preserve prior versions when historical comparison is required.

## 7. Publication Safeguards

- Redact account numbers, personal data, credentials, and other sensitive information from screenshots.
- Do not publish the sample as an original or authenticated email.
- Do not describe the synthetic CAB as the recovered original attachment.
- Do not claim a payment occurred based only on the message.

## Public Redacted Copies

- `public-evidence/email/challenge-redacted.eml` — sanitized copy of the current modified training sample.
- `public-evidence/email/challenge-older-redacted.eml` — sanitized copy of an older working version.
- These copies are derivatives; their hashes differ from their source files.
- The redaction check covered known account and financial-value patterns only.
  It does not establish that all sensitive information has been removed.
- Original evidence and screenshots must be reviewed separately before public release.
