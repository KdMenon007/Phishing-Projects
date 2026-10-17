# 07 — Credential Access

**Status: Mimikatz download and pass-the-hash process activity observed.**

A PowerShell command downloads `mimikatz_trunk.zip` from `https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip` to `mimi.zip`. On `WKSTN-1327`, Mimikatz process telemetry shows `sekurlsa::pth` targeting `itadmin`; later telemetry shows a pass-the-hash command targeting `administrator`.

Full hashes are redacted from this public release. Correlate the process events with authentication and logon telemetry before asserting successful authentication. Treat passwords, hashes, and tokens as sensitive.
