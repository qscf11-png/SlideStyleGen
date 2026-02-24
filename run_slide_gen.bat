@echo off
chcp 65001
cd /d "%~dp0"
echo 正在啟動投影片風格生成工具...
echo Starting Slide Style Generator...
uv run streamlit run app.py
pause
