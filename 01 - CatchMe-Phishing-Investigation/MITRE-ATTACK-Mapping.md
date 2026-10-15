# MITRE ATT&CK Mapping

## Assessment status

This is a cautious, hypothesis-led mapping for a phishing-analysis lab. The collected artifacts do not by themselves establish that a successful attack occurred. Therefore, candidate techniques below are investigation leads, not confirmed detections.

| Candidate technique | Why it may be relevant | Evidence status |
|---|---|---|
| **T1566 — Phishing** | The artifacts are email messages being examined for suspicious characteristics. | Investigation context only; malicious intent is not established. |
| **T1566.001 — Spearphishing Attachment** | One message contains a PDF attachment (`zmqpalgh.pdf`). | Attachment presence is observed; malicious content or delivery intent is not established. |
| **T1566.002 — Spearphishing Link** | Email bodies contain tracking-style and click-through URLs. | URLs were extracted; malicious destinations and user interaction are unverified. |

## Evidence needed before confirming a technique

- Establish message provenance and context.
- Validate URLs using approved, safe enrichment methods and record final destinations only if safely established.
- Determine whether a recipient clicked a link or opened an attachment using authorized endpoint, proxy, DNS, or email telemetry.
- Correlate with execution, process, network, or other host telemetry before asserting post-delivery behavior.

## Reporting rule

Do not mark these techniques as confirmed solely because a message contains a URL or attachment. Update this mapping only when additional evidence supports the behavior. Use the official MITRE ATT&CK knowledge base as the reference for technique definitions.
