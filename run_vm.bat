@echo off
chcp 65001
cd /d "%~dp0"

echo ==========================================
echo  Slide Style Generator - VM Deployment
echo ==========================================

REM 1. 檢查 Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [Error] Python not found or not in PATH.
    echo 請確認 VM 上已安裝 Python 3.8+ 並加入環境變數。
    pause
    exit /b
)

REM 2. 建立虛擬環境
if not exist .venv (
    echo [Info] 正在建立虛擬環境...
    python -m venv .venv
) else (
    echo [Info] 使用既有虛擬環境。
)

REM 3. 安裝/更新套件
echo [Info] 正在安裝依賴套件...
call .venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [Error] 套件安裝失敗，請檢查網路連線。
    pause
    exit /b
)

REM 4. 啟動服務
echo ==========================================
echo  Starting Service on Port 8506...
echo  Access URL: http://10.123.210.46:8506
echo ==========================================

python -m streamlit run app.py --server.port 8506 --server.address 0.0.0.0

pause
