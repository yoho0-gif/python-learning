# AI Resume Reviewer

一個使用 Python 與 Google Gemini API 開發的 AI 履歷分析工具。

使用者可以讀取履歷檔案，或直接貼上履歷內容，由 AI 分析履歷並提供改善建議，同時將分析結果輸出為 Markdown 報告。

---

## 功能特色

-  支援讀取 `.txt`、`.md` 履歷檔案
-  支援直接貼上履歷內容
-  使用 Google Gemini API 分析履歷
-  提供履歷優點、缺點與改善建議
-  推薦適合職缺
-  自動輸出 Markdown 分析報告
-  檔案不存在時提供錯誤提示
-  使用 `.env` 管理 API Key

---

## 專案架構

```text
resume-reviewer/
│
├── main.py
├── config.py
├── display.py
├── gemini_client.py
├── document_loader.py
├── report_writer.py
├── prompt_templates.py
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

啟動虛擬環境：

Windows PowerShell：

```powershell
.venv\Scripts\Activate.ps1
```

安裝相依套件：

```bash
pip install -r requirements.txt
pip install google-genai
pip install python-dotenv
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

## 執行流程

```text
輸入檔案

↓

自動判斷副檔名

↓

TXT Reader / PDF Reader

↓

Gemini AI

↓

Markdown Report
```

---

## 使用方式

啟動程式後，可以：

### 方法一：分析履歷檔案

```text
resume.txt
```

或

```text
resume.md
```

### 方法二：直接貼上履歷內容

```text
學歷：
逢甲大學 行銷系

工作經驗：
Apple 門市銷售三年

技能：
Python
Git
Excel
```

AI 會分析履歷並產生：

```text
review_result.md
```

---

## 使用技術

- Python 3
- Google Gemini API
- google-genai
- python-dotenv
- pypdf

---

## 學習重點

本專案練習了：

- 模組化設計
- Prompt Engineering
- 檔案讀取
- API 串接
- Exception Handling
- Markdown 報告輸出

---

## 未來規劃

- [v] 支援 PDF 履歷
- [ ] 支援 DOCX 履歷
- [ ] 自訂輸出檔名
- [ ] 串流（Streaming）回覆
- [ ] GUI 版本
- [ ] Web 版本（FastAPI / Streamlit）