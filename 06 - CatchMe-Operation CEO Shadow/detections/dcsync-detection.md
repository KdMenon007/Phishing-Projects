# Detection: DCSync Activity

## Evidence observed
A Mimikatz process command used `lsadump::dcsync /domain:quicklogistics.org /user:backupda`. The visible command supports a DCSync attempt targeting `backupda`; verify domain-controller audit records to confirm the operation and outcome.

## Hunting pivots
```kql
process.name : "mimikatz.exe" and process.command_line : "*lsadump::dcsync*"
```
Review domain-controller Security logs for directory replication access rights and correlate the requesting account, source host, time, and replication privileges.

## Response
Investigate privileged replication rights, contain the originating host, and rotate affected credentials according to incident-response procedures.
