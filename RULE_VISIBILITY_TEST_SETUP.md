# Rule Visibility Test Setup in AWX

## Purpose
This playbook will help us determine exactly what's happening with rule creation:
- Lists existing rules before creation
- Creates a very obvious test rule named "AWX-VISIBILITY-TEST" 
- Commits the configuration
- Lists rules after creation to verify it exists in the API
- Checks virtual system configuration
- Provides detailed debugging information

## AWX Template Setup

### Template Configuration
- **Name**: `Rule Visibility Test`
- **Job Type**: `Run`
- **Inventory**: `Demo Inventory`
- **Project**: `Palo Alto Playbooks`
- **Execution Environment**: `AWX EE (latest)`
- **Playbook**: `rule_visibility_test.yml`
- **Credentials**: (leave empty)
- **Variables**: (leave empty)

### Settings
- ☐ **Prompt on launch**: NOT needed (no variables required)
- ☐ **Enable Privilege Escalation**: NOT needed
- ☐ **Allow Simultaneous**: Can be unchecked

## What This Test Will Tell Us

### If the test rule appears in the API response but NOT in GUI:
- **Problem**: GUI display issue or rule location issue
- **Solution**: Check different rule sections (Pre/Post rules, different virtual systems)

### If the test rule does NOT appear in the API response:
- **Problem**: Rule creation is failing silently or being overwritten
- **Solution**: Check API permissions, rule conflicts, or validation errors

### If we see virtual system issues:
- **Problem**: Rules being created in wrong virtual system context
- **Solution**: Modify rule creation to specify correct virtual system

## Expected Output
The playbook will show:
1. Number of existing rules before creation
2. Rule creation API response and status
3. Commit result and status  
4. Number of rules after creation
5. Whether our test rule "AWX-VISIBILITY-TEST" exists in the API
6. List of all rule names in the system
7. Virtual system configuration

## After Running This Test
1. **Check AWX job output** for detailed information
2. **Refresh Palo Alto GUI** and look for rule named "AWX-VISIBILITY-TEST"
3. **Check all rule sections**: Pre Rules, Post Rules, Intrazone
4. **Note the rule count** - it should increase by 1 if successful

## Cleanup
If the test rule is created successfully, you can delete it later by:
- Finding "AWX-VISIBILITY-TEST" in the Palo Alto GUI and deleting it, OR
- Running a cleanup playbook to remove it via API