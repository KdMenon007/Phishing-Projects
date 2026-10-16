
---

### 🔐 **What’s the Deal with SPF, DKIM, and DMARC?**

They’re all about verifying identity and **ensuring authenticity**. You’re trying to make sure the sender **really is who they say they are**, and not some script kiddie spoofing "paypal.com" from a shady IP.

---

## 🛡️ 1. **SPF – Sender Policy Framework**

- **Purpose**: Prevents _forged sender addresses_ by validating that the email came from an IP **authorized** to send on behalf of a domain.
    
- **How**: DNS TXT record lists IPs or domains allowed to send for `example.com`.
    
- **Email Server**: When it receives an email claiming to be from `@example.com`, it checks the sender’s IP against that SPF record.
    
- **Result**: Pass or Fail (or Softfail, depending on config).
    

**Example DNS Record:**

```
v=spf1 ip4:192.0.2.0/24 include:_spf.google.com -all
```

> Translation: Only allow this IP range and Google's mail servers. Block everything else.

---

## 🧾 2. **DKIM – DomainKeys Identified Mail**

- **Purpose**: Ensures the **content of the email hasn't been tampered with** in transit.
    
- **How**: The sender signs parts of the email (like subject and body) using a **private key**. The recipient validates this using the **public key** published in DNS.
    
- **Result**: Authenticates the **integrity** of the email and verifies the sender is trusted.
    

**Example DNS Record (simplified):**

```
default._domainkey.example.com IN TXT "v=DKIM1; k=rsa; p=MIGfMA0..."
```

---

## 🧯 3. **DMARC – Domain-based Message Authentication, Reporting, and Conformance**

- **Purpose**: Gives domain owners control over **what to do when SPF or DKIM fails**.
    
- **How**: Published in DNS, tells recipient mail servers:
    
    - Check SPF/DKIM alignment.
        
    - What action to take if they fail (none, quarantine, reject).
        
    - Where to send reports.
        

**Example DMARC Record:**

```
v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@example.com; sp=reject
```

> This means: "Quarantine suspicious emails. Send failure reports. Reject if subdomains fail."

---

### 🧠 Why Does This Matter for SOC/IR Teams?

- Attackers spoof domains to increase trust. This trio says: _"Nice try, faker."_
    
- These controls help reduce **false positives** in phishing detection.
    
- Great source of **intel** — those DMARC reports? They're passive recon gold.
    

---

### ⚙️ **Per MITRE ATT&CK**

- **T1566 – Phishing**
    
    - **Sub-techniques**: Spearphishing via Service, Link, or Attachment.
        
    - **Mitigation**: [M1054 – Software Configuration](https://attack.mitre.org/mitigations/M1054/)
        
        - Highlights **SPF, DKIM, DMARC** as core mitigations.
            
        - Also mentions **limiting external content** and **content disarm/reconstruction (CDR)**.
            

---

### 👮 TL;DR

|Protocol|Protects Against|Enforced By|Stored In|
|---|---|---|---|
|SPF|IP Spoofing|Sender’s DNS|DNS TXT Record|
|DKIM|Tampered Content|Sender’s Mail Server|DNS TXT Record|
|DMARC|Domain Spoofing + Report Handling|DNS Policy|DNS TXT Record|

---