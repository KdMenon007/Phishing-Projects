# Evidence Register

## Scope and handling

This register lists the artifacts used in the CatchMe phishing-investigation lab.
Original email files were preserved. The PDF was decoded from the MIME attachment
and compared byte-for-byte with the existing extracted PDF. Hashes should be checked
against the integrity manifest. This is a lab record, not a digitally signed chain of custody.

| Evidence ID | Path | SHA-256 | Description |
|---|---|---|---|
| E-01 | `assets/evidence/email/email1.eml` | `2ed3d561ebc566b8bb131efb5db6fb227c6b6d9042b6ee835bbf8f61e6ec8a15` | Original email artifact |
| E-02 | `assets/evidence/email/email2.txt` | `d905c328fa169f892e89f66dc34595e3d00db9c530e349400cb692d2b86c82b6` | Email text and PDF attachment MIME evidence |
| E-03 | `assets/evidence/email/email3.eml` | `69f6d1ef0c1026e71c0268bda6e4a865176af9b5c105781868420555435e86a9` | Original email artifact |
| E-04 | `analysis/pdf/zmqpalgh.pdf` | `7a8fbf5de792a20a2f3be994e041f34f9ca3f37e10d829f77bef94dfe7b77900` | Decoded PDF attachment analyzed statically |

## Supporting analysis

- `analysis/evidence-timeline.csv` — normalized event timeline.
- `analysis/indicator-inventory.csv` — extracted URL indicators and validation status.
- `assets/evidence/integrity/SHA256-MANIFEST.txt` — integrity reference.
- `assets/screenshots/` — screenshots of selected analysis steps.

## Limitations

Extracted URLs have not been reputation-checked or followed to final destinations.
Metadata and authentication results are observations, not standalone proof that a message is safe or malicious.
