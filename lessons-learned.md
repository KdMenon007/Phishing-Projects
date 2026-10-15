# Lessons Learned

## What this investigation reinforced

1. **Validate the sender identity.** Compare display name, sender address, Reply-To, Return-Path, and sending domain. A brand/domain mismatch is a reason to investigate, not proof by itself.
2. **Interpret authentication carefully.** SPF, DKIM, and DMARC results relate to domain authentication/alignment; they do not establish that the message content is trustworthy or that the sender is authorized to represent a displayed brand.
3. **Inspect attachments statically first.** Confirm MIME type and filename, compute hashes, inspect metadata and PDF structure, and extract text without opening the file in a reader.
4. **Treat extracted URLs as indicators, not verdicts.** Record them safely, avoid visiting suspicious links, and distinguish extraction from reputation checks and redirect-chain analysis.
5. **Preserve evidence integrity.** Keep original artifacts unchanged, record SHA-256 hashes, and document how derived files were produced.
6. **Separate facts from hypotheses.** State what was observed, what remains unverified, and what evidence would be needed to reach a stronger conclusion.
7. **Make timelines cautiously.** A document's metadata timestamp does not establish when it was sent or prove its relationship to a particular email.

## Investigation limitations

- The extracted URL reputation and final redirect destinations were not verified.
- No claim is made that either email is conclusively phishing or conclusively legitimate.
- Static PDF checks and the lab flag support the exercise's benign classification but do not prove absolute safety in all contexts.
- The timeline alone does not establish a relationship between the PDF creation date and either email.

## Follow-up actions

- If authorized lab tooling is available, enrich indicators using approved reputation sources without directly browsing suspicious destinations.
- Document any future enrichment source, lookup time, result, and confidence.
- Keep public portfolio copies sanitized; avoid exposing unnecessary recipient addresses or personal data from raw evidence.
