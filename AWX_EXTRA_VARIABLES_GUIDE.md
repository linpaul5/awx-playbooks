# 🎯 AWX Extra Variables - Visual Guide

## 📍 **EXACTLY Where to Put Extra Variables**

### **Step 1: Open Your Job Template**
```
AWX Dashboard → Templates → Job Templates → "Palo Alto - Deploy Security Rule"
```

### **Step 2: Launch the Job**
```
Click the 🚀 Launch button (rocket icon on the right)
```

### **Step 3: Extra Variables Dialog**
AWX will show a popup with a text box labeled **"Extra Variables"**

**PASTE YOUR VARIABLES HERE:**
```yaml
rule_action: "create"
rule_name: "My-First-Rule"
rule_description: "Created through AWX automation"
source_zones: ["trust"]
destination_zones: ["untrust"]  
source_addresses: ["any"]
applications: ["web-browsing", "ssl"]
action_type: "allow"
```

### **Step 4: Click Launch**
AWX will run your playbook with these variables!

---

## 🌐 **Source Address Examples for YOUR Network**

### **Your Palo Alto VM Network Context:**
- Palo Alto VM IP: **192.168.0.100**
- Your network is likely: **192.168.0.x**

### **✅ Recommended Source Addresses:**

#### **1. Allow from Your Entire Local Network:**
```yaml
source_addresses: ["192.168.0.0/24"]
```
**What this means:** Any device on 192.168.0.1 through 192.168.0.254

#### **2. Allow from Anywhere (Simplest):**
```yaml
source_addresses: ["any"]
```
**What this means:** Any source IP address

#### **3. Allow from Specific Device:**
```yaml
source_addresses: ["192.168.0.50"]
```
**What this means:** Only from that specific IP

#### **4. Allow from Multiple Networks:**
```yaml
source_addresses: ["192.168.0.0/24", "10.0.0.0/8", "172.16.0.0/12"]
```
**What this means:** Multiple network ranges

---

## 🎮 **Ready-to-Use Variable Sets**

### **🌐 Basic Web Allow Rule (Your Network):**
```yaml
rule_action: "create"
rule_name: "Allow-Web-Local-Network"
rule_description: "Allow web browsing from local network"
source_zones: ["trust"]
destination_zones: ["untrust"]
source_addresses: ["192.168.0.0/24"]  # YOUR network
applications: ["web-browsing", "ssl"]
action_type: "allow"
```

### **🚫 Block Social Media (Any Source):**
```yaml
rule_action: "create"
rule_name: "Block-Social-Media"
rule_description: "Block social media access"
source_addresses: ["any"]
applications: ["facebook", "twitter", "instagram"]
action_type: "deny"
```

### **📋 List All Current Rules:**
```yaml
rule_action: "list"
```

### **🗑️ Delete a Specific Rule:**
```yaml
rule_action: "delete"
rule_name: "Rule-Name-To-Delete"
```

---

## 🎯 **Pro Tips:**

### **✅ DO:**
- Use `["any"]` for simplicity when testing
- Use your actual network range `192.168.0.0/24`
- Start with simple rules first
- Use descriptive rule names

### **❌ DON'T:**
- Use random IP ranges like `192.168.1.0/24` unless that's actually your network
- Forget quotes around values
- Use spaces in rule names (use hyphens instead)

---

## 🚀 **Quick Test Sequence:**

1. **First Test - Simple Web Rule:**
   ```yaml
   rule_action: "create"
   rule_name: "Test-Web-Allow"
   source_addresses: ["any"]
   applications: ["web-browsing"]
   action_type: "allow"
   ```

2. **Check if it worked:**
   ```yaml
   rule_action: "list"
   ```

3. **Clean up:**
   ```yaml
   rule_action: "delete"
   rule_name: "Test-Web-Allow"
   ```

**Now you know exactly where to put variables and why we use specific IP ranges!** 🎉