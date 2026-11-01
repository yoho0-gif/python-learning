# GitHub User Information (Modular Version)

## 專案介紹

本專案使用 Python 開發，透過 GitHub REST API 查詢指定使用者的公開資訊。

與前一版本相比，本專案將程式拆分為多個模組，讓程式更容易閱讀、維護及擴充，模擬實際軟體開發的專案結構。

---

## 功能

- 查詢 GitHub 使用者資訊
- 顯示使用者名稱
- 顯示姓名
- 顯示公開 Repository 數量
- 顯示 Followers / Following
- 顯示帳號建立時間
- 找不到使用者時顯示錯誤訊息

---

## 使用技術

- Python
- requests
- GitHub REST API
- JSON
- Python Module
- Function

---

## 專案結構

```
learning/Day06_github_user/
│
├── main.py          # 主程式
├── github_api.py    # GitHub API 呼叫
├── display.py       # 顯示畫面
├── requirements.txt
└── README.md
```


## ▶️ 執行方式

```bash
python main.py
```

輸入：

```
請輸入 GitHub 使用者：
torvalds
```

輸出：

```
=========================
GitHub User Information
=========================

使用者：torvalds
姓名：Linus Torvalds
公開 Repo：8
Followers：250000+
Following：0
建立時間：2011-09-03
```

---

## 本專案學習重點

本專案練習了以下內容：

- Python Module（模組）
- import 的使用方式
- Function 設計
- return 回傳資料
- requests 套件
- REST API
- JSON 解析
- 專案結構設計
- 程式碼分工（Separation of Concerns）

---

## 未來可擴充功能

- 查詢 Repository 清單
- 顯示個人簡介（bio）
- 顯示所在地（location）
- 顯示公司（company）
- 顯示個人網站（blog）
- 匯出查詢結果為 JSON 或 CSV
- 加入圖形化介面（Tkinter）
- 建立 Web 版本（Flask / FastAPI）

---

## 學習心得

將程式拆分為不同模組，使每個檔案只負責單一功能，提升程式的可讀性與維護性，也更貼近實際軟體開發流程。