# Tools and Resources

## Tools used in this investigation

| Tool | Purpose |
|---|---|
| `sha256sum` | Calculate SHA-256 hashes for evidence integrity checks |
| `file` | Identify artifact file types |
| `pdfinfo` | Inspect PDF properties and metadata |
| `exiftool` | Review document metadata |
| `pdfdetach` | Check for embedded PDF attachments |
| `pdftotext` | Extract searchable PDF text |
| `pdfid` | Inspect PDF structural indicators |
| Python 3 | Generate evidence inventories and reports |

## Official documentation

- Elastic Security: https://www.elastic.co/guide/en/security/current/index.html
- Elastic KQL: https://www.elastic.co/guide/en/kibana/current/kuery-query.html
- Sigma: https://sigmahq.io/docs/
- MITRE ATT&CK: https://attack.mitre.org/
- ExifTool: https://exiftool.org/
- Poppler: https://poppler.freedesktop.org/
- Python email package: https://docs.python.org/3/library/email.html

## Evidence-handling notes

- Keep original evidence unchanged and record hashes.
- Distinguish extracted indicators from reputation-verified indicators.
- SPF, DKIM, and DMARC results do not independently prove that email content is trustworthy.
- Do not visit suspicious URLs simply to discover their destinations.
- Record tool versions and timestamps when needed for reproducibility.
