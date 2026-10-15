# SOC Investigation Runbook
## CatchMe — Malicious URL & Phishing Infrastructure Investigation

**Audience:** SOC Analyst L2  
**Purpose:** Execute repeatable URL, RDAP, DNS, and evidence-integrity checks.  
**Safety:** Do not browse to suspicious indicators or send HTTP requests to target sites.

---

## Step 1 — Verify Project Artifacts

```bash
cd ~/Projects/CatchMe-Malicious-URL-Investigation

find analysis assets -maxdepth 4 -type f -print | sort
```

Confirm that the expected feed, sample dataset, RDAP results, DNS results, and resolver-comparison note exist.

## Step 2 — Validate the Feed Snapshot

```bash
wc -l analysis/raw/openphish-feed.txt
sha256sum analysis/raw/openphish-feed.txt
```

Compare the result with the recorded evidence hash. A changed hash means the file differs from the recorded version and requires investigation.

## Step 3 — Review URL Triage Results

```bash
python3 -m json.tool analysis/url-triage-results.json | less
```

Review the flags and parsed URL components. A flag is a reason to investigate, not proof of maliciousness.

## Step 4 — Review RDAP Results

```bash
python3 -m json.tool analysis/working/rdap-results.json | less
```

Record successful registration events. Treat HTTP 400, HTTP 404, timeouts, and service errors as unresolved unless corroborated through an appropriate registry source.

## Step 5 — Review DNS Results

```bash
python3 -m json.tool analysis/working/dns-results.json | less
```

Review A, AAAA, and MX answers, timestamps, and errors. Do not interpret a missing answer or timeout as proof that a domain is inactive.

## Step 6 — Repeat a DNS Query When Authorized

Use only approved resolvers and follow organizational policy.

```bash
dig +time=3 +tries=1 +noall +comments +answer example.com A
```

Replace `example.com` with an authorized investigation target. Record the query time, resolver, response code, and answer. DNS lookups disclose the queried name to the resolver.

For a resolver comparison, record each resolver used and keep the results separate. Different answers may reflect filtering, caching, geographic differences, or changes over time.

## Step 7 — Verify Evidence Integrity

```bash
sha256sum \
  analysis/raw/openphish-feed.txt \
  analysis/working/url-investigation-sample.csv \
  analysis/working/rdap-results.json \
  analysis/working/dns-results.json \
  assets/evidence/dns/resolver-comparison.md
```

Compare the hashes with `Evidence-Register.md`. If an artifact has been updated, record the new hash and update the register.

## Step 8 — Update the Investigation Timeline

For each action, record:

- Timestamp in UTC.
- Analyst action.
- Tool or data source.
- Observation or result.
- Evidence reference.
- Limitations and next action.

Do not backdate entries. Distinguish the time an event occurred from the time it was collected.

## Step 9 — Decide Whether to Escalate

Escalate according to organizational policy when evidence indicates user exposure, credential submission, payload execution, account compromise, or other material impact.

Do not declare a confirmed incident based only on feed inclusion, domain age, shared hosting, or a DNS filtering response.

## Step 10 — Final Case Review

Before closing the investigation, verify:

- [ ] Evidence files exist and hashes are recorded.
- [ ] Feed-listed indicators are distinguished from independently verified findings.
- [ ] RDAP failures and DNS timeouts remain unresolved where appropriate.
- [ ] Resolver differences and their limitations are documented.
- [ ] Detection rules are labelled proposed until validated.
- [ ] MITRE ATT&CK techniques are not marked confirmed without supporting evidence.
- [ ] The report states that victim impact was not assessed.
- [ ] Follow-up actions and evidence gaps are documented.

---

## Troubleshooting

| Issue | Action |
|---|---|
| RDAP returns HTTP 400 | Verify the queried domain format and use the appropriate registry service |
| RDAP returns HTTP 404 | Treat as inconclusive until verified through an appropriate registry source |
| DNS query times out | Record the timeout; check resolver availability and retry only when justified |
| DNS answers differ | Compare resolver identity, timestamps, policy, and caching; do not assume either answer is authoritative |
| Hash differs | Preserve the changed artifact, determine why it changed, and update the evidence record after review |

**Related documents:** `Playbook.md`, `Detection-Logic.md`, `Evidence-Register.md`, `Incident-Response-Report.md`
