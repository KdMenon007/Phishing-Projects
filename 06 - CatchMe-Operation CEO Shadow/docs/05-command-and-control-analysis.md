# 05 — Command-and-Control Analysis

**Status: endpoint observed; C2 attribution remains an assessment.**

Elastic network telemetry on `WKSTN-0051.quicklogistics.org` shows repeated `rundll32.exe` PID 4672 connections to **`165.232.170.151:80`** beginning around `2023-08-29 23:51:17.910`. This is temporally associated with the suspected `review.dat` execution chain.

## Validation
- Correlate with DNS, proxy, firewall, and packet data where available.
- Confirm connection outcome and any HTTP request path/host header.
- Do not label the endpoint confirmed C2 based only on process/network correlation.
