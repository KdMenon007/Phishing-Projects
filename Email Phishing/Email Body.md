
---

## ✍️ Email Body: The Candy-Coated Shell of Deception

There are two main body formats:

### 1. **Plain Text Emails**

- Simple, old-school, no flair.
    
- No images, links, or fancy formatting.
    
- Used less in phishing because it lacks visual trickery.
    

**Example:**

```
Hi John,

Please review the attached invoice.

Regards,
“HR Dept”
```

This is the email version of a handwritten ransom note — basic, but still potentially dangerous.

---

### 2. **HTML Emails** (aka ✨The Playground of Trickery✨)

This is where attackers stretch their creative muscles.

- Embedded images (sometimes from external URLs)
    
- Hyperlinks masked with legit-looking anchor text (e.g., `click here`)
    
- Spoofed branding/logos
    
- Invisible text (white-on-white for SEO/spam-bypass)
    
- Fake "Unsubscribe" links (which track if you're active)
    

**Example HTML snippet:**

```html
<a href="http://malicious.badguy.cn/stealyourstuff">
  Click here to view your Netflix bill
</a>
```

Yikes. Always inspect those `<a href>` targets. Just because the link _says_ `netflix.com` doesn't mean it's going there.

---

## 📎 Attachments: Email's Trojan Horses

Attachments are common payload delivery mechanisms — macros, droppers, malicious PDFs, weaponized Excel sheets with _surprises_ inside.

When analyzing them from the **source code**, keep an eye on these headers:

|Header Field|Meaning|
|---|---|
|`Content-Type:`|Describes the MIME type (e.g., `application/pdf`, `application/vnd.ms-excel`)|
|`Content-Disposition:`|`inline` or `attachment` (tells how it should be handled)|
|`Content-Transfer-Encoding:`|Often `base64` for binary attachments — decode this to extract|

> 💡 Base64 chunks can be _massive_. Use `base64 -d` or CyberChef to decode it, but _do not open the resulting file casually_ — sandbox it first.

---

## 🔥 Practical Tips for Email Body Analysis

- ✅ Always toggle to raw source if possible.
    
- 🕵️‍♂️ Compare anchor text to actual `href` values.
    
- 🧠 Watch for **invisible links**, CSS trickery, or right-to-left override (RTL) attacks in filenames.
    
- 📎 Dump base64 attachments in a sandbox. Don’t trust `.pdf`, `.doc`, or even `.html`.
    

---
