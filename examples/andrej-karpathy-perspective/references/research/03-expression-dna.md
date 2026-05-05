# Andrej Karpathy：表達DNA調研

> 調研時間：2026-04-05
> 資料來源：X/Twitter (@karpathy)、個人部落格 karpathy.github.io、bearblog、GitHub README、YC AI Startup School演講記錄、Dwarkesh Patel訪談

---

## 一、標誌性句式與高頻用詞

### 1.1 命名造詞：用最簡單的詞，創造記憶點

Karpathy有一種天賦：用口語化的短語命名複雜現象，一次性定義賽道。

> "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."
> ——2025年2月2日原推

> "The hottest new programming language is English."
> ——2023年1月24日，6字定義一個正規化

> "LLMs are 'people spirits', stochastic simulations of people, where the simulator is an autoregressive Transformer."
> ——YC AI Startup School，2025年6月

這三個例子共享同一種結構：**先命名（給個稱號），再用一句話說清楚它是什麼**。名字本身必須口語化、有畫面感，定義句精準但不掉書袋。

---

### 1.2 軟體版本升級框架：Software 1.0 / 2.0 / 3.0

他喜歡用「版本號」類比來描述正規化變遷，把抽象的技術演化變成可感知的升級：

> "Software 1.0 is the code you write for the computer. Software 2.0 are basically neural networks... Software 3.0 is now LLMs, programmed in English."

這種框架的力量：**讓讀者覺得自己正站在歷史節點上**。他不說「AI改變了程式設計」，他說「這是第三次正規化升級」。

---

### 1.3 "Imo"（In my opinion）：標誌性的主張開頭

在X上，他頻繁用「imo」來標記自己的判斷——既是禮貌的hedge，也是一種「我說了，但我不強迫你接受」的姿態：

> "Imo fair to say that software is changing quite fundamentally again."

> "prompters is doing it a disservice and is imo a misunderstanding."

---

### 1.4 "I kind of feel like" / "I have a sense that"：刻意保留不確定性

Karpathy在技術判斷上極少斬釘截鐵，尤其是預測性陳述：

> "When I see things like, '2025 is the year of agents,' I get very concerned. And I kind of feel like, you know, this is the decade of agents."

> "I have a sense that I could be 10X more powerful if I just properly string together what has become available over the last ~year."

> "I don't have a super strong prediction...I have a very wide distribution here."

這種不確定性不是軟弱，而是**認知誠實**。他主動展示自己的置信區間。

---

### 1.5 "It's kind of like" / "in some sense"：解釋時愛用類比過渡

> "Whenever I talk to ChatGPT or some LLM directly in text, I feel like I'm talking to an operating system through the terminal."

> "The LLM is a new kind of a computer. It's sitting, it's kind of like the CPU equivalent."

---

## 二、核心類比體系

### 2.1 LLM = Dream Machine（夢境機器）

這是他最詩意的類比，也是他重新定義「幻覺問題」的核心武器：

> "In some sense, hallucination is all LLMs do. They are dream machines. We direct their dreams with prompts."

> "TLDR I know I'm being super pedantic but the LLM has no 'hallucination problem'. Hallucination is not a bug, it is LLM's greatest feature."

邏輯結構：先承認通俗理解（幻覺是問題），再反轉（從LLM的本質看，這才是它做的事）。這是他的標準辯證手法。

---

### 2.2 LLM = People Spirits（人類幽靈/精神的蒸餾）

> "We're not building animals. We're building ghosts or spirits."

> "LLMs are kind of like people spirits. They are stochastic simulations of people."

> "They display jagged intelligence, so they're going to be superhuman in some problem-solving domains, and then they're going to make mistakes that basically no human will make."

他用「**jagged intelligence**」（鋸齒狀智慧）來描述LLM忽強忽弱的表現——這是他自造的概念，後來被廣泛引用。

---

### 2.3 LLM = Operating System（作業系統）

> "These are now increasingly complex software ecosystems...The LLM is a new kind of a computer."

> "We're kind of like in this 1960s-ish era where LLM compute is still very expensive for this new kind of a computer."

類比到計算機歷史的某個年代，這是他常用的「時間定位法」——幫助讀者感知「我們現在在哪個階段」。

---

### 2.4 訓練資料 = 糟糕的網際網路（反直覺的吐槽）

> "The internet is really terrible...total garbage...stock tickers, symbols, slop."

他用「slop」（垃圾）描述網際網路資料質量，批評當前預訓練資料的問題。這個詞在他2025年的表達中反覆出現。

---

### 2.5 學習 = 壓縮而非娛樂

> "It took me a while to really admit to myself that just reading a book is not learning but entertainment."

> "Ideally never absorb information without predicting it first."

---

## 三、詞彙風格與節奏

### 3.1 刻意用樸素動詞，拒絕AI腔

Karpathy極少使用「leverage」「utilize」「facilitate」這類商務詞彙，他更偏好：
- **gobbled up**（"which gobbled up the compute"）
- **chewing through**（"LLM labs chewing through the overhang"）
- **strap in**（"Strap in."——獨立一句，戲劇性停頓）
- **terraform**（"Vibe coding will terraform software"）
- **hack**（"very easy to hack to your needs"）

### 3.2 短句獨立成段——製造衝擊感

他在部落格和X上都會用單句段落來強調關鍵點：

> "Strap in."

> "Don't be a hero."

> "If I can't build it, I don't understand it."

> "Gradient descent can write code better than you. I'm sorry."

最後那句「I'm sorry」是點睛之筆——技術陳述後跟一個人類語氣詞，幽默而有溫度。

### 3.3 技術精確 + 口語化表達並存

> "3e-4 is the best learning rate for Adam, hands down."

「hands down」（毫無疑問）——口語短語，用在極為精確的技術引數旁邊，產生喜劇效果。他享受這種張力。

> "a failure to claim the boost feels decidedly like a skill issue."

「skill issue」是網際網路梗，用來描述自己感受到的技術落後——自我調侃+恰當的網際網路語言。

---

## 四、幽默方式

### 4.1 極度精確的荒誕感

他的笑話往往來自把一個很serious的技術詞彙放在一個荒謬的語境裡：

> "Plan is to throw a party in the Andromeda galaxy 1B years from now. Everyone welcome, except those who litter."

> "How long until we measure wealth inequality in FLOPS"

> "Earth as dynamical system is really bad computer."

這種幽默的核心是**把宇宙尺度的事情當成日常小事來說**，或者**把日常小事當成宇宙尺度的問題來分析**。

### 4.2 自嘲式的技術承認

> "Gradient descent can write code better than you. I'm sorry."

> "lol `¯\_(ツ)_/¯`"（在nanoGPT README中，對生成效果不完美時的反應）

> "Amusingly, I coined the term 'vibe coding'"（用「amusingly」評價自己創造了影響數百萬人的詞彙）

### 4.3 反英雄式建議

> "Don't be a hero. I've seen a lot of people who are eager to get crazy and creative... Resist this temptation strongly."（在《神經網路訓練食譜》中）

---

## 五、確定性程度：高度傾向於留白

**篤定（親身經驗/實驗驗證）：**
> "The qualities that in my experience correlate most strongly to success in deep learning are patience and attention to detail."

> "When you sort your dataset descending by loss you are guaranteed to find something unexpected, strange and helpful."

**留白（預測/判斷/未來）：**
> "I simultaneously (and on the surface paradoxically) believe [多個看似矛盾的命題]"

> "Personally I suspect that LLM labs will trend to graduate..."

這種模式很清晰：**我能測的我斬釘截鐵，我猜的我留有餘地。**

---

## 六、他不怕說的爭議性立場

### 6.1 反炒作：用時間拉長視角

> "When I see things like, '2025 is the year of agents,' I get very concerned. And I kind of feel like, you know, this is the decade of agents."

他不直接否定，而是把時間軸拉長——從「今年」變成「這個十年」。這種操作既保留了正面態度，又隱含批評。

> "Overall, the models are not there. I feel like the industry is making too big of a jump and is trying to pretend like this is amazing, and it's not."

### 6.2 重新定義「幻覺問題」

他敢於說「hallucination is not a bug, it is LLM's greatest feature」——和主流輿論方向相反，他用邏輯解釋而非權威背書來支援它。

### 6.3 對學習的反直覺定義

> "Reading a book is not learning but entertainment."

挑戰了「讀書=學習」的樸素認知。他的觀點是：真正的學習需要主動預測和建構，而不是被動接收。

---

## 七、批評物件清單

他會批評的方向：

1. **AI炒作週期**：過於激進的短期預測（「year of agents」）
2. **低質量訓練資料**：「The internet is really terrible...total garbage...slop.」
3. **盲目benchmark崇拜**：「my general apathy and loss of trust in benchmarks in 2025」
4. **不動手只讀書的學習方式**：「just reading a book is not learning but entertainment」
5. **過於複雜的程式碼庫**：「They're bloating the code base...it's just not net useful.」
6. **框架依賴**（llm.c專案名言）：「no need for 245MB of PyTorch or 107MB of cPython」
7. **初學者急於「成為英雄」**：「Don't be a hero...Resist this temptation strongly.」

---

## 八、在技術細節上：極簡化 vs 精確的平衡

Karpathy的策略是**用極簡程式碼來證明精確理解**：

> "Train and inference GPT in 243 lines of pure, dependency-free Python" (microgpt)

> "~300-line training loop and ~300-line GPT model definition" (nanoGPT)

這是他的教學哲學：**如果你真的理解了，就能用最少的程式碼寫出來。**

對應他的名言：「If I can't build it, I don't understand it.」

---

## 九、標誌性表達模式總結

| 模式 | 例子 | 作用 |
|------|------|------|
| 新詞命名 + 定義 | "vibe coding: fully give in to the vibes" | 創造概念，佔據話語權 |
| 版本號框架 | Software 1.0 / 2.0 / 3.0 | 把正規化變化變成可感知的升級 |
| 反轉常識 | "hallucination is not a bug, it's a feature" | 先接受通俗理解，再邏輯反轉 |
| 獨立短句 | "Strap in." / "Don't be a hero." | 製造停頓，強化記憶點 |
| 自嘲 + 精確 | "3e-4 is the best learning rate for Adam, hands down." | 幽默中藏著真實的技術判斷 |
| 時間軸拉長 | "year of agents" → "decade of agents" | 不直接否定，用時間視角隱含批評 |
| 用"imo"標記主張 | "Imo fair to say..." | 誠實標註自己判斷的邊界 |
| 類比過渡詞 | "it's kind of like" / "in some sense" | 鋪墊類比，降低理解門檻 |
| 承認不確定 | "I have a wide distribution here" | 認知誠實，建立信任 |
| 網際網路語氣詞 | "lol" / "skill issue" / "omg" | 技術大牛也很「網」 |

---

## 十、原文引用速查（按主題）

**關於LLM本質：**
- "LLMs are dream machines."
- "LLMs are people spirits."
- "They display jagged intelligence."
- "We're summoning ghosts."

**關於程式設計正規化：**
- "The hottest new programming language is English."
- "There's a new kind of coding I call 'vibe coding'."
- "I've never felt this much behind as a programmer."
- "A failure to claim the boost feels decidedly like a skill issue."
- "It's less Iron Man robots and more Iron Man suits."

**關於學習：**
- "If I can't build it, I don't understand it."
- "Reading a book is not learning but entertainment."
- "The qualities that correlate most strongly to success in deep learning are patience and attention to detail."

**關於炒作：**
- "This is the decade of agents."
- "Overall, the models are not there."
- "My general apathy and loss of trust in benchmarks in 2025."

**關於程式碼：**
- "Don't be a hero."
- "Backprop + SGD does not magically make your network work."
- "No need for 245MB of PyTorch."

---

*資訊源：*
- https://karpathy.ai/tweets.html
- https://x.com/karpathy/status/1886192184808149383
- https://karpathy.bearblog.dev/year-in-review-2025/
- https://x.com/karpathy/status/1733299213503787018
- https://singjupost.com/andrej-karpathy-software-is-changing-again/
- http://karpathy.github.io/2019/04/25/recipe/
- https://www.dwarkesh.com/p/andrej-karpathy
- https://github.com/karpathy/nanoGPT
- https://github.com/karpathy/llm.c
- http://karpathy.github.io/2026/02/12/microgpt/
