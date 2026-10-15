# Lessons Learned — CatchMe Business Email Investigation

## What the Investigation Demonstrates

1. **Compare sender and Reply-To fields.** A mismatch warrants review but does not independently prove fraud.
2. **Review the full header chronology.** Date, Message-ID, and Received fields may conflict; preserve and document discrepancies.
3. **Distinguish claims from facts.** A payment confirmation in an email is not proof of a completed transaction.
4. **Treat authentication results carefully.** Text copied or edited into a sample is not a substitute for independent SPF, DKIM, or DMARC validation.
5. **Do not substitute synthetic artifacts silently.** Clearly label the synthetic CAB and extracted text; neither represents the missing original attachment.
6. **Calculate hashes and maintain an evidence register.** Hashes support file-integrity tracking, not authenticity or maliciousness verdicts.
7. **Record limitations.** State what was inspected, what was unavailable, and what remains unverified.
8. **Protect sensitive data before publication.** Redact account details and personal information from screenshots and public artifacts.
9. **Use ATT&CK mappings cautiously.** Map hypotheses separately from techniques supported by confirmed telemetry.
10. **Verify financial requests independently.** In a real incident, use a trusted contact method and coordinate promptly with finance, security, and the bank as appropriate.

## Improvements for a Future Investigation

- Obtain the original email in native format with complete headers and attachment bytes, where legally authorized.
- Preserve original artifacts read-only and hash them before analysis.
- Validate SPF, DKIM, and DMARC independently using the appropriate message and DNS evidence.
- Review mail gateway, identity, endpoint, and network telemetry when available.
- Validate IP and domain reputation through documented, reputable sources before classifying them.
- Record analyst actions and timestamps contemporaneously.
- Test screenshots for exposed personal or financial information before committing them to a public repository.

## Final Limitation

This exercise uses a modified email sample and a synthetic attachment. It does not establish a real-world payment, fraud loss, compromise, malware infection, or sender attribution.
