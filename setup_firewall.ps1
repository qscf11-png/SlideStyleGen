# setup_firewall.ps1
# 請以「系統管理員身分 (Run as Administrator)」執行此腳本

$Port = 8506
$RuleName = "Slide Style Generator (Streamlit)"

Write-Host "Checking firewall rule for Port $Port..."

$exists = Get-NetFirewallRule -DisplayName $RuleName -ErrorAction SilentlyContinue

if ($exists) {
    Write-Host "Firewall rule '$RuleName' already exists."
} else {
    Write-Host "Creating firewall rule to allow inbound traffic on Port $Port..."
    New-NetFirewallRule -DisplayName $RuleName `
                        -Direction Inbound `
                        -LocalPort $Port `
                        -Protocol TCP `
                        -Action Allow `
                        -Profile Any
    Write-Host "Rule created successfully."
}

Write-Host "Firewall setup complete."
Pause
