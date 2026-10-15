# SOC Analyst Playbook
## CatchMe — Malicious URL & Phishing Infrastructure Investigation

**Audience:** SOC Analyst L1/L2  
**Trigger:** Threat-intelligence match, suspicious URL alert, or DNS filtering observation  
**Objective:** Validate the alert, assess exposure, preserve evidence, and recommend proportionate response actions.

---

## 1. Initial Alert Triage

Record:

- Alert ID and detection source.
- Event timestamp and timezone.
- User and device, if available.
- Original URL or hostname; defang it in analyst notes.
- Intelligence source and retrieval time.
- Related DNS, proxy, email, firewall, and EDR events.

Do not visit a suspicious URL directly from the analyst workstation.

## 2. Validate the Indicator

1. Confirm the indicator was captured correctly.
2. Check whether it appears in an approved threat-intelligence source.
3. Record when the intelligence was retrieved.
4. Inspect URL components without opening the destination.
5. Check domain registration and DNS metadata where appropriate.
6. Consider shared hosting, redirects, stale indicators, and resolver filtering.
7. Seek independent corroboration before assigning a definitive malicious verdict.

**Decision:** If the indicator cannot be corroborated, retain it as suspicious or unresolved rather than automatically classifying it as malicious.

## 3. Determine Exposure

Search authorized enterprise telemetry for the indicator:

- DNS query logs.
- Proxy or secure web gateway records.
- Email gateway and message-trace logs.
- Endpoint network connections and browser artifacts.
- Authentication events where credential exposure is suspected.

Record the search window, data sources, query logic, and results.

**Decision:**

- No match found: document the data sources and time window searched; do not claim that no exposure occurred across unsearched systems.
- Network or email match found: establish which user or device was involved and whether a connection or interaction occurred.
- Credential or endpoint evidence found: escalate according to incident severity and organizational procedures.

## 4. Assess Severity

| Level | Criteria | Response |
|---|---|---|
| Informational | Feed match or suspicious structure with no corroborating activity | Enrich and document |
| Low | Indicator corroborated, but no evidence of user or endpoint exposure | Review controls and consider scoped blocking |
| Medium | Confirmed enterprise DNS, proxy, or email activity involving a corroborated indicator | Investigate user/device exposure and related events |
| High | Evidence of credential submission, payload execution, account compromise, or other material impact | Escalate immediately and initiate the approved incident response process |

Severity must follow organizational policy and the evidence available. A feed match alone does not justify a high-severity classification.

## 5. Response Actions

When justified by evidence and authorized policy:

- Add confirmed indicators to approved security controls.
- Scope blocks carefully when domains use shared hosting.
- Search for related URLs, domains, and events.
- Preserve relevant logs and original message artifacts.
- Reset credentials or revoke sessions only when compromise is suspected or confirmed and the response is authorized.
- Isolate endpoints only when supported by evidence and approved procedures.
- Notify the incident response team when escalation criteria are met.

## 6. DNS Filtering Investigation

If a DNS response differs between resolver paths:

1. Save the exact query, resolver, timestamp, response code, and answer records.
2. Compare results using approved resolvers and organizational policy.
3. Check resolver logs and documented response-policy rules.
4. Consult the DNS or network administrator to identify the filtering component.
5. Do not treat the filtering destination as the suspicious domain's original infrastructure.
6. Do not infer maliciousness solely from the DNS response.

## 7. Closure Criteria

Close or downgrade the alert only when:

- The indicator and evidence have been recorded.
- Exposure searches and their limitations are documented.
- Required response and escalation actions are complete.
- The analyst disposition is justified by the evidence.
- Evidence references and hashes are recorded where applicable.

## 8. Required Case Notes

Document the alert, investigation timeline, indicator disposition, telemetry reviewed, response actions, evidence references, limitations, and recommended follow-up.

**Related documents:** `Runbook.md`, `Incident-Response-Report.md`, `Evidence-Register.md`, `Detection-Logic.md`
