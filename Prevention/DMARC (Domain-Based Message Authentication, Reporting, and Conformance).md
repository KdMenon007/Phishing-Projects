### What is **DMARC**?

**DMARC** (Domain-based Message Authentication, Reporting & Conformance) is the final piece of the email authentication puzzle. It ties together **SPF** and **DKIM** to provide a **policy-based framework** that tells email receivers how to handle emails that fail these authentication checks.

It's basically a way to enforce what should happen if an email isn’t authenticated properly — should it be rejected, quarantined, or let through?

---

### 🌐 Why DMARC Matters

- **Prevents phishing and spoofing:** By requiring emails to align with both SPF and DKIM, DMARC makes it harder for attackers to impersonate a domain.
    
- **Visibility & Reporting:** It gives domain owners insight into their email traffic and highlights any potential abuse.
    
- **Control:** It lets you decide what happens to emails that fail SPF and DKIM checks.
    

---

### 💡 Structure of a DMARC Record

Here’s an example of a **basic DMARC record**:

```text
v=DMARC1; p=quarantine; rua=mailto:postmaster@website.com
```

### Breakdown of the Record:

- `v=DMARC1` → **Version** of DMARC being used. This is always the same (`DMARC1`).
    
- `p=quarantine` → **Policy** to apply when an email fails DMARC checks:
    
    - `none` → No action, just monitor.
        
    - `quarantine` → Move to spam/junk folder.
        
    - `reject` → Reject the email entirely.
        
- `rua=mailto:postmaster@website.com` → **Reporting URI** for aggregate reports (sends data about all failed checks).
    

---

### 🚀 DMARC Alignment

**DMARC Alignment** is crucial because it ensures that the domain in the `From` field of the email matches the domain used in the SPF and DKIM checks.

- **SPF Alignment:** The domain in the `From` address must match the domain of the sending mail server in the SPF check.
    
- **DKIM Alignment:** The domain in the `From` field must match the domain used in the DKIM signature.
    

---

### 🔍 Example: **Checking DMARC Status of microsoft.com**

Using **dmarcian**’s **Domain Health Checker**, we can check the DMARC status for **microsoft.com**. When checked, we see:

- **Microsoft passed all checks** for DMARC, SPF, and DKIM.
    
- The **DMARC policy** was set to **reject**, meaning any emails that fail DMARC checks are **rejected** outright (a strong security posture).
    

---

### 🛡️ Why Every Domain Should Have DMARC

Without DMARC, a domain might be vulnerable to impersonation and spoofing. Attackers could easily spoof an email from a trusted domain, and recipients might not be able to tell it’s malicious. But with DMARC, **domain owners can enforce a policy** that blocks or quarantines those malicious attempts.

If you run a domain, don't just stop at SPF and DKIM — implement **DMARC** to lock down your domain’s email security.

---

