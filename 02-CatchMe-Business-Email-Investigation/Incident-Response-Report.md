# Incident Response Report
## CatchMe — Business Email Investigation

**Case ID:** CATCHME-BEC-001  
**Investigation type:** Business Email Compromise (BEC) / suspected payment fraud  
**Environment:** Controlled cybersecurity training lab  
**Status:** Investigation documented; original attachment unavailable  
**Classification:** Training scenario — not a verified real-world incident

---

## 1. Executive Summary

This investigation examines a modified, payload-redacted email training sample containing a claimed financial transfer and a synthetic CAB attachment created for safe analysis.

The email contains sender and Reply-To addresses that differ, financial-transfer language, a claimed transaction reference, and inconsistencies between the message's displayed date and older transport-header timestamps. The sample also contains SPF-related text, but those results are part of the edited artifact and have not been independently validated through a live authentication check.

The original attachment payload was unavailable. A synthetic CAB archive containing harmless text was created for file-analysis practice. It must not be treated as the original attachment or as evidence that the original attachment was malicious.

**Assessment:** The message exhibits characteristics that warrant investigation for suspected business email compromise or payment fraud. The available lab artifacts do not establish that a real payment occurred, that the named sender is genuine, or that malware was present.

## 2. Scope and Limitations

### In scope

- Review of the supplied email headers and body.
- Comparison of sender and Reply-To addresses.
- Review of message chronology and authentication-related header text.
- MIME structure and missing attachment-payload review.
- Safe inspection of the synthetic CAB and extracted text file.
- Evidence hashing, screenshot documentation, and IOC classification.

### Out of scope

- Access to the recipient's mail server or mailbox.
- Independent verification of the claimed financial transfer.
- Live DNS, SPF, DKIM, or DMARC validation.
- Independent reputation or ownership verification of the observed IP address.
- Recovery or forensic analysis of the original attachment payload.
- Attribution to a real person or organization.

## 3. Incident Details

| Field | Assessment |
|---|---|
| Suspected incident | Business email compromise / payment-themed social engineering |
| Severity | Potentially High if acted upon; actual impact not established |
| Likelihood | Suspicious indicators are present; confidence in a real incident is limited by the modified sample |
| Primary evidence | Modified email training sample |
| Attachment | Original payload unavailable; synthetic CAB used for safe practice |
| Claimed reference | `09674321` |
| Claimed amount | INR 1,495,650, according to the modified email body |
| Actual financial loss | Unknown; no transaction evidence supplied |
| Confirmed malware | None established |
| Confirmed compromise | None established |

Severity is a provisional scenario assessment, not a measurement of a confirmed real-world impact.

## 4. Evidence Reviewed

### E-01 — Email sample

Path: `assets/evidence/email/challenge.eml`

SHA-256:

`8d9e777637f66fd45fedc7388ffd97c6a0a771f1c0c59e0a15514a8bc510232d`

The file is a modified, payload-redacted training sample. Its headers and body must not be represented as an untouched original message.

### E-02 — Synthetic CAB

Path: `assets/evidence/attachments/SWT_09674321_synthetic.CAB`

SHA-256:

`dd04f62f7fb1a50850e1f76548a62d66d745ebf7bc207ac5930b031ee2b63d71`

This archive is a synthetic replacement, not the original email attachment.

### E-03 — Extracted text

Path: `analysis/attachment-extracted/payment-receipt-lab.txt`

SHA-256:

`21adb3bd7d3ca72fb4ae1371c69521e560a1ebb7969b39690aae6460dac4c66f`

The text identifies itself as synthetic lab material. Its contents do not verify a financial transaction.

Screenshots and further evidence details are indexed in `Evidence-Register.md`.

## 5. Key Observations

### 5.1 Sender and Reply-To discrepancy

The displayed From address is `info@hackerkiran.com`, while the Reply-To address is `info.hackerkiran@mail.com`.

This difference is worth investigating because a reply may be directed to a different mailbox. The discrepancy alone does not prove impersonation or fraud.

### 5.2 Financial-transfer claims

The body claims that a transfer was successful and provides a reference number, account details, amount, currency, and bank charges.

These are statements made by the email. No bank statement, payment-system record, or independent confirmation was supplied.

### 5.3 Chronology inconsistency

The modified email's Date header and transaction time refer to October 2026, while older Received-header timestamps and the Message-ID timestamp refer to June 2020.

This discrepancy is consistent with the sample having been edited. It cannot be treated as reliable evidence of the original message's actual chronology.

### 5.4 Authentication-related headers

The sample contains SPF-related failure text. Because the email was modified, the text does not establish the result of an independent live SPF check. No live SPF, DKIM, or DMARC verification is claimed in this report.

### 5.5 Attachment limitations

The original attachment payload was unavailable. A synthetic CAB containing harmless text was created to practise safe archive inspection and extraction.

No conclusion about the original attachment's contents, maliciousness, or execution behavior can be drawn from the synthetic replacement.

### 5.6 IP address

The address `192.119.71.157` appears in the supplied header material. Its ownership, reputation, and connection to malicious activity have not been independently established.

## 6. Investigation Workflow

1. Preserved the email sample and identified its modified, payload-redacted status.
2. Reviewed visible message headers and body claims.
3. Compared the From and Reply-To addresses.
4. Identified inconsistencies between newer message dates and older transport-header timestamps.
5. Reviewed MIME structure and documented the unavailable original attachment payload.
6. Inspected the synthetic CAB and extracted harmless text in the lab.
7. Calculated SHA-256 hashes for the three primary artifacts.
8. Captured screenshots and recorded evidence in `Evidence-Register.md`.
9. Documented limitations to prevent synthetic or edited material from being misrepresented as original evidence.

## 7. Recommended Incident Response

The following actions describe how a real organization should respond if a similar message were received. They are recommendations, not actions confirmed to have occurred in this lab.

### Identification and triage

- Preserve the original email in its native format with complete headers.
- Verify the sender through a trusted, previously established communication channel.
- Contact the organization's finance team to verify the transaction independently.
- Review mail gateway, authentication, endpoint, and identity-provider logs where authorized.

### Containment

- If the message is confirmed malicious, quarantine it and search for related messages.
- Block indicators only after validation and in accordance with organizational procedures.
- If credentials may have been exposed, follow the organization's identity incident-response process.

### Eradication and recovery

- Investigate affected endpoints only if there is evidence of attachment execution or other suspicious activity.
- Remove confirmed malicious artifacts and restore affected systems using approved procedures.
- Validate recovery and monitor for recurrence.

### Communication and escalation

- Escalate suspected payment fraud to the appropriate finance, security, and incident-response teams.
- If a transfer is suspected to be fraudulent, contact the bank through an independently verified channel promptly.
- Follow applicable legal, regulatory, and organizational reporting requirements.

## 8. MITRE ATT&CK Considerations

The email's social-engineering characteristics may be relevant to MITRE ATT&CK phishing techniques. However, the available evidence does not establish execution, persistence, credential theft, or other post-delivery activity.

Any technique mapping must be treated as a hypothesis until supported by relevant telemetry. See `MITRE-ATTACK-Mapping.md` for the separate mapping record.

## 9. Findings and Conclusion

The training sample contains indicators appropriate for a BEC-focused investigation: a From/Reply-To discrepancy, financial-transfer claims, and inconsistent chronology.

The strongest conclusion supported by the available evidence is that the **modified sample is suspicious and useful for investigation practice**. The artifacts do not establish a real-world payment, actual compromise, malware presence, sender attribution, or the original attachment's behavior.

## 10. Evidence Integrity

The SHA-256 hashes and evidence descriptions are recorded in `Evidence-Register.md`. Recalculate the hashes before publication or any later evidence transfer. If an artifact changes, record the new hash and explain the change.

## 11. Related Project Files

- `Evidence-Register.md`
- `Investigation-Timeline.md`
- `IOC-Register.csv`
- `MITRE-ATTACK-Mapping.md`
- `lessons-learned.md`
- `README.md`

---

**Handling note:** This report documents a cybersecurity training scenario using modified and synthetic artifacts. It is not a forensic finding about an independently verified real-world incident.
