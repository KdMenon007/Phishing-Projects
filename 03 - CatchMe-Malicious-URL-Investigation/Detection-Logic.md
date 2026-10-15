# Detection Logic
## CatchMe — Malicious URL & Phishing Infrastructure Investigation

**Status:** Proposed detections; validation against enterprise telemetry pending  
**Purpose:** Identify suspicious URL indicators and investigate DNS filtering behavior.

---

## Detection 1 — Threat-Intelligence URL Match

**Objective:** Identify URLs or hostnames matching an approved, maintained threat-intelligence list.

**Required data:** Proxy, secure web gateway, DNS, email security, or EDR telemetry containing a URL or hostname.

**Logic:**
1. Normalize the observed URL or hostname.
2. Compare it against an approved indicator list.
3. Record the matching indicator, source feed, observation time, and event source.
4. Enrich and validate the match before assigning a malicious verdict.

**Pseudo-query:**
```text
FOR each observed network_or_email_event:
    indicator = normalize(event.url_or_hostname)
    IF indicator matches approved_threat_intelligence:
        alert(
            event_time,
            device_or_user,
            indicator,
            intelligence_source,
            event_source
        )
```

**Severity:** Medium by default; increase only when corroborating evidence supports higher risk.

**False-positive considerations:**
- Stale or expired indicators.
- Shared hosting and multi-tenant platforms.
- URL normalization differences.
- Feed entries that are no longer active or are not independently verified.

**Validation:** Not tested against enterprise telemetry. Validate using synthetic events or an authorized test dataset.

---

## Detection 2 — Suspicious URL Structure

**Objective:** Flag URL characteristics that warrant analyst review.

**Potential signals:**
- Credentials or user information embedded before `@` in the authority component.
- IP-literal hostnames in contexts where they are unusual.
- Percent-encoded or traversal-like path sequences.
- Unexpected redirect parameters.
- Authentication-related keywords combined with other suspicious indicators.
- Non-HTTPS schemes where policy requires HTTPS.

**Logic:**
- Parse the URL according to its components.
- Evaluate multiple signals rather than relying on a single keyword.
- Assign a review score and preserve the original value safely.
- Defang URLs in analyst notes and public artifacts.

**Pseudo-query:**
```text
score = 0

IF authority_contains_userinfo:
    score += 2
IF hostname_is_ip_literal:
    score += 2
IF path_contains_encoded_traversal:
    score += 2
IF unexpected_redirect_parameter:
    score += 1
IF authentication_keyword_and_other_signal:
    score += 1
IF scheme_is_http:
    score += 1

IF score >= configured_threshold:
    create_review_alert()
```

**Severity:** Informational or low until corroborated. Increase based on context and additional evidence.

**False-positive considerations:**
- Legitimate redirect services.
- Development and internal test systems.
- URL encoding used by legitimate applications.
- IP-based services and legacy applications.

**Validation:** The local URL triage script was run against four controlled examples. Those examples validate script behavior only; they do not validate this proposed enterprise detection.

---

## Detection 3 — DNS Response-Policy or Sinkhole Indicator

**Objective:** Identify DNS responses that may indicate filtering or policy-based redirection.

**Required data:** DNS query logs containing the requested name, response code, answer records, resolver identity, and timestamp.

**Potential signals:**
- A response contains a known filtering or sinkhole CNAME.
- Multiple unrelated queried domains resolve to the same documented policy destination.
- The response differs between approved resolver paths.
- A policy response is recorded in resolver logs.

**Logic:**
1. Detect known policy destinations from a locally approved reference list.
2. Correlate the destination with the original query and resolver.
3. Preserve the original DNS response.
4. Verify the policy destination with the DNS or network administrator.
5. Do not classify the requested domain solely from the filtering response.

**Pseudo-query:**
```text
FOR each dns_event:
    IF answer_cname matches approved_policy_destination:
        create_dns_policy_observation(
            query_name,
            resolver,
            answer,
            timestamp
        )
        investigate_policy_source()
```

**Observed investigative lead:** The system resolver returned `restrictedspam.rpz.airtelspam.com` for two sampled domains. Resolver comparison for one domain produced a different A response through Cloudflare and Google DNS.

**Important:** This is a proposed detection pattern, not a validated production rule. The responsible filtering component remains unidentified.

---

## Alert Enrichment

For each alert, collect where available:

- Event timestamp and timezone.
- User and device identifiers.
- URL or queried hostname, safely defanged in reports.
- DNS resolver or network control that generated the event.
- Threat-intelligence source and retrieval time.
- Related proxy, email, EDR, firewall, and authentication events.
- Analyst disposition and evidence references.

## Validation Plan

1. Generate synthetic test events in an isolated lab.
2. Confirm each rule detects its intended condition.
3. Test benign redirects, encoded URLs, and shared-hosting cases.
4. Record true-positive, false-positive, and missed-test outcomes.
5. Tune thresholds and document the data fields required.
6. Promote rules only after review and approval.

## Limitations

- No enterprise DNS, proxy, email, or EDR telemetry was examined.
- No production SIEM query has been validated.
- Thresholds are illustrative and require tuning.
- Threat-intelligence matches require freshness and context checks.
- DNS policy observations do not independently establish maliciousness.
