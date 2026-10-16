
---

### **1. What Wireshark filter can you use to narrow down the packet output using SMTP status codes?**

In **Wireshark**, you can filter the output to display only SMTP traffic with status codes by using the following filter:

```
smtp.response.code
```

This will show all packets where an SMTP response code is present. You can further narrow it down by specifying a particular status code, for example:

```
smtp.response.code == 220
```

This filter would show only packets with the **220** SMTP response code.

---

### **2. What was the text description for status code 220?**

The **220** SMTP status code indicates the server is ready to receive a request. The full description of this code is typically:

**Service ready (domain ready)**

It's the server's greeting message, indicating that the SMTP server is ready to accept commands.

---

### **3. One packet shows a response that an email was blocked using spamhaus.org. What were the packet number and status code?**

To find the packet number and the status code for this response:

- Use the filter for SMTP traffic (`smtp`) and look for the response related to spamhaus.org.
    
- When you find the specific response indicating the email was blocked, note the packet number (in Wireshark's packet list) and the corresponding SMTP status code.
    

The status code would likely be **550** (Mailbox unavailable, as a common error when emails are blocked due to spam lists or blacklists).

Example filter:

```
smtp.response.code == 550
```

Once you find the matching packet, note the **packet number** and **status code**.

---

### **4. Based on the packet from the previous question, what was the message regarding the mailbox?**

For SMTP code **550**, the message is usually along the lines of:

**Requested mail action not taken: mailbox unavailable** (often associated with spam filtering or invalid email addresses).

---

### **5. What is the status code that will typically precede an SMTP DATA command?**

Before an SMTP **DATA** command is issued, the status code that typically precedes it is:

**354**: "Start mail input; end with ."

This indicates that the mail server is ready to receive the actual message content after the DATA command is issued.

---

### **6. What port is the SMTP traffic using?**

SMTP typically operates on **port 25** for sending email (non-secure). However, in secure connections, it could also use **port 465** (for SMTPS) or **port 587** (for submission).

To confirm this, check the **destination port** in the packets related to SMTP. Use this filter in Wireshark to see the destination port:

```
smtp
```

Or check specifically for the port with a filter like:

```
tcp.port == 25
```

---

### **7. How many packets are specifically SMTP?**

To count how many packets are SMTP, you can use the following Wireshark display filter:

```
smtp
```

Wireshark will then display only the SMTP packets. To count them, look at the number of matching packets at the bottom of the window.

---

### **8. What is the source IP address for all the SMTP traffic?**

The source IP address for SMTP traffic can be found by filtering SMTP traffic and looking at the IP header of the first packet. You can use the filter:

```
smtp
```

Then look at the **Source** IP address in the **Packet Details** pane. It will typically be listed under the **Internet Protocol** section.

---

### **9. What is the filename of the third file attachment?**

To find the filename of an attachment, look for the SMTP **DATA** command and the following multipart message that contains the file. The filenames are typically within the **Content-Disposition** header.

Use the **Wireshark** display filter to search for attachments:

```
smtp.data
```

Then, scroll through the data and look for the **Content-Disposition** header for each attachment. The filename will be listed there.

---

### **10. How about the last file attachment?**

For the last file attachment, use the same method to locate the **Content-Disposition** header for attachments in the **DATA** command. Look for the final entry in the email and check the corresponding filename.

---

### Summary of Filters & Methods:

- **Wireshark Filter for SMTP Responses**: `smtp.response.code`
    
- **Filter for SMTP Traffic**: `smtp`
    
- **Filter for TCP Port**: `tcp.port == 25` (or other relevant ports like 465 or 587)
    
- **Filter for SMTP Data**: `smtp.data`
    

