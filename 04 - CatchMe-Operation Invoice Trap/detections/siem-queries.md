# SIEM Queries — Splunk SPL and Elastic KQL

**Status:** Starter analytics. These queries were authored from the case evidence but have **not** been executed against a connected SIEM. Confirm index names, sourcetypes, ECS/CIM field mappings, timestamp handling, and data availability before use.

> Use the case indicators for lab hunting only. In production, maintain indicators as governed threat-intelligence data and tune detections against local baselines.

## 1. PowerShell script-block logging: remote retrieval and execution

### Splunk SPL — Windows PowerShell Operational / Event 4104

```spl
index=windows (EventCode=4104 OR EventID=4104)
| eval script_text=coalesce(ScriptBlockText, Message, MessageRendered)
| where match(lower(script_text), "downloadstring|invoke-expression|\\biex\\b")
    AND match(lower(script_text), "http|webclient|download")
| table _time host user EventCode ScriptBlockId script_text
| sort 0 _time
```

**Look for:** remote content retrieval combined with dynamic execution. Check whether script text is complete across multiple 4104 records.

### Elastic KQL — PowerShell script-block events

```kql
event.code: "4104" and
(
  powershell.file.script_block_text: *DownloadString* or
  powershell.file.script_block_text: *Invoke-Expression* or
  powershell.file.script_block_text: *iex*
)
```

**Field note:** `powershell.file.script_block_text` is an ECS-style example; actual integrations may expose script text under a different field. Validate field availability in Discover first.

## 2. Encoded or hidden PowerShell process creation

### Splunk SPL — Sysmon Event 1 or Security Event 4688

```spl
index=windows (EventCode=1 OR EventCode=4688)
| eval cmd=lower(coalesce(CommandLine, Process_Command_Line, process_command_line, Message))
| where match(cmd, "powershell|pwsh")
    AND (
      match(cmd, "-enc(odedcommand)?\\b")
      OR match(cmd, "-windowstyle\\s+hidden|-w\\s+hidden")
      OR match(cmd, "downloadstring|frombase64string|invoke-expression")
    )
| table _time host user ParentImage ParentCommandLine Image CommandLine cmd
| sort 0 _time
```

**Look for:** encoded commands, hidden window options, remote retrieval, and unusual parent processes. Normalize event fields for the source data.

### Elastic KQL — process creation

```kql
event.category: process and
process.name: (powershell.exe or pwsh.exe) and
process.command_line: (
  *-enc* or *-encodedcommand* or *-windowstyle* or
  *DownloadString* or *FromBase64String* or *Invoke-Expression*
)
```

KQL wildcard matching is case-insensitive in typical Elasticsearch keyword/wildcard fields, but verify the mapped field and syntax for your deployment. Treat this as a broad hunting query, not a final alert rule.

## 3. Suspicious HTTP communications

### Splunk SPL — Zeek HTTP example

```spl
index=network sourcetype=zeek:http
| eval uri=coalesce(uri, url, http_uri)
| eval host_header=coalesce(host, host_header, http_host)
| where dest_port=8080 OR host_header="cdn.bpakcaging.xyz"
    OR uri="/27fe2489"
| stats count values(method) as methods values(status_code) as statuses
        sum(request_body_len) as request_bytes sum(response_body_len) as response_bytes
        min(_time) as first_seen max(_time) as last_seen
  by src_ip dest_ip dest_port host_header uri
| convert ctime(first_seen) ctime(last_seen)
```

**Data-model note:** Zeek field names vary by add-on and pipeline. Map `src_ip`, `dest_ip`, `dest_port`, `method`, `status_code`, and body-length fields before running.

### Elastic KQL — HTTP/network events

```kql
(destination.port: 8080 or
 url.domain: "cdn.bpakcaging.xyz" or
 url.path: "/27fe2489")
```

Use this as a scoped hunt when the corresponding network integration populates `destination.port`, `url.domain`, and `url.path`. KQL itself does not perform time-window aggregation; use a threshold rule or EQL/ES|QL workflow for repeated requests.

## 4. Long-label DNS anomaly

### Splunk SPL — DNS logs

```spl
index=network (sourcetype=zeek:dns OR sourcetype=*dns*)
| eval qname=lower(coalesce(query, query_name, dns_query, queryName))
| eval src=coalesce(src_ip, source_ip, src)
| where isnotnull(qname)
| eval labels=split(qname, ".")
| eval first_label=mvindex(labels, 0)
| eval parent_domain=mvjoin(mvindex(labels, 1, 99), ".")
| eval first_label_len=len(first_label)
| where first_label_len >= 25
| stats count dc(qname) as unique_queries values(query_type) as query_types
        values(rcode_name) as response_codes
  by src parent_domain
| where unique_queries >= 10
```

**Important:** Adapt the domain grouping and response fields to your DNS data model. A long label or zero-answer response alone is not proof of DNS tunnelling.

### Elastic KQL — candidate DNS events

```kql
event.category: network and dns.question.name: *
```

KQL is not suitable for reliably expressing the required label-length and cardinality threshold by itself. Use a threshold rule, ES|QL, or an aggregation over DNS events to calculate unique long labels per host/domain and time window. Validate against endpoint-management, cloud-agent, CDN, and other benign DNS patterns.

## 5. Process discovery / Seatbelt-related activity

### Splunk SPL — process events

```spl
index=windows (EventCode=1 OR EventCode=4688)
| eval cmd=lower(coalesce(CommandLine, Process_Command_Line, Message))
| where match(cmd, "seatbelt|tasklist|processname|win32_process")
| table _time host user ParentImage Image CommandLine
| sort 0 _time
```

A name match is a hunting lead, not proof of maliciousness. Check file path, signer/hash where available, parent process, user context, and whether the tool was authorized.

### Elastic KQL

```kql
event.category: process and
process.command_line: (*Seatbelt* or *tasklist* or *Win32_Process*)
```

## 6. Correlation analytic

Raise severity when multiple signals occur on the same host within a tuned time window:

- PowerShell 4104 shows remote retrieval and dynamic execution.
- Process creation contains encoded/hidden PowerShell.
- Repeated HTTP POSTs go to a rare destination/URI.
- A host generates many unique long DNS labels under the same parent domain.
- Process enumeration or Seatbelt-related commands follow the suspicious execution.

**Recommended initial investigation window:** 30 minutes, then tune to the actual event sequence. Do not use a single shared indicator as the only correlation key.

## Validation checklist

- [ ] Confirm Windows PowerShell Operational logs and process-creation logs are collected.
- [ ] Confirm network/DNS telemetry fields and timestamp timezone.
- [ ] Run queries over the lab incident window and compare results with source evidence.
- [ ] Test against benign PowerShell administration and routine DNS/HTTP traffic.
- [ ] Record true positives, false positives, missing fields, and query version.
- [ ] Do not mark a detection as validated until it has been run against data and results reviewed.
