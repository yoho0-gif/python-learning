# RAG 文件問答系統

這是一個以 Python 實作的多文件問答專案。使用者提出問題後，程式會先從本機文件搜尋相關內容，再把搜尋結果交給 Gemini 生成回答，示範 Retrieval-Augmented Generation（RAG，檢索增強生成）的基本流程。

## 功能

- 讀取 PDF、TXT 與 Markdown 文件。
- 依文件條文切分文字，使用 Gemini Embedding 將內容轉成向量。
- 使用 FAISS 搜尋最相關的 3 個文字區塊，並在終端機顯示來源與距離。
- 以文件雜湊值偵測新增或修改的文件，更新向量索引。
- 保留近期對話，讓後續問題能參考對話脈絡。
- 提供答案相關性、忠實度、檢索內容相關性及引用有效性的實驗性評估模組。

## 專案結構

```text
rag_document_chat/
├── documents/             # 放置要搜尋的 PDF、TXT、Markdown 文件
├── src/
│   ├── main.py             # 啟動互動式問答
│   ├── document_loader.py  # 載入文件並擷取文字
│   ├── text_splitter.py    # 切分文件內容
│   ├── embedding.py        # 呼叫 Gemini 建立向量
│   ├── faiss_store.py      # 建立及搜尋 FAISS 索引
│   ├── incremental_indexer.py
│   ├── gemini_client.py    # 根據檢索內容生成回答
│   └── evaluation/         # RAG 品質評估模組（開發中）
├── document_metadata.json  # 文件雜湊中繼資料
├── faiss_index.bin         # FAISS 向量索引
└── faiss_texts.json        # 索引對應的文字區塊
```

## 環境設定

建議使用 Python 3.11，並在**儲存庫根目錄**建立及啟用虛擬環境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

目前專案尚未提供 `requirements.txt`。安裝主程式使用的套件：

```powershell
python -m pip install google-genai numpy faiss-cpu pypdf python-dotenv
```

在 `rag_document_chat/src/.env` 設定 Gemini API 金鑰：

```dotenv
GEMINI_API_KEY=你的_Gemini_API金鑰
```

請勿將 `.env` 或 API 金鑰提交至版本控制。

## 加入文件並啟動

將 `.pdf`、`.txt` 或 `.md` 檔案放進 `rag_document_chat/documents/`，然後從儲存庫根目錄執行：

```powershell
python rag_document_chat/src/main.py
```

首次執行時會讀取文件、建立 Embedding 並建立索引；之後會依文件內容是否變更更新索引。互動期間可使用：

- 輸入問題：搜尋文件並取得回答。
- `clear`：清除目前的對話紀錄。
- `exit`：結束程式。

## 問答流程

1. 載入 `documents/` 中支援的文件並計算文件雜湊值。
2. 將文件切分成文字區塊，並為新增或已修改的區塊建立 Embedding。
3. 把向量寫入 FAISS，依使用者問題搜尋最相關的 3 個區塊。
4. 將檢索內容與近期對話提供給 Gemini，產生繁體中文回答。

## 評估模組

`src/evaluation/` 與 `src/evaluation_api.py` 包含 RAG 回答及引用評估 API，與上述互動式聊天入口分開。從儲存庫根目錄啟動 API：

```powershell
python -m uvicorn --app-dir rag_document_chat/src evaluation_api:app --reload
```

啟動後可在 `http://127.0.0.1:8000/docs` 查看互動式 API 文件。這些功能仍在開發中，尚未整合成主程式的一部分。

## 注意事項與限制

- 使用 Gemini API 需要網路連線及有效的 API 金鑰。
- PDF 目前以文字擷取方式處理；掃描影像型 PDF 沒有 OCR，可能無法取得內容。
- 終端機會列出檢索到的文件來源，但回答目前尚未產生逐項對應的正式引用標記。
- 本專案用於學習與文件檢索示範；法律或其他重要資訊請回到原始文件核對。