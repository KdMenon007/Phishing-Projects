# Investigation Timeline — CatchMe Business Email Investigation

## 1. Purpose

This timeline separates timestamps recorded in the modified email sample from claims made in its body and activities performed during the lab investigation. The email is not an untouched original message.

## 2. Email-Recorded and Claimed Times

| Time or date | Source | Interpretation | Confidence and limitation |
|---|---|---|---|
| 9 June 2020, timestamp embedded in Message-ID | Message-ID header | Identifier contains an older timestamp | Header text only; not proof of message creation time |
| 10 June 2020 | Older Received-header timestamps | Transport-header text records an earlier date | Headers belong to a modified sample and have not been independently corroborated |
| 15 October 2026, 09:18:55 UTC+05:30 | Modified Date header | Displayed message date | Deliberately edited sample value; not an independently verified send time |
| 15 October 2026, 09:18:55 | Email body | Claimed transaction date and time | Unverified email claim; not proof that a transfer occurred |

## 3. Lab Investigation Sequence

The exact wall-clock times of the following activities were not recorded in the available notes. They are therefore listed in workflow order rather than assigned invented timestamps.

| Sequence | Activity | Result |
|---|---|---|
| L-01 | Reviewed the email sample | Identified it as modified and payload-redacted |
| L-02 | Inspected sender and Reply-To fields | Identified different mailbox addresses |
| L-03 | Compared message and transport-header dates | Identified a chronology inconsistency |
| L-04 | Reviewed MIME structure | Original attachment payload was unavailable |
| L-05 | Inspected the synthetic CAB archive | Confirmed a safe training artifact was available for analysis |
| L-06 | Extracted the CAB text file | Identified the content as synthetic lab material |
| L-07 | Calculated SHA-256 hashes | Recorded hashes for the email, CAB, and extracted text |
| L-08 | Captured investigation screenshots | Nine screenshots were inventoried under `assets/evidence/screenshots/` |
| L-09 | Documented findings | Created the evidence register and incident response report |

## 4. Timeline Assessment

The sample contains at least three distinct time references: a June 2020 timestamp in the Message-ID, June 2020 Received-header timestamps, and an October 2026 Date header and transaction claim.

These references are inconsistent. Because the sample was edited, they must not be combined into a single verified chronology of an original email or financial transaction.

## 5. Evidence References

- Email sample: `assets/evidence/email/challenge.eml`
- Evidence register: `Evidence-Register.md`
- Incident response report: `Incident-Response-Report.md`
- Screenshot evidence: `assets/evidence/screenshots/`

## 6. Limitations

- No original, unmodified email was established in the available evidence.
- The original attachment payload was unavailable.
- The synthetic CAB does not establish what the original attachment contained.
- No bank or payment-system records were provided to verify the claimed transfer.
- The exact dates and times of lab activities were not recorded.
