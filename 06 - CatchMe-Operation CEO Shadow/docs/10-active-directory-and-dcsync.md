# 10 — Active Directory and DCSync

**Status: DCSync command observed; outcome requires domain-controller corroboration.**

A Mimikatz process command contains `lsadump::dcsync /domain:quicklogistics.org /user:backupda`. The account besides Administrator targeted by the command is **`backupda`**. Review domain-controller Security audit events and replication-rights telemetry to confirm whether directory secrets were successfully replicated.
