import streamlit as st
import os
from style_manager import StyleManager
from prompt_builder import PromptBuilder

# st.set_page_config MUST be the first Streamlit command
st.set_page_config(page_title="Slide Style Generator", layout="wide")

# Initialize managers with error handling for better diagnostics
base_dir = os.path.dirname(os.path.abspath(__file__))
style_source_path = os.path.join(base_dir, "styles_source.txt")

@st.cache_resource
def get_managers():
    try:
        sm = StyleManager(style_source_path)
        pb = PromptBuilder()
        return sm, pb, None
    except Exception as e:
        return None, None, str(e)

style_manager, prompt_builder, init_error = get_managers()

st.title("投影片風格生成與規範工具 (Slide Style Generator)")
st.markdown("從現有風格中選擇，或使用 AI 擴充新風格，並生成詳細的設計規範與預覽。")

if init_error:
    st.error(f"初始化錯誤：{init_error}")
    st.info(f"嘗試讀取的路徑：{style_source_path}")
    st.stop()

# Sidebar - Style Selection
st.sidebar.header("風格選擇")
mode = st.sidebar.radio("模式", ["選擇現有風格", "AI 風格擴充 (模擬)"])

selected_style_data = {}

if mode == "選擇現有風格":
    style_names = style_manager.get_style_names()
    if not style_names:
        st.sidebar.warning("找不到任何風格資料。")
    else:
        selected_name = st.sidebar.selectbox("選擇風格", style_names)
        if selected_name:
            selected_style_data = style_manager.get_style(selected_name)

elif mode == "AI 風格擴充 (模擬)":
    st.sidebar.info("模擬 AI 生成新風格的功能。")
    keywords = st.sidebar.text_input("輸入關鍵字 (例如：賽博龐克、禪意)")
    if st.sidebar.button("生成新風格"):
        # partial 模擬 logic
        selected_style_data = {
            "name": f"AI Generated: {keywords}",
            "concept": f"Based on {keywords}",
            "design_settings": {
                "基調": "AI Generated customized tone",
                "配色": "Dynamic Palette based on keywords",
                "字體": "Modern Sans-Serif"
            },
            "layout_variations": [
                {"type": "Title Slide", "design": "Big bold text with keyword imagery"},
                {"type": "Content", "design": "Clean layout with data visualization"}
            ],
             "rules": [
                 "Keep it simple",
                 "High contrast"
             ]
        }
        st.success("新風格已生成！")

# Main Content
if selected_style_data:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("風格細節 (可編輯)")
        
        # Concept
        new_concept = st.text_area("概念", selected_style_data.get("concept", ""))
        selected_style_data["concept"] = new_concept

        # Design Settings
        st.markdown("### 視覺識別設定")
        settings = selected_style_data.get("design_settings", {})
        new_settings = {}
        for k, v in settings.items():
            new_val = st.text_input(f"{k}", v)
            new_settings[k] = new_val
        selected_style_data["design_settings"] = new_settings

    with col2:
        st.subheader("預覽與輸出")
        
        # Prompt Generation
        prompt = prompt_builder.build_prompt(selected_style_data)
        st.text_area("AI 繪圖提示詞 (Prompt)", prompt, height=150)
        
        # Spec Sheet Generation
        st.markdown("### 風格規範文件")
        spec_sheet = prompt_builder.build_spec_sheet(selected_style_data)
        st.text_area("規範內容 preview", spec_sheet, height=300)
        
        st.download_button(
            label="下載風格規範 (Markdown)",
            data=spec_sheet,
            file_name=f"{selected_style_data.get('name', 'style')}_spec.md",
            mime="text/markdown"
        )

        st.info("提示：複製上方的提示詞到 Midjourney 或 DALL-E 可生成高品質預覽圖。")

else:
    st.info("請從左側選擇或生成一個風格。")
