@echo off
cd /d "%~dp0"

echo ==========================================
echo  VM Repair and Restart Tool
echo  Recommendation: Right-click and "Run as Administrator"
echo ==========================================

REM 1. Kill old processes
echo [1/3] Killing old Python processes...
taskkill /F /IM python.exe >nul 2>&1
echo Done.

REM 2. Setup Firewall (using netsh)
echo [2/3] Setting firewall rules (Port 8506)...
netsh advfirewall firewall delete rule name="Slide Style Generator (VM)" >nul 2>&1
netsh advfirewall firewall add rule name="Slide Style Generator (VM)" dir=in action=allow protocol=TCP localport=8506
if %errorlevel% neq 0 (
    echo [WARNING] Firewall setup failed! Please run as Administrator.
) else (
    echo [SUCCESS] Firewall rule created.
)

REM 3. Start App without prompting for email
echo [3/3] Starting Application...
echo Please do not close this window.
echo Creating startup log (startup_log.txt)...

if not exist .venv (
    echo [ERROR] .venv not found. Please run run_vm.bat first or check your files.
    pause
    exit /b
)

call .venv\Scripts\activate.bat

REM Start Streamlit in headless mode to avoid email prompt
echo Starting Streamlit in background...
start "Streamlit Service" /min cmd /k "python -m streamlit run app.py --server.port 8506 --server.address 0.0.0.0 --server.headless true --browser.gatherUsageStats false > startup_log.txt 2>&1"

echo.
echo ==========================================
echo  Service Started!
echo  Access URL: http://10.123.210.46:8506
echo ==========================================
echo.
echo Logs are being written to startup_log.txt
echo You can check the logs by opening that file.
echo.
pause
