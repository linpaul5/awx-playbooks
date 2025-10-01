# Git Setup Commands (PowerShell or Bash)

# Navigate to directory
cd C:\Users\linpa\awx-vlan-change

# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Router VLAN change playbook"

# Add your remote repository (replace with your actual Git URL)
git remote add origin https://github.com/yourusername/awx-vlan-change.git

# Create main branch and push
git branch -M main
git push -u origin main
