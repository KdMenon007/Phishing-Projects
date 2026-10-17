# 11 — Ransomware Investigation

**Status: download attempt observed; execution and encryption are not established.**

A PowerShell `Invoke-Command -ComputerName WKSTN-0051.quicklogistics.org` command attempts to retrieve `http://ff.sillytechninja.io/ransomboogey.exe` and save it to `C:\Users\evan.hutchinson\ransomboogey.exe`. Related screenshots show searches and process/event details for `ransomboogey.exe`, including a later event on a path associated with `itadmin`; interpret this as follow-up evidence, not by itself proof of encryption.

Validate successful file creation, process start, file-system changes, ransom notes, and recovery artifacts. Do not retrieve or execute the binary.
