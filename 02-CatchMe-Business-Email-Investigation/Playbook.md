# CatchMe — Suspicious Email Response Playbook

## 1. Purpose
Provide a repeatable response process for suspected phishing, business email compromise (BEC), malicious attachments, spoofing, and payment-fraud emails.

## 2. Scope
Applies to suspicious email reported by a user or identified by a security monitoring team. This playbook guides investigation and response; it does not establish that a particular email is malicious.

## 3. Severity Guide

| Severity | Example | Initial response |
|---|---|---|
| Critical | Confirmed account takeover, unauthorized transfer, or active widespread compromise | Escalate immediately to incident response, identity, and fraud teams |
| High | Credential theft confirmed, malicious payload executed, or verified unauthorized mailbox activity | Urgent containment and investigation |
| Medium | Strong phishing indicators or suspicious attachment, with no confirmed execution | Analyze evidence and assess exposure promptly |
| Low | Suspicious characteristics but insufficient evidence of malicious activity | Validate indicators and document the outcome |

Adjust severity according to business impact, scope, and organizational policy.

## 4. Roles
- **SOC Analyst:** Validate the report, preserve evidence, investigate indicators, and document findings.
- **Incident Responder:** Coordinate containment, scope, remediation, and recovery.
- **Identity / Email Administrator:** Review authentication, mailbox rules, forwarding, and email security controls.
- **Fraud / Finance Team:** Verify payment instructions or transactions through an independent trusted channel.
- **Incident Lead:** Approve major containment actions and coordinate communications.

## 5. Response Workflow

### Phase 1 — Intake and preservation
1. Record the reporter, receipt time, recipient, subject, and business context.
2. Obtain the original email as an `.eml` or equivalent export when available.
3. Preserve full headers, message identifiers, attachment names, and relevant mail gateway logs.
4. Record file hashes and assign evidence IDs.
5. Preserve originals; analyze working copies.

### Phase 2 — Initial triage
1. Review sender and Reply-To alignment, display-name anomalies, and unexpected domains.
2. Review authentication results such as SPF, DKIM, and DMARC from trustworthy received headers.
3. Examine links, attachment types, urgency, payment requests, and unusual instructions.
4. Check whether the request is expected using an independent trusted communication channel.
5. Treat indicators as leads, not proof of compromise.

### Phase 3 — Technical investigation
1. Analyze headers and message chronology.
2. Inspect MIME structure and attachment metadata without executing attachments.
3. Calculate SHA-256 hashes and classify observed indicators.
4. Review email gateway, endpoint, DNS, proxy, identity, and authentication telemetry where authorized.
5. Determine whether a user opened the attachment, followed a link, submitted credentials, or approved a transaction.
6. Record evidence, timestamps, confidence, and alternative explanations.

### Phase 4 — Containment
Select actions according to verified risk and organizational authorization:
- Quarantine or remove confirmed malicious messages from affected mailboxes.
- Block confirmed malicious indicators through approved security controls.
- Revoke sessions, reset credentials, or enforce additional authentication when account compromise is suspected or confirmed.
- Disable malicious forwarding rules or OAuth grants after validation.
- Contact Finance through a trusted channel if payment fraud is suspected.
- Preserve logs and evidence before actions that may destroy relevant data.

### Phase 5 — Eradication and recovery
1. Remove malicious persistence or mailbox changes.
2. Remediate affected endpoints and identities.
3. Restore access using approved recovery procedures.
4. Verify that detections, authentication controls, and mail protections are operating.
5. Monitor for recurrence and related activity.

### Phase 6 — Closure
1. Document scope, impact, evidence, actions, and unresolved questions.
2. Record whether compromise or financial loss was confirmed.
3. Identify detection or process improvements.
4. Obtain the required incident-owner approval before closure.

## 6. Escalation Triggers
Escalate immediately when there is evidence of account takeover, credential disclosure, attachment execution, unauthorized mailbox rules, confirmed payment fraud, or activity affecting multiple users.

## 7. Evidence and Safety Rules
- Do not execute suspicious attachments on a production system.
- Do not rely on an email's own claims to validate a payment.
- Do not treat an edited sample, synthetic artifact, or unverified indicator as original evidence.
- Keep original evidence separate from sanitized publication copies.
- Record hashes and note whenever evidence is modified.
- Follow applicable retention, privacy, and incident-reporting policies.

## 8. Lab-Specific Limitation
The CatchMe training project uses a modified, payload-redacted email and a harmless synthetic CAB file. The lab artifacts do not, by themselves, prove real malware execution, account compromise, or financial loss.

## 9. Related Documents
- `Runbook.md`
- `Evidence-Register.md`
- `Incident-Response-Report.md`
- `Investigation-Timeline.md`
- `IOC-Register.csv`
- `MITRE-ATTACK-Mapping.md`
