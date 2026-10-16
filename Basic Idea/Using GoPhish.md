
---

### 🔑 **STEP 1: Log in to GoPhish**

- Visit: `https://LAB_WEB_URL.p.thmlabs.com:8443` or `https://MACHINE_IP:8443`
    
- Username: `admin`
    
- Password: `tryhackme`
    

Now you’re in the command center. Let’s gear up.

---

### 📤 **STEP 2: Configure Sending Profile**

> This tells GoPhish where to send the emails from.

1. Click **Sending Profiles** > **New Profile**
    
2. Fill out:
    
    - **Name**: `Local Server`
        
    - **From**: `noreply@redteam.thm`
        
    - **Host**: `127.0.0.1:25`
        
3. Hit **Save Profile**
    

---

### 🌐 **STEP 3: Create the Landing Page**

> This is your fake login page—where the user unknowingly spills their secrets.

1. Go to **Landing Pages** > **New Page**
    
2. **Name**: `ACME Login`
    
3. Click **Source** and paste in this HTML:
    

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ACME IT SUPPORT - Admin Panel</title>
    <style>
        body { font-family: "Ubuntu", monospace; text-align: center }
        div.login-form { margin:auto; width:300px; border:1px solid #ececec; padding:10px;text-align: left;font-size:13px;}
        div.login-form div input { margin-bottom:7px;}
        div.login-form input { width:280px;}
        div.login-form div:last-child { text-align: center; }
        div.login-form div:last-child input { width:100px;}
    </style>
</head>
<body>
    <h2>ACME IT SUPPORT</h2>
    <h3>Admin Panel</h3>
    <form method="post">
        <div class="login-form">
            <div>Username:</div>
            <div><input name="username"></div>
            <div>Password:</div>
            <div><input type="password" name="password"></div>
            <div><input type="submit" value="Login"></div>
        </div>
    </form>
</body>
</html>
```

4. Click **Source** again to preview it.
    
5. Tick:
    
    - ✅ **Capture Submitted Data**
        
    - ✅ **Capture Passwords**
        
6. Save the page.
    

---

### 📧 **STEP 4: Create the Email Template**

> The bait that lures the user in—this needs to look click-worthy.

1. Click **Email Templates** > **New Template**
    
2. **Name**: `Email 1`
    
3. **Subject**: `New Message Received`
    
4. Click **HTML** tab > then **Source**
    
5. Write your email body. Here’s a sample:
    

```html
<p>Hi,</p>
<p>You have received a new secure message. Please <a href="{{.URL}}">https://admin.acmeitsupport.thm</a> to view your message.</p>
<p>Best regards,<br>ACME IT Support Team</p>
```

- Highlight the link text and use the **link icon** to assign `{{.URL}}` as the real URL.
    
- Set the **protocol** to `<other>` during this.
    

6. Save the template.
    

---

### 👥 **STEP 5: Create the Target Group**

> Who are we sending this to? The “victims.”

1. Go to **Users & Groups** > **New Group**
    
2. **Name**: `Targets`
    
3. Add:
    
    - `martin@acmeitsupport.thm`
        
    - `brian@acmeitsupport.thm`
        
    - `accounts@acmeitsupport.thm`
        
4. Save.
    

---

### 🚀 **STEP 6: Launch the Campaign**

> Lights, camera, **phish**.

1. Click **Campaigns** > **New Campaign**
    
2. Fill out:
    
    - **Name**: `Campaign One`
        
    - **Email Template**: `Email 1`
        
    - **Landing Page**: `ACME Login`
        
    - **URL**: `http://MACHINE_IP` (actual IP of your VM)
        
    - **Launch Date**: Set to _2 days ago_ (timezone bypass trick)
        
    - **Sending Profile**: `Local Server`
        
    - **Groups**: `Targets`
        
3. Hit **Launch Campaign**
    
4. Confirm with **Launch** button
    

Now GoPhish is doing its thing.

---

### 📊 **STEP 7: Analyze the Results**

This is your **feedback loop**, showing you:

- Who got the email
    
- Who opened it
    
- Who clicked the link
    
- Who submitted credentials
    

You’ll notice:

- **Martin**: Email sent
    
- **Brian**: Will show **Submitted Data** eventually
    
- **Accounts**: Error – user unknown
    

Click Brian’s row > **Details** > view **submitted data**—you’ll see the **username and password** he entered.

---
