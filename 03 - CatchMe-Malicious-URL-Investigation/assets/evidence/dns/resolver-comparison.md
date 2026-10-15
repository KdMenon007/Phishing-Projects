# DNS Resolver Comparison

- Investigation: CatchMe — Malicious URL & Phishing Infrastructure Investigation
- Observation date: 2026-10-15
- Method: `dig` A-record queries; no browser or HTTP connection to the indicators.

## Indicator: humectaseis[.]com[.]tr

| Resolver | Observed response |
|---|---|
| System resolver (192.168.1.1) | CNAME `restrictedspam.rpz.airtelspam.com`; A `125.21.240.67` |
| Cloudflare DNS (1.1.1.1) | A `66.85.46.240` |
| Google DNS (8.8.8.8) | A `66.85.46.240` |

## Indicator: s4w[.]in

| Resolver | Observed response |
|---|---|
| System resolver (192.168.1.1) | CNAME `restrictedspam.rpz.airtelspam.com`; A `125.21.240.67` |
| Public resolver comparison | Not performed in this evidence capture |

## Analyst Assessment

The differing response for `humectaseis[.]com[.]tr` strongly supports DNS response rewriting or filtering somewhere along the system resolver path. The exact component responsible has not been established.

The public resolver responses agree with each other for the queried A record. This alone does not establish authoritative DNS, historical resolution, or domain maliciousness.

For `s4w[.]in`, the system resolver returned the same filtering-related CNAME and address, but a public resolver comparison remains outstanding.

## Limitations

- DNS observations are time-sensitive.
- No target website was opened.
- No HTTP request was made to either indicator.
- DNS answers alone do not prove maliciousness.
