# AI Resume Reviewer

以 Python 與 Google Gemini API 製作的命令列履歷分析工具。程式讀取 PDF、TXT 或 Markdown 履歷，請 Gemini 依照履歷內容提供優點、缺點、修改建議及適合職缺，並輸出 Markdown 報告。

## 功能

- 讀取 `.pdf`、`.txt` 與 `.md` 履歷檔案。
- 使用 Gemini 分析履歷並提供具體改善方向。
- 將分析結果輸出至 `review_result.md`。

## 專案結構

```text
resume_reviewer/
├── src/
│   ├── main.py             # 程式入口與互動流程
│   ├── document_loader.py  # 讀取 PDF、TXT 與 Markdown
│   ├── gemini_client.py    # 呼叫 Gemini 分析履歷
│   ├── prompt_templates.py # 履歷分析提示詞
│   ├── report_writer.py    # 儲存 Markdown 報告
│   └── display.py          # 顯示程式標題與使用提示
├── sample_resume.pdf       # 範例履歷
└── README.md
```

## 環境設定

本專案目前沒有 `requirements.txt`。在儲存庫根目錄啟用 `.venv`，再安裝依賴：

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install google-genai python-dotenv pypdf
```

在 `resume_reviewer/` 建立 `.env`，填入 Gemini API 金鑰：

```dotenv
GEMINI_API_KEY=你的_Gemini_API金鑰
```

請勿將 `.env` 或 API 金鑰提交至版本控制。

## 執行

從儲存庫根目錄切換到專案資料夾後執行：

```powershell
Set-Location resume_reviewer
python src/main.py
```

在提示中輸入履歷檔案路徑，例如：

```text
sample_resume.pdf
```

路徑以目前工作目錄（此處為 `resume_reviewer/`）為準。輸入 `exit` 可離開。分析完成後，程式會在目前工作目錄建立或覆寫 `review_result.md`。

## 分析流程

1. 依副檔名選擇 PDF 或純文字讀取方式。
2. 擷取履歷文字並送交 Gemini。
3. Gemini 依提示詞產生履歷評估。
4. 將結果寫入 Markdown 報告。

## 使用技術與學習重點

- Python 模組化設計與檔案處理
- PDF 文字擷取（`pypdf`）
- Gemini API、環境變數與 Prompt Engineering
- Markdown 報告輸出及例外處理

## 限制與隱私提醒

- 目前只能輸入檔案路徑，尚未實作直接貼上履歷文字的輸入流程。
- PDF 以文字擷取方式處理；掃描影像型 PDF 沒有 OCR，可能無法讀取。
- 履歷內容會傳送至 Gemini API 進行分析。請只使用你有權處理的資料，並先移除不必要的個人資訊。
- `review_result.md` 可能包含履歷個資；分享或提交前請先檢查。再次執行會覆寫工作目錄中同名的報告。
- AI 分析僅供參考，不能取代專業履歷顧問或招募決策。