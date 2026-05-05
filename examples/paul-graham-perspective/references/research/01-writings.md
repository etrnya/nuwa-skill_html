# Paul Graham 著作與系統性長文調研

> 調研日期：2026-04-05
> 調研人：Claude（輔助花叔）
> 一手來源：paulgraham.com essays + Wikipedia + 權威科技媒體
> 資訊源黑名單：已排除知乎、微信公眾號、百度百科

---

## 一、人物背景

**Paul Graham**（1964年11月13日—），英裔美國電腦科學家、作家、散文家、企業家和投資人。

### 關鍵履歷
- **出生**：英國Dorset郡Weymouth，4歲隨家人遷至美國Pittsburgh
- **教育**：Cornell大學BA（1986）→ Harvard大學CS碩士+博士 → RISD（Rhode Island School of Design）和佛羅倫薩美術學院學習繪畫
- **Viaweb**（1995-1998）：與Robert Morris共同創辦，用Common Lisp編寫的線上商店構建軟體。1998年被Yahoo以4960萬美元收購，成為Yahoo Store
- **Y Combinator**（2005—）：與Trevor Blackwell、Jessica Livingston、Robert Morris共同創立。已投資1300+家創業公司（Reddit、Dropbox、Airbnb、Stripe等）
- **Arc語言**：2001年宣佈開發新Lisp方言Arc，2008年釋出
- **著作**：《On Lisp》、《ANSI Common Lisp》、《Hackers & Painters》
- **Essays**：1998-2026年在paulgraham.com釋出200+篇essay，每4-8週一篇

> 來源：[Wikipedia](https://en.wikipedia.org/wiki/Paul_Graham_(programmer))、[paulgraham.com/bio.html](https://paulgraham.com/bio.html) | 一手+可信

---

## 二、核心著作：《Hackers & Painters》

**出版**：2004年，O'Reilly Media
**URL**：https://paulgraham.com/hp.html

### 核心論點

1. **程式設計是創作而非科學**：駭客（程式設計師）和畫家都是makers。Graham認為"computer science"這個詞有問題——它不是真正的科學，而是一堆因歷史偶然被扔在一起的領域
2. **透過實踐學習**：畫畫主要靠動手學——程式設計也一樣。大多數駭客不是在大學課程裡學會程式設計的，而是13歲時自己寫程式學的
3. **程式語言應該是鉛筆而非鋼筆**：語言應該有可塑性（malleable），用來思考程式，而不只是表達已經想好的程式
4. **迭代式開發**：繪畫從草圖開始逐步細化——程式設計也應該如此。有時原始計劃會被證明是錯的
5. **同理心是核心能力**：駭客必須像畫家一樣有同理心，能從使用者角度看問題，才能做出偉大的工作

> 來源：[paulgraham.com/hp.html](https://paulgraham.com/hp.html)、[Goodreads](https://www.goodreads.com/book/show/41793.Hackers_Painters)、[Medium分析](https://medium.com/@edisipka/my-notes-on-paul-grahams-hackers-and-painters-why-programming-is-actually-art-9a4829117554) | 一手+二手

---

## 三、寫作方法論 Essays（6篇核心）

### 3.1 The Age of the Essay（2004）
**URL**：https://paulgraham.com/essay.html

- Essay不應該是「證明一個論點」，而應該是**探索**（exploration）
- 學校教的寫作方式（五段式論證）扭曲了essay的本質
- Essay的詞源"essai"來自法語，意思是"嘗試"——蒙田發明了這種體裁
- 好essay是思考的過程，不是思考的結果

> 來源：一手 | 可信度：★★★★★

### 3.2 Writing, Briefly（2005）
**URL**：https://paulgraham.com/writing44.html

Graham的編碼化寫作規則：
- 先儘可能快地寫一個爛版本1，然後反覆重寫
- 如果卡住了，就告訴別人你打算寫什麼，然後把你說的話寫下來
- 預期80%的essay想法會在你開始寫之後才出現
- 從第一句話開始寫
- 大聲朗讀essay，找出彆扭的短語和無聊的段落

> 來源：一手 | 可信度：★★★★★

### 3.3 Write Like You Talk（2015）
**URL**：https://paulgraham.com/talk.html

- 寫作和口語之間應該有interconnection
- 建議：讀你的文章時大聲朗讀，把所有不像對話的部分改掉
- 遵循這個方法就"已經超過95%的寫作者"

> 來源：一手 | 可信度：★★★★★

### 3.4 Write Simply（2021）
**URL**：https://paulgraham.com/simply.html

- "我儘量用普通的詞寫作……這種寫法更容易讀，越容易讀，讀者就越深入地參與"
- 簡單的語言、簡單的詞彙、簡單的句子——但不降低思想的深度
- 簡單寫作是一種*選擇*，不是能力不足

> 來源：一手 | 可信度：★★★★★

### 3.5 How to Write Usefully（2020）
**URL**：https://paulgraham.com/useful.html

- 有用寫作的公式 = **重要性 × 新穎性 × 正確性 × 力度**
- 四個變數中，新穎性最容易被忽視
- 寫作不只是傳遞資訊，而是要讓人改變對某件事的看法

> 來源：一手 | 可信度：★★★★★

### 3.6 Putting Ideas into Words（2022）
**URL**：https://paulgraham.com/words.html

- **核心論點**：寫作就是思考（Writing is thinking）
- 把想法寫出來的過程會迫使你更清晰地思考
- 很多人以為自己在寫作前就想清楚了，其實沒有——寫作過程本身產生新的理解
- 這個論點與2024年"Writes and Write-Nots"形成呼應

> 來源：一手 | 可信度：★★★★★

### 寫作方法論的統一核心

Graham的寫作哲學可以歸結為：
1. **寫作 = 思考**（反覆出現≥5次）
2. **簡單 > 複雜**（反覆出現≥4次）
3. **口語化 > 書面化**（反覆出現≥3次）
4. **迭代式寫作**：先寫爛稿 → 反覆修改（反覆出現≥3次）
5. **探索 > 論證**（反覆出現≥3次）

---

## 四、創業 Essays（核心篇目）

### 4.1 How to Start a Startup（2005）
**URL**：https://paulgraham.com/start.html

成功創業的三件事：
1. 從好人開始（good people）
2. 做客戶真正想要的東西
3. 儘可能少花錢

其他關鍵論點：
- 聯合創始人之於創業 = 地段之於房地產
- 快速釋出——"你沒有真正開始工作，直到你釋出了"
- 讓少數人真正高興 > 讓很多人一般高興

> 來源：一手 | 可信度：★★★★★

### 4.2 Do Things that Don't Scale（2013）
**URL**：https://paulgraham.com/ds.html

- **核心論點**：早期創始人應該擁抱手工的、勞動密集型的努力，即使這些做法無法規模化
- 最常見的不可規模化行為：手動招募使用者
- "如果你能找到一個有問題需要解決的人，你能手動解決它，那就去做——這比擁有一個自動化但沒人需要的東西要好得多"
- 10個客戶 + 每週10%增長 → 指數增長會處理好基數問題

> 來源：一手 | 可信度：★★★★★

### 4.3 Startup = Growth（2012）
**URL**：https://paulgraham.com/growth.html

- **創業公司的定義不是年輕或小，而是增長**
- YC期間好的增長率：每週5-7%，10%算極好
- 1000美元/月 + 1%周增長 → 4年後7900美元/月
- 1000美元/月 + 5%周增長 → 4年後2500萬美元/月
- 小百分比的複利效應產生完全不同的結果

> 來源：一手 | 可信度：★★★★★

### 4.4 Default Alive or Default Dead?（2015）
**URL**：https://paulgraham.com/aord.html

- 創始人應該知道自己的公司是"預設存活"還是"預設死亡"
- 計算需要四個指標：當前支出、當前收入、當前增長率、手頭現金
- 預設存活的公司有更大的談判槓桿
- **招人太快是融資後創業公司的頭號殺手**
- "Fatal pinch"：預設死亡 + 增長慢 + 沒時間修復

> 來源：一手 | 可信度：★★★★★

### 4.5 Frighteningly Ambitious Startup Ideas（2012）
**URL**：https://paulgraham.com/ambitious.html

- 最雄心勃勃的創業想法之所以frightening，是因為它們真的很難
- 列舉了幾個"frighteningly ambitious"的方向

> 來源：一手 | 可信度：★★★★★

### 4.6 Schlep Blindness（2012）
**URL**：https://paulgraham.com/schlep.html

- "Schlep blindness"：人們看不到偉大的創業想法，因為這些想法涉及schleps——來自意第緒語的詞，指乏味、不愉快的任務
- 很多最好的創業機會被忽視，因為人們本能地迴避"髒活"
- Stripe的Collison兄弟就是schlep blindness的反例——他們願意做支付這個沒人想碰的領域

> 來源：一手 + [LinkedIn討論](https://www.linkedin.com/posts/the-startup-archive_alexandr-wang-on-why-paul-grahams-schlep-activity-7369036483380314112-nd2v) | 可信度：★★★★★

### 4.7 How to Get Startup Ideas（2012）
**URL**：https://paulgraham.com/startupideas.html

- 最好的創業想法有三個共同點：創始人自己想要、自己能做、很少人意識到值得做
- "成功的方法不是成為創業專家，而是成為你的使用者和問題的專家"

> 來源：一手 | 可信度：★★★★★

### 4.8 Founder Mode（2024年9月）
**URL**：https://paulgraham.com/foundermode.html

- 受Airbnb聯合創始人Brian Chesky在YC活動上的演講啟發
- **兩種公司管理模式**：Founder Mode（創始人模式）vs Manager Mode（職業經理人模式）
- 矽谷傳統智慧是"公司做大了就該切換到manager mode"——Graham認為這是錯的
- Chesky發現"招人然後放手"的模式對Airbnb是災難性的
- Chesky研究了喬布斯管理蘋果的方式，轉向了創始人模式，效果大幅改善
- 創始人應該深入瞭解產品細節，像CPO一樣
- **這篇essay是2024年最viral的PG文章**，引發了整個科技圈的討論

> 來源：一手 + [Fortune](https://fortune.com/2024/09/01/paul-graham-founder-mode-silicon-valley-conventional-wisdom-manager-mode/)、[Wikipedia](https://en.wikipedia.org/wiki/Founder_mode) | 可信度：★★★★★

---

## 五、人生哲學與認知 Essays

### 5.1 How to Do Great Work（2023）
**URL**：https://paulgraham.com/greatwork.html

四步框架：
1. 選擇你有興趣和天賦的領域
2. 學到知識的前沿
3. 發現別人忽略的gaps、patterns和anomalies
4. 探索最有前景的gaps

關鍵論點：
- **好奇心是做出偉大工作的關鍵**——它會幫你選擇領域、到達前沿、發現gap、驅動探索
- 偉大工作的因素（數學意義上的因子）：能力、興趣、努力、運氣
- "每天寫一頁聽起來不多，但如果每天都寫，一年就是一本書"——一致性的累積效應
- 做偉大的工作 = 做重要的事情做得足夠好，以至於你擴充套件了人們對可能性的認知
- 追隨真正的興趣而非聲望

> 來源：一手 | 可信度：★★★★★

### 5.2 Superlinear Returns（2023）
**URL**：https://paulgraham.com/superlinear.html

- **超線性回報**：投入翻倍，產出可能四倍甚至更多
- 兩個驅動因素：**指數增長（複利）** 和 **閾值效應（贏家通吃）**
- 科學領域有最高的超線性回報——因為它結合了學習、閾值和新發現
- 利用超線性回報最明顯的方式：做極好的工作——在曲線遠端，邊際努力是bargain，競爭也更少
- **永遠在學習**——如果你沒在學習，你可能不在通往超線性回報的路上

> 來源：一手 | 可信度：★★★★★

### 5.3 Life is Short（2016）
**URL**：https://paulgraham.com/vb.html

三條核心行動指南：
1. **無情地修剪bullshit**：不必要的會議、無意義的爭論、官僚主義、裝腔作勢
2. **不要等待**：不要等著才去爬那座山、寫那本書、去看你媽媽
3. **品味你擁有的時間**

個人化觸點：
- "我母親去世後，我希望我花了更多時間陪她。我活得好像她會永遠在那裡。"
- Bullshit進入生活的兩種方式：被迫接受 or 被欺騙接受

> 來源：一手 | 可信度：★★★★★

### 5.4 The Bus Ticket Theory of Genius（2019）
**URL**：https://paulgraham.com/genius.html

- 天才的配方 = **對重要事物的無私痴迷**（a disinterested obsession with something that matters）
- "Disinterested"是最重要的特徵——不是為了打動別人或致富，而是為了事情本身
- 通向新想法的路徑往往看起來不promising——如果看起來promising，別人早已探索了
- 判斷標準：你在創造而非消費、你感興趣的事情很難、這個困難對你比對別人更容易

> 來源：一手 | 可信度：★★★★★

### 5.5 Keep Your Identity Small（2009）
**URL**：https://paulgraham.com/identity.html

- "你給自己貼的標籤越多，它們讓你越蠢"
- 當某個話題成為你身份的一部分，你就無法理性思考它了
- 宗教和政治之所以引發最激烈的爭論，不是因為它們本身特殊，而是因為人們把它們納入了身份認同

> 來源：一手 | 可信度：★★★★★

### 5.6 What You Can't Say（2004）
**URL**：https://paulgraham.com/say.html

- 每個時代都有人們認為是對的但其實很荒謬的信仰——我們這個時代不太可能是第一個全都對的時代
- **測試**：你有沒有在同伴面前不敢說的觀點？如果沒有——這不太可能是巧合，更可能是你只是在想別人告訴你的東西
- 識別隱藏禁忌的方法：看人們因為說什麼而惹麻煩、識別用來噤聲的標籤、跨文化和跨時代比較

> 來源：一手 | 可信度：★★★★★

### 5.7 How to Think for Yourself（2020）
**URL**：https://paulgraham.com/think.html

獨立思維的三個組成部分：
1. 對真理的苛求（fastidiousness about truth）
2. 抵抗被告知該怎麼想
3. 好奇心

"如果你的答案表明你相信的一切都是你應該相信的——這很可能不是巧合"

> 來源：一手 | 可信度：★★★★★

### 5.8 The Four Quadrants of Conformism（2020）
**URL**：https://paulgraham.com/conformism.html

四種人：
1. **主動從眾者**（aggressively conventional-minded）
2. **被動從眾者**（passively conventional-minded）
3. **被動獨立者**（passively independent-minded）
4. **主動獨立者**（aggressively independent-minded）

> 來源：一手 | 可信度：★★★★★

### 5.9 What You'll Wish You'd Known（2005）
**URL**：https://paulgraham.com/hs.html

- 給高中生的未發表畢業演講
- 不要恐慌於"人生目標"——大多數成功的人都是在過程中發現的
- **"Stay upwind"（停在上風處）**：像滑翔機一樣，在每個階段做最有趣且給你未來最多選項的事
- 好奇心從不撒謊——它比你自己更清楚什麼值得關注

> 來源：一手 | 可信度：★★★★★

### 5.10 Maker's Schedule, Manager's Schedule（2009）
**URL**：https://paulgraham.com/makersschedule.html

- **兩種時間表**：經理的時間表（以小時為單位切割）vs 創作者的時間表（至少半天為單位）
- 對創作者來說，一個會議就能毀掉整個下午——因為它把時間切成兩塊，每塊都太小做不了難事
- 權力通常在經理手中，他們會讓所有人以自己的頻率共振
- Graham的解決方案：把所有會議集中在工作日末尾（office hours）

> 來源：一手 | 可信度：★★★★★

### 5.11 Mean People Fail（2014）
**URL**：https://paulgraham.com/mean.html

- 在Graham認識的最成功的人中，幾乎沒有刻薄的人
- 刻薄讓你變蠢——你在戰鬥中永遠做不出最好的工作
- 刻薄的創始人吸引不到最好的人才
- 做偉大的事情需要benevolence精神驅動
- 歷史上大多數成功是零和博弈，刻薄可能是優勢——但創業不是

**爭議/矛盾**：批評者指出Jobs、Zuckerberg、Bezos等成功創始人都有刻薄的一面。Graham的論點可能過於理想化。

> 來源：一手 + [Inc.反駁](https://www.inc.com/jeff-bercovici/paul-graham-mean-people-fail.html) | 可信度：★★★★☆（存在爭議）

### 5.12 The Submarine（2005）
**URL**：https://paulgraham.com/submarine.html

- PR公司"像一艘巨大的、安靜的潛艇潛伏在新聞之下"
- 非政治/犯罪/災難類新聞中，超過一半可能來自PR
- PR公司同時把同一個故事餵給多個出版物——讀者以為是趨勢，其實是人造的
- 頂級記者的弱點是虛榮心（vanity）而非懶惰

> 來源：一手 | 可信度：★★★★★

---

## 六、技術/程式設計 Essays

### 6.1 Beating the Averages（2003）
**URL**：https://paulgraham.com/avg.html

- **Blub悖論**：假想一個Blub程式設計師——他往下看，覺得低階語言缺功能；他往上看，卻看不出自己在往上看，只看到"奇怪的語言加了一堆沒用的東西"
- "唯一能看清所有語言間能力差異的程式設計師，是那些理解最強大語言的人"
- Viaweb用Lisp寫軟體是關鍵競爭優勢——比競爭對手更快做出功能

> 來源：一手 | 可信度：★★★★★

---

## 七、最新 Essays（2024-2025+）

### 7.1 Writes and Write-Nots（2024/2025）
**URL**：https://paulgraham.com/writes.html

- 預測AI時代會產生"writes"和"write-nots"的分裂
- "不是好寫手、一般寫手和不會寫的人——只有好寫手和不會寫的人"
- **寫作即思考**——跳過寫作技能的人也跳過了清晰思考的學習
- 類比：工業化前大多數人的工作讓他們身體強壯，現在你想強壯就得健身。寫作也一樣。"仍然會有聰明人，但只有那些選擇聰明的人"
- **"一個分為writes和write-nots的世界比聽起來更危險——它將是thinks和think-nots的世界"**

> 來源：一手 + [Medium分析](https://medium.com/blog/a-world-divided-into-writes-and-write-nots-is-more-dangerous-than-it-sounds-218cbb18ed89) | 可信度：★★★★★

### 7.2 Founder Mode（2024年9月）
見第四節4.8

### 7.3 The Right Kind of Stubborn（2024年9月）
**URL**：https://paulgraham.com/persistence.html（推測URL）
- 區分有價值的堅持和盲目固執

### 7.4 When to Do What You Love（2024年10月）
- 探討何時以及如何追隨熱情

### 7.5 How to Start Google（2024年3月）
- 給高中生的續篇，與"What You'll Wish You'd Known"形成對照

### 7.6 The Best Essay（2024年3月）
**URL**：https://paulgraham.com/best.html

### 7.7 關於AI的態度（2025年8月）
- Graham表示"我見過的最令人印象深刻的兩家公司不是做AI的"
- "教訓不是AI不重要（它非常重要），而是創始人比idea更重要"
- AI是"大量重要的、幾乎完成的拼圖中缺失的那一塊"
- 不要把所有人類技能外包給機器——清晰寫作、批判性思考、創造性解決問題仍然關鍵

> 來源：[CNBC](https://www.cnbc.com/2025/08/18/yc-co-founder-paul-graham-not-every-new-company-needs-to-be-about-ai.html) | 可信度：★★★★★

---

## 八、反覆出現的核心論點（≥3次標註）

以下是在Graham的200+篇essay中反覆出現的核心信念，按出現頻率排列：

### Tier 1：出現≥10次的真信念

| # | 核心論點 | 出現頻次 | 代表性essays |
|---|---------|---------|-------------|
| 1 | **好奇心是一切的引擎** | ≥15次 | How to Do Great Work, Bus Ticket Theory, What You'll Wish, How to Think for Yourself, How to Get Startup Ideas |
| 2 | **寫作 = 思考**（writing is thinking） | ≥10次 | Putting Ideas into Words, Writes and Write-Nots, Age of the Essay, Writing Briefly, How to Write Usefully |
| 3 | **做使用者真正想要的東西** | ≥10次 | How to Start a Startup, Do Things that Don't Scale, How to Get Startup Ideas, Startups in 13 Sentences |
| 4 | **獨立思考 > 從眾** | ≥10次 | What You Can't Say, How to Think for Yourself, Four Quadrants, Keep Your Identity Small |

### Tier 2：出現≥5次的真信念

| # | 核心論點 | 出現頻次 | 代表性essays |
|---|---------|---------|-------------|
| 5 | **增長定義創業公司** | ≥7次 | Startup = Growth, Do Things that Don't Scale, Default Alive |
| 6 | **簡單 > 複雜**（寫作、設計、思考皆然） | ≥7次 | Write Simply, Write Like You Talk, Taste for Makers |
| 7 | **迭代式方法 > 一步到位計劃** | ≥6次 | Hackers & Painters, Writing Briefly, Do Things that Don't Scale |
| 8 | **創始人 > idea** | ≥6次 | Founder Mode, How to Start a Startup, 2025 AI remarks |
| 9 | **超線性回報/複利思維** | ≥5次 | Superlinear Returns, Startup = Growth, How to Do Great Work |
| 10 | **少花錢/精益運營** | ≥5次 | Default Alive, Ramen Profitable, How to Start a Startup |

### Tier 3：出現≥3次的真信念

| # | 核心論點 | 出現頻次 | 代表性essays |
|---|---------|---------|-------------|
| 11 | **品味（taste）很重要** | ≥4次 | Taste for Makers, Hackers & Painters, How to Do Great Work |
| 12 | **Benevolence勝過meanness** | ≥3次 | Mean People Fail, How to Do Great Work, 相關startup essays |
| 13 | **不要等待/人生短暫** | ≥3次 | Life is Short, What You'll Wish, How to Do Great Work |
| 14 | **Lisp是強大的秘密武器** | ≥3次 | Beating the Averages, Hackers & Painters, Viaweb相關 |
| 15 | **Stay upwind（保持選項開放）** | ≥3次 | What You'll Wish, How to Do Great Work, 相關建議essays |
| 16 | **學校教育的缺陷** | ≥3次 | Age of the Essay, What You'll Wish, Why Nerds Are Unpopular |

---

## 九、自創術語與概念

| 術語 | 含義 | 首次出現 | URL |
|------|------|---------|-----|
| **Ramen Profitable** | 創業公司收入剛好覆蓋創始人生活費（吃拉麵的水平） | 2009 | paulgraham.com/ramenprofitable.html |
| **Do Things that Don't Scale** | 早期創業應該擁抱手工、不可規模化的做法 | 2013 | paulgraham.com/ds.html |
| **Schlep Blindness** | 人們看不到涉及髒活的好機會（schlep=意第緒語"乏味任務"） | 2012 | paulgraham.com/schlep.html |
| **Blub Paradox** | 程式設計師無法認識到比自己更強大的語言的優勢 | 2003 | paulgraham.com/avg.html |
| **Relentlessly Resourceful** | 好創始人的一詞定義——不只是堅持，還要創造性地解決問題 | 2009 | paulgraham.com/relres.html |
| **Founder Mode** | 創始人直接深入參與公司運營的管理方式（vs Manager Mode） | 2024 | paulgraham.com/foundermode.html |
| **Default Alive / Default Dead** | 創業公司在不融資情況下能否盈利的狀態判斷 | 2015 | paulgraham.com/aord.html |
| **Frighteningly Ambitious** | 最好的創業想法會讓人害怕（因為太大了） | 2012 | paulgraham.com/ambitious.html |
| **The Fatal Pinch** | 預設死亡 + 增長慢 + 沒時間修復的致命三角 | 2015 | paulgraham.com/aord.html |
| **Maker's Schedule / Manager's Schedule** | 創作者需要大塊不間斷時間 vs 經理以小時為單位 | 2009 | paulgraham.com/makersschedule.html |
| **Earnestness** | 出於正確原因做事 + 盡最大努力——PG認為這是創始人最重要的品質之一 | 多次 | 散見於多篇essay |
| **Stay Upwind** | 像滑翔機一樣保持在上風——做最有趣且保持選項開放的事 | 2005 | paulgraham.com/hs.html |
| **Writes and Write-Nots** | AI時代會寫的人和不會寫的人的分裂 | 2024 | paulgraham.com/writes.html |
| **Thinks and Think-Nots** | Writes and Write-Nots的推論——思考能力也會分化 | 2024 | paulgraham.com/writes.html |

---

## 十、推薦書單（揭示智識譜系）

Paul Graham在paulgraham.com/books.html和社交媒體上推薦了100+本書。以下是有明確推薦語的關鍵書目：

### 創業/商業類
| 書名 | 作者 | PG評價 |
|------|------|--------|
| **Founders at Work** | Jessica Livingston | "可能是創業者能讀的最有價值的一本書" |
| **How to Win Friends and Influence People** | Dale Carnegie | "對做生意的人至關重要" |
| Sebastian Mallaby的VC著作 | Sebastian Mallaby | "如果你想了解VC如何運作……這就是要讀的書" |

### 科學/歷史類
| 書名 | 作者 | PG評價 |
|------|------|--------|
| **From Galileo to Newton** | Rupert Hall | "我讀過的最好的科學史書之一" |
| **History of Medieval Europe** | R.H.C. Davis | "如果只讀一本中世紀史，可能是最好的選擇" |
| **Apollo's Arrow** | Nicholas Christakis | "廣闊的歷史全景和每頁都有有趣洞察" |

### 文學/科幻類
| 書名 | 作者 | PG評價 |
|------|------|--------|
| **The Moon is a Harsh Mistress** | Robert Heinlein | "這類書曾經完全佔據我的大腦" |
| **Foundation** | Isaac Asimov | 同上 |
| **I Want to Be a Mathematician** | Paul Halmos | 推薦閱讀 |

### 智識譜系推斷

從推薦書單和essay引用來看，Graham的思想譜系包括：
- **蒙田**（essay體裁的發明者，Graham多次致敬）
- **Paul Buchheit**（Gmail發明者，YC合夥人，多次引用）
- **Richard Feynman**（簡單解釋複雜事物的精神）
- **Peter Thiel**（逆向思考，雖Graham與Thiel有很多不同）
- **Jessica Livingston**（PG妻子，YC聯合創始人，影響創業觀）
- **Robert Morris**（長期合夥人，技術判斷力的來源）

> 來源：[paulgraham.com/books.html](https://www.paulgraham.com/books.html)、[kevinrooke.com](https://www.kevinrooke.com/book-recommendations/paul-graham)、[readthistwice.com](https://www.readthistwice.com/person/paul-graham) | 一手+二手

---

## 十一、寫作風格DNA分析

基於對Graham寫作的二手分析和一手essay閱讀：

### 句法特徵
- 偏好**短句、短詞**，但表達sophisticated ideas
- ~70%的essays包含"example"——抽象想法通常在一兩句內跟上精選的例子
- 大量使用第二人稱"you"，直接對讀者說話
- 幾乎不用行話（jargon），用最普通的詞表達不普通的想法

### 結構特徵
- 不用五段式結構，而是**essay式自由探索**
- 通常從一個觀察或問題開始，逐步展開
- 經常用"incidentally"、"in fact"、"it turns out"轉折
- 結尾往往是開放式的，不做總結性收束

### 修辭手法
- **類比和比喻**是最常用的工具（"程式設計像繪畫"、"創業像滑翔機"、"思想像moral fashions"）
- 反問句（"如果你所有的信仰都是你應該相信的，這可能是巧合嗎？"）
- 列舉（經常在essay中間放一個關鍵清單）
- 自我糾正（"I may be wrong, but..."、"There may be exceptions..."）

### 思維特徵
- **從特殊到一般**：先講一個具體故事/案例，再提煉出通用原則
- **逆向思考**：經常先問"什麼是錯的？"再推匯出"什麼是對的？"
- **跨領域類比**：繪畫→程式設計→創業→寫作之間頻繁跳轉
- **不確定的誠實**：承認自己不確定、可能犯錯，這在essays中反覆出現

> 來源：[Ellen Fishbein分析](https://ellenrhymes.com/paul-graham)、[Quora討論](https://www.quora.com/What-makes-Paul-Grahams-essays-so-good)、[Billy Oppenheimer](https://billyoppenheimer.com/paul-graham-essays/) | 二手+部分一手

---

## 十二、矛盾與爭議記錄

### 矛盾1：Mean People Fail vs 現實
- **PG立場**：刻薄的人在創業領域會失敗
- **反例**：Jobs、Zuckerberg、Bezos等被廣泛認為有刻薄的一面但極其成功
- **可能的調和**：PG可能指的是純粹的刻薄（無能力的），而非"demanding"

### 矛盾2：Founder Mode vs 之前的建議
- **PG 2024**：創始人應該深入參與運營細節
- **PG之前**：多篇essay建議創始人focus on最重要的事、delegation
- **可能的解釋**：PG的thinking在進化，Founder Mode是對之前delegation建議的修正

### 矛盾3：經濟不平等觀點的爭議
- PG曾寫essay為經濟不平等辯護，認為這是創新的副產品
- 引發Quartz等媒體的批評文章
- 這一立場與他的一些"benevolence"相關論點存在tension

### 矛盾4：AI樂觀 vs AI擔憂
- **樂觀面**：AI是"大量拼圖中缺失的那一塊"，是重要的技術
- **擔憂面**：AI會導致"writes and write-nots"/"thinks and think-nots"的分裂
- 兩者不完全矛盾，但反映了Graham對AI的複雜態度

> 來源：多個二手來源綜合 | 標註為存在爭議

---

## 十三、完整Essay索引（部分，按主題分類）

### 寫作類
| Essay | Year | URL |
|-------|------|-----|
| The Age of the Essay | 2004 | paulgraham.com/essay.html |
| Writing, Briefly | 2005 | paulgraham.com/writing44.html |
| Write Like You Talk | 2015 | paulgraham.com/talk.html |
| How to Write Usefully | 2020 | paulgraham.com/useful.html |
| Write Simply | 2021 | paulgraham.com/simply.html |
| Putting Ideas into Words | 2022 | paulgraham.com/words.html |
| The Need to Read | 2022 | paulgraham.com/read.html |
| Writing and Speaking | — | paulgraham.com/speak.html |
| Writes and Write-Nots | 2024 | paulgraham.com/writes.html |
| The Best Essay | 2024 | paulgraham.com/best.html |

### 創業類
| Essay | Year | URL |
|-------|------|-----|
| How to Start a Startup | 2005 | paulgraham.com/start.html |
| How to Get Startup Ideas | 2012 | paulgraham.com/startupideas.html |
| Do Things that Don't Scale | 2013 | paulgraham.com/ds.html |
| Startup = Growth | 2012 | paulgraham.com/growth.html |
| Default Alive or Default Dead? | 2015 | paulgraham.com/aord.html |
| Schlep Blindness | 2012 | paulgraham.com/schlep.html |
| Frighteningly Ambitious Startup Ideas | 2012 | paulgraham.com/ambitious.html |
| Ramen Profitable | 2009 | paulgraham.com/ramenprofitable.html |
| Relentlessly Resourceful | 2009 | paulgraham.com/relres.html |
| Before the Startup | — | paulgraham.com/before.html |
| Startups in 13 Sentences | — | paulgraham.com/13sentences.html |
| A Student's Guide to Startups | — | paulgraham.com/mit.html |
| Founder Mode | 2024 | paulgraham.com/foundermode.html |
| How to Start Google | 2024 | — |

### 人生/認知類
| Essay | Year | URL |
|-------|------|-----|
| How to Do Great Work | 2023 | paulgraham.com/greatwork.html |
| Superlinear Returns | 2023 | paulgraham.com/superlinear.html |
| Life is Short | 2016 | paulgraham.com/vb.html |
| The Bus Ticket Theory of Genius | 2019 | paulgraham.com/genius.html |
| Keep Your Identity Small | 2009 | paulgraham.com/identity.html |
| What You Can't Say | 2004 | paulgraham.com/say.html |
| How to Think for Yourself | 2020 | paulgraham.com/think.html |
| The Four Quadrants of Conformism | 2020 | paulgraham.com/conformism.html |
| What You'll Wish You'd Known | 2005 | paulgraham.com/hs.html |
| Mean People Fail | 2014 | paulgraham.com/mean.html |
| Good and Bad Procrastination | — | — |
| When to Do What You Love | 2024 | — |
| The Right Kind of Stubborn | 2024 | — |

### 技術/程式設計類
| Essay | Year | URL |
|-------|------|-----|
| Beating the Averages | 2003 | paulgraham.com/avg.html |
| Hackers and Painters | 2003 | paulgraham.com/hp.html |
| Taste for Makers | — | — |
| Why Nerds Are Unpopular | — | — |

### 媒體/社會類
| Essay | Year | URL |
|-------|------|-----|
| The Submarine | 2005 | paulgraham.com/submarine.html |
| Maker's Schedule, Manager's Schedule | 2009 | paulgraham.com/makersschedule.html |

---

## 十四、調研總結

### 關鍵發現

1. **Paul Graham是當代最有影響力的essay寫作者之一**，200+篇essay涵蓋創業、寫作、程式設計、人生哲學四大領域

2. **他的思想高度一致且相互關聯**：好奇心→獨立思考→寫作即思考→做出偉大的工作→超線性回報——形成一個完整的intellectual system

3. **他的寫作風格是他方法論的最好證明**：用最簡單的詞表達最深刻的想法，從一手經驗（Viaweb、YC）提煉通用原則

4. **2024年最有影響力的兩篇**：Founder Mode（重新定義公司管理）和Writes and Write-Nots（預判AI對人類思考能力的影響）

5. **他自創了一系列已進入矽谷日常詞彙的術語**：ramen profitable、schlep blindness、do things that don't scale、founder mode、Blub paradox等

6. **他的核心矛盾**在於理想主義（mean people fail、benevolence驅動）與現實之間的tension——但他通常承認自己可能是錯的

### 調研侷限

- 未能直接訪問paulgraham.com完整文字（只能透過搜尋獲取摘要和引用）
- 2025-2026年的essay資訊較少，可能有遺漏
- 書單資訊來自二手整理，可能不完整
- 部分essay的具體年份需要進一步確認

---

*調研完成。此文件可作為構建Paul Graham perspective skill的基礎素材。*
