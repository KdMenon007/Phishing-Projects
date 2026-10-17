# Detection: Credential Access and Pass-the-Hash

## Evidence observed
- Mimikatz ZIP download command references the official GitHub release URL: `https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20220919/mimikatz_trunk.zip`.
- Process telemetry shows Mimikatz `sekurlsa::pth` targeting `itadmin` on `WKSTN-1327` and later `administrator` on the second host.
- Complete NTLM hashes are intentionally omitted from this public release.

## Hunting pivots
- `process.name : "mimikatz.exe"`
- `process.command_line : "*sekurlsa::pth*"`
- `process.command_line : "*mimikatz_trunk.zip*"`
- Correlate PowerShell download, archive creation/extraction, Mimikatz process start, logon/authentication events, and subsequent remote execution.

## Response
Contain affected hosts, rotate exposed credentials, invalidate sessions, and review privileged account activity. Do not rely on a process name alone; validate full command lines and parent/child relationships.
