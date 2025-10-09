# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Ansible playbook repository for managing Cisco network devices, specifically focused on AWX automation. The repository contains playbooks for configuring Cisco routers and switches, with emphasis on VLAN management tasks.

## Architecture

### Core Components

- **Ansible Playbooks**: YAML files defining network automation tasks
- **Cisco IOS Collection**: Uses `cisco.ios` collection (v5.0.0+) for network device management
- **Connection Method**: Uses `network_cli` connection type for Cisco device interaction
- **Target Devices**: Cisco ISR1100 series routers (specifically C1117-4PLTELA) with IOS version 17.15

### Network Environment

The playbooks are designed to work with:
- Cisco router hostname: `Cisco-TPG-NBN`
- Management network: 192.168.0.0/24 (VLAN 10)
- Test VLAN: VLAN 20
- SSH-based access with local authentication

## Key Files

- `change_vlan_gi0-1-2.yml`: Main playbook for changing interface VLAN assignments
- `requirements.yml`: Ansible Galaxy collection dependencies
- `Cisco-TPG-NBN.log`: Reference configuration output from target router

## Development Commands

### Installing Dependencies

```bash
ansible-galaxy collection install -r requirements.yml
```

### Running Playbooks

Execute a playbook against inventory:
```bash
ansible-playbook -i inventory.ini change_vlan_gi0-1-2.yml
```

Run with connection variables:
```bash
ansible-playbook -i inventory.ini change_vlan_gi0-1-2.yml \
  -e "ansible_user=<username>" \
  -e "ansible_password=<password>" \
  -e "ansible_network_os=ios"
```

### Testing Playbooks

Syntax check:
```bash
ansible-playbook --syntax-check change_vlan_gi0-1-2.yml
```

Dry run (check mode):
```bash
ansible-playbook -i inventory.ini change_vlan_gi0-1-2.yml --check
```

## Playbook Structure

The VLAN change playbook follows this pattern:

1. **Gather Facts**: Collect current interface configuration
2. **Display Current State**: Debug output for verification
3. **Apply Configuration**: Change VLAN assignment with automatic save
4. **Verify Changes**: Re-gather configuration and switchport status
5. **Assert Success**: Validate VLAN change completed successfully

## Important Patterns

### Variable Definition

Playbooks use variables for flexibility:
- `interface_name`: Target interface (e.g., "GigabitEthernet0/1/2")
- `old_vlan`: Current VLAN ID
- `new_vlan`: Desired VLAN ID

### Configuration Application

Uses `cisco.ios.ios_config` with:
- `lines`: Configuration commands
- `parents`: Interface context
- `save_when: modified`: Auto-save configuration changes

### Verification

Always includes verification tasks:
- `show running-config interface` for configuration
- `show interfaces switchport` for operational status
- Assertion checks to confirm changes

## Network Device Context

The target router (Cisco-TPG-NBN) configuration includes:
- Switch ports on Gi0/1/0 through Gi0/1/3
- VLAN 10: Primary LAN network (192.168.0.0/24)
- VLAN 20: Test/alternate VLAN
- SSH access restricted to LAN network via ACL_VTY_MGMT
- SNMP monitoring enabled for Grafana integration

## Security Considerations

- Playbooks should never contain credentials in plaintext
- Use Ansible Vault for sensitive data or AWX credential management
- SSH keys or username/password should be passed via extra vars or inventory
- All VTY access is restricted to 192.168.0.0/24 network on the target device
