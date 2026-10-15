# Investigation Timeline

**Case ID:** CATCHME-URL-2026-001  
**Investigation date:** 2026-10-15  
**Timezone:** UTC unless otherwise stated

> This timeline records the investigation workflow and available timestamps. Exact execution times are included only where they were captured in the evidence. Do not infer event times from file order.

| Step | Timestamp (UTC) | Activity | Observation / Result | Evidence |
|---|---|---|---|---|
| T-001 | 2026-10-15T11:10:06Z | Acquired OpenPhish community feed snapshot | 300 non-empty lines; 300 valid unique URLs; 0 invalid lines reported | `analysis/raw/openphish-feed.txt` |
| T-002 | Not recorded | Ran URL triage against four controlled test URLs | URL-structure flags generated; examples were controlled tests, not confirmed malicious indicators | `analysis/url-triage-results.json` |
| T-003 | Not recorded | Built a ten-record defanged sample | Ten sample URLs; defanged CSV validation reported consistent columns | `analysis/working/url-investigation-sample.csv` |
| T-004 | Not recorded | Extracted unique domains from the sample | Ten sample records and ten unique domains | `analysis/working/domain-investigation.csv` |
| T-005 | 2026-10-15T11:12:07.357Z | RDAP lookup for `s4w[.]in` | HTTP 200; registration event dated 2007-11-15; record returned by `.in` RDAP service | `analysis/working/rdap-results.json` |
| T-006 | Not recorded | Ran RDAP enrichment for ten domains | 2 HTTP 200, 5 HTTP 404, 3 HTTP 400 | `analysis/working/rdap-results.json` |
| T-007 | Not recorded | Queried A, AAAA, and MX records | Mixed DNS answers, timeouts, and no-answer results | `analysis/working/dns-results.json` |
| T-008 | Not recorded | Compared DNS resolver responses for `humectaseis[.]com[.]tr` | System resolver returned a filtering-related CNAME; Cloudflare and Google returned A `66.85.46.240` | `assets/evidence/dns/resolver-comparison.md` |
| T-009 | 2026-10-15 | Created evidence register | Six evidence items documented with hashes and limitations | `Evidence-Register.md` |
| T-010 | 2026-10-15 | Drafted incident report, detection logic, ATT&CK mapping, playbook, and runbook | Documentation created; enterprise detection validation remains pending | Project Markdown files |
| T-011 | 2026-10-15 | Ran project syntax and completeness checks | Python syntax passed; four required documents were initially empty | Terminal validation output |

## Timeline Limitations

- Several command execution timestamps were not captured.
- The RDAP event timestamp is a registry-provided event time, not the time the analyst executed the query.
- Feed retrieval time and domain registration dates must not be confused with incident activity times.
- No enterprise telemetry was available to establish user exposure or victim impact.
