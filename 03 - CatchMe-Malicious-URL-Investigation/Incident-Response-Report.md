# Incident Response Report
## CatchMe — Malicious URL & Phishing Infrastructure Investigation

**Case ID:** CATCHME-URL-2026-001  
**Investigation date:** 2026-10-15  
**Analyst role:** SOC Analyst L2  
**Case status:** Initial investigation completed; enrichment pending  
**Classification:** Threat intelligence investigation  
**Scope:** Ten defanged URL indicators selected from an OpenPhish community feed

---

## 1. Executive Summary

This investigation examined a ten-URL sample from a retrieved OpenPhish community feed snapshot. The work included URL-structure triage, RDAP registration lookups, DNS record queries, and comparison of responses from the system-configured resolver and two public DNS resolvers.

The feed contained 300 non-empty, valid, unique URL entries when acquired. Ten entries were selected for this investigation. Feed inclusion was treated as a threat-intelligence lead rather than independent proof of current malicious activity.

Two sampled domains returned RDAP registration records. Other lookups returned HTTP 404 or HTTP 400 responses, which were treated as inconclusive. DNS queries returned a mixture of answers, timeouts, and no-answer results.

A significant observation was made for `humectaseis[.]com[.]tr`: the system-configured resolver returned a CNAME pointing to `restrictedspam.rpz.airtelspam.com` and address `125.21.240.67`, while Cloudflare DNS and Google DNS both returned `66.85.46.240` for the A query. The system resolver returned the same filtering-related CNAME and address for `s4w[.]in`. These observations strongly support DNS response filtering or rewriting somewhere along the system resolver path, although the exact component responsible has not been established.

No suspicious website was opened, and no HTTP requests were made to the sampled indicators.

## 2. Scope and Objectives

### Objectives

- Acquire and validate a threat-intelligence feed snapshot.
- Select and defang a small sample for investigation.
- Identify potentially suspicious URL structures.
- Collect domain registration metadata where available.
- Observe A, AAAA, and MX DNS responses.
- Compare resolver responses to identify possible DNS filtering.
- Preserve evidence, hashes, limitations, and reproducible outputs.
- Develop detection and response recommendations based on observed evidence.

### Out of Scope

- Visiting the sampled websites.
- Submitting indicators to third-party reputation portals.
- Confirming credential theft, malware delivery, or victim impact.
- Attributing infrastructure to a threat actor.
- Claiming that a feed-listed indicator is currently malicious without corroboration.

## 3. Data Sources and Methodology

| Source | Purpose | Limitation |
|---|---|---|
| OpenPhish community feed snapshot | Source of sampled URL indicators | Feed listing alone is not independent verification |
| Local URL triage script | Identify URL-structure features | Structural flags are investigative leads, not verdicts |
| RDAP services | Retrieve registration metadata | Availability and response behavior vary by registry and service |
| System-configured DNS resolver | Observe A, AAAA, and MX responses | Results may reflect filtering or rewriting |
| Cloudflare DNS and Google DNS | Compare the A response for one indicator | Public resolver answers are not a substitute for authoritative or historical DNS evidence |

## 4. Evidence Summary

| Evidence ID | Artifact | Observation |
|---|---|---|
| E-001 | `analysis/raw/openphish-feed.txt` | 300 non-empty feed entries; acquisition validation reported 300 valid unique URLs |
| E-002 | `analysis/working/url-investigation-sample.csv` | Ten defanged sample records |
| E-003 | `analysis/working/rdap-results.json` | Two HTTP 200 responses, five HTTP 404 responses, and three HTTP 400 responses |
| E-004 | `analysis/working/dns-results.json` | DNS responses, timeouts, and no-answer results for sampled domains |
| E-005 | `assets/evidence/dns/resolver-comparison.md` | Resolver comparison showing differing responses for one indicator |
| E-006 | `analysis/url-triage-results.json` | URL-structure results for four controlled test URLs |

See `Evidence-Register.md` for hashes and limitations.

## 5. Findings

### Finding F-01: Threat-intelligence feed indicators

**Observation:** Ten URLs were sampled from a retrieved OpenPhish community feed snapshot.

**Assessment:** The feed provides indicators for further investigation. This investigation does not independently establish the current malicious status of every sampled URL.

**Confidence:** High that the entries were present in the acquired snapshot; current maliciousness is not independently confirmed here.

### Finding F-02: RDAP registration metadata

**Observation:** RDAP returned HTTP 200 for `exoticafood[.]com[.]br` and `s4w[.]in`.

- `exoticafood[.]com[.]br`: registration event dated 2025-03-14; last changed 2025-04-09; expiration shown as 2027-03-14.
- `s4w[.]in`: registration event dated 2007-11-15; last changed 2026-02-20; expiration shown as 2026-11-15.

Five queries returned HTTP 404, and three returned HTTP 400.

**Assessment:** The two successful responses provide registration metadata. HTTP 404 and HTTP 400 results are inconclusive and do not establish non-registration. Registration age and status do not establish maliciousness.

**Confidence:** High for the metadata returned by the successful lookups at query time; unresolved for unsuccessful lookups.

### Finding F-03: DNS filtering or response rewriting

**Observation:** For `humectaseis[.]com[.]tr`, the system resolver returned:

- CNAME: `restrictedspam.rpz.airtelspam.com`
- A: `125.21.240.67`

Cloudflare DNS (`1.1.1.1`) and Google DNS (`8.8.8.8`) both returned A record `66.85.46.240`.

For `s4w[.]in`, the system resolver returned the same filtering-related CNAME and A address `125.21.240.67`. A public-resolver comparison for this domain has not yet been captured.

**Assessment:** The differing answers for `humectaseis[.]com[.]tr` strongly support DNS response filtering or rewriting somewhere along the system resolver path. The exact device, resolver, or policy responsible has not been identified.

The public resolver result does not prove that `66.85.46.240` is the authoritative or historical destination.

**Confidence:** High that the observed resolver responses differed at query time; moderate that filtering or rewriting explains the difference; exact attribution remains unknown.

### Finding F-04: DNS timeouts and missing answers

**Observation:** Several DNS queries timed out or returned no answer for one or more record types.

**Assessment:** These results are inconclusive. DNS timeouts and missing record types do not establish that a domain is inactive, unregistered, or benign.

**Confidence:** High that the recorded queries timed out or returned no answer; domain status remains unresolved.

## 6. Impact Assessment

No victim telemetry, endpoint logs, proxy logs, email gateway records, or authentication events were examined as part of this investigation. Therefore, no conclusion can be made about user exposure, credential submission, malware execution, data loss, or business impact.

If this work were performed in an operational SOC, the next step would be to search authorized enterprise telemetry for the indicators and their observed time ranges.

## 7. Recommended Response Actions

1. Preserve the original feed snapshot and associated hashes in restricted working storage.
2. Keep sampled URLs defanged in public-facing reports.
3. Validate indicators with additional independent reputation and passive-DNS sources before declaring current maliciousness.
4. Search authorized DNS, proxy, firewall, email, EDR, and authentication telemetry for matches.
5. Review the system resolver and network DNS policy to identify the source of the observed filtering response.
6. If enterprise logs show affected users or systems, follow the organization's approved incident response process.
7. Avoid blocking shared hosting IPs solely because a sampled URL resolves to that infrastructure.
8. Record false-positive checks, scope, time windows, and data-source limitations.

## 8. MITRE ATT&CK Considerations

No ATT&CK technique is confirmed by these metadata-only observations alone. Phishing-related techniques should only be mapped when supporting evidence demonstrates the relevant behavior, such as an observed phishing message or user interaction. See `MITRE-ATTACK-Mapping.md` for evidence-qualified mapping.

## 9. Limitations

- The investigation covers ten sampled URLs, not the full feed.
- Feed inclusion is not independent proof of current maliciousness.
- RDAP service responses varied by domain and registry.
- DNS data is time-sensitive and resolver-dependent.
- The exact source of DNS filtering was not established.
- No target websites were visited.
- No HTTP requests were sent to sampled indicators.
- No victim or enterprise telemetry was available.
- No threat actor attribution was attempted.

## 10. Conclusion

This investigation established a repeatable workflow for URL triage, registration metadata collection, DNS observation, resolver comparison, and evidence preservation. The most significant technical finding is the differing DNS response for `humectaseis[.]com[.]tr`, consistent with filtering or response rewriting on the system resolver path.

Further reputation validation and enterprise telemetry correlation are required before making definitive claims about the sampled indicators, exposure, or incident impact.

---

**Report status:** Initial investigation completed; additional enrichment and enterprise telemetry correlation pending.
