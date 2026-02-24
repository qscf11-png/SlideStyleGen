class PromptBuilder:
    def __init__(self):
        pass

    def build_prompt(self, style_data, additional_details=""):
        """
        Constructs a detailed prompt for image generation based on style data.
        """
        prompt = "Design a high-quality presentation slide. \n"
        
        if "name" in style_data:
            prompt += f"Style: {style_data['name']}. \n"
        
        if "concept" in style_data:
            prompt += f"Concept: {style_data['concept']}. \n"
            
        settings = style_data.get("design_settings", {})
        if settings:
            prompt += "Visual Elements: \n"
            for k, v in settings.items():
                prompt += f"- {k}: {v}. \n"
        
        variations = style_data.get("layout_variations", [])
        if variations:
           # Pick a random variation to focus the prompt, or use a generic one
           # For now, just listing keywords from variations
           types = ", ".join([v.get("type", "") for v in variations[:3]])
           prompt += f"Suggested Layouts: {types}. \n"

        if additional_details:
            prompt += f"Specific Details: {additional_details}. \n"

        prompt += "render, 8k, photorealistic, highly detailed, UI/UX design, presentation design, dribbble, behance."
        
        return prompt

    def build_spec_sheet(self, style_data):
        """
        Generates a markdown specification sheet.
        """
        spec = f"# 風格規範: {style_data.get('name', 'Custom Style')}\n\n"
        spec += f"## 概念\n{style_data.get('concept', 'N/A')}\n\n"
        
        spec += "## 視覺識別\n"
        settings = style_data.get("design_settings", {})
        for k, v in settings.items():
            spec += f"- **{k}**: {v}\n"
        
        spec += "\n## 版面配置參考\n"
        for v in style_data.get("layout_variations", []):
            spec += f"- **{v.get('type', 'Unknown')}**: {v.get('design', '')}\n"

        spec += "\n## 設計規則\n"
        for r in style_data.get("rules", []):
             spec += f"- {r}\n"

        return spec
