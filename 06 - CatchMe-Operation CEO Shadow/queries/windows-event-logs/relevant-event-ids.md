# Windows Event Log Reference

Investigative pivots if the relevant logs are collected:
- **4688** — process creation
- **4697** — service installed
- **4698 / 4702** — scheduled task created / updated
- **4624 / 4625** — successful / failed logon
- **5140 / 5145** — share access / detailed share access
- **4662** — directory service access; interpret with audit configuration and event details
- **Sysmon 1** — process creation, if configured
- **Sysmon 3** — network connection, if configured

Availability depends on audit policy and ingestion. These IDs are not asserted to be present in the screenshots.
