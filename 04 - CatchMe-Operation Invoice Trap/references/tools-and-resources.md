# Tools and References

## Tools used in this investigation

- **Email / MIME:** raw email header inspection and MIME attachment extraction
- **LNK analysis:** LnkParse3 (parse shortcut metadata; do not execute the shortcut)
- **Windows logs:** PowerShell Operational logs, including Event ID 4104 and related error events
- **Packet analysis:** Wireshark and TShark (DNS, HTTP, TCP streams, timestamps, request/response fields)
- **Data handling:** `sha256sum`, `file`, `unzip`, `jq`, Python for controlled parsing and timeline support

## Official and primary references

- MITRE ATT&CK: https://attack.mitre.org/
- Splunk Search Reference: https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/WhatsInThisManual
- Elastic Query Language (KQL): https://www.elastic.co/guide/en/kibana/current/kuery-query.html
- Elastic Security detection rules: https://www.elastic.co/guide/en/security/current/detection-engine-overview.html
- Microsoft PowerShell logging: https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_logging
- Wireshark User's Guide: https://www.wireshark.org/docs/wsug_html_chunked/
- TShark manual: https://www.wireshark.org/docs/man-pages/tshark.html

## Evidence and safety notes

- Keep original artefacts read-only and record hashes.
- Use an isolated lab for suspicious attachments; never run the LNK or payload on a production endpoint.
- The SIEM queries in this repository are starter examples and have not been validated against a connected SIEM.
- Avoid publishing raw email/PCAP data or sensitive identifiers without authorization.
