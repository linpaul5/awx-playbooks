# AWX Template Setup Helper
# PowerShell script to help set up Palo Alto automation templates

Write-Host "AWX PALO ALTO TEMPLATE SETUP HELPER" -ForegroundColor Green
Write-Host "===================================================="

# Check AWX connectivity
Write-Host "`nCHECKING AWX STATUS..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:32237" -UseBasicParsing -TimeoutSec 5
    Write-Host "AWX is running (Status: $($response.StatusCode))" -ForegroundColor Green
} catch {
    Write-Host "AWX is not accessible" -ForegroundColor Red
    Write-Host "Please start AWX with: docker-compose up -d" -ForegroundColor Yellow
    exit 1
}

# Template configurations
$templates = @(
    @{
        Name = "Palo Alto - Deploy Security Rule"
        Description = "Create, update, delete, or list Palo Alto security rules"
        Project = "Palo Alto Playbooks"
        Playbook = "palo_alto_security_rules.yml"
        ExecutionEnv = "AWX EE (latest)"
        Variables = "Required - Prompt on Launch"
        Purpose = "Production rule management"
    },
    @{
        Name = "Palo Alto - Rule Demo"  
        Description = "Deploy demonstration security rules"
        Project = "Palo Alto Playbooks"
        Playbook = "palo_alto_rule_demo.yml"
        ExecutionEnv = "AWX EE (latest)"
        Variables = "None needed"
        Purpose = "Show automation capabilities"
    },
    @{
        Name = "Palo Alto - Cleanup Demo Rules"
        Description = "Remove all demonstration rules"
        Project = "Palo Alto Playbooks"
        Playbook = "palo_alto_cleanup.yml"
        ExecutionEnv = "AWX EE (latest)"
        Variables = "None needed"
        Purpose = "Environment cleanup"
    }
)

Write-Host "`nTEMPLATES TO CREATE:" -ForegroundColor Yellow
foreach ($template in $templates) {
    Write-Host "`n$($template.Name)" -ForegroundColor Cyan
    Write-Host "   Project: $($template.Project)"
    Write-Host "   Playbook: $($template.Playbook)"
    Write-Host "   Execution Environment: $($template.ExecutionEnv)"
    Write-Host "   Variables: $($template.Variables)"
    Write-Host "   Purpose: $($template.Purpose)"
}

Write-Host "`nMANUAL SETUP STEPS:" -ForegroundColor Yellow
Write-Host "1. Open AWX: http://localhost:32237" -ForegroundColor White
Write-Host "2. Go to Templates - Job Templates" -ForegroundColor White
Write-Host "3. Click Add - Job Template" -ForegroundColor White
Write-Host "4. Use configurations shown above" -ForegroundColor White
Write-Host "5. Test with Palo Alto Rule Demo first" -ForegroundColor White

Write-Host "`nDOCUMENTATION FILES:" -ForegroundColor Yellow
Write-Host "AWX_TEMPLATES_SETUP.md - Complete setup guide" -ForegroundColor White
Write-Host "PALO_ALTO_AUTOMATION_GUIDE.md - Usage examples" -ForegroundColor White

Write-Host "`nQUICK TEST SEQUENCE:" -ForegroundColor Yellow
Write-Host "1. Run Palo Alto Rule Demo (creates demo rules)" -ForegroundColor White
Write-Host "2. Check Palo Alto GUI for new rules" -ForegroundColor White  
Write-Host "3. Run Palo Alto Cleanup Demo Rules (removes demo rules)" -ForegroundColor White
Write-Host "4. Create custom rules with Deploy Security Rule" -ForegroundColor White

Write-Host "`nREADY TO PROCEED!" -ForegroundColor Green
Write-Host "Your playbooks are ready - just need to create the AWX templates!" -ForegroundColor Green

# Show available playbooks
Write-Host "`nAVAILABLE PLAYBOOKS:" -ForegroundColor Yellow
Get-ChildItem -Path "*.yml" | Where-Object { $_.Name -like "*palo*" } | ForEach-Object {
    Write-Host "   $($_.Name)" -ForegroundColor Green
}