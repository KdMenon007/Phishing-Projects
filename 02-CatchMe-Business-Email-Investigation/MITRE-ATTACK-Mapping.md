# MITRE ATT&CK Mapping — CatchMe Business Email Investigation

## Purpose

This document records possible ATT&CK relevance for the training scenario. A mapping is not proof that a technique occurred. The email is modified, and the original attachment payload is unavailable.

## Technique Assessment

| Technique | Name | Relevance | Evidence status |
|---|---|---|---|
| T1566.001 | Phishing: Spearphishing Attachment | The message references an attachment, but its original payload is missing. | **Possible scenario mapping only**; malicious attachment delivery is not established |
| T1657 | Financial Theft | The message claims a financial transfer and supplies payment details. | **Unverified scenario context**; no real theft or transaction is confirmed |

Technique references: [MITRE ATT&CK T1566.001](https://attack.mitre.org/techniques/T1566/001/) and [MITRE ATT&CK T1657](https://attack.mitre.org/techniques/T1657/).

## Evidence and Limitations

- The From and Reply-To addresses differ in the modified sample.
- The body contains a payment-related claim.
- Message dates are inconsistent with older header timestamps.
- The original attachment payload was unavailable.
- The synthetic CAB contains harmless training text.
- No evidence establishes execution, persistence, credential theft, or successful compromise.

## Mapping Decision

Treat the techniques above as investigation hypotheses rather than confirmed adversary behavior. Do not map post-delivery execution or other endpoint techniques without supporting telemetry.

## Evidence References

- `Evidence-Register.md`
- `Incident-Response-Report.md`
- `Investigation-Timeline.md`
- `IOC-Register.csv`
