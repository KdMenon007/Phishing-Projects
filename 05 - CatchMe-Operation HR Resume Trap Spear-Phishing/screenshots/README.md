# Screenshot Evidence Index — Project 05

These screenshots were supplied during the initial email-triage stage of **CatchMe Project 05 — Operation HR Resume Trap: Spear-Phishing Investigation**. They are reference evidence for the investigation; findings should be confirmed against the original `.eml` and attachment files.

| File | Evidence captured | Notes |
|---|---|---|
| `01-email-overview.png` | Email overview: sender, recipient, subject, date, attachment indicator | Preserve as a visual reference; use the original email for exact values. |
| `02-email-body.png` | Email body and applicant narrative | The body claims to be a Junior IT Analyst application and is signed “Wesley Taylor.” |
| `03-attachment-summary.png` | Attachment bar and displayed filename/size | Shows `Resume_WesleyTaylor.doc` and a displayed size of 62.5 KB. |
| `04-authentication-results.png` | Email authentication and received-header excerpt | SPF/DKIM/DMARC results are visible; authentication results alone do not prove the message is benign. |
| `05-email-header-fields.png` | From, To, Subject, Date, and Message-ID fields | Use the original `.eml` to verify and record exact header values. |
| `06-attachment-mime-details.png` | MIME attachment metadata | Shows the attachment content type, filename, declared size, and base64 transfer encoding. |
| `07-suspicious-document-preview.png` | Opened document preview showing an “Enable Editing/Enable Content” lure | Do not enable editing/content or execute the document. Treat it as suspicious and analyze a copy in a controlled environment. |

| `08-attachment-hashes.png` | `file`, `md5sum`, `sha256sum`, and `ls -lh` output for the extracted document | Observed MD5 and SHA-256 are recorded in the evidence register; size shown by terminal as 63K. |

| `09-document-analysis-oleid.png` | `oleid` results: legacy Word OLE format, VBA macros flagged as suspicious, no external relationships reported | Static indicator output; not proof of what the macros actually did. |

| `10-macro-indicators-olevba.png` | `olevba -a` indicators: `AutoOpen`, file-write/download/shell-related keywords, hex strings, URL indicator, and filenames `update.js` / `wscript.exe` | The URL is line-wrapped in the screenshot; confirm the exact string from full macro source before reporting it. |

| `11-vba-source-analysis.png` | Full `olevba` output showing `AutoOpen`, HTTP retrieval, writing to `C:\ProgramData\update.js`, and launching via `wscript.exe` | URL and command are transcribed from the screenshot; preserve the text output as well if possible. |

| `12-workstation-artifact-inspection-ascii.png` | First 64 bytes shown as zeroes; ASCII strings include NTFS, BOOTMGR, and Windows boot/error text | Strings suggest disk/volume-related content somewhere in the file; this is not enough to identify the exact container format. |

| `13-workstation-artifact-inspection-unicode.png` | UTF-16LE strings include NTFS metadata names, `System Volume Information`, and Windows UI resource strings | Supports further format/offset validation; do not assume this is an ETL or memory image based on `file` alone. |

| `14-offset-and-signature-inspection.png` | Hex output at offsets 4096, 512, end-of-file, and offset 510 | Offset 510 is `0000`; no conventional MBR boot signature is shown there. This alone does not rule out all image formats. |

| `15-first-nonzero-offset.png` | File size and `grep` results locating printable bytes beginning at offset 4096 | A printable byte offset is not sufficient to determine the artefact format. |

| `16-volatility-process-tree.png` | Volatility `windows.pstree` filtered for Word, script, command shell, and scheduled-task indicators | Shows Outlook PID 1440 → Word PID 1124 → `wscript.exe` PID 4260 → `updater.exe` PID 6216. |

| `17-volatility-command-lines.png` | Volatility `windows.cmdline` filtered for likely attack-chain terms | Corroborates `wscript.exe C:\ProgramData\update.js` and `C:\Windows\Tasks\updater.exe`. |

| `18-volatility-network-connections.png` | Volatility `windows.netscan` filtered for the candidate endpoint | Multiple connections attributed to PID 6216 target `128.199.95.189:8080`; the displayed state is `CLOSED`. |

## Handling notes

- These screenshots are supporting references, not substitutes for the original evidence files.
- Do not publish the original email, document, or raw forensic artefact to a public repository unless authorized and safely sanitized.
- Record hashes of the original evidence and extracted attachment, and preserve timestamps where available.
- No conclusions about macros, payload URLs, process IDs, C2, or persistence should be added until independently verified.
