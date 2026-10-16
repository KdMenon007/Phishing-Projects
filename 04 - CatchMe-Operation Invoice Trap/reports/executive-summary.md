# Executive Summary

## Incident overview

An invoice-themed email addressed to finance employee Julianne Westcott contained `Invoice.zip`, which held a Windows shortcut. Shortcut metadata and PowerShell event logs show a hidden, encoded PowerShell command retrieving remote content and executing it. Packet capture corroborates the initial HTTP GET and shows recurring communications with `cdn.bpakcaging.xyz:8080`.

## Key findings

- Suspicious invoice lure with password-protected ZIP attachment.
- LNK target and arguments invoke hidden, encoded PowerShell and retrieve `http://files.bpakcaging.xyz/update`.
- PowerShell logs describe recurring command polling and execution of returned content.
- PCAP shows repeated HTTP GET/POST activity to `159.89.205.40:8080`; a POST body includes process-listing output.
- 88 unique long hexadecimal-label DNS queries under `bpakcaging.xyz` had matching responses with zero answer records.
- Endpoint logs contain Seatbelt-related host-enumeration commands.

## Overall assessment

High confidence of suspicious PowerShell execution and command-and-control-like behavior, with attempted host reconnaissance. Successful credential theft, successful data exfiltration, DNS tunnelling, persistence, and full business impact are not established by the reviewed evidence.

## Priority actions

Preserve evidence; isolate the endpoint if this were an active enterprise incident; hunt across endpoint, DNS, proxy, and firewall telemetry for the observed indicators and behaviors; validate the scope of activity; and remediate based on confirmed findings.
