# Search 04 — Network Pivots

Observed network pivot: `process.name : "rundll32.exe"` on `WKSTN-0051.quicklogistics.org` with destination `165.232.170.151:80`.

```kql
process.name : "rundll32.exe" and destination.ip : "165.232.170.151" and destination.port : 80
```

Use a time range around 29 August 2023 23:51 UTC. Confirm connection outcome and corroborate the suspected C2 assessment with DNS, proxy, firewall, or packet evidence.
