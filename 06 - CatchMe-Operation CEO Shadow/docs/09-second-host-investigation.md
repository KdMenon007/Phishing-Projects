# 09 — Second Host Investigation

The second host is `WKSTN-1327.quicklogistics.org`. Screenshots show Mimikatz process activity and a malicious PowerShell process (PID 6708) with parent `wsmprovhost.exe`, consistent with remote PowerShell execution. Mimikatz pass-the-hash activity later targets `administrator`.

Full credential hashes are redacted in the public package. Confirm process GUIDs, authentication outcome, and host logon events from raw event exports before concluding that each attempted action succeeded.
