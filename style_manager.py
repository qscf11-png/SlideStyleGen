import re
import random

class StyleManager:
    def __init__(self, source_file):
        self.source_file = source_file
        self.styles = self._parse_styles()

    def _parse_styles(self):
        """Parses the text file into a structured dictionary."""
        styles = {}
        current_style = None
        current_section = None
        
        try:
            with open(self.source_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            return {}

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Detect new style
            if line.startswith("風格："):
                style_name = line.split("：")[1].strip()
                current_style = {
                    "name": style_name,
                    "concept": "",
                    "design_settings": {},
                    "layout_variations": [],
                    "rules": []
                }
                styles[style_name] = current_style
                current_section = "general" # Default section
                continue
            
            if current_style is None:
                continue

            # Parse details based on headers
            if line.startswith("概念："):
                current_style["concept"] = line.split("：")[1].strip().strip('"')
            elif line.startswith("整體設計設定："):
                current_section = "design_settings"
            elif line.startswith("版面配置變化"):
                current_section = "layout_variations"
            elif line.startswith("設計規則：") or line.startswith("通用版面規則："):
                current_section = "rules"
            elif line.startswith("投影片結構模式：") or line.startswith("投影片結構："):
                current_section = "structure"
            
            # Parsing content within sections
            elif current_section == "design_settings":
                if "：" in line:
                    parts = line.split("：", 1)
                    key = parts[0].strip()
                    value = parts[1].strip().strip('"')
                    current_style["design_settings"][key] = value
            
            elif current_section == "layout_variations":
                if line.startswith("類型："):
                     current_style["layout_variations"].append({"type": line.split("：")[1].strip().strip('"'), "design": ""})
                elif line.startswith("設計：") and current_style["layout_variations"]:
                     current_style["layout_variations"][-1]["design"] = line.split("：")[1].strip().strip('"')

            elif current_section == "rules":
                if "：" in line:
                     parts = line.split("：", 1)
                     rule_content = parts[1].strip().strip('"')
                     current_style["rules"].append(f"{parts[0].strip()}: {rule_content}")

        return styles

    def get_style_names(self):
        return list(self.styles.keys())

    def get_style(self, name):
        return self.styles.get(name)

    def generate_random_style_prompt(self):
        """Generates a prompt for a random style mix."""
        if not self.styles:
            return "No styles available."
        
        s1 = random.choice(list(self.styles.values()))
        s2 = random.choice(list(self.styles.values()))
        
        prompt = f"Create a new slide design style that blends '{s1['name']}' and '{s2['name']}'. \n"
        prompt += f"Constructivism elements from {s1['name']}: {s1.get('concept', '')}. \n"
        prompt += f"Visual elements from {s2['name']}: {s2.get('concept', '')}. \n"
        prompt += "Define Colors, Fonts, and Layouts."
        return prompt

if __name__ == "__main__":
    # Test
    sm = StyleManager("c:\\Users\\tk_tsai\\.gemini\\antigravity\\scratch\\SlideStyleGen\\styles_source.txt")
    print(f"Loaded {len(sm.styles)} styles.")
    for name in sm.get_style_names():
        print(f"- {name}")
