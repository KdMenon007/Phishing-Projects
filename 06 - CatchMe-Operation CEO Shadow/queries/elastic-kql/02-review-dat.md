# Search 02 — review.dat

```kql
"review.dat"
```

The screenshot showed 39 hits. The visible row is `xcopy.exe` PID 3832 copying `D:\review.dat` to `C:\Users\EVAN~1.HUT\AppData\Local\Temp\review.dat`. Expand events and find a later process command line referencing the destination path; do not treat the copy as execution.


## Follow-up evidence — `rundll32.exe` and `fodhelper.exe`
The latest screenshot shows `fodhelper.exe` PIDs 5308 and 5180, parent `rundll32.exe`, with parent command line `"C:\Windows\System32\rundll32.exe" D:\review.dat,DllRegisterServer`. Use a process-name or command-line pivot to retrieve the full event JSON and validate the relationship. Example field-based KQL (adjust to mapped fields):

```kql
process.name : "fodhelper.exe" or process.parent.command_line : "*review.dat*"
```

The screenshot supports the observed process chain but not, by itself, successful UAC elevation.
