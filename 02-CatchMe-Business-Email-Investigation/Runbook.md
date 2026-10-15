# CatchMe — Suspicious Email Investigation Runbook

## 1. Objective
Execute a consistent, evidence-led investigation of a suspected phishing or business email compromise message in an authorized lab or incident-response environment.

## 2. Preconditions
- Authorization to inspect the email and associated telemetry.
- A working directory with sufficient storage.
- Original evidence preserved separately from analysis copies.
- No execution of suspicious attachments.
- Access to relevant mail, identity, endpoint, DNS, or proxy logs when available.

## 3. Step 1 — Identify the Case

Record the case ID, analyst, time received, reporter, affected user, subject, and reason for investigation.

Example case identifier: `CATCHME-BEI-001`

Use UTC for newly recorded timestamps where possible. Preserve the original timezone and timestamp as shown in the evidence.

## 4. Step 2 — Locate and Inventory Evidence

From the project root:

```bash
pwd
find assets/evidence analysis public-evidence -type f -printf '%p (%s bytes)\n' 2>/dev/null | sort
```

Check file types:

```bash
file assets/evidence/email/challenge.eml
file assets/evidence/attachments/SWT_09674321_synthetic.CAB
```

If a path differs in another case, substitute the verified path. Do not assume that a filename establishes the file's contents.

## 5. Step 3 — Preserve and Hash Evidence

Calculate SHA-256 hashes:

```bash
sha256sum assets/evidence/email/challenge.eml
sha256sum assets/evidence/attachments/SWT_09674321_synthetic.CAB
sha256sum analysis/attachment-extracted/payment-receipt-lab.txt
```

Record each hash, evidence ID, path, acquisition method, timestamp, and handler in `Evidence-Register.md`.

A hash supports integrity comparison; it does not establish authenticity or prove that a file is malicious.

## 6. Step 4 — Inspect Email Headers and MIME Structure

Inspect headers without launching a mail client:

```bash
sed -n '1,100p' assets/evidence/email/challenge.eml
```

Parse the email with Python:

```bash
python3 - <<'PY'
from email import policy
from email.parser import BytesParser
from pathlib import Path

path = Path("assets/evidence/email/challenge.eml")
msg = BytesParser(policy=policy.default).parsebytes(path.read_bytes())

for header in ("From", "To", "Reply-To", "Date", "Subject",
               "Message-ID", "Return-Path"):
    print(f"{header}: {msg.get(header, '(not present)')}")

print("MIME multipart:", msg.is_multipart())
for i, part in enumerate(msg.walk(), start=1):
    print(
        f"Part {i}: type={part.get_content_type()}, "
        f"disposition={part.get_content_disposition()}, "
        f"filename={part.get_filename()}"
    )
PY
```

Compare sender, Reply-To, Message-ID, Date, and Received headers. Record chronology inconsistencies for further investigation. Do not treat a header field or SPF-related text inside a sample as an independently verified result.

## 7. Step 5 — Inspect the Attachment Safely

Identify the file and calculate its hash:

```bash
file assets/evidence/attachments/SWT_09674321_synthetic.CAB
sha256sum assets/evidence/attachments/SWT_09674321_synthetic.CAB
```

If `cabextract` is installed, list archive contents without extracting:

```bash
cabextract -l assets/evidence/attachments/SWT_09674321_synthetic.CAB
```

If unavailable, use an approved archive-inspection tool. Do not install tools or execute content on a production endpoint merely to complete this step.

For the known synthetic text artifact:

```bash
file analysis/attachment-extracted/payment-receipt-lab.txt
sha256sum analysis/attachment-extracted/payment-receipt-lab.txt
sed -n '1,120p' analysis/attachment-extracted/payment-receipt-lab.txt
```

Do not execute or open suspicious embedded programs. Record whether the artifact is synthetic, extracted, modified, or original.

## 8. Step 6 — Build the IOC Register

Record each indicator in `IOC-Register.csv` with its source, evidence ID, classification, confidence, disposition, and notes.

Potential indicator categories:
- Sender and Reply-To addresses
- Domains, URLs, and IP addresses
- Attachment names and hashes
- Message identifiers
- Claimed payment references
- Authentication anomalies

Separate observed values from claims made in the email. A claimed transaction reference is not automatically a malicious IOC. Do not block an indicator solely because it appears in a suspicious message.

## 9. Step 7 — Review Available Telemetry

Where authorized, search for:
- Other recipients of the same message or related messages
- Clicks, downloads, and attachment execution
- Authentication failures, unusual sign-ins, or suspicious sessions
- Mailbox forwarding rules, inbox rules, and delegated access changes
- Endpoint, DNS, proxy, and email gateway events
- Verified payment or account changes

Record the time range, query or console used, result, and limitations. If telemetry is unavailable, document it as unavailable—not as proof that no activity occurred.

## 10. Step 8 — Decide and Escalate

Determine the current status:
- **Benign / expected:** Evidence supports legitimate activity.
- **Suspicious / inconclusive:** Indicators warrant follow-up but are insufficient to confirm malicious activity.
- **Malicious confirmed:** Evidence supports phishing or malicious behavior.
- **Compromise confirmed:** Evidence establishes unauthorized access, execution, or other impact.

Escalate according to `Playbook.md`. Verify payment instructions through an independent trusted channel.

## 11. Step 9 — Respond and Recover

After authorization:
1. Preserve relevant logs and evidence.
2. Quarantine messages or block confirmed indicators.
3. Contain affected identities or endpoints when justified.
4. Coordinate with Finance if fraud is suspected.
5. Remediate and restore affected systems.
6. Verify recovery and monitor for recurrence.

Record each action, approval, timestamp, operator, and outcome.

## 12. Step 10 — Document and Close

Update:
- `Incident-Response-Report.md`
- `Evidence-Register.md`
- `Investigation-Timeline.md`
- `IOC-Register.csv`
- `MITRE-ATTACK-Mapping.md`
- `lessons-learned.md`

Confirm that the report distinguishes facts, hypotheses, and unverified claims. Record the final disposition, remaining gaps, and closure approval.

## 13. CatchMe Lab Notes
This project contains a modified, payload-redacted email, an older working copy, and a harmless synthetic CAB attachment. The email versions differ, and the sample's headers and financial claims are not proof of a real transaction. The lab alone does not confirm compromise or financial loss.

## 14. Publication Check
Before manual GitHub upload:
- Review all files for personal, financial, and authentication data.
- Keep private originals out of public folders.
- Inspect screenshots at full size.
- Ensure documentation identifies modified and synthetic artifacts accurately.
- Do not publish secrets, credentials, session tokens, or unredacted sensitive evidence.
