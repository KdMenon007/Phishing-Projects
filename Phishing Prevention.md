
---

# 🌐 **Email Authentication & Anti-Phishing — Full Concept Summary**

## 1) **SPF (Sender Policy Framework)**

**Purpose:** Confirms whether the sending mail server (IP/domain) is allowed to send mail for that domain.

![[Pasted image 20251107074032.png]]

### **How It Works**

1. Sender sends email.
    
2. Receiving server checks the domain’s **SPF record** in DNS.
    
3. If sender’s IP matches authorized list → pass. If not → fail.
    

### **SPF Record Example**

```
v=spf1 ip4:127.0.0.1 include:_spf.google.com -all
```

|Part|Meaning|
|---|---|
|`v=spf1`|SPF version|
|`ip4:127.0.0.1`|Allowed IPv4 sender|
|`include:_spf.google.com`|Trust Google’s mail servers|
|`-all`|Reject everything else|

### **SPF Result → Action**

|Result|Action|
|---|---|
|Pass / Neutral / None|Accept email|
|SoftFail / PermError|Accept but flag as suspicious|
|Fail / TempError|Reject|

### **Important Note**

SPF can break when **emails are forwarded**, because the IP changes.

---

## 2) **DKIM (DomainKeys Identified Mail)**

**Purpose:** Ensures the **email content isn't altered** and verifies the sender using **cryptographic signatures**.

![[Pasted image 20251107074054.png]]

### **How It Works**

1. Sending server signs email with **private key**.
    
2. Receiving server fetches **public key** from DNS.
    
3. Public key verifies signature.
    

If it matches → Authentic  
If not → Spoofed or modified

### **DKIM Record Example**

```
v=DKIM1; k=rsa; p=<public_key>
```

|Part|Meaning|
|---|---|
|`v=DKIM1`|DKIM version|
|`k=rsa`|Key type|
|`p=`|Public key used for verification|

### **Strength**

- **DKIM survives forwarding.**  
    This is why it's crucial.
    

---

## 3) **DMARC (Domain-Based Message Authentication, Reporting, and Conformance)**

**Purpose:** Combines **SPF + DKIM** to enforce **domain identity alignment**.

If the email **fails alignment**, DMARC tells the receiver what to do.

### **DMARC Record Example**

```
v=DMARC1; p=quarantine; rua=mailto:postmaster@website.com
```

|Part|Meaning|
|---|---|
|`p=`|Policy: none / quarantine / reject|
|`rua=`|Where to send aggregate reports|

### **Policy Behavior**

|Policy|Meaning|
|---|---|
|none|Monitor only|
|quarantine|Send to spam|
|reject|Block completely|

---

## 4) **S/MIME (Secure/Multipurpose Internet Mail Extensions)**

Provides **encryption + digital signatures** using public key certificates.

### **Security Benefits**

|Feature|Meaning|
|---|---|
|**Authentication**|Confirms identity of sender|
|**Non-repudiation**|Sender cannot deny sending|
|**Data Integrity**|Detects alterations|
|**Confidentiality**|Encrypts message for privacy|

### **How It Works**

- Bob signs email with **private key**
    
- Mary verifies with **Bob’s public key**
    
- Mary replies the same way → Both exchange certificates.
    

![[Pasted image 20251107074119.png]]

---

## 5) **Technical Phishing Defenses**

|Defense|What It Does|
|---|---|
|**Email Filtering**|Blocks spam & bad reputation IPs/domains|
|**Secure Email Gateway (SEG)**|Detects spoofing, impersonation, phishing|
|**Link Rewriting**|Replaces links with safe redirect scans|
|**Sandboxing** ✅|Runs attachments in isolated environment to observe malware behavior|

---

## 6) **User-Facing Anti-Phishing Tools**

|Tool|Purpose|
|---|---|
|**Trust/Warning Indicators**|Labels external / new / suspicious senders|
|**Phishing Report Buttons**|One-click report to security team|
|**Awareness Training**|Teaches employees how attacks look|
|**Phishing Simulations**|Test real-world user responses|

![[Pasted image 20251107074144.png]]

---
