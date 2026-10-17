# Evidence Screenshots — Operation CEO Shadow

This folder contains the 23 screenshots supplied for this investigation, renamed for navigation. Screenshots reflect Elastic Discover and Windows Explorer views at capture time; several Discover time pickers extend beyond the 2023 incident window. Use the visible event timestamps and validate against exported event JSON before making final claims.

1. `01-phishing-email.png` — financial-themed email.
2. `02-attachment-in-downloads.png` — attachment in Downloads.
3. `03-mounted-iso-payload.png` — mounted image contents.
4. `04-elastic-projectfinancial-search.png` — attachment/payload search.
5. `05-elastic-mshta-payload-search.png` — process event associated with the HTA.
6. `06-elastic-xcopy-file-implant-command-line.png` — `xcopy.exe` file-copy command.
7. `07-elastic-review-dat-search.png` — `review.dat` search results.
8. `08-fodhelper-uac-bypass-reference.png` — reference on `fodhelper.exe` UAC bypass.
9. `09-elastic-fodhelper-process-events.png` — `fodhelper.exe` events with `rundll32.exe` parent context.
10. `10-elastic-rundll32-c2-connections.png` — repeated network events to `165.232.170.151:80`.
11. `11-elastic-remote-share-it-automation.png` — remote-share access to `IT_Automation.ps1`.
12. `12-elastic-mimikatz-itadmin-process.png` — Mimikatz process activity.
13. `13-elastic-mimikatz-itadmin-pth-detail.png` — Mimikatz pass-the-hash details.
14. `14-elastic-mimikatz-process-detail.png` — process command-line detail.
15. `15-elastic-mimikatz-administrator-pth.png` — Mimikatz activity targeting Administrator.
16. `16-elastic-dcsync-backupda.png` — DCSync command targeting `backupda`.
17. `17-elastic-second-host-remote-process.png` — remote PowerShell process on the second host.
18. `18-elastic-credentialed-remote-powershell-redacted.png` — credentialed remote PowerShell; plaintext lab password redacted for public release.
19. `19-elastic-ransomware-download-attempt.png` — ransomware-download command.
20. `20-elastic-ransomware-search.png` — ransomware-related search results.
21. `21-elastic-ransomware-process-events.png` — ransomware-related process/event details.
22. `22-elastic-ransomware-event-details.png` — further ransomware-related event detail.
23. `23-elastic-mimikatz-follow-up-results.png` — follow-up Mimikatz results.

## Evidence handling
- Public-release copy redacts the plaintext lab password visible in screenshot 18. Keep unredacted evidence private.
- Complete pass-the-hash values should not be copied into public documentation.
- A search hit or download command is not, by itself, proof of successful execution or impact.
