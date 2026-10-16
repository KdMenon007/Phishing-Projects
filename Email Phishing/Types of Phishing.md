
---

### 🎯 The Phishing Line-Up:

|Type|Description|
|---|---|
|**Spam**|Annoying, mostly harmless junk. Think “You won $10M from a Nigerian prince.”|
|**MalSpam**|Like spam, but meaner. Packs malware in attachments or links.|
|**Phishing**|Pretends to be a legit entity. Goal: steal credentials or data.|
|**Spear Phishing**|Highly targeted. Custom-tailored to one person/org.|
|**Whaling**|Phishing for executives — because CEOs click things too.|
|**Smishing**|Phishing via SMS. Because why stop at email?|
|**Vishing**|Voice phishing. Fake calls from “IT Support,” “IRS,” or “Bank Security.”|

---

### 🧠 Classic Phishing Email Clues:

1. **Spoofed Sender**  
    Think `support@paypa1.com` — that sneaky number "1" instead of an "l".
    
2. **Urgency/Scare Tactics**  
    “Your account has been suspended — act now or lose access!”
    
3. **Brand Masquerade**  
    HTML made to look like Netflix, Microsoft, or Amazon.
    
4. **Bad Grammar/Formatting**  
    Looks like it was written by a robot that failed English class.
    
5. **Generic Salutations**  
    “Dear Customer,” not your name? Big red flag.
    
6. **Weird Hyperlinks**  
    Hover to preview! If it doesn’t match what it claims to be — 🚨.
    
7. **Shady Attachments**  
    `Invoice.docm`, `Report.exe`, or anything base64-encoded and unexplained.
    

---

### 🔨 Tools of the Trade:

- Use **CyberChef** to:
    
    - Defang URLs (hxxp://example[.]com)
        
    - Decode base64 attachments
        
    - Extract HTML safely
        
- Open `.eml` files with a safe viewer like Thunderbird, Outlook (with preview disabled), or within the provided VM.
    

---

### 🕵️‍♀️ Your Mission:

You're now looking at `email3.eml`, sent from Alexa to Billy, the analyst.

- Start by viewing the **headers**: check `From`, `Reply-To`, `Received`, `X-Originating-IP`, and **authentication results**.
    
- Then move to the **body**:
    
    - Is there HTML?
        
    - Any hyperlinks? Hover them.
        
    - Any attachments? Look for base64 chunks or MIME sections.
        

When defanging, remember:

- `http://` → `hxxp[://]`
    
- `.` → `[.]`
    
- `@` → `[@]` or `at`
    

---
