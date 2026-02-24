# troubleshoot.ps1
$Port = 8506
$ErrorActionPreference = "Continue"

Write-Host "=== VM Troubleshooting Tool ===" -ForegroundColor Cyan

# 1. Check if Streamlit is running
Write-Host "`n[1] Checking Process..."
$process = Get-Process -Name "python" -ErrorAction SilentlyContinue
if ($process) {
    Write-Host "PASS: Python process is running." -ForegroundColor Green
} else {
    Write-Host "FAIL: Python process not found. Is the server running?" -ForegroundColor Red
}

# 2. Check if Port is Listening
Write-Host "`n[2] Checking Port $Port..."
$netstat = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
if ($netstat) {
    Write-Host "PASS: Service is listening on Port $Port." -ForegroundColor Green
    Write-Host "Local Address: $($netstat.LocalAddress)"
} else {
    Write-Host "FAIL: Nothing is listening on Port $Port." -ForegroundColor Red
}

# 3. Check Firewall Rule
Write-Host "`n[3] Checking Firewall..."
$rule = Get-NetFirewallRule -DisplayName "Slide Style Generator (Streamlit)" -ErrorAction SilentlyContinue
if ($rule) {
    Write-Host "PASS: Firewall rule exists." -ForegroundColor Green
    Write-Host "Enabled: $($rule.Enabled)"
    Write-Host "Profile: $($rule.Profile)"
    Write-Host "Action: $($rule.Action)"
} else {
    Write-Host "FAIL: Firewall rule not found." -ForegroundColor Red
}

# 4. Check Network Profiles
Write-Host "`n[4] Network Profiles..."
Get-NetConnectionProfile

# 5. Local Connectivity Test
Write-Host "`n[5] Testing Local Connection..."
try {
    $request = Invoke-WebRequest -Uri "http://localhost:$Port/_stcore/health" -UseBasicParsing -TimeoutSec 2
    if ($request.StatusCode -eq 200) {
        Write-Host "PASS: Service is responding locally (Health Check OK)." -ForegroundColor Green
    } else {
        Write-Host "WARN: Service responded with code $($request.StatusCode)." -ForegroundColor Yellow
    }
} catch {
    Write-Host "FAIL: Could not connect locally. Error: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`n=== End of Report ===" -ForegroundColor Cyan
Pause
