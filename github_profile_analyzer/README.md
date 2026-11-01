# GitHub Profile Analyzer

以 Python、GitHub REST API 與 Google Gemini API 製作的命令列分析工具。輸入 GitHub 使用者名稱後，程式會取得公開 Repository 資料、整理基本統計，並請 Gemini 根據統計結果產生繁體中文 Markdown 分析報告。

## 功能

- 統計取得的公開 Repository 數量與 Stars 總數。
- 統計 Repository 使用的程式語言，並找出 Stars 數最高的 Repository。
- 使用 Gemini 產生技術能力、專案特色與職涯方向分析。
- 將 AI 分析結果輸出為 `github_analysis.md`。

## 專案結構

```text
github_profile_analyzer/
├── src/
│   ├── main.py             # 程式入口與執行流程
│   ├── github_api.py       # 呼叫 GitHub REST API
│   ├── github_analyzer.py  # 統計 Repository 資料
│   ├── gemini_client.py    # 呼叫 Gemini 產生分析
│   ├── prompt_templates.py # AI 分析提示詞
│   └── report_writer.py    # 儲存 Markdown 報告
└── README.md
```

## 環境設定

本專案目前沒有 `requirements.txt`。在儲存庫根目錄啟用 `.venv`，再安裝依賴：

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install requests google-genai python-dotenv
```

在 `github_profile_analyzer/` 建立 `.env`，填入 Gemini API 金鑰：

```dotenv
GEMINI_API_KEY=你的_Gemini_API金鑰
```

請勿將 `.env` 或 API 金鑰提交至版本控制。

## 執行

從儲存庫根目錄切換到專案資料夾後執行：

```powershell
Set-Location github_profile_analyzer
python src/main.py
```

依提示輸入 GitHub 使用者名稱，例如：

```text
torvalds
```

程式會在目前工作目錄（此處為 `github_profile_analyzer/`）建立或覆寫 `github_analysis.md`。

## 執行流程

1. 向 GitHub REST API 請求使用者的公開 Repository。
2. 整理 Repository 數量、Stars 總數、語言分布及最高 Stars 專案。
3. 將統計資料交給 Gemini 產生分析。
4. 在專案資料夾輸出 Markdown 報告。

## 使用技術與學習重點

- Python 模組化設計與 JSON 資料處理
- GitHub REST API 與 `requests`
- Gemini API、環境變數與 Prompt Engineering
- Dictionary 統計、排序及 Markdown 檔案輸出

## 限制與注意事項

- 目前只讀取 GitHub API 預設回傳的一頁 Repository 資料，並非完整的個人檔案、Commit 活躍度或所有頁面的統計。
- 分析依據為公開 Repository 的統計摘要；AI 產生的職涯建議僅供參考。
- `github_analysis.md` 可能包含使用者名稱及 AI 分析內容，分享或提交前請先檢查。
