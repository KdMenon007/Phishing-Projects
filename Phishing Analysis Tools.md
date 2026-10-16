
---

# 🦾 **Phishing Email Analysis Workflow (The SOC Playbook)**

## ✅ **Step 1 — Collect Key Header Information**

Open the email **raw source** (not just what you see visually).

Extract:

|Data to Collect|Why It Matters|
|---|---|
|**Sender email address**|Check if spoofed / mismatched branding|
|**Sender IP address**|Identify origin mail server|
|**Reverse DNS hostname**|Can reveal non-legit hosts / cloud VPS spam kits|
|**Subject line**|Look for urgency / scams|
|**Recipient address**|Check for BCC mass-mailing|
|**Reply-To address**|If different → obvious phishing tactic|
|**Date/Time**|Useful for timeline + correlation|

### Tools to automate header parsing:

- **Google Messageheader Analyzer**  
    [https://toolbox.googleapps.com/apps/messageheader/analyzeheader](https://toolbox.googleapps.com/apps/messageheader/analyzeheader)
    
- **Microsoft Message Header Analyzer**  
    [https://mha.azurewebsites.net/](https://mha.azurewebsites.net/)
    
- **mailheader.org** (simple & clean)
    

---

## 🧠 **Step 2 — Investigate Sender IP**

Run the sender IP and domains:

|Tool|Use|
|---|---|
|**IPinfo.io**|IP owner, org, ASN, location|
|**Talos Reputation Center**|IP/domain reputation score|
|**URLScan.io**|Safe-render malicious pages, analyze redirects|

This helps determine:  
_“Is this a corporate mail server or some sketch VPS in Romania named `dragon-mail-revenge.biz`?”_

---

## 💌 **Step 3 — Examine the Email Body**

Look for:

- Branding impersonation (logos, formatting copied from PayPal / DHL / Netflix / Microsoft, etc.)
    
- Urgency language (“Your account will be suspended in 2 hours!!!”)
    
- Generic greetings (“Dear user, customer, sir/madam”)
    
- Weird grammar / spelling errors
    

Remember:  
**Social engineering always tries to push urgency or authority.**

---

## 🔗 **Step 4 — Extract & Analyze URLs (Safely!)**

### How to Extract URLs:

- **Copy link → do not click.**
    
- Or extract automatically using:
    
    - URL Extractor → [https://www.convertcsv.com/url-extractor.htm](https://www.convertcsv.com/url-extractor.htm)
        
    - **CyberChef** → _Recipe:_ `Extract URLs`
        

### Expand shortened or obfuscated URLs:

- Use unshortening tools (don’t follow link manually)
    
- Feed final URL into:
    
    - **URLScan.io**
        
    - **VirusTotal**
        
    - **Talos Reputation**
        

Check **root domain**, not just path.

> If the domain doesn’t match the brand being impersonated → **🚨 phishing confirmed.**

---

## 📎 **Step 5 — Handle Attachments (No Clicking!)**

### If attachments exist:

1. **Save it to a safe VM** (Thunderbird → Save Attachment)
    
2. **Hash it**:
    
    ```bash
    sha256sum filename
    ```
    
3. **Check reputation via hash**:
    
    - [https://talosintelligence.com/talos_file_reputation](https://talosintelligence.com/talos_file_reputation)
        
    - [https://www.virustotal.com/](https://www.virustotal.com/)
        

If VirusTotal shows:

- _“Low detection, unknown”_ → **Analyze further**
    
- _“Many AV detections”_ → **Tagged malicious immediately**
    

### Optional deeper analysis (if required):

Submit file to malware sandboxes:

- **Any.Run**
    
- **Hybrid Analysis**
    
- **Joe Sandbox**
    

These will show:

- Network traffic (C2 servers)
    
- Dropped files
    
- Registry modifications
    
- Persistence behavior
    

---

## 🤖 **Bonus — One Tool That Does (Almost) Everything**

**PhishTool**  
[https://phishtool.com/](https://phishtool.com/)  
_(Free community edition available)_

PhishTool auto-pulls:

- Sender / Recipient / IP / Reverse DNS
    
- URLs + attachments
    
- VirusTotal file hash results
    
- SMTP relay chain
    
- HTML + plain view toggles
    

Basically → **Phishing analysis but with power steering.**

---

# 🧾 **SOC Analyst Output / Reporting Checklist**

Before closing the case, ensure you document:

|IOC Type|Example|
|---|---|
|Sender email address|`service@paypal.com` (spoofed)|
|Actual domain source|`sultanbogor.com`|
|Sender IP & Hostname|`103.82.241.22` → `vps.victimmail.asia`|
|URLs & Redirects|Final destination and redirect chain|
|Attachment filename|e.g., `Invoice_Receipt.pdf`|
|Attachment hash|SHA256 hash|
|Outcome|_Phishing → credential harvest / malware dropper / scam_|
|Block actions|Email rule, domain blacklist, EDR, firewall|

---

## 🎤 **TL;DR — The Analyst Mindset**

- Don’t trust the display name — check the actual sender domain.
    
- Don't click anything — extract and analyze through tools.
    
- If it feels rushed, emotional, or panicky → **it’s bait.**
    
- Always defang links → `hxxp[:]//domain[.]com`.
    

---
