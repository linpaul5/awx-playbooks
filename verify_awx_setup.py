#!/usr/bin/env python3
"""
AWX Template Setup Verification Script
Helps verify that all prerequisites are met for Palo Alto automation templates
"""

import requests
import json
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# AWX Configuration
AWX_URL = "http://localhost:32237"
AWX_USERNAME = "admin"  # Replace with your AWX username
AWX_PASSWORD = "password"  # Replace with your AWX password

def check_awx_connectivity():
    """Test basic AWX connectivity"""
    try:
        response = requests.get(f"{AWX_URL}/api/v2/ping/", timeout=5)
        if response.status_code == 200:
            print("✅ AWX is accessible at", AWX_URL)
            return True
        else:
            print("❌ AWX returned status code:", response.status_code)
            return False
    except Exception as e:
        print("❌ Cannot connect to AWX:", str(e))
        return False

def get_awx_token():
    """Get AWX authentication token"""
    try:
        auth_data = {
            'username': AWX_USERNAME,
            'password': AWX_PASSWORD
        }
        response = requests.post(f"{AWX_URL}/api/v2/tokens/", 
                               json=auth_data, verify=False)
        if response.status_code == 201:
            token = response.json()['token']
            print("✅ AWX authentication successful")
            return token
        else:
            print("❌ AWX authentication failed:", response.status_code)
            print("Please update AWX_USERNAME and AWX_PASSWORD in this script")
            return None
    except Exception as e:
        print("❌ Authentication error:", str(e))
        return None

def check_prerequisites(token):
    """Check if all prerequisites exist"""
    headers = {'Authorization': f'Bearer {token}'}
    
    checks = []
    
    # Check Project
    try:
        response = requests.get(f"{AWX_URL}/api/v2/projects/", headers=headers)
        projects = response.json()['results']
        project_exists = any(p['name'] == 'Palo Alto Playbooks' for p in projects)
        status = "✅" if project_exists else "❌"
        checks.append(f"{status} Project 'Palo Alto Playbooks': {'Found' if project_exists else 'Not found'}")
    except Exception as e:
        checks.append(f"❌ Error checking projects: {e}")
    
    # Check Inventory
    try:
        response = requests.get(f"{AWX_URL}/api/v2/inventories/", headers=headers)
        inventories = response.json()['results']
        inventory_exists = any('palo' in i['name'].lower() for i in inventories)
        status = "✅" if inventory_exists else "❌"
        checks.append(f"{status} Palo Alto Inventory: {'Found' if inventory_exists else 'Not found'}")
    except Exception as e:
        checks.append(f"❌ Error checking inventories: {e}")
    
    # Check Execution Environment
    try:
        response = requests.get(f"{AWX_URL}/api/v2/execution_environments/", headers=headers)
        ees = response.json()['results']
        ee_exists = any('AWX EE' in ee['name'] or 'awx-ee' in ee['name'] for ee in ees)
        status = "✅" if ee_exists else "❌"
        checks.append(f"{status} Execution Environment 'AWX EE (latest)': {'Found' if ee_exists else 'Not found'}")
    except Exception as e:
        checks.append(f"❌ Error checking execution environments: {e}")
    
    return checks

def suggest_next_steps(checks):
    """Provide next steps based on check results"""
    print("\n🎯 NEXT STEPS:")
    
    missing_items = [check for check in checks if "❌" in check]
    
    if not missing_items:
        print("🎉 All prerequisites met! You can proceed with template creation.")
        print("📋 Follow the steps in AWX_TEMPLATES_SETUP.md")
    else:
        print("⚠️  Missing prerequisites detected:")
        for item in missing_items:
            print(f"   {item}")
        print("\n🔧 RESOLUTION:")
        print("1. Ensure your AWX project 'Palo Alto Playbooks' is synced")
        print("2. Create Palo Alto inventory with host 192.168.0.100")
        print("3. Use default execution environment AWX EE (latest)")
        print("4. Re-run this script to verify")

def main():
    """Main verification function"""
    print("🔍 AWX TEMPLATE SETUP VERIFICATION")
    print("=" * 40)
    
    # Step 1: Basic connectivity
    if not check_awx_connectivity():
        print("Please start AWX and try again")
        return
    
    # Step 2: Authentication
    token = get_awx_token()
    if not token:
        print("Please check your AWX credentials")
        return
    
    # Step 3: Prerequisites check
    print("\n📋 CHECKING PREREQUISITES:")
    checks = check_prerequisites(token)
    for check in checks:
        print(f"   {check}")
    
    # Step 4: Recommendations
    suggest_next_steps(checks)
    
    print("\n📚 DOCUMENTATION:")
    print("   📖 Full setup guide: AWX_TEMPLATES_SETUP.md")
    print("   📖 Usage examples: PALO_ALTO_AUTOMATION_GUIDE.md")

if __name__ == "__main__":
    main()