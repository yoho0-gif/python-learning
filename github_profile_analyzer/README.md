# GitHub Profile Analyzer

使用 Python、GitHub REST API 與 Google Gemini API 開發的 AI GitHub 分析工具。

輸入 GitHub 使用者名稱後，程式會自動取得公開 Repository 資料，整理統計資訊，再由 AI 分析技術能力、專案特色與適合的職涯方向，最後輸出 Markdown 報告。

---

## 功能特色

-  查詢 GitHub 使用者公開 Repository
-  統計 Repository 數量
-  統計總 Star 數
-  分析常用程式語言
-  找出 Star 最多的 Repository
-  使用 Gemini AI 分析 GitHub Profile
-  自動輸出 Markdown 分析報告

---

## 專案架構

```text
github-profile-analyzer/
│
├── config.py
├── github_api.py
├── github_analyzer.py
├── gemini_client.py
├── prompt_templates.py
├── report_writer.py
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## 安裝

建立虛擬環境：

```bash
python -m venv .venv
```

啟動虛擬環境（Windows）：

```powershell
.venv\Scripts\Activate.ps1
```

安裝套件：

```bash
pip install -r requirements.txt
```

---

## 建立 `.env`

```env
GEMINI_API_KEY=你的_API_Key
```

---

## 執行

```bash
python main.py
```

---

## 使用方式

輸入 GitHub 使用者名稱：

```text
torvalds
```

程式會：

1. 取得 Repository 資料
2. 統計 Repository 資訊
3. 使用 Gemini AI 分析
4. 產生 `github_analysis.md`

---

## AI 分析內容

- 技術能力
- 程式設計方向
- GitHub 作品特色
- 優勢分析
- 建議補強技能
- 推薦職缺

---

## 使用技術

- Python 3
- GitHub REST API
- Google Gemini API
- Requests
- python-dotenv

---

## 學習重點

本專案練習了：

- REST API 串接
- JSON 資料處理
- Dictionary 統計
- Lambda 排序
- Prompt Engineering
- 模組化設計
- AI 應用開發

---

## 未來規劃

- [ ] 分析 GitHub 使用者資訊（Followers、Bio、建立時間）
- [ ] 分析 Commit 活躍度
- [ ] 分析 Repository Topics
- [ ] 產生雷達圖
- [ ] Streamlit Web 版本
- [ ] 支援 OpenAI API