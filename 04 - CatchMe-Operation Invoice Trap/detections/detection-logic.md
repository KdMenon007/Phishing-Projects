# Detection Logic

## Analytic 1 — Suspicious PowerShell remote execution

- **Objective:** Identify PowerShell script content that retrieves remote content and dynamically executes it.
- **Evidence:** PowerShell Event 4104 contains a `DownloadString()` and `iex` pattern; the LNK contains hidden encoded PowerShell.
- **Required telemetry:** PowerShell Operational Event 4104; process creation (Sysmon Event 1 or Security Event 4688); host/user/timestamp.
- **Detection logic:** Match remote retrieval (`DownloadString`, `WebClient`, or related APIs) with dynamic execution (`Invoke-Expression`/`iex`); raise priority when paired with encoded or hidden command-line flags.
- **False positives:** Admin scripts, software deployment, automation frameworks, and approved testing.
- **Status:** Evidence-backed analytic hypothesis; SIEM query not executed in a connected environment.

## Analytic 2 — Repeated HTTP POST to rare destination

- **Objective:** Find recurring HTTP sessions from a host after suspicious PowerShell activity.
- **Evidence:** Repeated requests to `cdn.bpakcaging.xyz:8080`, URI `/27fe2489`; one observed POST declared 78,618 bytes and received HTTP 200.
- **Required telemetry:** HTTP/Zeek/proxy logs, source/destination, port, host, URI, method, status, request/response byte counts, timestamp.
- **Detection logic:** Threshold repeated POSTs to a rare host/URI or unusual port; correlate with PowerShell on the same host.
- **False positives:** Internal APIs, agents, backup clients, and approved applications using nonstandard ports.
- **Status:** Network behavior observed in PCAP; SIEM analytic not validated.

## Analytic 3 — Long-label DNS anomaly

- **Objective:** Surface hosts generating many unique long DNS labels under one parent domain.
- **Evidence:** 88 unique long hexadecimal-label queries under `bpakcaging.xyz`; matching responses had zero answer records. Partial decoded HTTP POST output contains errors for some matching names.
- **Required telemetry:** DNS query name/type, source host/IP, response code, answer count, timestamp.
- **Detection logic:** Use a per-host/domain time-window threshold for unique long labels; increase priority when correlated with suspicious PowerShell and HTTP activity.
- **False positives:** Cloud agents, endpoint-management tooling, service discovery, security products, and malformed application queries.
- **Status:** Suspicious anomaly observed; DNS tunnelling not confirmed.

## Analytic 4 — Process discovery / host enumeration

- **Objective:** Detect unexpected process enumeration following suspicious script execution.
- **Evidence:** A partially decoded HTTP POST body contains Windows process-listing output; PowerShell logs include Seatbelt-related commands.
- **Required telemetry:** Process creation, PowerShell logs, file/hash/signature telemetry, and outbound network events.
- **Detection logic:** Alert on unexpected Seatbelt execution or command-line process enumeration when correlated with suspicious PowerShell and rare outbound HTTP.
- **False positives:** Approved red-team exercises, incident response, IT administration, EDR, and inventory agents.
- **Status:** Reconnaissance behavior supported; tool-command success and complete output should be validated from endpoint telemetry.

## Case-level confidence

- **High:** suspicious hidden/encoded PowerShell pattern and recurring HTTP communications in the lab evidence.
- **High:** a POST body contains process-listing output (the decoded stream 150 evidence).
- **High:** repeated long-label DNS queries and zero-answer responses occurred.
- **Not established:** successful data exfiltration, credential theft, DNS tunnelling, or exact remote payload behavior.
