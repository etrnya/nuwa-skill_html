# 名人AI智囊團 — Google Gemini API Key 申請指南

> 本指引帶您申請 Gemini API Key，供「名人AI智囊團 (Nuwa Chat)」呼叫 Google 的 AI 模型來模擬各路大師的思維。
> 一般情況下，這個流程不到 3 分鐘即可免費完成。

### 步驟 1：登入 Google AI Studio

1. 開啟 [Google AI Studio](https://aistudio.google.com/)，用您的 Google 帳號登入。
2. 第一次登入會要求同意服務條款，勾選後按「Continue」。

### 步驟 2：建立 API Key

進入 [API keys 管理頁面](https://aistudio.google.com/api-keys)

1. 點擊頁面**右上角**的「**Create API key**」按鈕。
2. 系統會跳出設定畫面，您可以為這把 Key 命名（例如 `NuwaChat`，只是給您自己辨識用）。
3. 在「Choose an imported project」欄位中選擇要關聯的 Google Cloud 專案：
   - 您可以直接使用預設的 **General Gemini Apps**。
   - 或是點選「**Create new project**」，建立專屬專案以供辨識。
4. 點擊「**Create key**」。

API Key 會立刻顯示，格式會是一長串像 `AIzaSy...`（約 39 個字元）的英數字。

> **小提醒**：Key 建立後可以隨時回到 API keys 管理頁面，點擊該 Key 的名稱複製完整字串，不必擔心一次沒複製好。但仍建議馬上複製起來，方便進行下一步。

### 步驟 3：在「名人AI智囊團」中設定 API Key

1. 雙擊打開您本地資料夾中的 `nuwa_chat.html` 網頁。
2. 點擊網頁左下角的「**⚙️ API 設定**」按鈕。
3. 在「**Gemini API Key**」欄位中，貼上您剛才複製的 Key。
4. （選填）在「預設模型」與「使用者背景資料」可以進行個人化設定。
5. 點擊「**儲存**」。
6. 在左側清單選擇任何一位大師，發送一句話測試，如果大師成功回覆您，就代表開通成功了！

---

### 步驟 4：綁定信用卡（選擇性進階設定）

Google Gemini API 提供了非常大方的免費額度（Free tier），對於個人日常使用通常已經綽綽有餘。但如果您在對話時發現出現頻繁的「被限制」錯誤，或是希望模型回覆速度更快，可以考慮升級。

Free tier 有 **RPD**（每日請求上限）與 **RPM**（每分鐘請求上限）的限制。

1. 開啟 [Google AI Studio](https://aistudio.google.com/)。
2. 點擊左側選單的「**Billing**」。
3. 點選「**Set up billing**」。
4. 填寫付款資訊（姓名、地址、信用卡）。
5. 提交後 AI Studio 會自動把您的專案升級，不僅放寬請求上限，也能使用更進階的模型版本。

> **帳單防護機制**：升級後的帳戶 Google 會預設強制設定每月 250 美元的消費上限，這是保護機制，能有效避免意外產生天價帳單。

---
*本文件最後更新: 2026 年 5 月 5 日*
