# 如何執行投影片風格生成工具

本工具使用 Python 與 Streamlit 開發。請依照以下步驟執行：

## 1. 環境準備

請確保您的系統已安裝 Python 3.8 或以上版本。

## 2. 安裝相依套件

在專案目錄下執行以下指令：

```bash
pip install -r requirements.txt
```

若使用 `uv`：

```bash
uv pip install -r requirements.txt
```

## 3. 執行工具

執行以下指令啟動應用程式：

```bash
streamlit run app.py
```

若使用 `uv`：

```bash
uv run streamlit run app.py
```

## 4. 使用說明

1. **風格選擇**：在左側欄位選擇既有風格，或使用 AI 模擬生成新風格。
2. **編輯細節**：在中間區域調整風格的詳細設定（配色、字體等）。
3. **生成預覽/規範**：右側會即時顯示針對圖片生成的 Prompt，以及可下載的風格規範文件 (Markdown)。
4. **下載規範**：點擊「下載風格規範」按鈕取得完整檔案。

## 注意事項

- 本工具為 **Standalone 本地版本**，所有功能（Prompt 生成、規範文件匯出）皆在本機執行，不需連接外網 API，隱私安全性高。
- 生成的提示詞可複製至 Midjourney、DALL-E 等 AI 繪圖工具使用。
