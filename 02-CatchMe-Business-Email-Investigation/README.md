# CatchMe — Business Email Investigation

A hands-on cybersecurity portfolio project investigating a suspicious payment-themed email using email-header review, MIME inspection, safe attachment analysis, evidence integrity checks, and incident-response documentation.

> **Lab disclaimer:** The email is a modified, payload-redacted training sample. The CAB file is a synthetic replacement, not the original attachment. No real transaction, compromise, or malware infection has been confirmed.

## Objectives

- Examine sender and Reply-To discrepancies.
- Review message headers and identify chronology inconsistencies.
- Inspect MIME structure and document the unavailable original attachment payload.
- Safely examine a synthetic CAB archive and its extracted text.
- Record SHA-256 hashes and maintain an evidence register.
- Classify indicators without treating unverified claims as confirmed malicious activity.
- Document investigation findings, limitations, and recommended response actions.

## Project Structure

```text
.
├── README.md
├── Evidence-Register.md
├── Incident-Response-Report.md
├── Investigation-Timeline.md
├── IOC-Register.csv
├── MITRE-ATTACK-Mapping.md
├── lessons-learned.md
├── assets/
│   └── evidence/
│       ├── email/
│       ├── attachments/
│       └── screenshots/
├── analysis/
│   ├── attachment-extracted/
│   └── working-copy/
└── .gitignore
```

## Key Findings

- The From and Reply-To addresses differ in the modified sample.
- The email claims a successful financial transfer, but no independent payment records were provided.
- October 2026 message/body timestamps conflict with older June 2020 header timestamps.
- SPF-related text appears in the sample, but no live authentication check is claimed.
- The original attachment payload is unavailable.
- The synthetic CAB contains harmless training text and cannot establish the original attachment's behavior.

## Evidence Integrity

| Artifact | SHA-256 |
|---|---|
| Modified email sample | `8d9e777637f66fd45fedc7388ffd97c6a0a771f1c0c59e0a15514a8bc510232d` |
| Synthetic CAB | `dd04f62f7fb1a50850e1f76548a62d66d745ebf7bc207ac5930b031ee2b63d71` |
| Extracted lab text | `21adb3bd7d3ca72fb4ae1371c69521e560a1ebb7969b39690aae6460dac4c66f` |

Recalculate hashes after any artifact changes. Full descriptions and limitations are in [Evidence-Register.md](Evidence-Register.md).

## Investigation Documents

- [Incident Response Report](Incident-Response-Report.md)
- [Investigation Timeline](Investigation-Timeline.md)
- [Evidence Register](Evidence-Register.md)
- [IOC Register](IOC-Register.csv)
- [MITRE ATT&CK Mapping](MITRE-ATTACK-Mapping.md)
- [Lessons Learned](lessons-learned.md)

## Safe Reproduction

Inspect only the supplied lab artifacts. Do not execute unknown attachments. Use an isolated lab and trusted analysis utilities. The synthetic CAB is for file-handling practice, not malware simulation.

## Limitations

This project does not establish sender attribution, actual financial loss, successful compromise, original attachment contents, or maliciousness of the observed IP address. Indicators have not been independently validated against live external sources.

## Skills Demonstrated

Email-header analysis, email fraud triage, MIME inspection, safe archive handling, SHA-256 integrity verification, evidence documentation, IOC classification, timeline analysis, and incident-response reporting.

## Public Evidence and Redaction

Sanitized email copies for public review are stored in `public-evidence/email/`.
They are derived training artifacts, not the original email evidence. Known
account-number and financial-value strings were replaced in these copies.
The original lab files remain separate; do not publish them without reviewing
their contents and confirming authorization. Screenshots also require visual
privacy review before publication.
