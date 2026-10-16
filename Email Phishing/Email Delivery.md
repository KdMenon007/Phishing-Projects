
---

## 🏁 Protocol Roles in Email Transmission

|Protocol|What It Does|Direction|Used For|
|---|---|---|---|
|**SMTP**|Sends messages|Outgoing|From sender’s client to the recipient’s mail server|
|**POP3**|Downloads messages|Incoming|Client pulls email off server (and usually deletes from server)|
|**IMAP**|Syncs messages|Incoming|Client reads/syncs email from server (email stays on server)|

---
![[AI Tools & Notes/Screenshot/Screenshot 3/email-network-flow-4.png]]

## 📬 Email Transmission Workflow 

1. **Compose & Send**  
    Alexa hits _SEND_ in her email client (like Thunderbird, Outlook, or even Gmail’s web UI).  
    🔁 Enters: **SMTP**
    
2. **Domain Lookup (DNS Query)**  
    SMTP doesn’t just guess where to send it. It asks the **DNS server**:
    
    > “Hey, where’s the mail server for `johndoe.com`?”  
    > 📡 DNS replies: “MX record here, chief.”
    
3. **Transfer Across the Internet**  
    Now SMTP _relays_ the message to `johndoe.com`'s SMTP server.  
    (It may bounce around a few relays depending on security, SPF/DKIM checks, or spam filters.)
    
4. **Email Lands**  
    The message reaches Billy’s mailbox and chills on the **IMAP or POP3** server until Billy checks his mail.
    
5. **Inbox Refresh Time**  
    Billy’s email client connects using either:
    
    - **IMAP** if he’s modern and likes syncing across devices.
        
    - **POP3** if he lives like it’s 2003 and wants it downloaded once-and-done.
        

---

## 📡 Default & Recommended Ports (Because Firewalls Are Watching)

|Protocol|Default Port|Secure Port (TLS/SSL)|
|---|---|---|
|**SMTP**|25 (default)|465 (SSL) / 587 (TLS - recommended)|
|**POP3**|110|995 (SSL)|
|**IMAP**|143|993 (SSL)|

> **Pro Tip for Security Analysts:** If you see unencrypted traffic on 25/110/143 these days, that’s usually sus or legacy. Always prefer encrypted channels.

---

## 🧠 Analogy Time (For the Boomers _and_ Zoomers)

> **SMTP** is the mail truck.  
> **IMAP** is the cloud inbox you can check from anywhere.  
> **POP3** is that dusty old mailbox at your childhood home that deletes mail after you read it once.

---

