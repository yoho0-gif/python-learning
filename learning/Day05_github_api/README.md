# GitHub User Information

## 專案介紹

這是一個使用 Python 撰寫的 GitHub 使用者查詢工具。

使用 GitHub REST API 查詢指定使用者的公開資訊，並顯示：

- 使用者名稱
- 姓名
- 公開 Repository 數量
- Followers
- Following
- 帳號建立時間

---

## 使用技術

- Python 3
- requests
- GitHub REST API
- JSON
- Dictionary

---

## 安裝方式

安裝 requests：

```bash
pip install requests
```

---

## 執行方式

```bash
python github_user.py
```

---

## 執行畫面

請輸入 GitHub 使用者：

```
torvalds
```

輸出：

```
======================
GitHub User Information
======================

使用者：torvalds
姓名：Linus Torvalds
公開 Repo：8
Followers：250000+
Following：0
建立時間：2011-09-03
```

---

## 專案學習重點

本專案練習：

- requests 套件使用
- HTTP GET Request
- REST API
- JSON 資料解析
- Dictionary 操作
- API 錯誤處理

---

## 未來可新增功能

- 查詢 Repository 清單
- 顯示個人簡介（bio）
- 顯示所在地（location）
- 顯示首頁網址（blog）
- 匯出查詢結果成 JSON 或 CSV
- 圖形化介面（Tkinter 或 Streamlit）