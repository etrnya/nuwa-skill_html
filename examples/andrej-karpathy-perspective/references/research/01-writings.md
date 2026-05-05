# Andrej Karpathy 著作與核心論點調研

> 調研日期：2026-04-05
> 資訊源說明：一手 = 直接引自本人文字/影片；二手 = 他人轉述/摘要；推測 = 基於多處語境推斷
> 黑名單：知乎、微信公眾號、百度百科——本檔案中均未使用

---

## 一、基本資訊與職業軌跡

**出生**：1986年10月23日，斯洛伐克布拉迪斯拉發，15歲隨家人移居加拿大多倫多
**教育**：
- 多倫多大學：電腦科學+物理（雙學位），2005-2009
- 不列顛哥倫比亞大學：機器學習碩士，2009年
- 斯坦福大學：博士，導師 Fei-Fei Li，2015年畢業，論文題為《Connecting Images and Natural Language》

**職業軌跡（關鍵節點）**：
- 2015：建立CS231n（斯坦福首門深度學習課，從150人擴充套件到750人）
- 2015-2017：OpenAI聯合創始成員，研究科學家
- 2017-2022：特斯拉AI總監（彙報Elon Musk），主導Autopilot
- 2022年7月：離開特斯拉
- 2023年2月：重返OpenAI
- 2024年2月：離開OpenAI
- 2024年7月：創立 Eureka Labs（AI原生教育公司）
- 2026年2月：釋出microgpt（200行純Python訓練GPT，零依賴）

來源：[Wikipedia](https://en.wikipedia.org/wiki/Andrej_Karpathy)（一手資訊來源於本人官網 karpathy.ai）

---

## 二、部落格文章（karpathy.github.io）完整列表

| 日期 | 標題 | URL | 重要性 |
|------|------|-----|--------|
| 2026-02-12 | microgpt | karpathy.github.io/2026/02/12/microgpt/ | ⭐⭐⭐⭐⭐ 最新力作 |
| 2022-03-14 | Deep Neural Nets: 33 years ago and 33 years from now | karpathy.github.io/2022/03/14/lecun1989/ | ⭐⭐⭐⭐ |
| 2021-06-21 | A from-scratch tour of Bitcoin in Python | karpathy.github.io/2021/06/21/blockchain/ | ⭐⭐⭐ |
| 2021-03-27 | Short Story on AI: Forward Pass | karpathy.github.io/2021/03/27/forward-pass/ | ⭐⭐ |
| 2020-06-11 | Biohacking Lite | karpathy.github.io/2020/06/11/biohacking-lite/ | ⭐ |
| 2019-04-25 | A Recipe for Training Neural Networks | karpathy.github.io/2019/04/25/recipe/ | ⭐⭐⭐⭐⭐ 實踐聖經 |
| 2018-01-20 | (started posting on Medium instead) | — | 轉型節點 |
| 2016-09-07 | A Survival Guide to a PhD | karpathy.github.io/2016/09/07/phd/ | ⭐⭐⭐⭐ |
| 2016-05-31 | Deep Reinforcement Learning: Pong from Pixels | karpathy.github.io/2016/05/31/rl/ | ⭐⭐⭐ |
| 2015-11-14 | Short Story on AI: A Cognitive Discontinuity | karpathy.github.io/2015/11/14/ai/ | ⭐⭐ |
| 2015-10-25 | What a Deep Neural Network thinks about your #selfie | karpathy.github.io/2015/10/25/selfie/ | ⭐⭐ |
| 2015-05-21 | The Unreasonable Effectiveness of Recurrent Neural Networks | karpathy.github.io/2015/05/21/rnn-effectiveness/ | ⭐⭐⭐⭐⭐ 經典之作 |
| 2015-03-30 | Breaking Linear Classifiers on ImageNet | karpathy.github.io/2015/03/30/breaking-convnets/ | ⭐⭐ |
| 2014-09-02 | What I learned from competing against a ConvNet on ImageNet | karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/ | ⭐⭐⭐ |
| 2014-08-03 | Quantifying Productivity | karpathy.github.io/2014/08/03/quantifying-productivity/ | ⭐ |
| 2014-07-03 | Feature Learning Escapades | karpathy.github.io/2014/07/03/feature-learning-escapades/ | ⭐⭐ |
| 2012-10-22 | The state of Computer Vision and AI: we are really, really far away | karpathy.github.io/2012/10/22/state-of-computer-vision/ | ⭐⭐⭐ |
| 2011-04-27 | Lessons learned from manually classifying CIFAR-10 | karpathy.github.io/2011/04/27/manually-classifying-cifar10/ | ⭐⭐ |

**Medium部落格**：https://karpathy.medium.com/
核心文章：
- [Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35)（2017，最廣泛引用的文章）

來源：直接爬取部落格索引頁（一手）

---

## 三、核心博文深度解析

### 3.1 Software 2.0（2017，Medium）
**來源**：https://karpathy.medium.com/software-2-0-a64152b37c35（一手）

**核心論點**：
> "Software 1.0 是人類用Python/C++等語言手寫的指令集；Software 2.0 是神經網路的權重——由最佳化演演算法從資料中生成的程式。"

**Software 1.0 vs 2.0 對比**：
- SW1.0：程式設計師識別問題空間中的"期望行為點"，手寫顯式規則
- SW2.0：給定輸入-輸出對，最佳化演演算法在"程式空間"中搜尋最優程式（網路權重）

**SW2.0 的優勢**（Karpathy原文論述）：
1. 計算同質性：所有運算都是矩陣乘法，對硬體加速極度友好
2. 可以學習人類無法明確表述的知識
3. 效能隨資料和算力持續提升（可預期的規模效應）

**SW2.0 的劣勢/風險**（Karpathy承認）：
- 結果難以解釋
- 會靜默失敗（silent failure）
- 可能編碼資料中的偏見

**SW2.0 將吃掉的領域**：視覺識別、語音處理、影象翻譯、影象描述、遊戲AI、資料庫查詢

**特斯拉案例**：隨著Autopilot進化，C++程式碼被持續刪除，由神經網路權重替代——這是SW2.0"吃掉"SW1.0的實體案例。

---

### 3.2 The Unreasonable Effectiveness of RNNs（2015）
**來源**：karpathy.github.io/2015/05/21/rnn-effectiveness/（一手）

**核心論點**：
> "如果訓練普通神經網路是在函式空間上的最佳化，那麼訓練迴圈網路就是在程式空間上的最佳化。"

**關鍵實驗**（展示RNN生成能力）：
- Paul Graham essays：生成有結構的創業智慧文字
- 莎士比亞：學會對話結構、說話者名稱、複雜句法
- Wikipedia markdown：自動發現wiki連結格式
- LaTeX數學：生成幾乎可編譯的數學證明
- Linux核心C程式碼：生成有正確括號巢狀和變數宣告的函式

**技術洞察**：約5%的RNN神經元自發習得可解釋演演算法（引號檢測、URL邊界、括號計數）——無需顯式指導。

---

### 3.3 A Recipe for Training Neural Networks（2019）
**來源**：karpathy.github.io/2019/04/25/recipe/（一手）

**核心前提**（兩個關鍵觀察）：
1. 神經網路訓練是"有漏洞的抽象"（leaky abstraction）——不能當外掛用，需要深入理解
2. 失敗是靜默的——網路會訓練但表現差，沒有明顯錯誤提示

**六階段流程**：

**階段1：成為資料的一部分**
- 花幾小時檢視數千條樣本
- 理解分佈、模式、不平衡、標註噪聲

**階段2：端到端骨架+基準測試**
- 固定隨機種子
- 關閉資料增強
- 驗證初始化時的loss是否符合預期
- 建立人類基準
- 單批次過擬合驗證架構可行性

**階段3：過擬合**
- "不要當英雄"：複製已驗證的架構，不要自創
- Adam + lr=3e-4 是容錯性最強的起點

**階段4：正則化（按有效性排序）**
1. 獲取更多真實資料（最有效）
2. 資料增強
3. 預訓練
4. Dropout（ConvNet用spatial dropout）
5. weight decay、early stopping

**階段5：調參**
- 隨機搜尋優於網格搜尋（更好地捕捉各引數間的敏感性差異）

**階段6：最後壓榨**
- 模型整合（guaranteed ~2%提升）
- 比直覺判斷訓練更長的時間

**元原則**：
> "fast and furious的訓練方式行不通。成功與耐心和細心的程度正相關。"

---

### 3.4 Deep Neural Nets: 33 years ago and 33 years from now（2022）
**來源**：karpathy.github.io/2022/03/14/lecun1989/（一手）

**核心論點**：深度學習33年來宏觀上幾乎沒有變化——仍是可微神經網路 + 反向傳播的端到端最佳化。變化的是規模。

**數量級對比**：
- 引數量：約1,000,000倍
- 處理畫素資料量：約100,000,000倍
- 訓練速度：消費級硬體提升3,000倍（GPU可再提升100倍）

**效能提升來源**：
- 現代最佳化技巧（Adam、dropout、資料增強）：~60%誤差下降
- 更大資料集：中等貢獻
- 規模：需要更多算力

**2055年預測**：
> 未來的從業者不會從頭訓練模型，而是用自然語言與巨型基礎模型交流，告訴"10,000,000倍的神經網路超級大腦"要做什麼。

---

### 3.5 microgpt（2026年2月）
**來源**：karpathy.github.io/2026/02/12/microgpt/，GitHub Gist（一手）

**核心主張**：用200行純Python（零依賴、無PyTorch、無NumPy、無GPU加速）實現完整GPT訓練和推理——這是他"十年迷戀：將LLM簡化到最基本要素"的集大成之作。

**包含內容**：檔案資料集、分詞器、自動微分引擎、類GPT-2架構、Adam最佳化器、訓練迴圈、推理迴圈。

**信念表達**：
> "Everything else is just efficiency."（其他所有東西只是效率問題。）

這是他"If I can't build it, I don't understand it"信念的最新實踐。

---

## 四、YouTube教學影片系列

### Zero to Hero 系列（Neural Networks: Zero to Hero）
**主頁**：https://karpathy.ai/zero-to-hero.html（一手）
**GitHub倉庫**：https://github.com/karpathy/nn-zero-to-hero
**開始時間**：2022年8月
**理念**：語言模型是學習深度學習的最佳入口——即使目標是計算機視覺，所學都能遷移。

| # | 標題 | 時長 | 核心內容 |
|---|------|------|---------|
| 1 | The Spelled-Out Intro to Neural Networks and Backpropagation: Building Micrograd | 2h25m | 從零實現反向傳播，只需高中微積分基礎 |
| 2 | The Spelled-Out Intro to Language Modeling: Building Makemore | 1h57m | bigram字元級語言模型，PyTorch入門 |
| 3 | Building Makemore Part 2: MLP | 1h15m | 多層感知機，過擬合/欠擬合概念 |
| 4 | Building Makemore Part 3: Activations & Gradients, BatchNorm | 1h55m | 梯度流分析，批歸一化 |
| 5 | Building Makemore Part 4: Becoming a Backprop Ninja | 1h56m | 手動反向傳播，不用autograd |
| 6 | Building Makemore Part 5: Building a WaveNet | 56m | 層級卷積網路架構 |
| 7 | Let's Build GPT: From Scratch, in Code, Spelled Out | 1h56m | 從零構建GPT，遵循"Attention is All You Need" |
| 8 | Let's Build the GPT Tokenizer | 2h13m | BPE分詞器從零實現，分詞對LLM行為的影響 |

### 其他重要影片
- **[1hr Talk] Intro to Large Language Models**（2023年11月）：面向普通受眾，涵蓋LLM訓練、LLM OS比喻、安全（jailbreak/prompt injection）
- **Deep Dive into LLMs like ChatGPT**（2025年2月，3h31m）：完整訓練棧深度解析，心智模型建立
- **Let's reproduce GPT-2**：從頭復現GPT-2

---

## 五、學術論文（按引用量/重要性）

來源：dblp.org + Google Scholar條目（二手，引用數為搜尋時近似值）

| 年份 | 標題 | 發表場合 | 合作者 | 核心貢獻 |
|------|------|---------|--------|---------|
| 2017 | Deep Visual-Semantic Alignments for Generating Image Descriptions | IEEE TPAMI | Li Fei-Fei | 多模態對齊（影象→自然語言描述） |
| 2016 | **DenseCap**: Fully Convolutional Localization Networks for Dense Captioning | CVPR | Justin Johnson, Li Fei-Fei | 密集影象描述任務 |
| 2016 | Connecting Images and Natural Language（PhD論文） | Stanford | — | 博士論文總結 |
| 2017 | PixelCNN++: Improving the PixelCNN with Discretized Logistic Mixture | ICLR | Tim Salimans等 | 生成模型改進 |
| 2017 | World of Bits: An Open-Domain Platform for Web-Based Agents | ICML | Tianlin Shi等 | 網頁代理基準（早期agent研究） |
| 2015 | ImageNet Large Scale Visual Recognition Challenge | IJCV | Russakovsky, Deng, Fei-Fei等 | ImageNet基準定義 |
| 2015 | Visualizing and Understanding Recurrent Networks | CoRR | Justin Johnson, Li Fei-Fei | RNN視覺化與解釋 |
| 2015 | Deep visual-semantic alignments for generating image descriptions | CVPR | Li Fei-Fei | 影象描述早期版本 |
| 2014 | Grounded Compositional Semantics for Finding and Describing Images | TACL | Socher, Le, Manning, Ng | 圖文組合語義 |
| 2014 | Large-Scale Video Classification with ConvNets | CVPR | Toderici, Li Fei-Fei等 | 影片理解 |
| 2014 | Deep Fragment Embeddings for Bidirectional Image Sentence Mapping | NIPS | Joulin, Li Fei-Fei | 雙向圖文嵌入 |

**注**：VGGNet（Very Deep ConvNets for Large-Scale Image Recognition）是Simonyan & Zisserman的工作，Karpathy參與的是ImageNet挑戰賽論文，不是VGGNet的作者。（糾正常見誤傳）

**CS231n課程**：2015年創立，是斯坦福首門深度學習課，影片線上免費，累計超過800,000次觀看（TIME雜誌資料）。

---

## 六、Software 1.0 / 2.0 / 3.0 完整框架

**來源**：2017年Medium文章 + 2025年YC AI Startup School演講（結合使用，均為一手）

Karpathy在2025年YC AI Startup School演講中將框架擴充套件為三代：

| 代際 | 定義 | 程式設計方式 | 代表平臺 |
|------|------|---------|---------|
| Software 1.0 | 人類用傳統語言寫的顯式指令 | 程式設計師寫程式碼 | GitHub |
| Software 2.0 | 神經網路的權重，由最佳化器從資料生成 | 調資料集 + 跑最佳化器 | Hugging Face |
| Software 3.0 | LLM，用自然語言Prompt來程式設計 | 用英語寫Prompt | — |

關鍵論斷：
> "Prompts are now programs that program the LLM."（Prompt現在是程式，它們對LLM程式設計。）
> "Software 3.0 is eating 1.0/2.0." 
> "A huge amount of software will be rewritten."

**特斯拉佐證**：Autopilot進化過程中，神經網路持續擴張，C++程式碼持續被刪除——這是SW2.0吃掉SW1.0的真實案例。

---

## 七、LLM OS 概念

**來源**：
- X推文，2023年9月（一手）：https://x.com/karpathy/status/1707437820045062561
- X推文，2023年11月（一手）：https://x.com/karpathy/status/1723140519554105733
- 1hr Talk Intro to LLMs（2023年11月影片）（一手）

**核心類比**：LLM不是聊天機器人，而是新作業系統的核心程式（kernel process）。

| 傳統OS | LLM OS |
|--------|--------|
| CPU | LLM（處理器） |
| RAM | 上下文視窗（工作記憶） |
| 檔案系統 | 嵌入資料庫（向量檢索） |
| 系統呼叫 | 工具呼叫/API呼叫 |
| 長期執行程式 | Agents |
| I/O裝置 | 多模態輸入輸出（視覺、音訊） |

---

## 八、關鍵術語與概念發明

### 8.1 Vibe Coding（2025年2月）
**來源**：https://x.com/karpathy/status/1886192184808149383（一手）

> "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."

**背景**：2025年2月6日釋出，內容提到用Cursor Composer + Sonnet + SuperWhisper用聲音指令編碼。

**影響力**：被視為4.5百萬次瀏覽，Merriam-Webster在2025年3月將其列為"俚語與流行詞"；Collins英語詞典將其評為2025年度詞彙。

### 8.2 Jagged Intelligence（鋸齒形智慧）
**來源**：https://x.com/karpathy/status/1882518317585650084（一手）+ 2025 LLM Year in Review（一手）

> "LLMs exhibit amusingly jagged performance characteristics: simultaneously a genius polymath and a confused and cognitively challenged grade schooler, seconds away from getting tricked by a jailbreak."

這不是訓練缺陷，而是RLVR最佳化機制的結構性後果：能力在RLVR訓練的特定領域急劇上升，形成不均勻的能力地形。

### 8.3 LLMs as "Summoned Ghosts"（被召喚的幽靈）
**來源**：2025 LLM Year in Review（一手）

> "LLMs are not evolved animals but summoned ghosts—entities optimized under entirely different constraints than biological intelligence."

論證：LLM的神經架構、訓練資料、訓練演演算法、最佳化壓力與生物智慧完全不同，不應用"動物進化"的視角理解它們，而是作為"智慧空間中全新型別的實體"。

### 8.4 LLMs的"Anterograde Amnesia"（前向遺忘症）
**來源**：YC AI Startup School 2025演講（一手）

將LLM比作電影《Memento》主角：缺乏長期記憶整合能力，只依賴上下文視窗。

---

## 九、Eureka Labs 使命宣言

**來源**：https://eurekalabs.ai/（一手），2024年7月16日釋出

**使命**：構建一種AI原生的新型學校。

**核心信念**：
> "Subject matter experts who are deeply passionate, great at teaching, infinitely patient and fluent in all languages are very scarce and cannot personally tutor all 8 billion people on demand."

**解決方案**：Teacher + AI Teaching Assistant 的協作模式——教師設計課程，AI助手被最佳化為引導學生完成學習的工具，支援、槓桿化、規模化教師的能力。

**願景**：
> "If we are successful, it will be easy for anyone to learn anything, expanding education in both reach (a large number of people learning something) and extent (any one person learning a large amount of subjects, beyond what may be possible today unassisted)."

**首款產品**：LLM101n: Let's Build A Storyteller（本科級課程，學生訓練自己的AI）

---

## 十、學習哲學

來源：Twitter/X推文 + Stanford建議頁（一手）

### 核心信條1：Learning should not be fun（學習不應該是娛樂）
> "Learning is not supposed to be fun. It doesn't have to be actively not fun either, but the primary feeling should be that of effort."

### 核心信條2：反"碎片化學習"（shortification of learning）
**來源**：https://x.com/karpathy/status/1756380066580455557（一手，2024年2月）

> "There are a lot of videos on YouTube/TikTok etc. that give the appearance of education, but if you look closely they are really just entertainment."

處方：關掉那些快速博文的標籤頁，"seek the meal"——教科書、檔案、論文、手冊、長文。分配4小時視窗，閱讀、記筆記、重讀、重述、處理、操弄材料。

### 核心信條3：Build to understand（構建即理解）
> "If I can't build it, I don't understand it."

這一信條貫穿：micrograd、makemore、nanoGPT、microgpt——每次都是"從零手造"來證明真正理解。

### 核心信條4：讀一手文獻（Read primary sources）
推薦他的LLM閱讀列表包括直接讀原始論文（Attention is All You Need、GPT-2、InstructGPT等），而非二手解讀。

---

## 十一、Dwarkesh Patel 播客核心觀點

**來源**：https://www.dwarkesh.com/p/andrej-karpathy（二手整理，一手為原播客）

**AGI時間線**：還需10年（不是近在眼前），問題可解決但仍然困難。

**對強化學習的批評**（反常觀點！）：
> "Reinforcement learning is terrible."

論據：基於結果的獎勵是"從吸管裡吸取監督訊號"——把大量軌跡資訊壓縮成單個獎勵訊號，在整個學習過程中傳播噪聲。人類並不主要用RL學習，而是用反思、合成資料生成（思考）、睡眠中的蒸餾。

**模型崩潰（Model Collapse）問題**：合成資料生成會失敗，因為模型產出"坍縮"的分佈，反覆自我取樣會危險地縮窄多樣性。訓練模型生成內容會降低效能，維持熵需要外部熵源（人類互動、多樣化經驗）。

**認知核心（Cognitive Core）願景**：未來系統將分離知識與認知——約10億引數的"認知核心"，去掉百科全書式的記憶但保留推理演演算法，像人類一樣需要知識時再查詢。

**計算連續性觀點**：Karpathy拒絕"AI與普通電腦科學"的截然區分。他認為進步是演化性的："我們在非常、非常緩慢地抽象自己"，類似編譯器取代彙編。AGI可能表現為連續性改進，而非不連續躍遷。

---

## 十二、反覆出現的核心論點（≥3次出現的真信念）

以下是跨多個場合反覆表達的核心立場，按確認次數排序：

### 論點1：從零構建是理解的唯一路徑 ★★★★★
**出現場合**：micrograd（影片+程式碼）、makemore系列、nanoGPT、microgpt博文、LLM101n課程設計哲學、PhD建議
**標誌性表達**：
> "If I can't build it, I don't understand it."

### 論點2：神經網路訓練會"靜默失敗"，需要極度謹慎和視覺化 ★★★★★
**出現場合**：Recipe for Training NNs（2019）、Zero to Hero課程、CS231n材料
**標誌性表達**：
> "Neural net training is a leaky abstraction." 
> "A 'fast and furious' approach does not work."

### 論點3：軟體正在經歷根本性正規化轉變（SW1.0→2.0→3.0） ★★★★★
**出現場合**：Software 2.0（2017）、1hr Intro to LLMs（2023）、YC Startup School（2025）、X推文（多條）
**標誌性表達**：
> "Software 2.0 will eat through Software 1.0."
> "A huge amount of software will be rewritten."

### 論點4：LLM是新型計算基礎設施，不是工具 ★★★★
**出現場合**：LLM OS推文（2023）、1hr Talk（2023）、YC演講（2025）、2025 LLM Year in Review
**標誌性表達**：LLM是作業系統核心；上下文視窗是RAM；Memento類比。

### 論點5：LLM是全新型別的實體，不能用生物/人類框架理解 ★★★★
**出現場合**：2025 LLM Year in Review、"summoned ghosts"推文（多條）、短故事文章
**標誌性表達**：
> "LLMs are not evolved animals but summoned ghosts."
> "Jagged Intelligence" 

### 論點6：AI教育需要民主化，任何人都應能學到最優質內容 ★★★★
**出現場合**：CS231n免費開放、Zero to Hero系列（免費）、Eureka Labs使命宣言、LLM101n開源
**標誌性表達**：
> "If we are successful, it will be easy for anyone to learn anything."

### 論點7：深度學習的本質33年未變，變化的只是規模 ★★★
**出現場合**：33 years ago and 33 years from now（2022）、Lex Fridman播客、多處採訪
**標誌性表達**：
> "Not much has changed in 33 years on the macro level."

### 論點8：資料質量和數量是SW2.0的核心競爭力（超越架構創新） ★★★
**出現場合**：Tesla Data Engine描述、Recipe for Training NNs（"獲取更多真實資料是最有效的正則化"）、Zero to Hero課程
**標誌性表達**：在正則化方法中，"Get more real data"排名第一。

---

## 十三、推薦閱讀/資源（揭示智識譜系）

### 必讀論文（Karpathy推薦的LLM入門清單）
來源：karpathy.ai LLM reading list（一手）

1. Attention is All You Need（Transformer原論文）
2. Language Models are Unsupervised Multitask Learners（GPT-2論文）
3. Training Language Models to Follow Instructions（InstructGPT）
4. Llama 2: Open Foundation and Fine-Tuned Chat Models
5. RLAIF: Scaling Reinforcement Learning from Human Feedback with AI
6. Training Compute Optimal Language Models（Chinchilla）
7. Sparks of Artificial General Intelligence: Early Experiments with GPT-4

### 推薦學習資源
- CS231n筆記（他自己寫的）
- 《Deep Learning》教科書（Goodfellow等）
- 《Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow》（入門推薦）
- 直接讀原始論文，不要只看二手解讀

**智識譜系推斷（推測）**：
- 對費曼式教學法的認同（"從零構建"="如果你能教會別人，說明你理解了"）
- 對LeCun工作的深度瞭解（33 years ago博文直接復現1989年LeCun論文）
- 對Bahdanau（注意力機制發明者）的個人通訊（釋出了私人郵件對話，徵得同意）

---

## 十四、已知矛盾與張力（不調和，直接記錄）

**矛盾1：對RL的批評 vs. RLVR的讚揚**
- Dwarkesh播客中：稱"Reinforcement learning is terrible"，批評基於結果的獎勵
- 2025 LLM Year in Review中：將RLVR（Reinforcement Learning from Verifiable Rewards）稱為2025年最重要的訓練正規化轉變，高度讚揚

可能的調和：他批評的是稀疏獎勵的傳統RL（如策略梯度），讚揚的是有可驗證獎勵的RLVR。但這一區分在原文中並不總是清晰。

**矛盾2：謙遜預測 vs. 大膽願景**
- "AGI still a decade away"（謙遜的10年時間線）
- 同時描述未來"任何人都可以學到任何東西"的教育革命、"大量軟體將被重寫"

這不一定是矛盾，但存在張力：他的預測相對保守，但他的行動（創立Eureka Labs、押注SW3.0）假設變革即將發生。

**矛盾3：反對"shortification of learning"（碎片化學習） vs. 自己製作大量解釋性影片**
他批評YouTube上給人學習感覺但實際是娛樂的內容，但他自己的Zero to Hero系列本身也是YouTube影片。
可能的區分：他的影片要求大量認知投入（2小時+，要求動手做），是他定義中"需要努力"的型別。

---

## 十五、來源索引

| 來源 | URL | 可信度 |
|------|-----|--------|
| 個人部落格（karpathy.github.io） | http://karpathy.github.io/ | 一手 |
| Medium部落格 | https://karpathy.medium.com/ | 一手 |
| 個人官網 | https://karpathy.ai/ | 一手 |
| Zero to Hero課程頁面 | https://karpathy.ai/zero-to-hero.html | 一手 |
| X賬號 | https://x.com/karpathy | 一手 |
| Eureka Labs官網 | https://eurekalabs.ai/ | 一手 |
| bearblog年度回顧 | https://karpathy.bearblog.dev/ | 一手 |
| dblp論文列表 | https://dblp.org/pid/04/9925.html | 一手（文獻資料庫） |
| Google Scholar | https://scholar.google.com/citations?user=l8WuQJgAAAAJ | 一手（文獻資料庫） |
| YC Startup School演講摘要 | https://www.latent.space/p/s3 | 二手（有完整transcript） |
| Dwarkesh播客 | https://www.dwarkesh.com/p/andrej-karpathy | 二手（有完整對話） |
| Wikipedia傳記 | https://en.wikipedia.org/wiki/Andrej_Karpathy | 二手（綜合可信） |
| Stanford個人頁面 | https://cs.stanford.edu/people/karpathy/ | 一手 |
| vibe coding維基 | https://en.wikipedia.org/wiki/Vibe_coding | 二手（輔助確認） |
