# 投影片風格生成工具 (Slide Style Generator)

從現有風格中選擇，或使用 AI 擴充新風格，並生成詳細的設計規範與 AI 繪圖提示詞。

## 🌐 線上使用

**免安裝，直接打開瀏覽器即可使用：**

👉 [https://slidestylegen-5fsnbusbdtwj8pbyiqnq9k.streamlit.app/](https://slidestylegen-5fsnbusbdtwj8pbyiqnq9k.streamlit.app/)

## 🖥️ 本機執行

若想在本機執行，請依照以下步驟：

### 環境準備

請確保您的系統已安裝 Python 3.8 或以上版本。

### 安裝相依套件

```bash
pip install -r requirements.txt
```

### 啟動應用程式

```bash
streamlit run app.py
```

## 📖 使用說明

1. **風格選擇**：在左側欄位選擇既有風格，或使用 AI 模擬生成新風格。
2. **編輯細節**：在中間區域調整風格的詳細設定（配色、字體等）。
3. **生成預覽/規範**：右側會即時顯示針對圖片生成的 Prompt，以及可下載的風格規範文件 (Markdown)。
4. **下載規範**：點擊「下載風格規範」按鈕取得完整檔案。

## 注意事項

- 本工具不需連接外網 API，所有功能皆在本機/伺服器端執行。
- 生成的提示詞可複製至 Midjourney、DALL-E 等 AI 繪圖工具使用。
