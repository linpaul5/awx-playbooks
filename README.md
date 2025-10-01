# AWX VLAN Change Playbook

This playbook changes a Cisco router interface from VLAN 20 to VLAN 10.

## Files in this directory:

- **change_vlan.yml** - Main playbook to change interface VLAN
- **requirements.yml** - Required Ansible collections (cisco.ios)
- **README.md** - This file

## Quick Setup Guide

### Step 1: Create Git Repository (Optional but Recommended)

```bash
cd awx-vlan-change
git init
git add .
git commit -m "Initial commit - VLAN change playbook"
```

Then push to your Git hosting service (GitHub, GitLab, etc.)

### Step 2: Configure AWX

#### A. Create Credentials (if not already done)

1. Go to **Resources → Credentials** in AWX
2. Click **Add**
3. Create a **Machine Credential**:
   - Name: `Router SSH Credential`
   - Credential Type: `Machine`
   - Username: Your router username
   - Password: Your router password
   - Privilege Escalation Method: `enable`
   - Privilege Escalation Password: Your enable password

#### B. Create Project

1. Go to **Resources → Projects** in AWX
2. Click **Add**
3. Fill in:
   - Name: `Network VLAN Management`
   - Organization: `ABC`
   - SCM Type: `Git` (or `Manual` if using local files)
   - SCM URL: Your Git repository URL (e.g., `https://github.com/yourusername/awx-vlan-change.git`)
   - SCM Update Options: Check "Update Revision on Launch"
4. Click **Save**

#### C. Create Job Template

1. Go to **Resources → Templates** in AWX
2. Click **Add → Job Template**
3. Fill in:
   - Name: `Change Interface VLAN 20 to 10`
   - Job Type: `Run`
   - Inventory: `Home Network`
   - Project: `Network VLAN Management`
   - Playbook: `change_vlan.yml`
   - Credentials: Select your `Router SSH Credential`
   - Enable Privilege Escalation: `Yes`
4. Click **Save**

### Step 3: Run the Job

1. Go to **Resources → Templates**
2. Find your template `Change Interface VLAN 20 to 10`
3. Click the **Launch** button (rocket icon)
4. Monitor the job execution

## Customization

### Change Interface or VLANs

Edit the `vars` section in `change_vlan.yml`:

```yaml
vars:
  interface_name: "GigabitEthernet0/1/2"  # Change interface here
  old_vlan: 20                             # Current VLAN
  new_vlan: 10                             # New VLAN
```

### For Trunk Ports

If your interface is a trunk port instead of access port, modify the configuration task:

```yaml
- name: Configure interface with new VLAN
  cisco.ios.ios_config:
    lines:
      - "switchport trunk allowed vlan {{ new_vlan }}"
    parents: "interface {{ interface_name }}"
    save_when: modified
```

## Troubleshooting

### Collection Not Found Error

If you get "cisco.ios collection not found", ensure:
1. The `requirements.yml` file is in your project
2. AWX has internet access to download collections
3. Or manually install: `ansible-galaxy collection install cisco.ios`

### Authentication Failed

1. Verify credentials in AWX
2. Test SSH access manually: `ssh username@192.168.0.1`
3. Ensure enable password is correct

### Connection Timeout

1. Verify router IP: `192.168.0.1`
2. Check network connectivity
3. Verify SSH is enabled on router: `show ip ssh`

## What This Playbook Does

1. ✓ Connects to the router via SSH
2. ✓ Displays current interface configuration
3. ✓ Changes VLAN from 20 to 10
4. ✓ Saves the configuration automatically
5. ✓ Verifies the change was successful
6. ✓ Shows before/after configuration

## Manual Execution (Outside AWX)

If you want to test locally:

```bash
ansible-playbook -i inventory.ini change_vlan.yml
```

Create an `inventory.ini` file:

```ini
[routers]
router ansible_host=192.168.0.1

[routers:vars]
ansible_network_os=cisco.ios.ios
ansible_connection=network_cli
ansible_user=admin
ansible_password=your_password
ansible_become=yes
ansible_become_method=enable
ansible_become_password=your_enable_password
```

## Support

Created for AWX/Ansible Automation Platform
- Ansible Core: 2.14+
- Python: 3.9+
- cisco.ios collection: 5.0.0+
