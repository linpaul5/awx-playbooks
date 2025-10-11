# 🚨 AWX Job Troubleshooting Guide

## 🔍 **Current Issues Identified:**

### **Issue 1: Variables Not Being Passed**
```
"Rule Action: NOT SET"
"Rule Name: NOT SET" 
"Action Type: NOT SET"
```

### **Issue 2: HTTP 403 Authentication Error**
```
HTTP Error 403: API Error: Invalid Credentials
```

---

## 🛠️ **IMMEDIATE FIXES:**

### **Step 1: Fix Variable Passing in AWX**

#### **📋 Check Your Job Template Settings:**
1. **Go to Templates → Job Templates → "Palo Alto - Deploy Security Rule"**
2. **Click EDIT (pencil icon)**
3. **Scroll down to "OPTIONS" section**
4. **ENSURE these are checked:**
   - ✅ **"Prompt on launch"** under **Variables**
   - ✅ **"Ask variables on launch"** (if available)

#### **📋 When Launching the Job:**
1. **Click the 🚀 Launch button**
2. **You SHOULD see a dialog box with "Extra Variables" field**
3. **If NO dialog appears** → Your template is NOT configured to prompt for variables!

### **Step 2: Fix API Authentication**

#### **Option A: Generate New API Key**
```bash
# In your Palo Alto VM web interface:
# 1. Go to Device → API Key Management
# 2. Generate new key for admin user
# 3. Update the playbook with new key
```

#### **Option B: Use Direct Password Authentication**
The debug playbook will test both methods.

---

## 🧪 **TESTING PROCEDURE:**

### **Step 1: Update Job Template to Use Debug Playbook**
1. **Edit your job template**
2. **Change Playbook to:** `awx_debug_test.yml`
3. **Save**

### **Step 2: Test Variable Passing**
1. **Launch the job with these variables:**
   ```yaml
   rule_action: "test"
   rule_name: "Variable-Test"
   action_type: "allow"
   rule_description: "Testing if variables work"
   ```
2. **Check output** - should show "RECEIVED" instead of "NOT_PROVIDED"

### **Step 3: Check Results**
The debug playbook will tell you:
- ✅ **Variables**: Are they being passed from AWX?
- ✅ **Network**: Can we reach the Palo Alto VM?
- ✅ **Authentication**: Is the API key/password working?

---

## 🎯 **EXPECTED OUTCOMES:**

### **✅ SUCCESS Output Should Show:**
```
Variables from AWX: RECEIVED
Basic connectivity: OK  
API authentication: OK
```

### **❌ If Variables Still "NOT_PROVIDED":**
**Problem**: AWX template not configured properly
**Solution**: 
1. Edit job template
2. Enable "Prompt on launch" for Variables
3. Save and try again

### **❌ If Auth Still FAILED:**
**Problem**: API key expired or wrong password
**Solution**: 
1. Log into Palo Alto VM web interface
2. Generate new API key
3. Update playbook with new key

---

## 🚀 **QUICK FIX CHECKLIST:**

- [ ] Job template has "Prompt on launch" enabled for Variables
- [ ] Extra Variables dialog appears when launching job
- [ ] Palo Alto VM is running and accessible at 192.168.0.100
- [ ] Admin password is correct (Lin@226659)
- [ ] API key is valid and not expired

---

## 📞 **IMMEDIATE ACTION:**

1. **Run the debug playbook first** → `awx_debug_test.yml`
2. **Check the output** → Tells you exactly what's wrong
3. **Fix the identified issues** → Follow solutions above
4. **Re-test** → Should show all green checkmarks

**This will pinpoint exactly where the problem is!** 🎯