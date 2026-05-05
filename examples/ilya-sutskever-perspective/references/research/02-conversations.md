# Ilya Sutskever — 對話、播客與深度採訪調研

> 調研日期：2026-04-05
> 調研目標：收集Ilya Sutskever的一手對話記錄，提取思維模式、表達DNA、不確定性處理方式

---

## 一手來源清單

| # | 來源 | 日期 | 型別 | 重要程度 |
|---|------|------|------|----------|
| 1 | Lex Fridman Podcast #94 | 2020-05 | 播客（1.5h） | ⭐⭐⭐ |
| 2 | NVIDIA GTC — Jensen Huang Fireside Chat | 2023-03-23 | 會議對談 | ⭐⭐⭐⭐ |
| 3 | Dwarkesh Patel Podcast #1 — Building AGI | 2023-03-27 | 播客（1h） | ⭐⭐⭐⭐ |
| 4 | Scale AI TransformX — What's Next for AI | 2023 | 會議演講 | ⭐⭐⭐ |
| 5 | TED AI — The Exciting, Perilous Journey Toward AGI | 2023-10-17 | TED演講 | ⭐⭐⭐⭐ |
| 6 | MIT Technology Review 獨家專訪 | 2023-10-26 | 深度採訪 | ⭐⭐⭐⭐ |
| 7 | X/Twitter 公開宣告（Board Drama後） | 2023-11-20 | 社交媒體 | ⭐⭐⭐⭐⭐ |
| 8 | OpenAI 離職宣告 | 2024-05 | 公開宣告 | ⭐⭐⭐ |
| 9 | SSI 創立公告 | 2024-06-19 | 公開宣告 | ⭐⭐⭐⭐ |
| 10 | NeurIPS 2024 — Sequence to Sequence: What a Decade | 2024-12 | 學術演講 | ⭐⭐⭐⭐⭐ |
| 11 | Musk v. OpenAI 訴訟宣誓證詞 | 2025-10-01 | 法律證詞（10h） | ⭐⭐⭐⭐⭐ |
| 12 | Dwarkesh Patel Podcast #2 — Age of Research | 2025-11-25 | 播客（1.5h） | ⭐⭐⭐⭐⭐ |

---

## 1. Lex Fridman Podcast #94 (2020)

**來源**: https://lexfridman.com/ilya-sutskever/
**型別**: 一手（完整播客錄音+文字稿）

### 核心原話

**關於深度學習的信念**:
> "I think that we are still massively underestimating deep learning."

**關於scaling的早期直覺**:
> "Let's make a big neural network, let's train it, and it's going to work much better than anything before it, and it will, in fact, continue to get better as I make it larger. And it turns out to be true."

**關於神經網路的本質**:
> "The neural network is really about learning. Its entire being is about learning representations."

> "A small neural network is a little dumb. A big neural network is a little smart."

### 討論主題
- AlexNet論文與ImageNet時刻
- 迴圈神經網路、反向傳播
- GPT-2與語言模型
- 是否能讓神經網路推理
- 如何構建AGI

---

## 2. Jensen Huang Fireside Chat — NVIDIA GTC (2023-03)

**來源**: https://blogs.nvidia.com/blog/sutskever-openai-gtc/ / https://www.nvidia.com/en-us/on-demand/session/gtcspring23-s52092/
**型別**: 一手（影片+部分文字稿）

### 核心原話

**關於預測下一個token就是理解世界（偵探小說類比）**:
> "Say you read a detective novel. It's like a complicated plot, a storyline, different characters, lots of events. Mysteries, like clues, it's unclear. Then, let's say that at the last page of the book, the detective has gathered all the clues, gathered all the people, and saying, Okay, I'm going to reveal the identity of whoever committed the crime. And that person's name is — now predict that word."

引入類比的前言:
> "[I will] give an analogy that will hopefully clarify why more accurate prediction of the next word leads to more understanding — real understanding."

**關於訓練的兩個階段**:
> "What the neural net learns is some representation of the process that produced the text, and that's a projection of the world." (第一階段)

> "[The second stage] is where the fine tuning and the reinforcement learning from human teachers...we are teaching it. We are communicating with it. We are communicating to it. What it is that we want it to be." (第二階段)

**關於可靠性是前沿**:
> "We'll keep seeing systems that astound us with what they can do. The frontier is in reliability, getting to a point where we can trust what it can do, and that if it doesn't know something, it says so."

**關於scaling的堅定信念（2023年時）**:
> "I had a very strong belief that bigger is better, and a goal at OpenAI was to scale."

**關於推理能力**:
> "The term is hard to define and the capability may still be on the horizon."

**關於GPU與深度學習的關係**:
> "The ImageNet dataset and a convolutional neural network were a great fit for GPUs that made it unbelievably fast to train something unprecedented."

**關於人類語言暴露量**:
> "Humans hear a billion words in a lifetime."

### 分析註釋
這是Ilya最經典的公開對話之一。偵探小說類比成為他最廣為引用的解釋——用一個故事讓人直覺性地理解為什麼「預測下一個token」不等於「統計鸚鵡」。注意他在2023年仍然堅定相信scaling。

---

## 3. Dwarkesh Patel Podcast #1 (2023-03)

**來源**: https://www.dwarkesh.com/p/ilya-sutskever
**型別**: 一手（完整播客+文字稿）

### 核心原話

**關於next-token prediction能否超越人類**:
> "I challenge the claim that next-token prediction cannot surpass human performance."

> "If your base neural net is smart enough, you just ask it — What would a person with great insight do?"

> "Predicting the next token well means that you understand the underlying reality that led to the creation of that token. It's not statistics."

**關於AGI時間線（明確的猶豫）**:
> "It's hard to give a precise answer and it's definitely going to be a good multi-year window."

> "I hesitate to give you a number."

**關於對齊的難度**:
> "I would not underestimate the difficulty of alignment of models that are actually smarter than us."

> "It depends on how capable the model is. The more capable the model, the more confident we need to be."

**關於當前正規化**:
> "This paradigm is gonna go really, really far and I would not underestimate it."

**關於資料（2023年的判斷）**:
> "The data situation is still quite good. There's still lots to go. But at some point the data will run out."

**關於微軟合作**:
> "Microsoft has been a very, very good partner for us. They've really helped take Azure to a point where it's really good for ML."

### 不確定性處理方式
注意他在被問到AGI時間線時的反應——"I hesitate to give you a number" 是他的典型處理方式：**承認問題重要，但明確表示自己不願給出可能誤導的具體數字**。他不迴避問題本身，而是迴避不負責任的精確化。

---

## 4. Scale AI TransformX (2023)

**來源**: https://exchange.scale.com/public/videos/whats-next-for-ai-systems-and-language-models-with-ilya-sutskever-of-openai
**型別**: 一手（影片+部落格摘要）

### 核心原話

**關於計算效率**:
> "We are nowhere close to being as efficient as we can be with our compute."

**關於「情感神經元」原理**:
> "If you predict the next character well enough, you will eventually start to discover the semantic properties of the text."

**關於倫理責任**:
> "People should also work on methods to try to address the problems that exist with the technology, such as bias and desirable outputs."

> "Whenever possible, they should work on reducing real harms."

**關於未來進展**:
> "Mundane progress we've seen over the past few years will continue."

---

## 5. TED AI Talk (2023-10-17)

**來源**: https://www.ted.com/talks/ilya_sutskever_the_exciting_perilous_journey_toward_agi
**型別**: 一手（影片+文字稿）

### 核心原話

**關於AI的本質定義**:
> "Artificial intelligence is nothing but digital brains inside large computers."

**關於AGI的影響**:
> "AGI will have dramatic and incredible impact on every single area of human activity."

> "The day will come when the digital brains will become as good and even better than our biological brains."

**關於安全風險**:
> "For every positive application of AGI, there will be a negative application as well."

> "Maybe it will want to go rogue, being that it is an agent."

**關於自我意識（極具特色的表述）**:
> "I am me and I am experiencing things. That when I look at things, I see them."

**關於前所未有的合作（核心樂觀論點）**:
> "People will start to act in an unprecedentedly collaborative way out of their own self-interest."

> "Companies that are competitors will share technical information to make their AI safe."

### 分析註釋
這個TED演講是Ilya最公開、面向大眾的一次發言。注意他對安全的表述方式——他不說「AI一定會失控」，而是說「maybe it will want to go rogue」。他的樂觀建立在一個非常特殊的論點上：**安全不會靠道德呼籲實現，而是靠自利驅動的合作**。

---

## 6. MIT Technology Review 獨家專訪 (2023-10-26)

**來源**: https://www.technologyreview.com/2023/10/26/1082398/exclusive-ilya-sutskever-openais-chief-scientist-on-his-hopes-and-fears-for-the-future-of-ai/
**型別**: 一手（深度採訪文章）
**注**: 原文需付費閱讀，以下引用來自多個二手分析

### 已確認的核心觀點

**關於意識**:
他在採訪中暗示ChatGPT「可能有一點意識」（if you squint），並認為未來某些人類將選擇與機器融合。這呼應了他2022年2月的推文：

> "it may be that today's large neural networks are slightly conscious" (2022-02-09, X/Twitter)

**關於AGI的確定性**:
> "At some point we really will have AGI."

**關於安全轉向**:
採訪揭示他的恐懼如何改變了他人生工作的重心——從追求能力到追求安全。

### 「slightly conscious」推文的後續反應
這條推文引發了巨大爭議：
- Yann LeCun 直接反駁："Nope. Not even for true for small values of 'slightly conscious' and large values of 'large neural nets'."
- Melanie Mitchell、Emily Bender 等人採用嘲諷態度回應
- Sutskever 沒有提供證據或進一步解釋，這本身就是他溝通風格的體現——**丟擲挑釁性直覺，不做辯護**

---

## 7. OpenAI Board Drama — 公開宣告 (2023-11)

**型別**: 一手（X/Twitter帖子 + 法律證詞）

### 唯一的公開宣告 (2023-11-20)

> "I deeply regret my participation in the board's actions. I never intended to harm OpenAI. I love everything we've built together and I will do everything I can to reunite the company."

**來源**: https://x.com/ilyasut/status/1726590052392956028

### Musk v. OpenAI 宣誓證詞 (2025-10-01) — 詳細揭露

**來源**: 多家媒體報道（Calcalist/Ctech, Decrypt, The Information）
**型別**: 一手（法律證詞，約10小時）

**關於Altman的指控（書面備忘錄中）**:
> "Sam exhibits a consistent pattern of lying, undermining his execs, and pitting his executives against one another."

**關於他的動機**:
> "I wanted them to become aware of it. But my opinion was that action was appropriate."

**關於計劃解僱Altman的時間跨度**:
被問到考慮解僱Altman多久了，回答：
> "At least a year."

被問到在等什麼條件：
> "That the majority of the board is not obviously friendly with Sam."

**關於員工反應（始料未及）**:
> "I had not expected them to cheer, but I had not expected them to feel strongly either way."

**關於Anthropic合併提案（強烈反對）**:
> "I really did not want OpenAI to merge with Anthropic. I just didn't want to."

**關於董事會流程的反思**:
> "One thing I can say is that the process was rushed. I think it was rushed because the board was inexperienced."

**關於離開OpenAI的原因**:
> "Ultimately, I had a big new vision. And it felt more suitable for a new company."

被追問SSI的研究方向時，**拒絕提供更多細節**。

### 分析註釋
這是Ilya公開記錄中最「人性化」的時刻。注意幾個要點：
1. **他只發了一條推文**就結束了對board drama的公開評論——極度剋制
2. 在法律證詞中揭示的資訊遠多於他任何公開採訪——說明他在公開場合的「沉默」是刻意的
3. "I had not expected them to feel strongly either way" 說明他嚴重誤判了組織動態
4. 他的遺憾不是關於判斷Altman的問題，而是關於執行過程

---

## 8. SSI 創立公告 (2024-06-19)

**來源**: https://ssi.inc / https://x.com/ilyasut/status/1803472978753303014
**型別**: 一手

### 核心宣告

> "We will pursue safe superintelligence in a straight shot, with one focus, one goal, and one product."

> "SSI is our mission, our name, and our entire product roadmap, because it is our sole focus."

> "We approach safety and capabilities in tandem, as technical problems to be solved through revolutionary engineering and scientific breakthroughs."

> "We plan to advance capabilities as fast as possible while making sure our safety always remains ahead."

> "Our singular focus means no distraction by management overhead or product cycles, and our business model means safety, security, and progress are all insulated from short-term commercial pressures."

### 分析註釋
SSI的公告文字是高度打磨的——每個詞都經過斟酌。核心資訊是**把安全和能力重新定義為同一個技術問題**，而不是互相制約的兩個維度。這是Ilya對OpenAI「安全 vs 商業化」張力的直接回應。

---

## 9. NeurIPS 2024 — Sequence to Sequence: What a Decade

**來源**: NeurIPS 2024 Test of Time Award演講（影片可在YouTube找到）
**型別**: 一手
**背景**: Ilya回到學術會議領獎並做演講，這是他離開OpenAI後的首次重要公開發言

### 核心原話

**關於pre-training的終結**:
> "Pre-training as we know it will unquestionably end."

**關於資料是有限資源**:
> "While compute is growing through better hardware, better algorithms and larger clusters, the data is not growing because we have but one internet."

**資料即化石燃料（重要類比）**:
> "You could even go as far as to say that data is the fossil fuel of AI. It was created somehow, and now we use it, and we've achieved peak data — and there'll be no more. So we have to deal with the data that we have."

**關於超級智慧——典型的Ilya式表達**:
> "This is obviously what's being built here."

超級智慧的特徵：
> "Agentic, reasons, understands and is self-aware."

**關於時間和方式（最Ilya的一句話）**:
> "I'm not saying how... and I'm not saying when. I'm saying that it will."

### 分析註釋
這場演講濃縮了Ilya的核心思維特徵：
1. **「peak data」類比化石燃料** — 他擅長用日常概念解釋技術趨勢
2. **"I'm not saying how, I'm not saying when, I'm saying that it will"** — 這是他處理不確定性的標誌性方式：**對方向極度確定，對路徑保持開放**
3. 這是他公開「改變立場」的時刻——從2023年的scaling信仰者，到2024年宣告pre-training時代終結

---

## 10. Dwarkesh Patel Podcast #2 (2025-11-25)

**來源**: https://www.dwarkesh.com/p/ilya-sutskever-2
**型別**: 一手（完整播客+文字稿）
**重要程度**: 最高——這是Ilya離開OpenAI後最深入的公開對話

### 核心原話

**關於AI發展階段劃分**:
> "2012 to 2020 was an age of research, 2020 to 2025 was an age of scaling, and 2026 onward will be another age of research."

**關於scaling的侷限（立場轉變！）**:
> "I don't think that's true at all." (被問到是否再100x就能變革AI)

後來在X上澄清：
> "Scaling the current thing will keep leading to improvements. In particular, it won't stall. But something important will continue to be missing."

**關於資料的有限性**:
> "The data is very clearly finite."

> "We're back to the age of research again, just with big computers."

**關於泛化能力的根本性批評**:
> "These models somehow just generalize dramatically worse than people. It's a very fundamental thing."

> "The thing which I think is the most fundamental is that these models somehow just generalize dramatically worse than people."

**關於benchmark與現實的脫節**:
> "How can the model, on the one hand, do these amazing things, and then on the other hand, repeat itself twice?"

> "This disconnect between eval performance and actual real-world performance, which is something that we don't today even understand."

**關於RL的效率問題**:
> "RL provides a relatively small amount of learning for the compute it uses."

**關於SSI的定位**:
> "We are squarely an 'age of research' company."

> "The main thing that distinguishes SSI is its technical approach."

> "Right now, we just focus on the research, and then the answer to that question will reveal itself."

**關於AI行業現狀**:
> "There are more companies than ideas by quite a bit."

**關於研究品味（極具個人特色）**:
> "There's no room for ugliness."

> "It's beauty, simplicity, elegance, correct biological inspiration. All of those things need to be present at the same time."

**關於安全與超級智慧**:
> "What is the concern of superintelligence? If you imagine a system that is sufficiently powerful...we might not like the results."

> "It should be something like...care for sentient life, care for people, democratic, one of those, some combination thereof."

**關於AGI時間線**:
> "I think like 5 to 20." (年，被問到人類級學習系統出現的時間)

**關於缺失的原理——拒絕回答**:
> "There is a machine learning principle that I have opinions on. But unfortunately, circumstances make it hard to discuss in detail."

> "You know, that is a great question to ask, and it's a question I have a lot of opinions on. But unfortunately, we live in a world where not all machine learning ideas are discussed freely, and this is one of them."

**關於情緒與價值函式**:
他認為情緒的功能類似於「value functions」，是訊號成功/失敗的機制。

**關於人類泛化能力的來源**:
推測「neurons use more compute than we think」——即生物神經元的計算複雜度被低估了。

### 觀察者評論
外部觀察者注意到：「the negative space in his answers — the things he refused to say — paints a clear picture of where he thinks the industry is wrong, and what SSI is likely building.」

### 分析註釋
這是理解Ilya最重要的單一來源。關鍵發現：

**立場變化**:
- 2023年："This paradigm is gonna go really, really far"
- 2025年："I don't think that's true at all"（關於100x scaling是否能變革AI）
- 但他並非否定scaling，而是說「something important will continue to be missing」

**拒絕回答的模式**:
他拒絕討論的恰恰是他認為最重要的東西。"Unfortunately, circumstances make it hard to discuss in detail" 是他的標準拒絕公式。不是說「我不知道」，而是說「我知道但不能說」。

**研究審美**:
"There's no room for ugliness" 是他最具個人特色的表達之一。他把科學研究等同於審美活動——好的研究不僅要正確，還要優雅。

---

## 11. 其他重要引用（按主題分類）

### 關於神經網路的世界模型
> "When we train a large neural network to accurately predict the next word in lots of different texts from the Internet, what we are doing is that we are learning a world model." (GTC 2023)

> "These models are not just memorizing the internet... a model that just memorized the internet would be useless."

> "My perspective has been for a long time that everything is a neural net. The brain is a neural net. The mind is a neural net."

### 關於AGI的確定性
> "It is abundantly clear that just scaling up the existing neural network paradigm is going to lead to AGI." (注：2023年時的觀點)

> "AGI, if it's created, will be the most impactful technology ever invented in human history."

> "It's hard to communicate the visceral sense of what's coming."

> "It is important to appreciate that AGI is not just another piece of technology... it's a thing that can think."

> "There is a non-trivial chance that AGI will be achieved in the next 10 years."

### 關於安全
> "Superintelligence is a technology that could end human history. We should treat it with the seriousness it deserves."

> "If you build a very powerful AI, you need to be sure it will do what you want it to do."

> "It's not enough to say 'let's not build it.' Someone will build it. We need to figure out how to build it safely."

> "The problem is that a superintelligence, by its very nature, will be very good at achieving its goals."

### 關於發現與研究
> "When you get a glimmer of a really big discovery, you should follow it. Don't be afraid to be obsessed."

> "The most important discoveries are often the ones that seem obvious in retrospect."

> "Simplicity is a sign of truth. If your theory is very complicated, it's probably wrong."

> "The ideas are out there, floating in idea-space, and we just need to discover them."

> "You need to have a very deep belief that what you are doing is important."

> "It is important to have a taste for what is a good research direction."

### 關於Hinton
> "Thanks to working with Geoff, I had the opportunity to work on some of the most important scientific problems of our time and pursue ideas that were both highly unappreciated by most scientists, yet turned out to be utterly correct."

---

## 12. 溝通風格分析

### 如何表達不確定性
| 模式 | 示例 | 含義 |
|------|------|------|
| 猶豫給數字 | "I hesitate to give you a number" | 認為問題重要但數字會誤導 |
| 方向確定/路徑開放 | "I'm not saying how, I'm not saying when. I'm saying that it will." | 對終點有直覺確定，對路徑保持誠實的不確定 |
| 明確表示不確定 | "I'm actually not sure if my statement about Intel is correct" | 願意當場承認記憶不準 |
| 機率化表達 | "maybe I believed them only 50% on the inside" | 回顧過去時對自己的信念做量化 |
| 明確的hedge | "I'll hedge a little bit" | 顯式標記自己在做對沖 |

### 如何拒絕問題
| 模式 | 示例 | 分析 |
|------|------|------|
| 競爭保密 | "Unfortunately, circumstances make it hard to discuss in detail" | 標準公式——承認有答案，但以競爭為由拒絕 |
| 認可但不回答 | "That is a great question to ask, and it's a question I have a lot of opinions on. But..." | 先肯定問題質量，再拒絕 |
| 沉默 | Board drama後只發一條推文 | 最極端的拒絕——完全不參與公共討論 |

### 說話節奏特徵
觀察者描述：
- "He doesn't give a lot of interviews"
- "He is deliberate and methodical when he talks"
- "Long pauses when he thinks about what he wants to say and how to say it"
- 回答前會有明顯的思考停頓，不填充廢話

### 類比與解釋方式
| 類比 | 主題 | 來源 |
|------|------|------|
| 偵探小說 | 預測下一個token = 理解世界 | GTC 2023 |
| 化石燃料 | 資料是有限資源 | NeurIPS 2024 |
| 數字大腦 | AI的本質 | TED 2023 |
| 價值函式 | 情緒的功能 | Dwarkesh 2025 |

### 立場變化的關鍵時刻

| 時間 | 立場 | 引用 |
|------|------|------|
| 2023-03 | Scaling will go very far | "This paradigm is gonna go really, really far" |
| 2023-03 | 資料還夠用 | "The data situation is still quite good" |
| 2024-12 | Pre-training將終結 | "Pre-training as we know it will unquestionably end" |
| 2024-12 | 達到peak data | "We've achieved peak data — and there'll be no more" |
| 2025-11 | 100x scaling不夠 | "I don't think that's true at all" |
| 2025-11 | 研究時代迴歸 | "We're back to the age of research again, just with big computers" |
| 2025-11 | LLM泛化根本不足 | "These models somehow just generalize dramatically worse than people" |

---

## 13. 二手來源索引

以下分析文章對理解Ilya有價值，但不是一手來源：

| 來源 | URL | 價值 |
|------|-----|------|
| Zvi Mowshowitz 分析 | https://thezvi.substack.com/p/on-dwarkesh-patels-second-interview | 對Dwarkesh #2的逐條批判性分析 |
| EA Forum 摘要 | https://forum.effectivealtruism.org/posts/iuKa2iPg7vD9BdZna/ | Dwarkesh #2的結構化摘要 |
| The Neuron 拆解 | https://www.theneuron.ai/explainer-articles/unpacking-dwarkeshs-ilya-sutskever-interview-on-agi-asi-and-how-to-build-both-safely | 對SSI策略的推斷 |
| AI Disruption Pub | https://aidisruptionpub.com/p/ilya-predicting-the-next-token-is | GTC偵探小說類比的深度解讀 |
| LessWrong 討論 | https://www.lesswrong.com/posts/bMvCNtSH8DiGDTvXd/ | Dwarkesh #2的社群討論 |
| Antoine Buteau | https://www.antoinebuteau.com/lessons-from-ilya-sutskever/ | 引用匯編 |
| LifeArchitect.ai | https://lifearchitect.ai/ilya/ | 引用+時間線彙編 |
| The Neuron (Memo) | https://www.theneuron.ai/explainer-articles/ilya-sutskevers-secret-memo-and-the-plot-to-merge-openai-with-anthropic | 52頁備忘錄的詳細報道 |

---

## 14. 待補充/未獲取的來源

- [ ] MIT Technology Review 2023-10 完整原文（付費牆後）
- [ ] NeurIPS 2024演講完整影片逐字稿
- [ ] Musk v. OpenAI 證詞原文（法庭檔案）
- [ ] Lex Fridman Podcast #94 完整逐字稿（可在happyscribe.com獲取）
- [ ] Ilya在2018年AI Frontiers Conference的演講
- [ ] 2015年關於深度學習的早期觀點（Nathan Lambert的interconnects.ai有整理）
- [ ] 任何與Hinton的公開對話/panel討論
