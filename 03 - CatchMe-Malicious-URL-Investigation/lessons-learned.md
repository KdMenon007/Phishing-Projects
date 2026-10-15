# Lessons Learned

## 1. Separate Intelligence Leads from Confirmed Findings

A feed listing is useful for prioritizing investigation, but it does not independently establish that a domain is currently malicious. Corroboration and context are required before making a definitive verdict.

## 2. DNS Results Depend on the Resolver Path

The system resolver returned a filtering-related CNAME for two sampled domains. Comparing one of those results with Cloudflare and Google DNS revealed a different A response. This demonstrates why resolver identity and policy context should be recorded during investigations.

The exact component responsible for the filtering behavior remains unidentified.

## 3. Failed Lookups Are Not Negative Proof

RDAP HTTP 400 and 404 responses, DNS timeouts, and missing record types must remain inconclusive unless additional evidence supports a stronger conclusion.

## 4. Hosting Infrastructure Requires Context

Cloudflare, EdgeOne, and other shared hosting services may serve many unrelated customers. An IP address or provider association should not be treated as malicious solely because it appears in an investigation.

## 5. Preserve Reproducibility

Saving raw observations, UTC timestamps, scripts, evidence references, and SHA-256 hashes makes the investigation easier to reproduce and review. Hashes must be recalculated when artifacts change.

## 6. Keep Public Artifacts Safe

Raw threat-intelligence feeds should remain in restricted working storage. Public reports should use defanged indicators and exclude unnecessary raw data.

## 7. Detection Logic Needs Validation

Proposed detection patterns are not production-ready until tested against representative data. Future work should include synthetic positive and negative events, false-positive analysis, threshold tuning, and documented test outcomes.

## 8. Improve Future Enrichment

Next steps include:
- Capture exact command execution timestamps automatically.
- Compare additional indicators through approved DNS sources.
- Validate registration results with appropriate registry endpoints.
- Use independent reputation sources only after considering their data-sharing policies.
- Search authorized enterprise DNS, proxy, email, EDR, and authentication logs when available.
- Record the exact query, time range, data source, and result for every enterprise search.

## Conclusion

The strongest result in this investigation was the observed difference between the system resolver and public DNS resolver responses for one indicator. The project demonstrates a repeatable evidence-handling workflow while explicitly documenting what remains unknown.
