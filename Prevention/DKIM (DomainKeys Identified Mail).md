
---

## 🕵️ What is DKIM?

**DomainKeys Identified Mail (DKIM)** is an **email authentication method** that allows the **receiver** to check that an email _really_ came from the domain it claims to be from, and that it **hasn't been tampered with in transit**.

### 🧠 TL;DR:

It digitally signs emails using a private key and publishes the corresponding public key via DNS. The receiving mail server verifies the signature using that public key.

---

## 🔐 DKIM Anatomy: What’s in a DKIM DNS Record?

Here’s a sample DKIM record:

```text
v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9...
```

### 🔍 Let's break it down:

- `v=DKIM1` → Version of DKIM being used (always this for now).
    
- `k=rsa` → Key type. RSA is standard (for now).
    
- `p=...` → This long string is the **public key**. Think of this like a padlock — the sender locked the message with their private key, and recipients can unlock it with this public one to verify authenticity.
    

This record lives in DNS under a **selector**, which is a custom name you define during setup. Example:

```
selector._domainkey.example.com
```

---

## 🧬 How DKIM Works (Step-by-Step)

1. ✍️ The sending mail server **generates a hash** (digital signature) of the email headers and body using its **private key**.
    
2. 📩 It **adds that signature to the email header**, typically under `DKIM-Signature:`.
    
3. 🌍 The receiving server extracts that signature and **looks up the domain’s public key** in DNS.
    
4. 🔍 If the signature **validates** (meaning the hash of the received content matches the signature):
    
    - ✅ It’s authentic and untampered.
        
    - ❌ If not, someone messed with it — spam, spoof, or misconfigured mail.
        

---

## 🤹 SPF vs DKIM — Why We Need Both

- **SPF** says: “Was this server _allowed_ to send this email?”
    
- **DKIM** says: “Was this email _authored_ by who it says it was, and not altered?”
    

And unlike SPF, **DKIM survives email forwarding** — _huge win_. SPF fails if forwarding isn't handled correctly.

---

## 💡 Why DKIM Is Critical

- Prevents **header spoofing**.
    
- Helps build a domain’s **sending reputation**.
    
- Works with **DMARC** to align and enforce policies.
    
- Makes it harder for attackers to impersonate your domain.
    

---
