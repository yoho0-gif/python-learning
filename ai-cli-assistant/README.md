# Gemini AI Chat CLI

使用 Python 與 Google Gemini API 開發的終端機 AI 聊天助手。

支援多輪對話、角色切換、聊天歷史以及 Prompt Engineering，是一個練習 AI API 串接與模組化設計的專案。

---

# 功能

-  Gemini AI 對話
-  多輪聊天（Conversation History）
-  System Prompt（角色扮演）
-  模式切換（`/switch`）
-  清除聊天紀錄（`clear`）
-  查看目前模式（`/help`）
-  離開程式（`exit`）
-  基本例外處理（Exception Handling）

---

# AI 模式

| 模式 | 說明 |
|------|------|
| Python 講師 | 使用初學者容易理解的方式解釋 Python |
| 英文老師 | 提供文法說明、例句與翻譯 |
| 履歷顧問 | 提供履歷修改與求職建議 |
| 面試官 | 模擬技術面試並逐步提問 |

---

# 專案結構

```
ai-chat-cli/
│
├── src/
│   ├── main.py
│   ├── config.py
│   ├── display.py
│   ├── gemini_client.py
│   ├── history.py
│   └── prompt_templates.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 安裝

建立虛擬環境：

```bash
python -m venv .venv
```

啟動虛擬環境：

Windows PowerShell：

```powershell
.venv\Scripts\Activate.ps1
```

安裝套件：

```bash
pip install -r requirements.txt
```

---

# 建立 `.env`

請建立 `.env`：

```env
GEMINI_API_KEY=你的_API_Key
```

---

# 執行

```bash
python src/main.py
```

---

# 使用方式

程式啟動後先選擇 AI 模式：

```
1. Python 講師
2. 英文老師
3. 履歷顧問
4. 面試官
```

聊天時可使用指令：

| 指令 | 功能 |
|------|------|
| `/help` | 顯示目前 AI 模式 |
| `/switch` | 切換 AI 模式 |
| `clear` | 清除聊天紀錄 |
| `exit` | 結束程式 |

---

# 使用技術

- Python 3
- Google Gemini API
- google-genai
- python-dotenv

---

# 學習重點

本專案練習了：

- 模組化設計
- Prompt Engineering
- Conversation History
- API 串接
- System Prompt
- Exception Handling

---

# 未來規劃

- [ ] Markdown 聊天紀錄匯出
- [ ] 串流（Streaming）回覆
- [ ] 對話紀錄儲存（SQLite）
- [ ] GUI 介面（Tkinter / PySide6）
- [ ] Web 版本（Streamlit / FastAPI）