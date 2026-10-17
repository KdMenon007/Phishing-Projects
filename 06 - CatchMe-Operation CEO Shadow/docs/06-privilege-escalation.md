# 06 — Privilege Escalation

## Observed evidence
Screenshot `09-elastic-fodhelper-rundll32-review-dat-uac-bypass.png` shows `fodhelper.exe` process events on `WKSTN-0051.quicklogistics.org`:

- PID `5308` at `2023-08-29 23:54:49.043`
- PID `5180` at `2023-08-29 23:54:49.213`
- Parent process: `rundll32.exe`
- Parent command line: `"C:\Windows\System32\rundll32.exe" D:\review.dat,DllRegisterServer`

## Assessment
`fodhelper.exe` is the observed process associated with the suspected UAC-bypass sequence. The process relationship is consistent with an attempt to abuse auto-elevated Windows functionality, but this screenshot alone does not prove that the bypass succeeded or that the resulting process ran elevated. Validate process tokens/integrity level and expanded event details if available.

## Current room answer
Q6: `fodhelper.exe` (observed process; successful bypass unconfirmed).
