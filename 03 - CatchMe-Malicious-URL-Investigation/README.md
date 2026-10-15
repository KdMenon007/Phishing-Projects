# CatchMe — Malicious URL & Phishing Infrastructure Investigation

A practical SOC L2 threat-intelligence investigation covering URL triage, domain registration metadata, DNS analysis, resolver comparison, detection design, and evidence preservation.

> **Investigation status:** Initial investigation completed; independent reputation validation and enterprise telemetry correlation remain pending.

## Objectives

- Acquire and validate a public threat-intelligence feed snapshot.
- Build a safe, defanged sample of URL indicators.
- Inspect URL structure without opening suspicious destinations.
- Collect RDAP registration metadata where available.
- Observe DNS A, AAAA, and MX records.
- Compare DNS resolver responses and investigate possible filtering.
- Preserve evidence, timestamps, hashes, and limitations.
- Propose detection logic and response procedures.

## Investigation Summary

- Feed snapshot: 300 non-empty, valid, unique URL entries reported by the acquisition validation.
- Investigation sample: 10 defanged URLs.
- RDAP: 2 HTTP 200 responses, 5 HTTP 404 responses, and 3 HTTP 400 responses.
- DNS: responses, timeouts, and no-answer results were observed.
- Resolver comparison: the system resolver returned a filtering-related CNAME for two indicators. For one indicator, Cloudflare and Google DNS returned a different A record.
- No sampled website was opened and no HTTP request was sent to a sampled indicator.

These observations do not independently establish the current malicious status of every sampled domain or demonstrate victim impact.

## Repository Structure

```text
.
├── README.md
├── Incident-Response-Report.md
├── Investigation-Timeline.md
├── Evidence-Register.md
├── IOC-Register.csv
├── MITRE-ATTACK-Mapping.md
├── Detection-Logic.md
├── Playbook.md
├── Runbook.md
├── lessons-learned.md
├── analysis/
│   ├── raw/                 # Restricted raw feed snapshot; do not publish
│   ├── working/             # Working datasets and enrichment outputs
│   ├── scripts/             # RDAP and DNS enrichment scripts
│   ├── url_triage.py
│   ├── build_url_dataset.py
│   ├── extract_domains.py
│   └── url-triage-results.json
└── assets/
    └── evidence/
        └── dns/
            └── resolver-comparison.md
```

## Methodology

1. Acquire and validate the feed snapshot.
2. Select ten records and defang the indicators.
3. Run local URL-structure triage.
4. Query RDAP services for registration metadata.
5. Query DNS records using the configured resolver.
6. Compare resolver responses for a selected indicator.
7. Record observations, limitations, and artifact hashes.
8. Draft proposed detections, an analyst playbook, and an operational runbook.

## Tools

- Python 3
- `requests`
- `dig`
- RDAP services
- OpenPhish community feed
- SHA-256 hashing

## Safety and Evidence Handling

- Do not open suspicious URLs or send HTTP requests to the sampled destinations.
- Keep raw threat-intelligence feeds in restricted working storage.
- Publish only defanged indicators and appropriately sanitized evidence.
- Treat feed inclusion as an intelligence lead, not proof of current maliciousness.
- Treat failed RDAP lookups and DNS timeouts as inconclusive.
- Do not attribute DNS filtering to a specific device or provider without corroboration.
- Do not label proposed detections as production-validated.

## Key Documents

| Document | Purpose |
|---|---|
| `Incident-Response-Report.md` | Investigation findings and limitations |
| `Evidence-Register.md` | Evidence inventory and hashes |
| `Investigation-Timeline.md` | Investigation activity log |
| `IOC-Register.csv` | Defanged indicators and investigation status |
| `MITRE-ATTACK-Mapping.md` | Evidence-qualified ATT&CK mapping |
| `Detection-Logic.md` | Proposed detection patterns |
| `Playbook.md` | Analyst decisions and escalation |
| `Runbook.md` | Repeatable investigation steps |
| `lessons-learned.md` | Lessons and future improvements |

## Validation Status

The Python scripts passed syntax checks during project validation. Detection logic remains proposed and has not been validated against enterprise SIEM telemetry.

## Disclaimer

This is a controlled educational portfolio investigation. No claim of victim compromise, credential theft, malware execution, or threat-actor attribution is made.
