# CatchMe — Phishing Email Investigation Playbook

**Document type:** Security Operations Playbook  
**Project:** CatchMe — Phishing Email Investigation  
**Audience:** SOC Analyst L1/L2, Incident Responder, Detection Engineer  
**Version:** 1.0  
**Status:** Portfolio/lab procedure — adapt and approve before production use

---

## 1. Purpose

Provide a repeatable investigation method for suspected phishing or brand-impersonation emails. The playbook covers evidence preservation, message analysis, URL and attachment triage, correlation, severity assessment, containment decisions, escalation, and documentation.

This is a workflow, not a claim that every message is malicious. Analysts must distinguish **observed evidence**, **inference**, and **unverified hypotheses**.

## 2. Scope

### In scope
- Suspicious email reported by a user or identified by monitoring.
- Sender/display-name mismatch and possible brand impersonation.
- Email headers and authentication results (SPF, DKIM, DMARC).
- URLs, redirectors, domains, IPs, attachments, and file hashes.
- Mailbox/search-based scoping where authorized telemetry is available.
- Evidence preservation, incident documentation, and response recommendations.

### Out of scope
- Opening links or attachments on a production endpoint without an approved isolated-analysis process.
- Credential submission to a suspicious site.
- Active interaction with suspected attacker infrastructure.
- Deleting/quarantining messages without authorization and evidence retention.
- Declaring a sender legitimate solely because SPF/DKIM/DMARC passed.
- Claiming endpoint compromise, credential theft, or successful delivery without supporting telemetry.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Reporting user / service desk | Submit the original message as an attachment where possible; provide time and interaction details. |
| SOC L1 | Validate the report, preserve evidence, perform initial triage, and escalate when thresholds are met. |
| SOC L2 / Incident responder | Correlate indicators, scope affected users, assess impact, recommend/execute authorized containment, and lead investigation. |
| Messaging / IT administrator | Run authorized mail searches, quarantine or purge messages, block indicators, and preserve relevant logs. |
| Incident commander / security lead | Approve high-impact actions and coordinate communications for significant incidents. |

## 4. Required inputs and tools

- Original email in `.eml` or equivalent export; retain the original unmodified.
- Case/ticket ID, reporter, receipt time, recipient, and user-interaction status.
- Approved header parser and static attachment-analysis tools.
- Authorized mail security logs, message trace, SIEM/EDR telemetry, DNS/proxy logs, and identity logs where available.
- Approved reputation/threat-intelligence sources.
- Evidence register, timeline, IOC register, and incident report template.

Use only organization-approved services for submitting potentially sensitive samples. Do not upload confidential email or attachments to public scanners without authorization.

## 5. Investigation workflow

### Phase A — Intake and preservation
1. Open a case and assign a unique case ID.
2. Record who reported the email, when it was received/reported, recipient(s), subject, and whether the user clicked, opened, replied, scanned a QR code, or entered credentials.
3. Request the original message as an attachment (`.eml`/`.msg`) when possible; screenshots alone are insufficient for complete header analysis.
4. Preserve the original file read-only. Calculate SHA-256 and record the hash, file size, collection time, source, and collector.
5. Work from a separate analysis copy. Record every transformation or redaction applied to a public/sanitized derivative.
6. Do not execute attachments or browse to URLs during intake.

### Phase B — Header and sender analysis
1. Extract `From`, display name, `Reply-To`, `Return-Path`, `Sender`, `To`, `Date`, `Subject`, `Message-ID`, and relevant `Received` headers.
2. Identify the originating/first trusted relay only where the header chain supports it. Treat untrusted or user-supplied header lines cautiously.
3. Review SPF, DKIM, and DMARC results and note the authenticated domain and DMARC policy.
4. Compare the visible brand, sender domain, reply domain, link domains, and expected business context.
5. Record anomalies such as lookalike domains, unexpected reply destinations, mismatched branding, unusual urgency, payment/order claims, or unsolicited attachments.
6. Do not treat authentication pass as proof of brand authorization or benign intent.

### Phase C — Content and URL triage
1. Extract URLs without visiting them. Normalize and deduplicate indicators while retaining the original value in restricted evidence.
2. Record hostname, path, query-string presence, redirector/tracking status, and where the URL appeared.
3. Use approved passive reputation and DNS sources where permitted. Record source and lookup time; reputation results are context, not proof.
4. If redirects need to be examined, use an approved isolated environment and follow organizational rules. Do not use personal accounts or enter credentials.
5. Record QR codes, shortened URLs, image-only content, and link text versus actual destination.
6. Preserve the email body and any relevant MIME parts.

### Phase D — Attachment triage
1. Calculate SHA-256 and record file type, size, and source message.
2. Inspect metadata and perform static checks with approved tools.
3. Look for scripts, macros, embedded files, launch actions, suspicious object references, or other active content appropriate to the file type.
4. If detonation is required, obtain approval and use a disposable isolated sandbox with controlled networking.
5. Do not call a file safe solely because static checks show no obvious suspicious structures.

### Phase E — Scope and correlation
1. Search authorized mail telemetry for matching sender, subject, Message-ID, URLs, attachment hashes, and related domains.
2. Identify recipients, delivery status, whether messages were opened or interacted with, and whether similar messages exist.
3. If a click or credential submission is reported, correlate proxy/DNS/browser, endpoint, identity, and authentication logs around the event time.
4. Look for suspicious sign-ins, MFA changes, mailbox-rule changes, OAuth consent, downloads, process execution, and other follow-on activity when relevant and available.
5. Record each search query, time range, data source, result count, and limitations.
6. No telemetry available means **not assessed**, not “no activity occurred.”

### Phase F — Assessment and severity
Assess:
- Evidence strength and confidence.
- Number of recipients and message spread.
- User interaction and credential submission.
- Attachment behavior and URL destination/reputation.
- Evidence of endpoint, identity, or mailbox compromise.
- Business impact, privileged accounts, and sensitive data exposure.

Suggested severity guide (use local policy if it differs):

| Severity | Example criteria | Expected handling |
|---|---|---|
| Critical | Confirmed compromise of privileged identity or broad active campaign with material impact | Immediate incident escalation and coordinated containment |
| High | Credential submission, malicious execution, confirmed harmful destination, or strong compromise evidence | Urgent L2/IR escalation; containment under authorization |
| Medium | Strongly suspicious message delivered to one or more users; interaction/impact unclear | L2 investigation and mail scoping |
| Low | Suspicious but weak evidence; no known interaction and no corroborating indicators | Complete triage, document uncertainty, monitor or close per policy |

Severity is provisional and should be updated as evidence changes.

### Phase G — Response and recovery
Select actions based on confidence, scope, and authorization:
- Quarantine or remove matching messages using approved mail controls.
- Block confirmed malicious URLs/domains/hashes where technically appropriate and approved.
- Reset credentials and revoke sessions/tokens when credential exposure or compromise is supported.
- Isolate endpoints only when endpoint risk justifies the disruption and policy permits.
- Remove malicious mailbox rules or persistence only after preserving evidence and validating the change.
- Search for additional affected users and related indicators.
- Validate containment and recovery; record who approved and executed each action.

Do not block a shared hosting domain or broad infrastructure based only on a weak association. Prefer the narrowest effective indicator.

### Phase H — Closure and lessons learned
1. Complete the incident report, timeline, evidence register, and IOC register.
2. Label each conclusion as confirmed, likely, possible, or not established.
3. Document actions taken, actions recommended but not performed, owners, timestamps, and verification results.
4. Add detection opportunities and lessons learned.
5. Close only when required response actions are complete or explicitly transferred to an owner.

## 6. Decision points

- **Did a user click, open an attachment, scan a QR code, reply, or submit credentials?** If yes or unknown, prioritize scoping and L2 review.
- **Is there evidence of execution, suspicious sign-in, or mailbox change?** If yes, activate the relevant endpoint/identity incident process.
- **Are multiple recipients or matching messages present?** If yes, scope campaign-wide and coordinate messaging actions.
- **Is the only positive signal a brand mismatch or authentication pass/fail?** Continue analysis; neither alone proves maliciousness or legitimacy.
- **Are required logs unavailable?** Record the gap and state that impact is undetermined.

## 7. Required case documentation

- Case ID, analyst, timestamps, source, and scope.
- Original evidence filenames, hashes, and custody notes.
- Header/authentication findings.
- URL/domain/IP/hash indicators with context and confidence.
- Attachment analysis results and limitations.
- Mail/endpoint/identity searches and query results.
- Timeline and MITRE ATT&CK mapping only where evidence supports it.
- Severity and rationale.
- Actions taken, approvals, verification, and outstanding tasks.
- Final disposition, confidence, and lessons learned.

## 8. Case-specific notes for this portfolio investigation

The sample project reviewed three email artifacts and a PDF attachment. The analyzed messages displayed brand names associated with ADT and Home Depot, while the sender domains were `ant.anki-tech.com` and `teckbe.com`. SPF/DKIM/DMARC passed for those sending domains, but that does **not** establish authorization to represent the named brands. The PDF's static checks found no obvious active-content indicators, and the text included `THM{BENIGN_PDF_ATTACHMENT}`; this is not proof that the file is universally safe. URL destinations/reputation and real-world recipient interaction were not independently established in the available evidence. Treat conclusions as limited to the collected artifacts.

## 9. Quality checklist

- [ ] Original evidence preserved and SHA-256 recorded.
- [ ] Public derivatives are clearly labeled and sanitized.
- [ ] No live URL or attachment was accessed outside approved controls.
- [ ] Authentication results interpreted in domain context.
- [ ] Indicators have source, context, timestamp, and confidence.
- [ ] Scope searches and data gaps are documented.
- [ ] Severity includes rationale and is updated as needed.
- [ ] Containment is authorized, targeted, and verified.
- [ ] Report separates facts, hypotheses, and unperformed actions.
