# 第 2 章　三個區域：工作目錄、暫存區、儲存庫

> 📍 **專案與修改位置**
>
> - 專案進度：`fan-controller` 還只是一個普通的資料夾，本章讓它變成儲存庫，並做出第一個 commit
> - 前一站：bug 被發現，Git 和 Sourcetree 都已經裝好
> - **本章：修正寫好了，被放進暫存區**
> - 下一站：打開 commit，看看提交之後會變成什麼

---

## 為什麼要分成三個區域

用 Git 管理的檔案，會待在三個地方。用寄包裹來比喻最容易懂：

- **工作目錄（Working Directory）**是你的書桌。檔案放在上面，隨時可以改。
- **暫存區（Staging Area）**是準備寄出的紙箱。你從書桌上挑出這次要寄的東西，放進箱子。
- **儲存庫（Repository）**是寄件紀錄。封箱寄出之後，箱子裡有什麼就被永久記錄下來，這個動作就是**提交（Commit）**。

```mermaid
flowchart LR
    W["工作目錄"] -- "git add" --> S["暫存區"]
    S -- "git commit" --> R["儲存庫"]
```

為什麼還要多一個紙箱？因為你常常同時改了好幾件事。例如你修好了溫度換算，同時在 `main.c` 加了幾行除錯用的輸出。你只想把修正記成一個版本，除錯的程式不要。暫存區讓你挑選：這次要記錄哪些修改，其他的先留在書桌上。

> [!NOTE]
> **📖 名詞｜儲存庫（Repository）**
>
> - **定義**：Git 記錄一個專案所有版本的地方，就是專案資料夾裡那個隱藏的 `.git` 資料夾。
> - **現場用法**：大家通常直接叫 repo，例如「這個 repo 是韌體的，硬體圖檔在另一個 repo」。
> - **相關名詞**：工作目錄、暫存區、遠端儲存庫
> - **常見混淆**：專案資料夾不等於儲存庫。刪掉 `.git`，資料夾裡的檔案都還在，但所有歷史都沒了。

---

## 建立儲存庫：git init

在專案資料夾裡執行 `git init`，Git 就會建立 `.git` 資料夾，開始管理這個專案。

```bash
cd ~/git-practice/fan-controller
git init
```

**在 Sourcetree 裡**：**新分頁的 Create → 選擇 fan-controller 資料夾 → Create**（macOS 版是 **New → Create Local Repository**）。Sourcetree 會提醒資料夾已經存在，選擇繼續即可。

> [!TIP]
> **🔧 Know-how｜git init 之前，先確認自己在哪個資料夾**
>
> - **情境**：剛開啟終端機，就直接輸入 `git init`。
> - **做法**：先用 `pwd` 確認目前的位置，確定是專案資料夾再執行。
> - **為什麼**：終端機一開始通常在使用者的家目錄。在那裡執行 `git init`，整個家目錄都會被當成一個專案。
> - **沒做會怎樣**：`git status` 會列出成千上萬個檔案，之後在任何子資料夾裡都會誤用到這個儲存庫。要刪掉家目錄裡的 `.git` 才能恢復。
> - **相關章節**：[第 1 章 準備工具](../../0-before-you-start/01-setup/README.md)

<details>
<summary><strong>🔍 深入一點｜.git 資料夾裡有什麼</strong></summary>

整個 Git 就藏在 `.git` 裡。其中幾個最重要的項目，後面各章都會再遇到：

```text
HEAD       目前在哪一條分支（第 4 章）
config     這個儲存庫自己的設定（第 1 章）
index      暫存區（本章）
objects/   所有版本的內容（第 3 章）
refs/      分支和 tag（第 4、8 章）
```

這些都是一般的檔案。打開 `HEAD`，裡面只有一行 `ref: refs/heads/main`，意思是「現在在 main 分支上」。

</details>

---

## 看狀態：git status

`git status` 會告訴你每個檔案現在在哪一區。這是最常用的指令，不確定發生什麼事的時候，先打它就對了。

剛執行完 `git init` 時，Git 還沒開始追蹤任何檔案，所以每個檔案都被列在「未追蹤」（Untracked files）底下。

| `git status` 裡的標題 | 意思 |
|---|---|
| Untracked files | Git 從來沒記錄過的新檔案 |
| Changes not staged for commit | 改過了，但還在書桌上 |
| Changes to be committed | 已經放進紙箱，下次 commit 會記錄 |

**在 Sourcetree 裡**：左側的 **File Status**。下半部的 Unstaged files 是書桌，上半部的 Staged files 是紙箱。

![Sourcetree File Status 畫面的示意圖](../../../images/02-file-status.svg)

*圖：① Staged files，也就是紙箱；② Unstaged files，也就是書桌；③ Stage All，把書桌上的修改全部放進紙箱；④ 訊息欄；⑤ Commit 按鈕。右邊是選取的檔案的差異。*

---

## 放進暫存區並提交：git add、git commit

**挑選檔案 → git add → git commit**

1. **git add**：把檔案放進暫存區。`git add .` 代表目前資料夾裡的所有檔案。
2. **git commit**：把暫存區的內容記錄成一個版本，`-m` 後面是這個版本的說明。

```bash
git add .
git commit -m "Initial commit"
```

**在 Sourcetree 裡**：**Stage All → 在下方輸入訊息 → Commit**。

專案的第一個 commit 就誕生了。這時的歷史只有一個點：

```mermaid
gitGraph
    commit id: "建立專案"
```

> [!NOTE]
> **📖 名詞｜暫存區（Staging Area）**
>
> - **定義**：下一個 commit 的內容清單。commit 時，Git 只記錄暫存區裡的東西。
> - **現場用法**：動詞常說「stage」或「加進去」，例如「這個檔案你還沒 stage，所以沒 commit 到」。
> - **相關名詞**：工作目錄、`git add`、index
> - **常見混淆**：暫存區又叫 index，兩個是同一個東西。它和第 9 章的 `git stash`（把修改暫時收起來）完全不同。

---

## 修正那個 bug：git diff

現在來修正溫度換算。打開 `sensor.c`，註解寫著感測器在 0 °C 時輸出 500 mV，程式卻寫成 `(mv - 600)`。把 600 改成 500 存檔後，`sensor.c` 就變成「改過了，但還在書桌上」。在放進紙箱之前，先用 `git diff` 看看到底改了什麼：

```bash
git diff             # 看書桌上和紙箱裡有什麼不同
git add sensor.c
git diff --staged    # 看紙箱裡和上一個 commit 有什麼不同
```

**在 Sourcetree 裡**：在 File Status 點一下檔案，右邊就會顯示差異。紅色是刪掉的行，綠色是新增的行。

暫存區記錄的是 `git add` 那一刻的內容。如果 add 之後又改了同一個檔案，`git status` 會同時在兩個標題底下列出它，要再 add 一次，新的修改才會進紙箱。

> [!TIP]
> **🔧 Know-how｜commit 之前，先看 git diff --staged**
>
> - **情境**：改了好幾個檔案，準備要 commit。
> - **做法**：先執行 `git diff --staged`，逐行確認紙箱裡的東西都是你想記錄的。
> - **為什麼**：`git add .` 會把資料夾裡所有改過的檔案一起放進去，包括除錯用的輸出、暫時改掉的設定值。
> - **沒做會怎樣**：除錯的程式被記進正式版本，甚至一路被燒進產品。之後要找出是哪個 commit 帶進來的，得花更多時間。
> - **相關章節**：[第 10 章 好習慣](../../3-when-things-go-wrong/10-good-habits/README.md)

<details>
<summary><strong>🔍 深入一點｜暫存區其實是一個檔案</strong></summary>

暫存區就是 `.git/index` 這個二進位檔。它記錄每個檔案的路徑、權限，以及內容的雜湊值。用下面的指令可以看到它的內容：

```text
$ git ls-files --stage
100644 6305a5e833282a7ac1c6fa02a0c455706b169145 0	Makefile
100644 c50b3ace27f06cf09657fbd19635ee6d06f268ed 0	README.md
```

中間那串 40 個字元，是檔案內容的雜湊值。`git add` 做的事，其實是把檔案內容存進 `.git/objects/`，再把雜湊值寫進 index。所以 add 的當下，內容就已經被 Git 保存起來了，這也是 add 之後再改檔案不會影響紙箱的原因。第 3 章會打開這些物件。

</details>

---

## 常見問題

| 狀況 | 原因 | 怎麼處理 |
|---|---|---|
| `fatal: not a git repository` | 目前所在的資料夾不是儲存庫 | 用 `cd` 進到專案資料夾 |
| `Author identity unknown` | 還沒設定姓名與 email | 照第 1 章設定 `user.name` 與 `user.email` |
| `LF will be replaced by CRLF` | Windows 與其他系統的換行字元不同 | 這是提醒，可以忽略，第 1 章有說明 |

---

## 🧪 跟著做

**開始前**：在本書的根目錄執行 `bash practice/setup.sh 2`，把練習專案複製到 `~/git-practice/fan-controller`。這時它還不是儲存庫。

1. 建立儲存庫，做出第一個 commit：

   ```bash
   cd ~/git-practice/fan-controller
   git init
   git status          # 所有檔案都在 Untracked files 底下
   git add .
   git commit -m "Initial commit"
   ```

   在 Sourcetree 裡：新分頁的 Create 選擇這個資料夾，再 **Stage All → 輸入訊息 → Commit**。

2. 用編輯器打開 `sensor.c`，把 `(mv - 600)` 改成 `(mv - 500)` 後存檔。
3. 看差異，再把修正放進暫存區，但**先不要 commit**：

   ```bash
   git diff
   git add sensor.c
   git status
   ```

**你應該看到**：最後的 `git status` 第一行是 `On branch main`，並在 Changes to be committed 底下列出 `modified: sensor.c`。如果第一行是 `On branch master`，請照第 1 章設定預設分支，刪掉 `.git` 資料夾後重做。這筆修正會在第 4 章提交到新的分支上。

---

## 📋 本章指令

| 想做的事 | 指令 | 在 Sourcetree 裡 |
|---|---|---|
| 把資料夾變成儲存庫 | `git init` | Create（macOS：New → Create Local Repository） |
| 查看目前狀態 | `git status` | 左側的 File Status |
| 把檔案放進暫存區 | `git add <檔案>`、`git add .` | 選取檔案 → Stage Selected，或 Stage All |
| 提交 | `git commit -m "訊息"` | 輸入訊息 → Commit |
| 看還沒放進暫存區的修改 | `git diff` | 點 Unstaged files 裡的檔案 |
| 看已經放進暫存區的修改 | `git diff --staged` | 點 Staged files 裡的檔案 |

---

## 本章重點

1. 檔案會待在三個地方：工作目錄（書桌）、暫存區（紙箱）、儲存庫（寄件紀錄）。
2. `git add` 把修改放進暫存區，`git commit` 把暫存區記錄成一個版本。
3. 暫存區讓你挑選這次要記錄哪些修改，一個 commit 只放相關的東西。
4. 不確定狀況時先打 `git status`；commit 之前先看 `git diff --staged`。

---

## 延伸閱讀

- Scott Chacon、Ben Straub，《[Pro Git](https://git-scm.com/book/zh-tw/v2)》第二版，第 2 章（Git 的基本操作，可免費線上閱讀）
- Git 官方文件：[git-status](https://git-scm.com/docs/git-status)、[git-add](https://git-scm.com/docs/git-add)、[git-commit](https://git-scm.com/docs/git-commit)

---

[← 上一章：第 1 章 準備工具](../../0-before-you-start/01-setup/README.md) ｜ [目錄](../../README.md) ｜ [下一章：第 3 章 Commit 的真面目 →](../03-commits/README.md)
