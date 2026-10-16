
---

## 🎯 **Email, Phishing & Why We Care**

- **Spam** = Annoying junk email.
    
- **Phishing** = Looks legit, but it's tricking someone into clicking / opening / giving away credentials.
    
- **One careless click** from one clueless user → _Congrats, attacker now has a foothold in your network._
    

Even with all the fancy security layers, **humans are still the weakest link**.  
Welcome to cybersecurity. :)

---

## 📬 **What Makes an Email Address**

Example: `billy@johndoe.com`

- **billy** → Mailbox (user)
    
- **@** → Separator (shout-out to Ray Tomlinson, the OG)
    
- **johndoe.com** → Domain (like the street name)
    

Think "mail delivery but digital." The domain is the neighborhood. The username is the house.

---

## 🚚 **How Email Travels (Oversimplified but Accurate)**

1. Sender writes email → hits **Send**.
    
2. **SMTP** server checks **DNS** to find recipient’s mail server.
    
3. Email is routed across the internet → arrives at recipient’s SMTP server.
    
4. **POP3/IMAP** lets the recipient actually view/download the message.
    

### Protocol Cheat Sheet:

|Protocol|Purpose|Default Ports|Notes|
|---|---|---|---|
|**SMTP**|Sends emails|25 / 465 / 587|Sending only|
|**POP3**|Downloads email to one device|110 / 995|Local storage|
|**IMAP**|Syncs email across devices|143 / 993|Server storage|

---

## 🧠 **Email Has Two Parts**

|Part|Meaning|
|---|---|
|**Header**|Technical info (sender, servers, routing)|
|**Body**|The actual message / text / HTML / images / attachments|

To investigate email threats → **You will always check headers**.

---

## 🔍 **Key Header Fields to Pay Attention To**

|Header Field|Why It Matters|
|---|---|
|**From:**|Who the email _claims_ to be from|
|**Reply-To:**|Where replies _actually_ go (popular scam trick)|
|**X-Originating-IP:**|Real IP of the sender|
|**Authentication Results (SPF/DKIM/DMARC):**|Tells if the email server was legit or spoofed|

---

## 🧱 **Phishing Red Flags**

Look for these — they show up _constantly_:

- Fake or spoofed sender names
    
- Sketchy urgency (“Your account will be suspended in 12 minutes!!!”)
    
- Generic greetings (no personalization)
    
- Weird grammar / formatting
    
- Links that redirect / shortened URLs
    
- Attachments claiming to be invoices, resumes, FedEx packages, etc.
    

---

## 🪤 **Types of Malicious Emails**

|Type|Who It's Targeting|Goal|
|---|---|---|
|**Spam**|Everyone|Annoy / advertise|
|**MalSpam**|Everyone|Install malware|
|**Phishing**|Many|Steal credentials|
|**Spear Phishing**|Specific people|Targeted data theft|
|**Whaling**|Executives|$$$ or access|
|**Smishing**|SMS|Mobile phishing|
|**Vishing**|Voice calls|Human manipulation|

---

## 🧯 Safety Tip: **Always Defang Links**

To safely share suspicious links:  
`http://badsite.com` → `hxxp[:]//badsite[.]com`

CyberChef makes this easy. Use it. Don’t raw-dog URLs.

---

## In short:

- **Emails are simple on the surface but full of forensic clues.**
    
- **Your job as a defender is to read those clues before users do something regrettable.**
    
- **Phishing works because humans are humans.**  
    No tool completely fixes that.
    

---

