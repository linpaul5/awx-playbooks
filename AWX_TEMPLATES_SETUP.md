# 🎯 AWX Job Templates Setup Guide
## Palo Alto Security Rule Automation

### 📋 Prerequisites Checklist
Before creating job templates, ensure you have:
- ✅ AWX running at http://localhost:32237
- ✅ Project "Palo Alto Playbooks" synced with GitHub
- ✅ Inventory "Palo Alto Firewall" with host 192.168.0.100
- ✅ Execution Environment "AWX EE (latest)" - Default working environment
- ✅ Credential "Palo Alto API Key" (if separate from playbook)

---

## 🚀 Job Template 1: Security Rule Management

### Template Configuration:
```
Name: Palo Alto - Deploy Security Rule
Description: Create, update, delete, or list Palo Alto security rules
Job Type: Run
Inventory: Palo Alto Firewall
Project: Palo Alto Playbooks
Execution Environment: AWX EE (latest)
Playbook: palo_alto_security_rules.yml
Prompt on Launch: ✅ Extra Variables
```

### Extra Variables Examples:

#### Create Allow Rule:
```yaml
rule_action: "create"
rule_name: "Allow-Web-Browsing"
rule_description: "Permit standard web traffic from internal network"
source_zones: ["trust"]
destination_zones: ["untrust"]
source_addresses: ["192.168.0.0/24"]  # Your actual network range
applications: ["web-browsing", "ssl"]
action_type: "allow"
```

#### Simple Allow Rule (Any Source):
```yaml
rule_action: "create"
rule_name: "Allow-Web-Any-Source"
rule_description: "Allow web browsing from any source"
source_zones: ["trust"]
destination_zones: ["untrust"]
source_addresses: ["any"]  # Simpler - allows from anywhere
applications: ["web-browsing", "ssl"]
action_type: "allow"
```

#### Create Deny Rule:
```yaml
rule_action: "create"
rule_name: "Block-Social-Media"
rule_description: "Block access to social media platforms"
applications: ["facebook", "twitter", "instagram", "youtube"]
action_type: "deny"
```

#### List All Rules:
```yaml
rule_action: "list"
```

#### Delete Rule:
```yaml
rule_action: "delete"
rule_name: "Rule-To-Remove"
```

---

## 🎮 Job Template 2: Demonstration Scenarios

### Template Configuration:
```
Name: Palo Alto - Rule Demo
Description: Deploy demonstration security rules (Web Allow + Social Block)
Job Type: Run
Inventory: Palo Alto Firewall
Project: Palo Alto Playbooks
Execution Environment: AWX EE (latest)
Playbook: palo_alto_rule_demo.yml
Prompt on Launch: ❌ (No variables needed)
```

**What it does:**
- Creates "AWX-Demo-Web-Allow" rule (permits web browsing)
- Creates "AWX-Demo-Block-Social" rule (blocks social media)
- Lists all current rules
- Shows complete automation workflow

---

## 🧹 Job Template 3: Environment Cleanup

### Template Configuration:
```
Name: Palo Alto - Cleanup Demo Rules
Description: Remove all demonstration rules from firewall
Job Type: Run
Inventory: Palo Alto Firewall
Project: Palo Alto Playbooks
Execution Environment: AWX EE (latest)
Playbook: palo_alto_cleanup.yml
Prompt on Launch: ❌ (No variables needed)
```

**What it does:**
- Removes all AWX demo rules
- Commits changes automatically
- Resets environment for new tests

---

## 🎯 Step-by-Step Creation Process

### Step 1: Access AWX
1. Open browser: http://localhost:32237
2. Login with your AWX credentials
3. Navigate to **Templates** → **Job Templates**

### Step 2: Create Template 1 (Security Rule Management)
1. Click **"+ Add"** → **Job Template**
2. Fill in the configuration above
3. **Important**: Enable "Prompt on launch" for Extra Variables
4. Save the template

### Step 3: Create Template 2 (Demo)
1. Click **"+ Add"** → **Job Template**
2. Fill in the demo configuration
3. No extra variables needed
4. Save the template

### Step 4: Create Template 3 (Cleanup)
1. Click **"+ Add"** → **Job Template**
2. Fill in the cleanup configuration  
3. No extra variables needed
4. Save the template

---

## 🧪 Testing Your Templates

### Test Sequence:
1. **Run "Palo Alto - Rule Demo"** first
   - Should create 2 demo rules successfully
   - Check Palo Alto GUI to see new rules

2. **Run "Palo Alto - Deploy Security Rule"** with list action
   ```yaml
   rule_action: "list"
   ```
   - Should show all current rules including demos

3. **Run "Palo Alto - Deploy Security Rule"** with custom rule
   ```yaml
   rule_action: "create"
   rule_name: "My-Custom-Rule" 
   rule_description: "My first custom AWX rule"
   applications: ["ping"]
   action_type: "allow"
   ```

4. **Run "Palo Alto - Cleanup Demo Rules"**
   - Should remove all demo rules
   - Your custom rule should remain

---

## 📊 Job Template Summary

| Template Name | Playbook | Variables | Purpose |
|---------------|----------|-----------|---------|
| Deploy Security Rule | `palo_alto_security_rules.yml` | Required | Production rule management |
| Rule Demo | `palo_alto_rule_demo.yml` | None | Show capabilities |
| Cleanup Demo Rules | `palo_alto_cleanup.yml` | None | Environment reset |

---

## 🎮 Advanced Usage Examples

### Bulk Rule Creation
Run "Deploy Security Rule" multiple times with different variables:

```yaml
# Rule 1: Email Access
rule_action: "create"
rule_name: "Allow-Email-Services"
source_addresses: ["192.168.1.0/24"]
destination_addresses: ["mail.company.com"]
services: ["tcp-25", "tcp-993", "tcp-443"]
action_type: "allow"
```

```yaml
# Rule 2: Database Access
rule_action: "create"
rule_name: "Allow-Database-Access"
source_addresses: ["192.168.2.0/24"] 
destination_addresses: ["db.company.com"]
services: ["tcp-3306", "tcp-5432"]
action_type: "allow"
```

### Emergency Blocking
```yaml
rule_action: "create"
rule_name: "Emergency-Block-Malicious-IP"
rule_description: "Block malicious IP - Incident Response"
source_addresses: ["1.2.3.4"]
destination_addresses: ["any"]
action_type: "deny"
```

---

## 🔧 Troubleshooting

### Common Issues:
1. **Template not found**: Ensure project sync completed
2. **Execution Environment error**: Verify awx-palo-ee:latest exists
3. **API authentication failed**: Check API key in playbook
4. **Rule creation failed**: Verify zone names and applications exist

### Debug Mode:
Add to Extra Variables:
```yaml
debug_mode: true
ansible_verbosity: 2
```

---

## 🎉 Success Criteria

After setup, you should be able to:
- ✅ Create security rules through AWX interface
- ✅ Delete rules with one click  
- ✅ Run demonstrations for stakeholders
- ✅ Clean up test environments automatically
- ✅ Deploy production rules with confidence

**Your AWX is now a professional firewall management platform!** 🚀