import os
import re

tags_map = {
    "alex-hormozi-perspective": ["價值方程式", "行銷", "銷售", "獲客模型"],
    "andrej-karpathy-perspective": ["深度學習", "AI原理", "第一性原理"],
    "carl-jung-perspective": ["潛意識", "陰影整合", "原型", "心理學"],
    "chris-voss-perspective": ["戰術同理心", "談判", "極限溝通"],
    "daniel-kahneman-perspective": ["認知偏誤", "雙系統思維", "決策心理學"],
    "elon-musk-perspective": ["第一性原理", "物理思維", "極限效率", "系統思考"],
    "feynman-perspective": ["費曼學習法", "本質拆解", "大白話解釋"],
    "ilya-sutskever-perspective": ["深度學習", "AGI", "長期視野"],
    "james-clear-perspective": ["原子習慣", "系統設計", "微小進步", "PDCA"],
    "jeff-bezos-perspective": ["逆向工作法", "顧客痴狂", "Day1思維", "雙向門決策"],
    "mckinsey-consultant-perspective": ["MECE", "金字塔原則", "問題樹", "結構化思維"],
    "mrbeast-perspective": ["流量池", "鉤子", "注意力工程", "極致投入"],
    "munger-perspective": ["反向思考", "跨領域網格", "預先驗屍", "避免愚蠢"],
    "naval-perspective": ["槓桿", "複利", "特殊知識", "長期博弈"],
    "paul-graham-perspective": ["創造財富", "創業本質", "MVP", "精實"],
    "peter-thiel-perspective": ["逆向真理", "壟斷", "藍海戰略", "冪次法則"],
    "ray-dalio-perspective": ["絕對真實", "系統思考", "機器學習思維", "第二序思考"],
    "rick-rubin-perspective": ["減法藝術", "內在感知", "破除制約"],
    "robert-mckee-perspective": ["故事工程", "敘事架構", "價值轉換", "衝突設計"],
    "rory-sutherland-perspective": ["行為經濟學", "心理煉金術", "心理感知", "框架效應"],
    "sherlock-holmes-perspective": ["演繹推理", "極致觀察", "邏輯推演", "排除法"],
    "socrates-perspective": ["蘇格拉底提問", "假設驗證", "自我反思"],
    "steve-jobs-perspective": ["極簡主義", "產品直覺", "扭曲現實力場", "用戶體驗"],
    "sun-tzu-perspective": ["大戰略", "避實擊虛", "降維打擊", "安全邊際"],
    "sun-yuchen-perspective": ["敘事套利", "流量變現", "爭議行銷", "資源整合"],
    "taleb-perspective": ["反脆弱", "黑天鵝", "槓鈴策略", "尾部風險"],
    "trump-perspective": ["極端談判", "框架控制", "破除常規", "聲量遊戲"],
    "x-mastery-mentor": ["鉤子", "注意力工程", "爆款思維", "寫作"],
    "the-architect-perspective": ["思維中樞", "OODA迴圈", "框架組合", "全知視角", "SCAMPER"],
    "zhang-yiming-perspective": ["延遲滿足", "ROI", "上帝視角", "演算法思維"],
    "zhangxuefeng-perspective": ["降維解析", "資訊差", "現實主義", "殘酷真相"]
}

def inject_tags():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    examples_dir = os.path.join(base_dir, 'examples')
    
    for folder_name, new_tags in tags_map.items():
        skill_file = os.path.join(examples_dir, folder_name, 'SKILL.md')
        if not os.path.exists(skill_file):
            print(f"Skipping {folder_name}, not found.")
            continue
            
        with open(skill_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if already has tags
        if re.search(r'^tags:\s*\[', content, re.MULTILINE):
            print(f"Skipping {folder_name}, tags exist.")
            continue
            
        tags_str = "tags: [" + ", ".join(new_tags) + "]"
        
        # Insert tags after description
        # We need to find the end of description.
        # It could be single line or multiline block.
        # Find the frontmatter
        match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if match:
            yaml_part = match.group(1)
            # Just append tags to the yaml_part
            new_yaml_part = yaml_part + f"\n{tags_str}"
            new_content = content[:match.start(1)] + new_yaml_part + content[match.end(1):]
            
            with open(skill_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added tags to {folder_name}")
        else:
            print(f"Failed to find frontmatter in {folder_name}")

if __name__ == "__main__":
    inject_tags()
