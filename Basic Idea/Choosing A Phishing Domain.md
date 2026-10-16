
---

## 🎯 Choosing the Right Phishing Domain

### ✅ 1. **Expired Domains (With History)**

- Domains with _existing reputations_ are _less likely to get flagged_ by spam filters.
    
- Use tools like:
    
    - [Expireddomains.net](https://www.expireddomains.net/)
        
    - [Domain Hunter Gatherer](https://domainhuntergatherer.com/)
        

💡 **Pro Tip:** Look for domains in a similar industry or that have old backlinks—Google juice matters.

---

### ✅ 2. **Typosquatting Techniques**

Psychology meets typography. Here’s your cheat sheet:

|**Method**|**Example**|**Notes**|
|---|---|---|
|Misspelling|`goggle.com`|Easy mistake—visual similarity|
|Extra Period|`go.ogle.com`|Subdomain spoofing|
|Number-for-Letter|`g00gle.com`|Leetspeak confusion|
|Phrasing|`googles.com`|Slight plural or variation|
|Additional Word|`googlesupport.com`|Looks legit in context|

🧠 **Cognitive bias in action:** Users _read what they expect to see_, not what’s actually there. Exploit that.

---

### ✅ 3. **TLD Swapping**

A classic move:

- `tryhackme.co.uk` instead of `tryhackme.com`
    
- Works especially well when:
    
    - The real org uses a .com
        
    - You pick something _regionally relevant_ to the victim (like `.ca`, `.de`, `.tech`, etc.)
        

---

### ✅ 4. **IDN Homograph Attacks**

This is next-level sneakiness. You exploit characters from **non-Latin scripts** that _look like Latin characters_.

#### For Example:

- Latin lowercase “**a**” → Unicode `U+0061`
    
- Cyrillic lowercase “**а**” → Unicode `U+0430`
    

They look _identical_ to the human eye but are completely different characters. With this, you could register:

> **[www.pаypal.com](http://www.xn--pypal-4ve.com/)** ← (Cyrillic "а", not Latin)

It’ll look **pixel-perfect**, but it’s totally evil.

---

### 🔍 Diagram Description: Latin "a" vs Cyrillic "a"

**Visual:** Side-by-side of the two “a” characters, identical in appearance.

|**Character Type**|**Glyph**|**Unicode Code**|**Font Render**|
|---|---|---|---|
|Latin Small 'a'|**a**|`U+0061`|_Looks normal_|
|Cyrillic Small 'а'|**а**|`U+0430`|_Identical-looking_|

But under the hood, they're different beasts.

> Want me to _generate this diagram for real_ so you can use it in a report or presentation?

---

### 🛠️ Tools to Detect or Exploit Homograph Attacks:

- [Punycode Converter](https://www.punycoder.com/)
    
- `whois` tools with Unicode decoding
    
- Look for “xn--” in URLs—that's how IDNs appear under the hood
    

---

### 🔒 Defender's Angle

- **Browsers like Chrome and Firefox** now block many homoglyph domains automatically, but not always.
    
- Domain registrars like Namecheap & GoDaddy are working on this, but it's a cat-and-mouse game.
    

---

