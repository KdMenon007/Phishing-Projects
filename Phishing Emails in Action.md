
---

# 🔑 Universal keypoints (applies to all samples)

- **Main techniques seen:** spoofed sender, link manipulation (shorteners/redirects), HTML impersonation, tracking pixels, urgency, credential-harvesting pages, malicious attachments, BCC recipients, typosquatting/poor grammar.
    
- **Always check:** `From`, `Reply-To`, authentication results (SPF/DKIM/DMARC), `X-Originating-IP`, and the raw HTML source.
    
- **Don’t click.** Defang links before sharing: `hxxp[:]//example[.]com`.
    
- **View raw source** to extract full URLs, image src, and embedded attachments (base64).
    
- **Open attachments only in an isolated VM/sandbox** and scan with multiple AV/endpoint tools.
    
- **Look for mismatch signals:** branding + domain mismatch, unexpected recipients (BCC), urgent deadlines, and poor language.
    

---

# Sample-specific keypoints & analyst actions

### 1) **PayPal-style email (spoofed address + shortener)**

- **Techniques:** spoofed `From` name ([service@paypal.com](mailto:service@paypal.com)) while actual sender domain ≠ PayPal; shortened URL that redirects.
    
- **Red flags:** recipient address not matching account, subject claims purchase you didn’t make, Reply-To different from From.
    
- **Analyst actions:** expand the shortener (use URL unshortening service), verify redirect chain, check SPF/DKIM/DMARC, extract and block the final destination if malicious.
    

---

### 2) **Mail distribution / tracking-number lure (tracking pixel + shady domain)**

- **Techniques:** tracking pixel images, link to suspicious domain, spoofed distribution pretense.
    
- **Why images were blocked:** email provider prevented auto-loading to stop pixel tracking.
    
- **Analyst actions:** fetch image src from HTML, query domain/host/IP, check pixel URL for unique identifiers (used to confirm recipient validity), add pixel host to blocklist if malicious.
    

---

### 3) **OneDrive/Adobe credential-harvest (link→fake MS/Adobe pages)**

- **Techniques:** urgency + impersonated SharePoint/Adobe pages, credential harvesting via fake OAuth/email login.
    
- **Red flags:** domain not Microsoft/Adobe, grammar mistakes, page title mismatch, “expire today” urgency.
    
- **Analyst actions:** take a snapshot of the phishing page (do not login), capture POST endpoints, identify form target URLs, create IOC (phishing domain + form action + hosting IP) and add to email/web filters, inform users.
    

---

### 4) **Netflix billing with PDF attachment**

- **Techniques:** spoofed Netflix sender, urgency (“account suspended”), attachment with embedded malicious link.
    
- **Red flags:** sender domain unrelated to Netflix, typos, foreign phone numbers, attachment asks to update payment.
    
- **Analyst actions:** extract PDF from raw email, base64-decode if needed, scan in sandbox for macros/external links, block attachment hash and source.
    

---

### 5) **Apple Support with BCC + .DOT attachment**

- **Techniques:** spoofed Apple, recipient BCCed, attachment is a Word template (.DOT) with embedded image+links.
    
- **Red flags:** BCC usage (mass send), recipient address looks spoofed, misspellings in sender/recipient.
    
- **Analyst actions:** extract .DOT, inspect for macros and embedded links, open only in isolated VM, log attachment behavior (calls, downloads, network IO), blacklist attacker domain and attachment hash.
    

---

### 6) **DHL/package delivery with Excel attachment**

- **Techniques:** HTML impersonation of DHL, attachment (Excel) containing a payload that caused an error in sandbox.
    
- **Red flags:** HTML designed to look like DHL but domain mismatch, only interactive element is attachment.
    
- **Analyst actions:** extract Excel, analyze macros and external calls, trace payload behavior in sandbox, capture Indicators of Compromise (C2 domains, IPs), update EDR/AV signatures.
    

---

# Quick SOC checklist — what you must capture immediately

1. **Email raw source** (save copy).
    
2. **All headers** (`From`, `Reply-To`, `Return-Path`, `Received`, `X-Originating-IP`, `Authentication-Results`).
    
3. **All URLs** (expanded final destinations + redirect chain).
    
4. **Attachment file(s)** (base64-decoded copy + hash: MD5/SHA1/SHA256).
    
5. **Screenshots** of rendered HTML & phishing site (don’t interact).
    
6. **Sandbox run report** for attachments & pages (network calls, processes).
    
7. **IOCs**: domains, full URLs, IPs, hashes, email addresses — push to blocklists/filters.
    
8. **User notification** if phishing targeted org users — tell them to change creds if they clicked.
    

---

# Fast indicator judgement (TL;DR)

- Sender domain ≠ brand domain → **high risk**.
    
- Shortened URL unknown → **treat as phishing** until expanded.
    
- Images blocked + tracking pixel present → likely mass-mailing & tracking.
    
- Credential page on non-official domain → **credential harvest** (urgent).
    
- Attachments (PDF, DOT, XLS) with links/macros → **malware risk** (sandbox required).
    

---

# Tools / Techniques to use (one-liners)

- **Expand URL:** use unshortening services (or `curl -I` to follow redirects).
    
- **View email raw:** email client “view source” / `ripmime` / `munpack`.
    
- **Extract attachments:** open raw and base64-decode to file, then hash/scan.
    
- **Check auth:** verify SPF/DKIM/DMARC headers in the raw message.
    
- **Sandbox:** AnyRun / Cuckoo / private VM for attachments & hosted pages (don’t reuse VMs).
    

---
