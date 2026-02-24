# run_server_VM.ps1
$ErrorActionPreference = "Stop"
$Port = 8506

Write-Host "=========================================="
Write-Host "  Slide Style Generator - VM Deployment"
Write-Host "=========================================="

# 1. Check Python
try {
    $pyVersion = python --version 2>&1
    Write-Host "Detected Python: $pyVersion"
} catch {
    Write-Host "Error: Python not found. Please install Python 3.8+ on this VM first." -ForegroundColor Red
    Pause
    Exit 1
}

# 2. Setup Virtual Environment
if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment (.venv)..."
    python -m venv .venv
} else {
    Write-Host "Using existing virtual environment."
}

# 3. Install Dependencies
Write-Host "Installing/Updating dependencies..."
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\python -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error installing dependencies. Please check your internet connection." -ForegroundColor Red
    Pause
    Exit 1
}

# 4. Run App
# Attempt to find the primary IP address for display purposes
try {
    $IP = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.InterfaceAlias -notlike "*Loopback*" -and $_.PrefixOrigin -ne "WellKnown"}).IPAddress[0]
} catch {
    $IP = "YOUR_VM_IP"
}

Write-Host "------------------------------------------"
Write-Host "Starting Service..."
Write-Host "You can access the tool at: http://$IP:$Port"
Write-Host "------------------------------------------"

# Launch Streamlit from the virtual environment
.\.venv\Scripts\python -m streamlit run app.py --server.port $Port --server.address 0.0.0.0
