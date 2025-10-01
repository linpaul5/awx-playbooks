# AWX Playbooks

Collection of Ansible playbooks for AWX automation.

## Playbooks

### change_vlan.yml
Changes router interface VLAN configuration.

**Target:** GigabitEthernet0/1/2  
**Change:** VLAN 20 → VLAN 10

**Customization:**
Edit the `vars` section to change interface or VLANs:
```yaml
vars:
  interface_name: "GigabitEthernet0/1/2"
  old_vlan: 20
  new_vlan: 10
```

## Requirements
See `requirements.yml` for Ansible collection dependencies.

## Usage in AWX
1. Create project pointing to this repository
2. Create job template using the desired playbook
3. Run with appropriate inventory and credentials
