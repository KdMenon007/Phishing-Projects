# CatchMe Project 05 — Operation HR Resume Trap

## Investigation status
Core attack-chain reconstruction completed; documentation and release
validation are in progress.

## Key findings
- Malicious Word AutoOpen macro
- Script download and Windows Script Host execution
- Suspicious updater.exe process
- Updater scheduled-task persistence
- Hidden PowerShell and registry-based payload retrieval
- C2-related network indicators
- Possible AMSI and PowerShell ETW tampering attempts

## Outstanding limitations
- Registry debug value payload not recovered
- PowerShell fragment incomplete
- Successful defense evasion and complete C2 exchange unconfirmed
- Network records available for review show closed sockets

## Safety
This repository is intended for defensive security analysis.
Do not execute recovered payloads. Original memory images and sensitive
evidence should remain private and be shared only when authorized.
