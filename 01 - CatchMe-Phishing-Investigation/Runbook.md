# CatchMe — Phishing Email Investigation Runbook

**Document type:** SOC operational runbook  
**Project:** CatchMe — Phishing Email Investigation  
**Audience:** SOC Analyst L1/L2  
**Version:** 1.0  
**Status:** Portfolio/lab procedure — adapt and approve before production use

---

## 1. Trigger

Use this runbook when:
- A user reports a suspicious email.
- Mail security tooling flags a suspected phishing message.
- An email is suspected of brand impersonation, credential harvesting, malicious URL delivery, or suspicious attachment delivery.

## 2. Safety and authorization gates

Before starting:
- [ ] Confirm a case/ticket ID exists.
- [ ] Confirm you are authorized to access the message and associated logs.
- [ ] Preserve the original email and calculate SHA-256.
- [ ] Use an analysis copy for parsing or redaction.
- [ ] Do not click URLs, submit credentials, or execute attachments on a normal workstation.
- [ ] Use only approved threat-intelligence services for potentially sensitive indicators/samples.
- [ ] Obtain approval before quarantine/purge, broad blocking, credential reset, token revocation, or endpoint isolation.

If a user reports credential submission, suspicious execution, or active account compromise, notify the L2/IR lead immediately while continuing safe evidence collection.

## 3. Quick triage — first 10–15 minutes

### Step 1 — Record intake
Capture:
- Case ID:
- Reporting user/team:
- Recipient(s):
- Received time and timezone:
- Reported time:
- Subject:
- Display name and From address:
- User actions: not clicked / clicked / attachment opened / replied / credentials entered / unknown.
- Other affected users known? yes / no / unknown.

### Step 2 — Preserve
1. Save the original message as `.eml`/`.msg` where possible.
2. Record original filename, size, source, collection time, and collector.
3. Calculate SHA-256 using an approved tool.
4. Store it in the restricted evidence location with access controls.
5. Make a working copy for analysis.

Example commands (run only in the appropriate local lab or approved workstation):

**Linux**
```bash
sha256sum suspicious-email.eml
file suspicious-email.eml
```

**PowerShell**
```powershell
Get-FileHash .\suspicious-email.eml -Algorithm SHA256
Get-Item .\suspicious-email.eml | Select-Object Name, Length, LastWriteTimeUtc
```

### Step 3 — Initial assessment
Check for:
- Brand/display-name versus sender-domain mismatch.
- Unexpected `Reply-To` or return path.
- Urgency, payment/order notices, password prompts, or unusual requests.
- URL text versus actual URL.
- Unexpected attachments or file types.
- SPF/DKIM/DMARC results and authenticated domains.

**Important:** SPF/DKIM/DMARC pass means the message passed those domain-authentication checks; it does not prove that the sender is authorized by the brand shown in the display name.

### Step 4 — Decide escalation
Escalate immediately to L2/IR if any of the following are true:
- Credentials were submitted or MFA was approved unexpectedly.
- An attachment was executed or a suspicious download ran.
- A suspicious sign-in, mailbox rule, token/OAuth change, or endpoint alert is correlated.
- Multiple recipients or an active campaign are suspected.
- A privileged user or sensitive business process is involved.
- Available evidence indicates likely compromise.

If interaction status is unknown, contact the reporter and treat impact as undetermined until checked.

## 4. Detailed analyst procedure

### A. Header analysis
Record these fields when present:
- `From`, display name, `Reply-To`, `Return-Path`, `Sender`
- `To`/`Cc`, `Date`, `Subject`, `Message-ID`
- Relevant `Received` headers
- SPF, DKIM, DMARC results and domains

Actions:
1. Identify which domain authenticated the message.
2. Compare visible brand and sending domain.
3. Note unexpected reply domains, relay inconsistencies, and header gaps.
4. Do not assume every header line is trustworthy; interpret the chain in context.

### B. URL analysis
1. Extract URLs from body, HTML, QR codes, and attachments without opening them.
2. Record the original URL in restricted evidence.
3. For the public report, redact sensitive tokens and personal identifiers.
4. Extract hostname/domain and deduplicate indicators.
5. Check reputation/DNS using approved sources, recording source and lookup time.
6. If redirect behavior is relevant, use the approved isolated analysis workflow.

Do not enter credentials or download content from suspected destinations.

### C. Attachment analysis
1. Record filename, file type, size, and SHA-256.
2. Inspect metadata and static structure using approved tools.
3. Record whether active content indicators were observed.
4. Escalate to isolated detonation only if needed and authorized.
5. Document the limitations of static analysis.

### D. Scope searches (authorized telemetry only)
Search the mail platform for:
- Exact Message-ID.
- Sender address/domain.
- Subject and date range.
- URL hostnames/domains.
- Attachment SHA-256.
- Related lookalike domains or message variants.

For each search record:
- Data source and query/filter.
- Time range and timezone.
- Analyst and execution time.
- Result count and sample IDs.
- Whether the search was complete or limited by retention/permissions.

If user interaction is reported, correlate:
- DNS/proxy/web gateway logs.
- Endpoint process/download telemetry.
- Identity sign-ins, MFA events, token/session activity.
- Mailbox rules, forwarding, OAuth consent, and suspicious sent messages.

A missing log source is a coverage gap; it is not proof that no activity occurred.

## 5. Containment decision table

| Finding | Recommended next step | Approval / note |
|---|---|---|
| Suspicious email, no known interaction, no corroboration | Scope recipients and related messages; monitor or close according to policy | L2 review if confidence or spread warrants |
| Confirmed malicious URL and message delivered | Quarantine/remove matching messages; block the narrow confirmed indicator | Use approved change process |
| Credentials entered | Contact identity/IR team; reset credentials, revoke sessions/tokens, check MFA and sign-ins | Follow identity incident policy |
| Attachment executed or suspicious process observed | Start endpoint incident workflow; collect EDR evidence; consider isolation | Endpoint isolation may disrupt work; authorize per policy |
| Suspicious mailbox rule or forwarding | Preserve details, remove/disable rule if confirmed and authorized, review sent/deleted items | Coordinate with messaging/identity teams |
| Multiple recipients or campaign | Expand message search, coordinate purge/blocking and user communications | Incident lead coordinates broad actions |
| Evidence inconclusive | Keep disposition provisional; document gaps and next owner | Do not label as confirmed phishing without support |

## 6. Example investigation queries

These are generic search patterns. Adapt to your mail platform and field names; do not run against systems without authorization.

### SIEM / Elastic KQL starter
```kql
email.url.domain: *
```
This is a **field-presence hunt only**: it finds events with a populated URL-domain field. It is not, by itself, a phishing detection. Confirm the correct data view and field mapping before use.

Example indicator pivot (replace placeholders with verified values and valid field names for your environment):
```kql
email.from.address: "sender@example.invalid"
```

```kql
email.subject: "Example suspicious subject"
```

```kql
file.hash.sha256: "REPLACE_WITH_VERIFIED_SHA256"
```

These field names may not match your integration or ECS version. Validate mappings and test queries on known events before relying on results.

## 7. Evidence and reporting

Complete or update:
- `Evidence-Register.md`
- `Investigation-Timeline.md`
- `IOC-Register.csv`
- `analysis/evidence-timeline.csv`
- `analysis/indicator-inventory.csv`
- `Incident-Response-Report.md`
- `MITRE-ATTACK-Mapping.md`
- `lessons-learned.md`

For each IOC include:
- Value and type.
- Source artifact and exact context.
- First observed timestamp if known.
- Confidence and status (observed, suspicious, confirmed malicious, benign, unknown).
- Lookup source/time, if checked.
- Action taken and expiry/review date, where applicable.

Map MITRE ATT&CK only when supported by evidence. Use “candidate mapping” or “not established” when the technique is not confirmed.

## 8. Case-specific findings from the CatchMe sample

Use these as context for this portfolio sample, not as a general verdict on all messages:

- One message displayed ADT branding but used `ant.anki-tech.com`; another displayed Home Depot branding but used `teckbe.com`.
- SPF/DKIM/DMARC passed for the respective sending domains. This does not prove brand authorization.
- A PDF attachment was statically examined; no obvious active-content indicators were identified by the checks recorded in the project. Static checks do not prove universal safety.
- The extracted URL destinations/reputation and real-world recipient interaction were not independently established in the available evidence.
- Do not claim credential theft, successful exploitation, endpoint compromise, or confirmed malicious infrastructure without additional evidence.

## 9. Closure checklist

- [ ] Original evidence retained and hashes verified.
- [ ] Header, content, URL, and attachment analysis recorded.
- [ ] User interaction status established or explicitly marked unknown.
- [ ] Mail scope completed or limitations documented.
- [ ] Endpoint/identity checks performed when warranted.
- [ ] Containment actions approved, completed, and verified—or assigned to an owner.
- [ ] Timeline, IOC register, evidence register, and report updated.
- [ ] Confidence and severity rationale documented.
- [ ] Final status selected: confirmed malicious / likely malicious / suspicious inconclusive / benign / unable to determine.
- [ ] Lessons learned and detection improvements recorded.

## 10. Suggested final case note

> **Disposition:** [status]  
> **Severity:** [severity] — [brief rationale]  
> **Summary:** [what was observed, without overstating conclusions]  
> **Scope:** [recipients and systems searched; time range]  
> **User interaction:** [known / none reported / unknown]  
> **Actions:** [completed actions and verification]  
> **Limitations:** [missing telemetry, unverified URLs, static-only analysis, etc.]  
> **Next owner / follow-up:** [owner and due date, if applicable]
