# MITRE ATT&CK Mapping
## CatchMe — Malicious URL & Phishing Infrastructure Investigation

**Mapping status:** Evidence-qualified; no adversary technique confirmed  
**Investigation type:** Threat-intelligence and DNS metadata analysis

---

## 1. Mapping Principles

MITRE ATT&CK techniques describe adversary behavior. A URL appearing in a threat-intelligence feed, a registration record, or a DNS response does not by itself prove that an adversary performed a specific technique.

This investigation did not examine phishing messages, user interactions, malware execution, or victim telemetry. Therefore, the observations below are not sufficient to confirm a technique.

## 2. Candidate Technique for Further Investigation

| Technique | Name | Current status | Evidence required |
|---|---|---|---|
| T1566 | Phishing | Not confirmed | A phishing message or equivalent delivery evidence, with context showing an attempt to deliver a malicious link or attachment |

**Caution:** Do not assign a phishing sub-technique solely because a URL is present in a threat-intelligence feed. Confirm the delivery mechanism from the relevant email, messaging, or other telemetry first.

Official reference: https://attack.mitre.org/techniques/T1566/

## 3. Observed Behaviors That Are Not ATT&CK Technique Confirmations

| Observation | Why it is not enough to confirm an ATT&CK technique |
|---|---|
| URL present in an OpenPhish feed snapshot | Establishes a feed observation, not the delivery method or adversary behavior |
| Suspicious URL structure flagged by local triage | Indicates a feature for review; it does not prove exploitation or credential theft |
| RDAP registration metadata returned | Registration metadata does not demonstrate adversary behavior |
| DNS response differs between resolver paths | Supports investigation of DNS filtering or rewriting; it does not demonstrate adversary command-and-control |
| A domain resolves to shared hosting infrastructure | Hosting and resolution alone do not establish malicious use of that infrastructure |

## 4. Additional Evidence Needed

Before mapping techniques, collect and validate relevant evidence such as:

- Original email or message headers and body.
- Secure email gateway or proxy records.
- DNS query logs and endpoint network telemetry.
- Browser or endpoint artifacts showing user interaction.
- Process execution or file artifacts if a payload was delivered or executed.
- Authentication logs if credential submission or account compromise is suspected.

## 5. Conclusion

No MITRE ATT&CK technique is confirmed by the current metadata-only investigation.

T1566 (Phishing) is retained as a candidate for investigation only. The mapping should be updated if new evidence establishes a phishing delivery event or another specific adversary behavior.

---

**Evidence references:** `Evidence-Register.md`, `Incident-Response-Report.md`, `Detection-Logic.md`
