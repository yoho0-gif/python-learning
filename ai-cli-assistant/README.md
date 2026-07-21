# Gemini AI Chat CLI

## 專案介紹

使用 Python 與 Google Gemini API 建立一個終端機聊天助手。

使用者可以在命令列輸入問題，AI 即時回覆內容。

---

## 功能

- AI 問答
- 持續聊天
- exit 離開
- 空字串檢查
- API Key 使用 .env 管理

---

## 使用技術

- Python
- google-genai
- python-dotenv

---

## 安裝

```bash
pip install -r requirements.txt
```

---

## 建立 .env

```
GEMINI_API_KEY=你的APIKEY
```

---

## 執行

```bash
python main.py
```

---

## 專案結構

```
src/
│
├── main.py
├── config.py
├── gemini_client.py
└── display.py
```