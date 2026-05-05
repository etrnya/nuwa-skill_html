# Ilya Sutskever: 重大決策、轉折點與爭議行為

> 調研時間: 2026-04-05
> 資訊源: Wikipedia, TechCrunch, Time, Fortune, Axios, CNBC, Gizmodo, Decrypt, Dwarkesh Patel Podcast, Calcalist, EA Forum, LessWrong, The Neuron, Israel Hayom
> 排除源: 知乎, 百度百科, 微信公眾號

---

## 1. 學術生涯決策: 師從Hinton

### 背景
Ilya Sutskever 1986年生於俄羅斯(前蘇聯), 5歲移民以色列, 16歲移居加拿大。在多倫多大學完成數學本科(2005)、計算機碩士(2007)、計算機博士(2013)。

### 選擇
選擇Geoffrey Hinton作為導師, 在深度學習仍被主流AI學界邊緣化的年代押注神經網路。

### 邏輯
Sutskever很早就對神經網路的潛力有直覺。當時主流AI研究偏向符號主義和統計方法, Hinton的連線主義路線被認為是少數派。選擇Hinton意味著押注一個不被看好的方向。

### 結果
2012年與Hinton、Alex Krizhevsky合作完成AlexNet, 在ImageNet競賽中以碾壓性優勢獲勝, 被視為深度學習革命的起點。Hinton後來說: "Ilya thought we should do it, Alex made it work, and I got the Nobel prize."

### 關鍵細節
- Sutskever相信神經網路效能會隨資料量增長而提升(scaling intuition的最早體現)
- ImageNet大規模資料集的出現恰好驗證了這一直覺
- 這是他後來一系列scaling押注的思想原點

**事實確認度: 高** (多個一手來源交叉驗證)

---

## 2. 加入Google Brain (2012-2015)

### 背景
AlexNet成功後, Sutskever短暫在Stanford跟Andrew Ng做博士後(約2個月), 隨後回到多倫多加入Hinton創辦的DNNResearch。2013年Google收購DNNResearch, Sutskever隨之加入Google Brain。

### 選擇
從學術界轉向工業界, 進入Google Brain團隊。

### 邏輯
Google提供了學術界無法比擬的算力和資料資源。DNNResearch被收購是一個package deal(Hinton、Krizhevsky、Sutskever一同加入), 不完全是個人獨立決策。

### 在Google的成果
- 與Oriol Vinyals、Quoc Viet Le合作開發sequence-to-sequence學習演算法(成為現代機器翻譯和語言建模的核心框架)
- 參與TensorFlow早期開發
- 參與AlphaGo論文(作為合著者之一)

### 結果
在Google期間的工作為他後來在OpenAI推動GPT系列奠定了技術基礎, 尤其是sequence-to-sequence的經驗。

**事實確認度: 高**

---

## 3. 離開Google, 聯合創立OpenAI (2015)

### 背景
2015年底, Elon Musk、Sam Altman等人籌備建立一個非營利AI實驗室。Sutskever是被重點招募的物件。

### 選擇
放棄Google的優厚條件(資源、算力、團隊), 加入一個尚未成立的非營利AI組織。

### 決策過程 [已確認]
這不是一個輕鬆的決定。據Elon Musk 2023年公開描述:
- Sutskever反覆搖擺, 多次表示要加入OpenAI, 又被DeepMind的Demis Hassabis說服留下
- 來回拉鋸了好幾次, 最終決定加入OpenAI
- Musk稱"Ilya joining was the linchpin for OpenAI being ultimately successful"

### 邏輯
- Sutskever自述: 他在Google享受了工作, 但想做更多(wanted to do more)
- OpenAI的非營利結構和"benefit humanity"使命可能吸引了他
- 作為首席科學家(而非Google大團隊中的一員), 他可以主導技術方向

### 結果
- 成為OpenAI六名董事會成員之一
- 獲得首席科學家頭銜, 全面主導研究方向
- OpenAI後來的所有核心技術突破(GPT系列)都在他的科學領導下完成

### 言行一致性分析
加入時的理想主義動機(非營利、benefit humanity)與後來OpenAI轉向商業化的矛盾, 成為2023年董事會危機的伏筆。

**事實確認度: 高** (Musk的證詞作為一手來源)

---

## 4. OpenAI技術路線決策

### 4a. GPT/Transformer路線的選擇

**背景**: OpenAI早期探索了多種方法(包括強化學習、機器人等)。Sutskever推動了基於大規模無監督預訓練的語言模型路線。

**關鍵押注**: 
- 大規模無監督文字預訓練能解鎖通用能力
- Transformer架構(2017年Google "Attention is All You Need"論文提出)適合大規模scaling
- GPT-1(2018) → GPT-2(2019) → GPT-3(2020) → GPT-4(2023)全部在Sutskever的科學領導下完成

**事實確認度: 高**

### 4b. Scaling Hypothesis的押注

**背景**: 2020年, Sutskever領導了OpenAI的neural scaling laws研究, 建立了模型效能與規模(引數量、資料量、計算量)之間的power law關係。

**選擇**: 把OpenAI的核心策略押在"越大越好"上。

**邏輯**: 
- 這可以追溯到AlexNet時期的直覺: 效能隨資料規模提升
- Scaling laws提供了數學化的預測框架
- 與Dario Amodei(後來離開建立Anthropic)等人共同推動這一方向

**結果**: 
- GPT-3和GPT-4的成功驗證了scaling hypothesis
- OpenAI一度成為全球AI領域的領導者

**後來的立場轉變** [重要矛盾]:
- 2024年12月NeurIPS演講: 宣稱"pre-training as we know it will end", 提出"peak data"概念("we have but one internet")
- 2025年11月Dwarkesh Patel採訪: 明確說"2020-2025是scaling時代, 2026起進入research時代"
- 被問100x更多scaling是否能改變一切, 回答"I don't think that's true"
- 後續在X上澄清: scaling當前方法仍會帶來改進, 但"something important will continue to be missing"

**言行一致性分析**: 
這是一個重大立場轉變。Sutskever從scaling的核心推動者變成了質疑者。但這不一定是矛盾——他可能認為scaling在2020-2025確實有效, 只是現在觸及天花板了。問題是: 他在SSI做的是什麼? 如果不是scaling, 那他押注的新方向是什麼? 他拒絕透露。

**事實確認度: 高** (公開演講和採訪)

---

## 5. 2023年11月董事會事件 [最重要]

這是Sutskever職業生涯中最具爭議的決策, 也是資訊量最大的事件。

### 5a. 事前準備 (至少一年)

**已確認事實** (來源: 2025年10月1日宣誓證詞, 近10小時):
- Sutskever至少花了一年時間考慮罷免Altman
- 他等待的條件是"the majority of the board is not obviously friendly with Sam"
- 他撰寫了一份52頁的備忘錄, 以brief形式組織, 指控Altman:
  - "a consistent pattern of lying" (持續撒謊的模式)
  - "undermining his execs" (破壞高管)
  - "pitting his execs against one another" (讓高管互相對立)
- 備忘錄透過disappearing emails傳送給獨立董事, 以防洩露
- CTO Mira Murati對備忘錄部分內容做了截圖儲存

**關鍵薄弱點** [需注意]:
- Sutskever在證詞中承認, 備忘錄中的指控"幾乎全部來自單一來源: CTO Mira Murati"
- 他承認沒有與其他高管交叉驗證
- 他承認依賴的是"secondhand knowledge"(二手資訊)
- 事後反思: "In hindsight, I realize that I didn't know it"

**事實確認度: 高** (宣誓證詞)

### 5b. 罷免行動 (2023年11月17日)

**時間線**:
- 11月17日: 董事會宣佈解僱Altman
- 11月18日(次日): 開始討論與Anthropic合併
- 11月20日: Sutskever公開表示"deeply regrets"自己的角色
- 11月21日: Altman復職

**Sutskever的動機** [多重資訊源]:
1. **安全擔憂**: Sutskever認為Altman推動AI部署和商業化的速度太快, 風險過高
2. **管理問題**: 備忘錄中記錄的撒謊和操縱行為
3. **結構性矛盾**: 非營利使命vs商業化壓力

**Anthropic合併計劃** [已確認]:
- 在Altman被解僱後48小時內, 董事會討論了與Anthropic合併
- 董事會成員Helen Toner"the most supportive"(最支援合併)
- Toner甚至表示"destroying OpenAI could be consistent with the mission"
- Sutskever本人明確反對合並: "I really did not want OpenAI to merge with Anthropic. I just didn't want to."
- Anthropic方面提出了實際操作障礙, 計劃未能推進

**事實確認度: 高** (宣誓證詞)

### 5c. 員工反撲與後悔

**已確認事實**:
- 770名員工中有738人簽署請願書要求恢復Altman
- 多名高管立即辭職
- Sutskever承認: "I had not expected them to feel strongly either way"(他預期員工會無所謂)
- 他隨後公開在X上發帖說"deeply regrets"參與此事

**Sutskever對過程的事後評價**:
- 承認過程"rushed"(倉促)
- 原因是"the board was inexperienced"(董事會缺乏經驗)

### 5d. 言行一致性分析

**矛盾點**:
1. 花一年精心準備罷免行動, 卻沒有做基本的資訊交叉驗證(依賴單一來源Murati)
2. 聲稱為安全而戰, 卻在行動後三天就"deeply regrets"
3. 反對Anthropic合併(說明他不想毀掉OpenAI), 但又發動了險些毀掉OpenAI的行動
4. 52頁備忘錄顯示深思熟慮, 但對員工反應的預判完全失誤

**可能的解釋**:
- 他的核心關切(AI安全)是真實的, 但執行能力遠遠跟不上
- 他是科學家而非管理者/政治家, 嚴重低估了組織動態
- "deeply regrets"可能更多是策略性表態(保全自身位置), 而非真正的認知轉變

**事實確認度: 高** (直接證詞和公開宣告)

---

## 6. 離開OpenAI (2024年5月)

### 背景
2023年11月事件後, Sutskever在OpenAI的處境變得尷尬。他仍保留首席科學家頭銜, 但實際影響力已被邊緣化。

### 選擇
2024年5月14日正式宣佈離開OpenAI。

### 公開表態
- X發帖: "The company's trajectory has been nothing short of miraculous, and I'm confident that OpenAI will build AGI that is both safe and beneficial under the leadership of @sama"
- 後來在Calcalist採訪中說: "Ultimately, I had a big new vision...it felt more suitable for a new company"

### Superalignment團隊的崩潰
- Sutskever離開後數天, Superalignment團隊聯合負責人Jan Leike也辭職
- Leike公開批評: OpenAI的"safety culture and processes have taken a backseat to shiny products"
- Leike說團隊被"under-resourced", 在"sailing against the wind"
- OpenAI隨後解散了整個Superalignment團隊
- 這個團隊是2023年成立的, 當時承諾投入20%算力

### 言行一致性分析
- 離開時的公開宣告極為友好(稱讚Altman領導), 與他此前52頁指控備忘錄形成鮮明對比
- 可能原因: equity/股權協議要求他不能公開批評, 或是策略性選擇
- Jan Leike的辭職宣告間接印證了Sutskever長期以來的安全擔憂是真實的

**事實確認度: 高**

---

## 7. 創立SSI (2024年6月至今)

### 7a. 創立決策

**時間**: 2024年6月19日宣佈

**聯合創始人**: 
- Daniel Gross (前Apple AI負責人, Y Combinator合夥人)
- Daniel Levy (前OpenAI研究員)

**辦公地點**: Palo Alto + Tel Aviv

**核心定位**: "Our first product will be the safe superintelligence, and it will not do anything else up until then"

### 7b. 融資策略

**時間線**:
- 2024年9月: 籌集$10億 (a16z, Sequoia, DST Global, SV Angel)
- 2025年3月: 再籌$20億, 估值達$320億 (Greenoaks Capital $5億領投, 加上Alphabet, NVIDIA, a16z, Lightspeed, DST Global)
- 截至2025年: 約20名員工, 零收入, $320億估值

**融資邏輯**: 幾乎完全依賴Sutskever的個人聲望。沒有產品, 沒有收入, 沒有公開的技術路線圖。

### 7c. 運營策略

**已確認**:
- 不做產品、不做服務, 只做一件事: safe superintelligence
- 2025年4月與Google Cloud達成合作, 獲得TPU算力
- Sutskever拒絕透露任何技術細節

**領導層變動** (2025年中):
- Meta試圖收購SSI, 被Sutskever拒絕
- 2025年7月, 聯合創始人Daniel Gross離開加入Meta Superintelligence Labs
- Sutskever接任CEO, Daniel Levy升任總裁

### 7d. 言行一致性分析

**矛盾與疑問**:

1. **安全vs商業**: Sutskever離開OpenAI是因為商業化壓力影響安全。但SSI接受了$30億風險投資, 投資人必然期待回報。"insulated from short-term commercial pressures"能維持多久?

2. **scaling質疑者卻依賴算力**: 如果scaling時代已結束, 為什麼還需要Google TPU和$30億? SSI到底在做什麼?

3. **時間壓力悖論**: 批評OpenAI過於急躁, 但SSI自身也面臨壓力——不可能花20年做"patient research", 否則投資人不會容忍。

4. **透明度**: 公開倡導AI安全和公眾知情權, 但對SSI的技術方向完全保密。

5. **聯合創始人流失**: Daniel Gross在SSI成立僅一年多就被Meta挖走, 暗示團隊凝聚力或方向可能存在問題。

**事實確認度: 中高** (融資資料確認, 但技術方向和內部狀態幾乎無公開資訊)

---

## 8. 哲學立場演變 (橫跨全部決策)

### 早期 (2012-2020): 純粹的技術樂觀主義
- 相信scaling會解鎖一切
- 推動GPT系列不斷增大

### 中期 (2020-2023): 安全覺醒
- 推動成立Superalignment團隊
- 越來越擔憂AI的existential risk
- 2023年MIT Technology Review採訪: 討論人類可能與機器融合

### 後期 (2024-至今): 哲學化轉向
- NeurIPS 2024: "pre-training as we know it will end"
- Dwarkesh Patel 2025採訪: 
  - AI發展5-20年可達到超越人類水平
  - 討論情感在認知中的必要性(引用失去情感能力的腦損傷患者案例)
  - AI agent可能需要"intrinsic concern for sentient beings"
  - 如果未來大多數有意識實體是AI, "caring about sentient life dilutes human primacy"
  - 長期均衡可能是人機融合

### 外部批評
- 安全策略依賴AI具有sentience, 這是未經驗證的哲學假設
- "safe superintelligence"在絕對意義上可能不存在
- 從scaling的堅定推動者變成質疑者, 這種轉變的深層原因不明

---

## 9. 總結: Sutskever決策模式

### 一致的特徵
1. **直覺驅動**: 從AlexNet到GPT到SSI, 他的重大決策都基於強烈直覺而非充分驗證
2. **科學家思維**: 擅長技術判斷, 但在組織管理和政治博弈中屢屢失算
3. **理想主義底色**: 無論是加入OpenAI還是創立SSI, 都有真實的使命感驅動
4. **資訊繭房傾向**: 52頁備忘錄依賴單一來源; 對員工反應完全誤判

### 矛盾清單
| 領域 | 早期立場 | 後期立場/行為 | 矛盾程度 |
|------|----------|---------------|----------|
| Scaling | 核心推動者 | 宣稱時代已結束 | 中(可解釋為認知演化) |
| OpenAI使命 | 非營利理想主義 | 離開時稱讚Altman領導 | 高(與52頁指控矛盾) |
| 安全行動 | 發動罷免 | 三天後deeply regrets | 高 |
| 透明度 | 主張公眾知情 | SSI完全保密 | 中高 |
| 商業化 | 批評OpenAI商業化 | SSI接受$30億VC | 中(結構不同但壓力相似) |

### 待觀察
- SSI到底在研究什麼? 他的"big new vision"是什麼?
- $320億估值零收入的模式能維持多久?
- Daniel Gross離開後, SSI的方向是否會發生變化?
- Sutskever關於"情感對認知必要"的觀點是否會體現在SSI的技術路線中?

---

## 資訊源

### 一手來源(宣誓證詞/本人宣告/公開演講)
- Ilya Sutskever宣誓證詞 (2025年10月1日, Elon Musk訴OpenAI案)
- NeurIPS 2024演講
- Dwarkesh Patel播客採訪 (2025年11月)
- Calcalist Tech採訪
- X/Twitter公開宣告

### 權威媒體報道
- [TechCrunch: Ilya Sutskever departs](https://techcrunch.com/2024/05/14/ilya-sutskever-openai-co-founder-and-longtime-chief-scientist-departs/)
- [Time: Sutskever leaves OpenAI](https://time.com/6978195/ilya-sutskever-leaves-open-ai/)
- [Fortune: Sutskever deeply regrets](https://fortune.com/2023/11/20/ilya-sutskever-openai-cofounder-deeply-regrets-resign/)
- [Axios: Sutskever regrets firing](https://www.axios.com/2023/11/20/sam-altman-fired-openai-board-illya-sutsever-regrets)
- [CNBC: SSI founding](https://www.cnbc.com/2024/06/19/openai-co-founder-ilya-sutskever-announces-safe-superintelligence.html)
- [CNBC: Sutskever becomes CEO](https://www.cnbc.com/2025/07/03/ilya-sutskever-is-ceo-of-safe-superintelligence-after-meta-hired-gross.html)
- [Gizmodo: Deposition details](https://gizmodo.com/former-openai-exec-explains-why-he-tried-to-do-a-coup-against-sam-altman-2000680769)
- [Decrypt: Inside the deposition](https://decrypt.co/347349/inside-deposition-showed-openai-nearly-destroyed-itself)
- [The Neuron: Secret memo and Anthropic merger](https://www.theneuron.ai/explainer-articles/ilya-sutskevers-secret-memo-and-the-plot-to-merge-openai-with-anthropic)
- [Israel Hayom: SSI in Tel Aviv](https://www.israelhayom.com/2025/03/06/a-secret-ai-startup-in-tel-aviv-got-30b-this-israeli-raised-pioneer-did-it/)
- [Wikipedia: Ilya Sutskever](https://en.wikipedia.org/wiki/Ilya_Sutskever)
- [Wikipedia: Safe Superintelligence Inc.](https://en.wikipedia.org/wiki/Safe_Superintelligence_Inc.)
- [EA Forum: Dwarkesh interview highlights](https://forum.effectivealtruism.org/posts/iuKa2iPg7vD9BdZna/highlights-from-ilya-sutskever-s-november-2025-interview)
