# 外部視角：別人眼中的 Andrej Karpathy

> 調研日期：2026-04-05
> 資訊範圍：截至 2026 年 4 月的公開資料
> 來源可信度標註：★★★（高）/ ★★（中）/ ★（低/推斷）

---

## 一、同行與同事的評價

### Sam Altman

- Karpathy 第二次迴歸 OpenAI（2023年2月）時，Altman 在 X 上發推「@karpathy welcome back!」。★★★
- **核心分歧**：Altman 預測 AI 將在 2030 年前超越任何專業領域的人類智慧；Karpathy 則稱自己的 AGI 時間線「比主流預測悲觀 5 到 10 倍」。Karpathy 曾在公開場合直接反駁 Altman、Dario Amodei、Jensen Huang 的樂觀預測，稱他們「誇大了 AI 的能力」。★★★（Fortune 報道，2025年10月）

### Ilya Sutskever

- 兩人幾乎同時離開 OpenAI（Karpathy 2024年2月，Sutskever 2024年6月），但原因和走向完全不同。
- Sutskever 參與了 2023年11月推翻 Altman 的董事會政變；Karpathy 自始至終與 OpenAI 保持友好關係，與 Sutskever 路徑明顯分叉。
- 外部觀察者：「兩人分別代表 AI 將成為你的導師（Karpathy）和 AI 將成為你的神明（Sutskever）這兩種根本不同的願景。」★★

### Andrew Ng

兩人均是深度學習教育領域的核心人物，但在「vibe coding」概念上有正面交鋒。

Ng 在 2025年6月 LangChain Interrupt 活動中發言：「很遺憾這個東西叫 vibe coding，這個名字會誤導人們以為工程師只是隨便感覺一下。實際上，引導 AI 寫出有用的軟體是一項深度智識工作。我用 AI 輔助程式設計工作一整天，坦率地說，結束時我精疲力竭。」★★★

Ng 並非否定 AI 輔助程式設計本身，而是認為 Karpathy 的命名方式造成了認知誤導。

### Richard Sutton（RL 領域奠基人）

Karpathy 與 Sutton 之間有實質性的學術路線分歧。Karpathy 提出「我們在 summoning ghosts（召喚鬼魂）」，反駁 Sutton 的「我們在 building animals（培育動物）」框架。

Sutton 認為 LLM 是「dead end（死衚衕）」，強調 RL 和 continual learning 才是正途；Karpathy 不認同 RL 作為主路線，稱其為「用吸管吮吸監督訊號」（sucking supervision through a straw），存在根本性的噪聲問題。★★★

### Fei-Fei Li（博士導師）

兩人共同開設 Stanford CS231n，課程從 2015年的 150 人增長到 2017年的 750 人，側面印證了外界對這門課的高度認可。沒有找到 Fei-Fei Li 公開評價 Karpathy 的直接宣告。★★（間接證據）

---

## 二、離職事件的行業反應

### 離開 Tesla（2022年7月）

行業反應較為震驚。Fortune 標題：「誰是 Andrej Karpathy？Tesla AI 主管突然辭職，這對 Elon Musk 意味著麻煩。」★★★

外部分析（Medium）：離職的「真實原因」可能是 Musk 對 FSD 過於樂觀的公開承諾與 Karpathy 實際工程認知之間的長期張力——Karpathy 從不公開誇大進度。★（推測性分析，可信度有限）

### 離開 OpenAI（2024年2月）

Karpathy 本人的表述：「什麼都沒發生，不是任何事件或戲劇的結果。」TechCrunch 標題：「Andrej Karpathy 再次離開 OpenAI——但他說沒有任何戲劇性事件。」★★★

與 Sutskever 同時期離職形成對比，外部媒體普遍將兩者捆綁報道，但實際原因截然不同：Karpathy 是主動選擇，Sutskever 是政治失敗後的出走。

---

## 三、「Vibe Coding」概念引發的爭議

### 原始定義

「有一種新的程式設計方式，我稱之為 vibe coding——你完全沉浸於 vibes 中，擁抱指數增長，忘記程式碼甚至存在。」★★★

### 支持者的論點

Simon Willison（Django 聯合創始人）：高度讚賞 Karpathy 的原始定義，認為「精準且有趣」，因為 Karpathy 是頂級程式設計師，他用這個詞描述的是一種具體的探索模式，而非主張放棄理解。★★★

### 批評者的論點

1. **Andrew Ng 的命名批評**：術語本身具有誤導性，讓人以為工程是「隨便感覺」，實際上 AI 輔助程式設計是繁重的智識工作。★★★
2. **安全漏洞風險**：CodeRabbit 2025年12月分析發現，AI 協作程式碼比人類程式碼安全漏洞率高 2.74 倍。★★★
3. **可維護性問題**：Fast Company 報道「vibe coding 宿醉」——senior 工程師描述接手 AI 生成程式碼庫後陷入「開發地獄」。★★★
4. **初學者技能退化**：批評者擔心 vibe coding 消滅了新手程式設計所需的入門級任務，破壞技能梯隊。★★

### 2026 年的反轉

Karpathy 自己宣佈 vibe coding「已經過時」，他的新偏好詞是「agentic engineering」：「預設情況下，你 99% 的時間不是在直接寫程式碼，而是在編排 agents 並擔任監督者角色。」★★★

---

## 四、「Job Risk Map」刪除事件（2026年3月）

### 事件經過

Karpathy 用兩小時「vibe coded」了一個互動式圖表，對 342 個 BLS 職業進行 AI 暴露度評分（0-10 分）。圖表顯示白領職業評分最高，體力勞動職業評分最低。Elon Musk 轉發並評論「所有工作都將是可選的」，圖表迅速病毒式傳播。

數小時內，Karpathy 刪除了 GitHub 倉庫。他的解釋：「'暴露度'是 LLM 根據工作數字化程度打分的。這與這些職業實際會發生什麼無關。人們在歪曲這個視覺化工具，把話塞進我嘴裡。」★★★

### 社群批評

- **方法論缺陷**：用 LLM 打分作為勞動市場替代指標，在方法上過於粗糙。
- 這一事件被部分觀察者解讀為 Karpathy「公開試驗文化」的代價：他願意公開半成品想法，但當這些想法被媒體放大時，選擇退縮而非承擔辯論。★★

---

## 五、Eureka Labs 的外部評價

### 期待

TechCrunch 報道基調正面，將其視為自然延伸：從斯坦福 CS231n 到 YouTube 教學影片，再到正式創業。★★★

### 質疑與批評（Dan Meyer，數學教育者）

Dan Meyer 在 Substack 撰文《Andrej Karpathy Is in Trouble》，是迄今最有分量的公開批評：

- **前人失敗先例**：Sebastian Thrun 的 Udacity、Andrew Ng 的 Coursera，均是技術精英線上教育領域的先行者，但都未能實現宏大的教育轉型目標。
- **核心矛盾**：「很少有設計教育軟體的人有成功管理課堂或學校的經驗。」Karpathy 幫助構建了世界上最先進的計算技術，但他需要將全部創造力投入「幫助人們學習」這一更難的任務。
- **學習規模化的歷史失敗**：「每一種承諾規模化學習的技術都辜負了其宣傳。」★★★

---

## 六、AI 學習者社群的評價

### 高度正面的評價（主流聲音）

- Google Scholar 顯示超過 78,000 次引用（截至調研時）。★★★
- 「Zero to Hero」課程被廣泛認為是深度學習領域最好的入門課程之一。DeepLearning.AI 將其列為「Heroes of Deep Learning」。★★★
- 教學風格被高度評價為「真實」：強調「不要抽象掉任何東西」，實時編碼並展示錯誤修復。

### 細微的批評（少數聲音）

- 少數學習者認為課程假設學習者已有相當基礎，「zero to hero」名稱有些誇張。
- Hacker News 上對 Eureka Labs 的討論：部分人期待，部分人持「證明給我看」的觀望態度。

---

## 七、學術影響力與同代人對比

| 維度 | Karpathy | LeCun / Bengio / Hinton |
|------|----------|------------------------|
| 學術引用 | ~78,000（Google Scholar） | 數十萬（圖靈獎得主級別） |
| 研究貢獻 | CS231n、ImageNet 人類基準、RNN博文 | 深度學習理論奠基 |
| 影響力路徑 | 工程實踐 + 大眾教育 | 學術體系 + 機構影響力 |
| 公眾知名度 | 遠超多數學術同行 | 圈內知名，圈外有限 |

外部評價的核心共識：Karpathy 是罕見的「頂級研究者 + 頂級溝通者」組合。他在科普和工程實踐層面的影響力可能超過任何同代研究者。★★★

---

## 八、外部觀察到的行為模式

### 1. 公開試驗文化，但有時收場倉促
job risk map 事件是典型案例：釋出半成品 → 病毒式傳播 → 刪除澄清。先做再想，但當社會後果超出預期時，選擇退縮而非辯論。★★★

### 2. 敢於反對行業共識
在 AGI 泡沫時期，他是少數願意公開說「models are not there」「產品是 slop」的頂級人物。TradeFox CEO：「如果這個 Karpathy 採訪不能戳破 AI 泡沫，沒有什麼能了。」★★★（Fortune，2025年10月）

### 3. 說話速度快，思維領先於表達
Karpathy 自己承認：「我知道，我說話太快了。這對我不利，因為有時我的說話執行緒執行速度超過了我的思考。」★★★

### 4. 與 Elon Musk 的關係耐人尋味
Musk 轉發了他的 job risk map，兩人似乎保持聯絡，但 Karpathy 從未公開表態支援 Musk 的政治行動。他離開 Tesla 被分析為與 Musk「過度樂觀的公開承諾」文化存在底層張力。★（推測性，無直接證據）

### 5. 低調的個人生活，高調的技術觀點
沒有找到任何關於他私人生活的可信報道。他的公開形象與私下形象幾乎完全重合——技術博文、課程影片、X 上的技術評論。

---

## 九、有根據的批評彙總

| 批評 | 來源 | 可信度 | 是否有根據 |
|------|------|--------|-----------| 
| vibe coding 命名誤導了行業 | Andrew Ng，2025-06 | ★★★ | 有根據：AI 輔助程式設計的嚴肅性被低估 |
| 教育行業經驗不足，Eureka Labs 面臨歷史先例挑戰 | Dan Meyer，2024 | ★★★ | 有根據：Udacity/Coursera 前車之鑑真實存在 |
| 釋出半成品分析（job risk map）引發不必要的社會恐慌 | 綜合報道，2026-03 | ★★★ | 部分有根據：方法論確實不足，但他主動刪除 |
| 有時表述不夠嚴謹，說話速度超過思考 | Karpathy 自述 + 外界觀察 | ★★★ | 他自己承認 |
| 學術引用量不及「Godfathers」級別 | Google Scholar 資料 | ★★★ | 事實，但他的影響力路徑本就不同 |
| vibe coding 產生安全漏洞 | CodeRabbit 研究，2025-12 | ★★★ | 有根據，但這是技術趨勢的代價，非 Karpathy 個人責任 |

---

## 十、核心差異化特徵（外部觀察）

與同代 AI 領袖相比，外部觀察者普遍注意到以下獨特之處：

1. **雙重稀缺性**：他既是頂級工程師，又是頂級溝通者。LeCun 能研究但溝通曲高和寡；很多科普者能講但缺乏工程深度。
2. **機構獨立性**：他在斯坦福、Tesla、OpenAI、Eureka Labs 之間流動，不依附於單一機構，這使他的公開表態更可信。
3. **建設性批評者**：他批評 AI hype，但不否定 AI 價值——與 Gary Marcus 等人的「反 AI」立場形成鮮明對比。
4. **概念生產力**：「Software 2.0」（2017）、「vibe coding」（2025）、「summoning ghosts」（2025）、「agentic engineering」（2026）——他定期貢獻能在行業內流通的概念詞彙。
5. **公開脆弱性**：他願意公開說「我從未感覺作為程式設計師落後得這麼厲害」（2025年），承認自己說話太快等——這在頂級 AI 領袖中罕見。

---

*來源：Fortune、TechCrunch、The New Stack、Dwarkesh Podcast、simonwillison.net、danmeyer.substack.com、SC Media UK、Hacker News、Futurism、Google Scholar*
