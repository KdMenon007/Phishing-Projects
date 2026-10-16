
---

## 🎭 1. The Sender’s Email Address: The Mask

This is your **first impression**, so it better be dressed to kill.

### 🎯 Goal:

Make it look like it came from someone **the victim knows or trusts**. You want them thinking:

> “Oh hey, that’s from my boss, my bank, or that weird but friendly IT guy.”

### 🧠 How You Find Who They Trust (Enter OSINT):

You stalk. Gently. Like a digital ninja.

- **Social Media** – Who are they tagging? Complaining about? Thanking?
    
- **Google Footprints** – Old reviews or blog comments can reveal favorite restaurants, vendors, or tools.
    
- **Business Website** – Suppliers, partners, or even press contacts.
    
- **LinkedIn** – Their coworkers, boss, HR rep—people worth impersonating.
    

### 🔥 Example:

Victim talks about their love for “Acme Coffee” on Twitter? Register `acmecoffee-orders.com` and send them a “Free coffee sample” email. Boom—trust earned.

---

## 🧨 2. The Subject Line: The Clickbait Hook

This is your attention grabber. You want to trigger **emotions**: panic, urgency, curiosity, FOMO.

> If your subject doesn’t make them pause mid-scroll and go “Wait, what?”, then it’s trash.

### 💣 Killer Subject Line Examples:

- ❗**Your account has been compromised.**
    
- 📦 **Your package has shipped – tracking enclosed.**
    
- 🤑 **Payroll data – strictly internal (DO NOT FORWARD).**
    
- 😳 **Your private photos were published.**
    

Short. Punchy. Stress-inducing. Just like a horror movie trailer.

---

## 🧬 3. The Email Content: The Body Count

This is where you close the deal. The **content has to match the disguise**.

> Imagine sending a fake Microsoft email that looks like it was typed by your 6-year-old cousin. Insta-suspicion. Game over.

### 🎨 What Makes It Convincing?

- Use **logos, fonts, colors** that match the real brand (grab templates or screenshots).
    
- Mimic their **writing style** – how formal/casual are they?
    
- Add **email signatures** with real-looking job titles, phone numbers, or LinkedIn links.
    
- Use **nicknames or signoffs** they actually use (from OSINT).
    

#### Example:

If Dorothy always signs her emails as “Dot” and uses “Cheers” instead of “Regards,” your spoof better say:

> Cheers,  
> Dot

These subtle cues hit the **subconscious trust triggers** in your target’s brain.

---

## 🕸 Link Cloaking: The Trap is Set

If you’re linking to a **malicious or spoofed site**, never just show the real sketchy URL. You want the **text to look clean and familiar**, even though it redirects to doom.

### 💀 Example:

```html
<a href="http://badguysite.thm">Click Here</a>
<a href="http://badguysite.thm">https://secure.payroll.com</a>
```

So the victim thinks:

> “Oh cool, it’s just payroll stuff. Looks normal.”

Click. Owned.

---

