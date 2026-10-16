
---

## 1️⃣ Initial Triage (Before Touching the Email)

**Goal:** Decide if this email deserves deep analysis or instant containment.

- Was the email **reported by users**? (Yes → higher confidence)
    
- Multiple recipients? Same department?  
    → Indicates **targeted phishing (spear-phish)**
    
- Business context leveraged? (Invoice, payment, shipping)  
    → High-risk lure
    
- Attachment or link present?  
    → Immediate red flag
    

📌 _Decision:_ If finance + attachment + urgency → **escalate immediately**

---

## 2️⃣ File Identification & Preservation

**Goal:** Preserve evidence and avoid accidental execution.

- Save email as `.eml` or `.msg`
    
- Do **NOT** open attachments directly
    
- Work on a **forensic VM**
    
- Hash the `.eml` file:
    
    ```bash
    sha256sum dump.eml
    ```
    

📌 _Why:_ Chain of custody matters. Always.

---

## 3️⃣ Email Header Analysis (Technical Trust Check)

### 🔍 Extract Headers

```bash
cat dump.eml | less
```

---

### 🧱 Key Header Fields to Analyze

#### A. `From`

- Display name vs actual domain mismatch
    
- Lookalike domains (`rn` vs `m`, extra hyphens)
    

#### B. `Return-Path`

- Must align with sender domain
    
- If different → spoofing or forwarding abuse
    

#### C. `Received` Chain (MOST IMPORTANT)

- Trace **bottom → top**
    
- Check:
    
    - First mail server (origin)
        
    - Country / ASN anomalies
        
    - Suspicious hosting providers
        

📌 _Rule:_ Legit business emails don’t originate from random VPS providers.

---

#### D. Authentication Results

Check:

- `SPF` → pass / softfail / fail
    
- `DKIM` → pass / fail
    
- `DMARC` → none / quarantine / reject
    

📌 _Insight:_

> Phishing often **passes SPF but fails DMARC alignment**.

---

#### E. Message-ID

- Free email providers?
    
- Randomized or malformed format?
    
- Legit orgs have consistent Message-ID patterns
    

---

## 4️⃣ MIME Structure Analysis (Hidden Payloads Live Here)

**Goal:** Understand how content is delivered.

- Look for:
    
    - `Content-Type: multipart/mixed`
        
    - `Content-Transfer-Encoding: base64`
        
- Identify attachment boundaries
    
- Check if payload is:
    
    - Embedded inline
        
    - Obfuscated at the bottom
        

📌 _Red flag:_ Long Base64 blocks inside email body.

---

## 5️⃣ Attachment Extraction (Manual & Safe)

### ✋ Manual Extraction (Preferred for Analysts)

- Copy Base64 blob
    
- Remove line breaks if needed
    
- Decode:
    
    ```bash
    base64 -d payload.txt > Invoice.zip
    ```
    
- Verify file type:
    
    ```bash
    file Invoice.zip
    ```
    

📌 _Why manual wins:_  
You see **exactly what the attacker sent** — no mail client interference.

---

## 6️⃣ Attachment Type Analysis

### 📦 If ZIP / RAR / ISO

- Password protected? (social engineering)
    
- Password often included in email body
    
- Check archive contents **without executing**
    

---

### 🧨 If LNK (Shortcut) — HIGH RISK

- Common finance lure
    
- Abuses user trust + Windows behavior
    

📌 _Instant escalation trigger._

---

## 7️⃣ LNK File Deep Analysis

### Tool

```bash
lnkparse malicious.lnk
```

### Fields to Inspect

- **Target Path**
    
    - `powershell.exe`
        
    - `cmd.exe`
        
    - `wscript.exe`
        
- **Arguments**
    
    - Encoded PowerShell
        
    - Download cradles
        
- **Working Directory**
    
    - `%TEMP%`
        
    - `%APPDATA%`
        
- **Icon Location**
    
    - Fake PDF / Excel icons
        

📌 _Classic trick:_  
Looks like a document. Runs a script. Users lose.

---

## 8️⃣ Script / Command Analysis (If Present)

### PowerShell Red Flags

- `-enc` / `-encodedcommand`
    
- `-w hidden`
    
- `Invoke-WebRequest`
    
- `DownloadString`
    
- `FromBase64String`
    

📌 _Reality check:_  
Legit invoices **do not run PowerShell**. Ever.

---

## 9️⃣ URL & Network Indicator Analysis

### If URLs Found:

- Extract without clicking
    
- Normalize (remove hxxp, brackets)
    
- Check:
    
    - Domain age
        
    - IP reputation
        
    - Hosting ASN
        

📌 _Red flags:_

- Newly registered domains
    
- Free hosting / cloud storage abuse
    
- Raw IP URLs
    

---

## 🔟 Content & Language Analysis (Human Layer)

**Goal:** Detect social engineering patterns.

- Urgency:
    
    - “Immediate payment required”
        
- Authority:
    
    - Vendor / finance pressure
        
- Fear:
    
    - Account suspension
        
- Familiarity:
    
    - Known partner name
        
- Grammar:
    
    - Slightly off, but not terrible (intentional)
        

📌 _Modern phishing is written “just good enough.”_

---

## 1️⃣1️⃣ Campaign Correlation

- Same sender → multiple users?
    
- Same attachment hash?
    
- Same subject theme?
    
- Same execution behavior?
    

📌 _Conclusion:_  
Multiple hits = **campaign**, not accident.

---

## 1️⃣2️⃣ Mapping to ATT&CK (Optional but Pro)

- Initial Access → Phishing Attachment
    
- Execution → User Execution (LNK)
    
- Defense Evasion → Encoded Commands
    
- Persistence → Registry / Startup (possible)
    
- C2 → HTTP/HTTPS outbound
    

📌 _This helps detection engineering later._

---

## 1️⃣3️⃣ Impact Assessment

### Confirmed

- User interaction occurred
    
- Attachment executed
    
- Script launched
    

### Potential

- Credential theft
    
- Lateral movement
    
- Internal phishing
    
- Financial fraud
    

📌 _Finance compromise = business risk, not just IT risk._

---

## 1️⃣4️⃣ Final Analyst Verdict

This email is:

- ✔ Socially engineered
    
- ✔ Technically deceptive
    
- ✔ Context-aware
    
- ✔ Weaponized for execution
    

**Verdict:**  
🎯 **Targeted phishing with malicious attachment — confirmed compromise vector**

---

## 1️⃣5️⃣ Analyst Pro Tips (Hard Truths)

- If it says _invoice_ → assume malicious until proven otherwise
    
- LNK files have **no business being emailed**
    
- Users don’t fail security — **email design does**
    
- Attackers exploit routine, not ignorance
    

---

