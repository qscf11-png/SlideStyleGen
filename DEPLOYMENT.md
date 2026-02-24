# 部署至 VM 說明文件

本文件說明如何將 **Slide Style Generator** 部署至遠端 VM (`10.123.210.46`) 並在 Port `8506` 執行。

## 前置作業

1. 確認您有該 VM 的存取權限 (帳號/密碼)。
2. 確認該 VM 已安裝 **Python (3.8+)**。
3. 確認該 VM 的防火牆已開啟 **Port 8506**。

---

## 方法一：使用 PowerShell (Windows to Windows/Linux via SSH)

若是透過 SSH 連線 (最通用)，請依照以下步驟：

### 1. 複製檔案到 VM

在您的本機電腦開啟 PowerShell，執行以下指令 (請替換 `<username>` 為您的 VM 使用者名稱)：

```powershell
# 設定變數
$User = "您的使用者名稱"
$IP = "10.123.210.46"
$LocalPath = "c:\Users\tk_tsai\.gemini\antigravity\scratch\SlideStyleGen"
$RemotePath = "~/SlideStyleGen"  # 若是 Windows VM 可改為 "C:\SlideStyleGen"

# 複製檔案 (需要輸入密碼)
scp -r "$LocalPath" "${User}@${IP}:${RemotePath}"
```

### 2. 連線並啟動服務

接著 SSH 進入 VM 並執行：

```powershell
# SSH 連線
ssh "${User}@${IP}"

# --- 以下指令在遠端 VM 內執行 ---

# 1. 進入目錄
cd SlideStyleGen

# 2. 建立虛擬環境 & 安裝套件 (若尚未安裝)
pip install uvicorn streamlit python-docx google-generativeai openai

# 3. 啟動 Streamlit (指定 Port 8506)
# --server.address 0.0.0.0 確保外部可存取
python -m streamlit run app.py --server.port 8506 --server.address 0.0.0.0
```

---

## 方法二：Windows 檔案共用 (SMB)

若 VM 與您在同一個 Windows 網域且開啟檔案共用：

1. 開啟檔案總管，輸入 `\\10.123.210.46\c$` (或其他共用路徑)。
2. 將 `SlideStyleGen` 資料夾複製到 VM 上。
3. 使用「遠端桌面連線 (RDP)」登入 VM。
4. 開啟 CMD 或 PowerShell，進入該資料夾。
5. 執行啟動指令：

```powershell
pip install -r requirements.txt
python -m streamlit run app.py --server.port 8506 --server.address 0.0.0.0
```

---

### 自動化啟動腳本 (for VM)

為了方便您在 VM 上未來快速啟動，請在 VM 的專案目錄下建立一個名為 `run_server.ps1` 的檔案，內容如下：

```powershell
# run_server.ps1
Write-Host "Starting Slide Style Generator on Port 8506..."
python -m streamlit run app.py --server.port 8506 --server.address 0.0.0.0
```
