
---

## 📧 Email Anatomy 101: The Two Main Organs

### 1. **Email Header**

Think of this as the **envelope and postmarks** of your message. It tells the whole story — who sent it, when, through what servers, and whether it's trying to lie to you.

### 2. **Email Body**

This is the **content** — what the sender actually wants you to see. Often includes:

- Plain text
    
- HTML content (e.g. styled phishing lures)
    
- Embedded images or links
    
- Potential attachments (macros, droppers, etc.)
    

---

## 🔍 Key Email Header Fields You Should Always Investigate

### ✅ **Visible Fields** (straightforward, but often forged)

|Field|What It Tells You|
|---|---|
|`From:`|Claimed sender (easy to spoof)|
|`To:`|Who it’s sent to|
|`Subject:`|Social engineering bait|
|`Date:`|When the email was sent (can be fake too)|

These are what the user sees. They're useful for quick context — _“Does this look fishy?”_ — but don't stop here.

---

### 🔬 **Deep Header Fields** (where the real forensics happen)

|Field|What It Means|Why It’s Critical|
|---|---|---|
|`Received:`|Mail relay hops|Shows path the email took; read bottom-up|
|`Reply-To:`|Where replies go|Mismatch here can be a red flag|
|`X-Originating-IP:`|IP of sender|Often gives away sketchy sources (e.g., VPS in Russia)|
|`Return-Path:`|Bounceback address|Can differ from `From:` — another red flag|
|`Authentication-Results:`|DKIM / SPF / DMARC validation|Failures = likely spoofed|
|`Message-ID:`|Unique email identifier|Can give away fake services (e.g., Gmail-style ID from a non-Gmail domain? Sketch.)|

---

### 📡 Fun Fact: `Received:` is **your best friend**

Each mail server the email passed through adds a new `Received:` line **on top** of the previous one. So, to trace the origin:

- Read `Received:` **bottom to top**
    
- The **lowest one** (chronologically) is likely the originating server
    

> 🤓 Think of this like peeling back the layers of a stinky onion — the deeper you go, the closer you get to the original stink source.

---

## 🔥 Red Flags When Analyzing Email Headers

- ✅ SPF/DKIM/DMARC **failures** in `Authentication-Results`
    
- 🧠 `From:` and `Reply-To:` don’t match
    
- 🧀 Strange or low-reputation domain in `Return-Path`
    
- 🚨 `X-Originating-IP` is from a consumer ISP or a sketchy VPS
    
- 🕵️‍♂️ Message-ID doesn't align with sending domain (e.g., `message-id:<xyz@gmail.com>` sent from `@mailru.com`)
    

---
