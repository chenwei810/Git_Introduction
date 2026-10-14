# 附錄 A　術語總表

本表收錄書中出現的主要術語，依英文字母排序。「章節」欄是該術語主要出現或說明的章節編號。

「繁體中文」欄寫的是書中實際使用的說法。團隊裡習慣直接講英文的術語，例如 commit、tag、rebase，正文就直接用英文，這一欄會同時列出中文譯名，方便查詢。

這份術語表也是全書用詞的**單一來源**：撰寫或翻譯時，請以本表的用詞為準。新增語言時，在表格中加上該語言的欄位即可，詳見 [TRANSLATIONS.md](../../TRANSLATIONS.md)。

想知道團隊裡怎麼講這些詞，可以參考[附錄 B 現場行話](jargon.md)。

| 英文 | 縮寫 | 繁體中文 | 說明 | 章節 |
|---|---|---|---|---|
| Annotated Tag | — | 附註 tag | 帶有作者、日期與說明的 tag，本身是一個物件；發布版本用這種 | 8 |
| Blame | — | blame | 列出檔案每一行最後是在哪個 commit、由誰修改的 | 10 |
| Blob | — | blob | 存放一個檔案內容的物件，不含檔名 | 3 |
| Branch | — | 分支 | 貼在某個 commit 上、會跟著新 commit 往前移的名稱 | 4 |
| Branch Protection | — | 分支保護 | 平台上的規則，例如禁止直接推送、要求審查與自動檢查通過 | 7 |
| Centralized Version Control | — | 集中式版本控制 | 完整歷史只存在一台伺服器上的版本控制方式 | 0 |
| Clone | — | clone（複製儲存庫） | 把遠端儲存庫連同完整歷史複製到自己的電腦 | 6 |
| Code Review | — | 程式碼審查 | 合併之前，由其他人檢查修改的內容 | 7 |
| Commit | — | 提交；書中多直接說 commit | 一次完整的快照，加上作者、時間、訊息與上一個 commit 的編號 | 2、3 |
| Commit Message | — | commit 訊息 | 說明這次修改做了什麼、為什麼的文字，第一行是標題 | 2、10 |
| Conflict Marker | — | 衝突標記 | 檔案裡標出衝突範圍的 `<<<<<<<`、`=======`、`>>>>>>>` 三行 | 5 |
| Continuous Integration | CI | 持續整合 | 每次推送都自動建置與測試，結果顯示在 Pull Request 上 | 7 |
| CRLF、LF | — | 換行字元 | Windows 用 CRLF 表示換行，macOS 與 Linux 用 LF | 1 |
| Detached HEAD | — | detached HEAD | HEAD 直接指向某個 commit，而不是指向一條分支的狀態 | 4、8 |
| Directed Acyclic Graph | DAG | 有向無環圖 | commit 歷史的資料結構：每個 commit 指向上一個，不會繞回自己 | 5 |
| Distributed Version Control | — | 分散式版本控制 | 每個人的電腦上都有完整歷史的版本控制方式，Git 屬於這一種 | 0 |
| Fast-forward | — | 快轉 | 目標分支沒有新的 commit 時，合併只是把分支往前移，不產生新的 commit | 5 |
| Feature Branch | — | 功能分支 | 為了開發一個功能或修正而開的分支，完成後合併回 `main` | 8 |
| Fetch | — | fetch | 下載遠端的新 commit，更新遠端追蹤分支，但不動你的檔案 | 6 |
| Garbage Collection | gc | 垃圾回收 | 清掉沒有任何分支、tag 或 reflog 指向的物件 | 9 |
| Git Flow | — | Git Flow | 使用 `main`、`develop`、功能、release、hotfix 等多種分支的分支策略 | 8 |
| Git LFS（Large File Storage） | LFS | Git LFS | 把大檔案存在另外的伺服器，儲存庫裡只放指向它的小檔案 | 10 |
| .gitignore | — | .gitignore | 列出不要讓 Git 追蹤的檔案與資料夾 | 10 |
| Hash | — | 雜湊值 | 由內容算出來的固定長度編號，內容差一個字就完全不同 | 3 |
| Hash Function | — | 雜湊函式 | 把任意長度的資料算成雜湊值的函式 | 3 |
| HEAD | — | HEAD | 表示「你現在在哪裡」的指標，通常指向目前所在的分支 | 4 |
| Hotfix | — | hotfix（緊急修正） | 已經發布的版本出問題時，從那個版本開分支做的緊急修正 | 8 |
| Lightweight Tag | — | 輕量 tag | 只是一個指向 commit 的名稱，沒有作者與說明 | 8 |
| Loose Object | — | 鬆散物件 | 單獨壓縮存放的物件，之後會被打包成 packfile | 10 |
| Merge | — | 合併 | 把另一條分支的修改結合進目前的分支 | 5 |
| Merge Base | — | 合併基準 | 兩條分支最近的共同祖先 commit，三方合併以它為比較基準 | 5 |
| Merge Commit | — | 合併 commit | 有兩個上一個 commit 的 commit，記錄一次合併 | 5、7 |
| Merge Conflict | — | 衝突 | 兩條分支改到同一處，Git 無法自動決定要用哪一邊 | 5 |
| Object | — | 物件 | Git 儲存資料的基本單位，包括 blob、tree、commit 與附註 tag | 3 |
| origin | — | origin | clone 或加上遠端時預設使用的遠端名稱 | 6 |
| Packfile | — | packfile | 把許多物件壓縮在一起，相似的內容只存差異的檔案 | 10 |
| Parent Commit | — | 父 commit（上一個 commit） | commit 記錄的「前一個版本」；合併 commit 有兩個 | 3、5 |
| Personal Access Token | PAT | 個人存取權杖 | 代替密碼、用來向 GitHub 證明身分的一串字元 | 6 |
| Pull | — | pull | fetch 之後，再把遠端的新 commit 合併進目前的分支 | 6 |
| Pull Request | PR | Pull Request | 請求把一條分支合併進另一條，並在合併前討論與審查 | 7 |
| Push | — | push（推送） | 把本機的 commit 上傳到遠端 | 6 |
| Push Protection | — | 推送保護 | 平台偵測到密碼或金鑰時，擋下這次推送的功能 | 10 |
| Rebase | — | rebase（重新定基） | 把一串 commit 搬到新的起點上重新做一次，commit 編號會改變 | 5 |
| Rebase and Merge | — | Rebase and merge | Pull Request 的合併方式之一：把分支上的 commit 一個一個接到目標分支上 | 7 |
| Reflog | — | reflog | 記錄 HEAD 與分支曾經指向哪些 commit，用來救回「消失」的 commit | 9 |
| Release | — | release（發布版本） | 平台上以 tag 為基礎、附上發布說明與檔案的版本 | 8 |
| Remote | — | 遠端 | 另一個地方的同一個儲存庫，通常在 GitHub 上 | 6 |
| Remote Repository | — | 遠端儲存庫 | 放在伺服器上、大家約好以它為準的儲存庫 | 6 |
| Remote-tracking Branch | — | 遠端追蹤分支 | 記錄遠端分支上次看到的位置，例如 `origin/main` | 6 |
| Repository | repo | 儲存庫 | Git 記錄專案所有版本的地方，也就是專案資料夾裡的 `.git` | 2 |
| Reset | — | reset | 把目前的分支移回某個 commit，依模式決定是否一併改動暫存區與檔案 | 9 |
| Restore | — | restore | 把檔案還原成暫存區或某個 commit 裡的樣子 | 9 |
| Revert | — | revert | 新增一個反向的 commit，抵銷某個舊 commit 的修改，不改寫歷史 | 9 |
| Semantic Versioning | SemVer | 語意化版本 | 用「主版號.次版號.修訂號」表示這次改動大小的版本號規則 | 8 |
| SHA-1、SHA-256 | — | SHA-1、SHA-256 | Git 用來計算物件編號的兩種雜湊演算法，編號分別是 40 和 64 個字元 | 3 |
| Snapshot | — | 快照 | 某個時間點所有檔案的完整樣子 | 3 |
| Squash and Merge | — | Squash and merge | Pull Request 的合併方式之一：把分支上的所有修改壓成一個新的 commit | 7 |
| SSH Key | — | SSH 金鑰 | 一對公鑰與私鑰，用來向 GitHub 證明身分 | 6 |
| Staging Area | — | 暫存區 | 準備放進下一個 commit 的內容，也叫 index | 2 |
| Stash | — | stash | 把還沒 commit 的修改暫時收起來，工作目錄回到乾淨狀態 | 9 |
| Submodule | — | 子模組 | 在一個儲存庫裡，固定引用另一個儲存庫的某個 commit | 10 |
| Tag | — | tag（標籤） | 固定貼在某個 commit 上、不會移動的名稱，通常用來標示版本 | 8 |
| Terminal | — | 終端機 | 輸入文字指令的視窗 | 1 |
| Three-way Merge | — | 三方合併 | 用合併基準與兩條分支的版本比較，自動合併兩邊的修改 | 5 |
| Tree | — | tree | 代表一個資料夾的物件，列出裡面的檔名與對應的 blob 或 tree | 3 |
| Trunk-Based Development | — | 主幹開發 | 只用 `main` 加上短命的功能分支，頻繁合併的分支策略 | 8 |
| Two-Factor Authentication | 2FA | 兩步驟驗證 | 登入時除了密碼，還要輸入手機產生的驗證碼 | 1 |
| Untracked File | — | 未追蹤的檔案 | 在工作目錄裡、但 Git 還沒開始記錄的檔案 | 2 |
| Version Control | — | 版本控制 | 記錄檔案每一個版本，並能比較、回復與合併的方法 | 0 |
| Working Directory | — | 工作目錄 | 你實際打開、編輯的那些檔案 | 2 |

---

[← 第 10 章 好習慣](../3-when-things-go-wrong/10-good-habits/README.md) ｜ [目錄](../README.md) ｜ [附錄 B 現場行話 →](jargon.md)
