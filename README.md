<div align="center">

# 名人AI智囊團 (Celebrity AI Think Tank)

> *這是一個為「Nuwa Skill」量身打造的 Web 視覺化擴充介面，讓你輕鬆召喚各路大師為你出謀劃策。*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<br>

**基於花叔 (Huashu) 的 [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) 專案深度擴充與視覺化改造。**
我們不僅繼承了原專案強大的「思維模型蒸餾」理念，更進一步新增了多位各領域頂尖人物的視角，並開發了專屬的 Web 聊天介面，讓你無需透過命令列，直接在瀏覽器中與大師們展開對話。

</div>

---

## 🌟 為什麼要有這個專案？

原專案 [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) 提供了一個非常棒的概念：將名人的思維模型（如喬布斯、馬斯克、芒格）蒸餾成 AI 角色（Skill），讓 AI 用他們的認知框架來幫我們分析問題。

然而，在原專案中，切換與呼叫角色需要依賴特定的命令列環境。為了讓這個強大的工具更平易近人且便於操作，我做出了以下擴充：

1. **🖥️ 視覺化 Web 介面 (`nuwa_chat.html`)**：無需安裝任何環境，點開 HTML 檔案即可在瀏覽器中使用。
2. **🔄 一鍵切換多重宇宙**：內建角色選單與搜尋功能，隨時隨地在不同名人的腦袋間切換。
3. **🧠 擴充智囊庫**：除了原有的 13 位人物外，我又耗費了大量心血進行蒸餾，將智囊團擴充至 **33 種視角**，涵蓋商業、科學、哲學、行銷、心理學等多個維度。
4. **🤖 AI 自動選角**：不知道該問誰？交給 AI 幫你判斷最適合回答目前問題的大師。

---

## 🚀 如何使用 (Web UI 版)

本專案將複雜的環境依賴降到最低，您只需要準備一個 Google Gemini API Key：

1. **取得 Gemini API Key**：前往 [Google AI Studio](https://aistudio.google.com/app/apikey) 免費申請一組 API Key。
2. **開啟網頁**：直接雙擊打開專案目錄下的 `nuwa_chat.html` 檔案（建議使用 Chrome 或 Edge 瀏覽器）。
3. **設定 API Key**：點擊網頁左下角的「⚙️ API 設定」，填入您的 Gemini API Key 並儲存。
4. **開始對話**：在左側選單選擇一位您想諮詢的大師，然後在下方輸入您的問題即可！

*(註：您的 API Key 只會存在您的本地瀏覽器中，不會上傳到任何其他伺服器，非常安全。)*

---

## 🏛️ 目前收錄的智囊團名單 (共 33 種視角)

我們將大師們分為以下幾大類別，所有角色的詳細設定檔都存放在 `examples/` 目錄下：

### 💼 商業、投資與創業巨頭
- **Steve Jobs (喬布斯)**：產品極簡主義與現實扭曲視角
- **Elon Musk (馬斯克)**：第一性原理與極致工程思維
- **Jeff Bezos (貝佐斯)**：顧客痴狂與 Day 1 思維
- **Ray Dalio (達利歐)**：絕對真實與機器學習思維
- **Peter Thiel (提爾)**：創造壟斷與逆向真理
- **Charlie Munger (芒格)**：逆向思考與多元思維模型
- **Paul Graham (格雷厄姆)**：Y Combinator 創投思維
- **張一鳴**：延遲滿足與 ROI 演算法思維

### 🧠 科技、AI 與科學家
- **Richard Feynman (費曼)**：費曼學習法與拆解第一原理
- **Andrej Karpathy**：AI 學習與神經網絡專家視角
- **Ilya Sutskever**：OpenAI 共同創辦人信念視角

### ⚖️ 人生哲學、風險與批判者
- **Naval Ravikant (納瓦爾)**：財富自由與複利人生哲學
- **Nassim Taleb (塔勒布)**：反脆弱與黑天鵝風險視角

### 📣 媒體、網紅與極端影響力
- **MrBeast**：頂級注意力工程與內容迭代邏輯
- **Donald Trump (川普)**：媒體聲量操作與強勢談判視角
- **孫宇晨**：流量收割與加密貨幣行銷模式
- **張雪峰**：極致現實主義與升學/職涯規劃視角

### 📈 頂級商業行銷與變現
- **Alex Hormozi**：無法拒絕的 $100M 報價與價值方程式
- **Rory Sutherland**：奧美行銷大師的行為經濟學與煉金術

### 🎨 極致藝術與發散創造力
- **Rick Rubin**：靈魂製作人的減法與感知藝術

### 🧠 人類認知與行為心理學
- **Alfred Adler (阿德勒)**：目的論、課題分離與勇氣心理學
- **Sigmund Freud (佛洛伊德)**：潛意識探索、童年創傷與防衛機制
- **Daniel Kahneman (康納曼)**：雙系統思維與認知偏誤
- **Carl Jung (榮格)**：無意識、原型與陰影整合

### ⚙️ 生產力、習慣與系統設計
- **James Clear (克萊爾)**：微小進步與習慣系統化

### 🛡️ 談判、博弈與人際危機處理
- **Chris Voss (沃斯)**：戰術同理心與極限談判
- **孫子**：戰略計算、地形優劣與降維打擊

### 🔍 邏輯推理與結構化解題
- **McKinsey Consultant (麥肯錫顧問)**：MECE 原則與金字塔解題
- **Sherlock Holmes (福爾摩斯)**：演繹推理、極致觀察與排除法

### 📖 故事工程與敘事力
- **Robert McKee (麥基)**：《故事的解剖》好萊塢編劇教父敘事力

### 🗣️ 對話與引導 (教練模式)
- **Socrates (蘇格拉底)**：不給答案，只用反問揭示你的盲點

### 🎯 專題視角與中樞系統
- **X Mastery Mentor**：X (原推特) 爆款思維
- **The Architect**：內建 28 種跨領域神級思維模型的智囊中樞

---

## 🙏 致謝與聲明

本專案的底層邏輯與思維模型蒸餾框架，全部歸功於原作者 **花叔 (Huashu)** 所開發的 [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) 專案。

*   **原專案 Github**: [https://github.com/alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill)
*   **原專案作者 X (Twitter)**: [@AlchainHust](https://x.com/AlchainHust)

我（本專案作者）的主要貢獻在於開發了本地端視覺化的 HTML 介面 (`nuwa_chat.html`)，並基於原作者的框架，耗費大量心力額外蒸餾並擴充了數十位人物視角，以打造這個更易用的「名人AI智囊團」。

## 📜 許可證
本專案與原專案同樣遵循 [MIT License](LICENSE)。您可以自由使用、修改與分發，只需保留原有的授權聲明。
