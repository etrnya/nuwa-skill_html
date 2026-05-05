import os
import re

translations = {
    "andrej-karpathy-perspective": {
        "name": "Andrej Karpathy 視角",
        "desc": "以前 Tesla AI 總監 Andrej Karpathy 的視角解讀 AI 與深度學習技術。"
    },
    "elon-musk-perspective": {
        "name": "馬斯克 (Elon Musk) 視角",
        "desc": "秉持第一性原理的思考方式，極度追求效率、創新與突破傳統框架。"
    },
    "feynman-perspective": {
        "name": "理查·費曼 (Richard Feynman) 視角",
        "desc": "以費曼技巧深入淺出地解釋複雜概念，強調真正的理解而非死記硬背。"
    },
    "ilya-sutskever-perspective": {
        "name": "Ilya Sutskever 視角",
        "desc": "以 OpenAI 前首席科學家的視角，深入探討通用人工智慧 (AGI) 的發展與安全性。"
    },
    "mrbeast-perspective": {
        "name": "MrBeast (野獸先生) 視角",
        "desc": "極致的內容創作者視角，專注於吸引注意力、數據分析與病毒式傳播策略。"
    },
    "munger-perspective": {
        "name": "查理·蒙格 (Charlie Munger) 視角",
        "desc": "提倡多元思維模型與普世智慧，追求長期價值與理性決策的投資泰斗視角。"
    },
    "naval-perspective": {
        "name": "Naval Ravikant 視角",
        "desc": "結合財富與哲學的深刻見解，強調槓桿作用、特定知識與內在平靜。"
    },
    "paul-graham-perspective": {
        "name": "Paul Graham 視角",
        "desc": "Y Combinator 創辦人視角，專注於新創公司本質、駭客精神與創造力的實用語錄。"
    },
    "steve-jobs-perspective": {
        "name": "賈伯斯 (Steve Jobs) 視角",
        "desc": "極致追求完美與使用者體驗，強調設計哲學與將複雜事物簡單化的魅力。"
    },
    "sun-yuchen-perspective": {
        "name": "孫宇晨 (Justin Sun) 視角",
        "desc": "以極致的行銷與公關操作為核心，探討加密貨幣與流量變現的實戰觀點。"
    },
    "taleb-perspective": {
        "name": "塔雷伯 (Nassim Taleb) 視角",
        "desc": "以「反脆弱」思維看待黑天鵝事件，強烈批判偽科學與不對稱風險的知識份子視角。"
    },
    "trump-perspective": {
        "name": "川普 (Donald Trump) 視角",
        "desc": "展現商人與前總統的談判藝術、強勢風格與「讓美國再次偉大」的直白口吻。"
    },
    "x-mastery-mentor": {
        "name": "X (Twitter) 經營導師",
        "desc": "專精於社群平台 X 的增長策略，教授文案寫作、互動提升與演算法掌握技巧。"
    },
    "zhang-yiming-perspective": {
        "name": "張一鳴 視角",
        "desc": "字節跳動創辦人視角，主推「延遲滿足感」、演算法導向與全球化擴張的企業思維。"
    },
    "zhangxuefeng-perspective": {
        "name": "張雪峰 視角",
        "desc": "以犀利幽默的風格，提供最接地氣、直擊現實的職涯與升學人生規劃指導。"
    }
}

base_dir = r"C:\Users\etrny\.gemini\antigravity\scratch\nuwa-skill\examples"

for root, _, files in os.walk(base_dir):
    if "SKILL.md" in files:
        key = os.path.basename(root)
        if key in translations:
            filepath = os.path.join(root, "SKILL.md")
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # Replace name
            content = re.sub(r"^name:\s*.+", f"name: {translations[key]['name']}", content, flags=re.M)
            
            # Replace description
            # Description is typically block formatted like description: |\n  Line 1\n  Line 2
            # We match 'description: |' and any following lines that start with spaces or are empty, until a line without leading spaces.
            def repl_desc(m):
                return f"description: |\n  {translations[key]['desc']}\n"
                
            content = re.sub(r"^description:\s*\|\n(?:[ \t]+.*\n|\n)+", repl_desc, content, flags=re.M)

            with open(filepath, "w", encoding="utf-8", newline="\n") as f:
                f.write(content)
            print(f"Updated {key}")

