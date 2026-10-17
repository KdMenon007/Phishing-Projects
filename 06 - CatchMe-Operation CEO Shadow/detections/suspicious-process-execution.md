# Detection: Suspicious HTA, Rundll32, and Fodhelper Chain

## Observed chain
- `mshta.exe` PID 6392 launched `D:\ProjectFinancialSummary_Q3.pdf.hta`.
- `xcopy.exe` PID 3832 copied `D:\review.dat` into the CEO user's Temp directory.
- A parent command line references `rundll32.exe D:\review.dat,DllRegisterServer`.
- `fodhelper.exe` process events are consistent with a suspected UAC-bypass chain.

## KQL pivots
```kql
process.name : "mshta.exe" and process.command_line : "*ProjectFinancialSummary_Q3.pdf.hta*"
```
```kql
process.name : "xcopy.exe" and process.command_line : "*review.dat*"
```
```kql
process.name : "rundll32.exe" and process.command_line : "*review.dat*"
```
```kql
process.name : "fodhelper.exe"
```

Correlate process GUIDs and parent-child events. Treat successful UAC elevation as unconfirmed until elevation/token evidence supports it.
