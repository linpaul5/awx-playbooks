# Simple Diagnostic Setup in AWX

## Quick Setup Instructions

1. **Go to AWX**: http://localhost:32237
2. **Navigate to**: Resources → Templates
3. **Click**: "Add" → "Add job template"

## Template Configuration

- **Name**: `Simple Palo Alto Diagnostic`
- **Job Type**: `Run`
- **Inventory**: `Demo Inventory` (or your default)
- **Project**: `Palo Alto Playbooks`
- **Execution Environment**: `AWX EE (latest)`
- **Playbook**: `simple_diagnostic.yml`
- **Credentials**: (leave empty - no SSH needed)
- **Variables**: (leave empty - playbook has no variables)

## Important Settings
- ☑️ **Prompt on launch**: NOT needed (no variables)
- ☑️ **Enable Privilege Escalation**: NOT needed
- ☑️ **Allow Simultaneous**: Can be unchecked

## Purpose
This diagnostic will:
1. Test basic connectivity to Palo Alto at 192.168.0.100
2. Force commit any pending configuration changes
3. Check if rules exist in the system
4. Help identify why rules created successfully in AWX aren't visible in GUI

## Expected Results
- Should see "TASK [Force commit pending changes]" with success
- Should see connectivity test results
- Will help determine if rules need commit or are in wrong location

## Troubleshooting
If the job fails:
- Check Palo Alto is accessible at 192.168.0.100
- Verify the hardcoded API key is still valid
- Check network connectivity from AWX container

## Next Steps After Running
1. Check AWX job output for any errors
2. Refresh Palo Alto GUI (Security → Policies → Security)
3. Look in both Pre Rules and Post Rules sections
4. Check if commit was successful