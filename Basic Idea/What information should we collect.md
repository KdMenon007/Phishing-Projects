
---

## 📬 **Header Analysis — The Metadata Autopsy**

These fields are your **forensics goldmine**. Open the raw email source (within the `.eml` file), and collect:

|Field|What You're Looking For|
|---|---|
|**Sender Email**|Found in the `From:` field. May be spoofed.|
|**Sender IP**|Look in `X-Originating-IP` or the earliest `Received:` line.|
|**Reverse DNS Lookup**|Take the sender IP, do a `dig -x IP` or use a WHOIS tool.|
|**Subject**|`Subject:` field. Check for urgency or bait language.|
|**Recipient**|`To:`, `Cc:`, `Bcc:` if available. Confirm it’s targeted.|
|**Reply-To**|Often different from `From:` — trick to redirect replies.|
|**Date/Time**|`Date:` field. Useful for timeline and correlation.|

---

## 💌 **Body Analysis — What the Attacker Wants You to See**

Next, examine the message body (plain and HTML). Don't render it — **view source only**.

|Artifact|What to Collect|
|---|---|
|**Hyperlinks**|Look for `<a href>` tags in HTML. Hover or parse manually.|
||Use CyberChef to **defang** and check for obfuscation.|
||Unshorten links using `curl -I` or online services.|
|**Attachments**|Look for `Content-Disposition: attachment`. Note filename.|
|**Attachment Hash**|Extract and save the file. Run `sha256sum` or `md5sum`.|

> ⚠️ **Pro Tip:** Always hash before opening, and never interact with `.docm`, `.exe`, or `.js` files unless you're inside a malware analysis sandbox. Even PDFs can be weaponized.

---

## 🛠️ Tools That Help You Not Die

- **CyberChef**: For defanging, base64 decoding, extracting links
    
- **VirusTotal**: Upload the hash (not the file) to check reputation
    
- **WHOIS/NSLookup**: To investigate sender domains or IPs
    
- **Email Header Analyzer**: Use tools like MXToolbox or Google's tool to quickly parse
    

---

## ✅ Final Deliverables (Analyst's Report)

After your analysis, compile your findings like this:

### 📌 Header Analysis

- **From:** boss[@]paypal-security[.]net
    
- **Reply-To:** hr[@]paypalsecuremail[.]io
    
- **Subject:** "Urgent Payroll Issue - Action Required"
    
- **To:** alexa[@]company[.]com
    
- **Date:** 2025-05-04 12:14:32 UTC
    
- **Sender IP:** 185.198.57.23
    
- **rDNS:** mail[.]blx1[.]pro (suspicious domain, likely bulletproof hosting)
    

### 📌 Body/Attachment

- **URL:** hxxps[:]//bit[.]ly/3XyZz123 → resolves to hxxp[:]//secure[.]payrollfix[.]com
    
- **Attachment:** Payroll_Document.pdf
    
- **SHA256:** `c3f0b4a7c99e59f7750a1ddffbd91714f5e62dc1d36cf95ec12e84e90b6db234`
    

---

