# 附錄 C　指令與 Sourcetree 對照表

本附錄把各章結尾的「📋 本章指令」依操作分類合在一起。想做某件事卻忘了怎麼做時，從這裡查，再到「章節」欄的那一章看完整說明。

Sourcetree 的按鈕名稱以英文介面為準。Windows 與 macOS 版的介面略有不同，差異較大的地方會在括號註明 macOS 的位置。表中的「—」表示 Sourcetree 沒有對應的按鈕，可以按工具列的 **Terminal** 開啟終端機輸入指令。

---

## 設定

| 想做的事 | 指令 | 在 Sourcetree 裡 | 章節 |
|---|---|---|---|
| 確認 Git 的版本 | `git --version` | — | 1 |
| 設定姓名與 email | `git config --global user.name`、`user.email` | Tools → Options → General（macOS：Settings → General） | 1 |
| 新儲存庫的分支叫 main | `git config --global init.defaultBranch main` | — | 1 |
| 設定換行（macOS、Linux） | `git config --global core.autocrlf input` | — | 1 |
| 列出全域設定 | `git config --global --list` | — | 1 |
| 連結 GitHub 帳號 | — | Tools → Options → Authentication（macOS：Settings → Accounts） | 1 |

## 建立與取得儲存庫

| 想做的事 | 指令 | 在 Sourcetree 裡 | 章節 |
|---|---|---|---|
| 把資料夾變成儲存庫 | `git init` | Create（macOS：New → Create Local Repository） | 2 |
| 複製整個遠端儲存庫 | `git clone <網址>` | 新分頁的 Clone | 6 |

## 記錄修改

| 想做的事 | 指令 | 在 Sourcetree 裡 | 章節 |
|---|---|---|---|
| 查看目前狀態 | `git status` | 左側的 File Status | 2 |
| 把檔案放進暫存區 | `git add <檔案>`、`git add .` | 選取檔案 → Stage Selected，或 Stage All | 2 |
| 看還沒放進暫存區的修改 | `git diff` | 點 Unstaged files 裡的檔案 | 2 |
| 看已經放進暫存區的修改 | `git diff --staged` | 點 Staged files 裡的檔案 | 2 |
| 提交 | `git commit -m "訊息"` | 輸入訊息 → Commit | 2 |
| 提交所有改過的檔案 | `git commit -am "訊息"` | Stage All → Commit | 4 |
| 寫有內文的 commit 訊息 | `git commit -m "標題" -m "內文"` | 訊息欄第一行寫標題，空一行寫內文 | 10 |

## 查看歷史

| 想做的事 | 指令 | 在 Sourcetree 裡 | 章節 |
|---|---|---|---|
| 查看歷史 | `git log` | 左側的 History | 3 |
| 一個 commit 一行 | `git log --oneline` | History 預設就是這樣 | 3 |
| 畫出所有分支的歷史 | `git log --oneline --graph --all` | History，選擇 All Branches | 4 |
| 看某個 commit 改了什麼 | `git show <編號>` | 在 History 點那個 commit | 3 |
| 只看改了哪些檔案 | `git show --stat <編號>` | 在 History 點 commit，看下方的檔案清單 | 3 |
| 查每一行是誰改的 | `git blame <檔案>` | 右鍵檔案 → Blame Selected | 10 |
| 打開一個物件 | `git cat-file -p <編號>` | — | 3 |
| 目前離哪個 tag 最近 | `git describe` | — | 8 |

## 分支

| 想做的事 | 指令 | 在 Sourcetree 裡 | 章節 |
|---|---|---|---|
| 列出分支 | `git branch` | 左側的 Branches | 4 |
| 開新分支並切換過去 | `git switch -c <名稱>` | 工具列的 Branch | 4 |
| 切換分支 | `git switch <名稱>` | 雙擊左側的分支名稱 | 4 |
| 從 tag 開分支 | `git switch -c <分支> <tag>` | 在 History 右鍵該 commit → Branch | 8 |
| 刪掉已經合併的分支 | `git branch -d <分支>` | 右鍵分支 → Delete | 5 |

## 合併

| 想做的事 | 指令 | 在 Sourcetree 裡 | 章節 |
|---|---|---|---|
| 把某條分支合進目前的分支 | `git merge <分支>` | 右鍵分支 → Merge … into current branch | 5 |
| 一定要做合併 commit | `git merge --no-ff <分支>` | Merge 時勾選 Create a new commit even if fast-forward is possible | 8 |
| 標記衝突已解決 | `git add <檔案>` | 右鍵檔案 → Resolve Conflicts → Mark Resolved | 5 |
| 用預設訊息完成合併 | `git commit --no-edit` | Commit | 5 |
| 放棄這次合併 | `git merge --abort` | — | 5 |
| 把分支重新接到 main 前端 | `git rebase main` | 右鍵 main → Rebase current changes onto main | 5 |

## 遠端

| 想做的事 | 指令 | 在 Sourcetree 裡 | 章節 |
|---|---|---|---|
| 加上遠端 | `git remote add origin <網址>` | Settings → Remotes → Add | 6 |
| 查看遠端 | `git remote -v` | Settings → Remotes | 6 |
| 第一次推送一條分支 | `git push -u origin <分支>` | Push，勾選分支與 Track | 6 |
| 推送 | `git push` | Push | 6 |
| 只下載，不動檔案 | `git fetch` | Fetch | 6 |
| 下載並合併 | `git pull` | Pull | 6 |
| 列出遠端有、自己還沒有的 commit | `git log main..origin/main` | — | 6 |
| 清掉已刪除的遠端分支 | `git fetch --prune` | Fetch，勾選 Prune | 7 |

## Pull Request

| 想做的事 | 指令 | 在 Sourcetree 裡 | 章節 |
|---|---|---|---|
| 開 Pull Request | —（在 GitHub 網頁上） | 右鍵分支 → Create Pull Request | 7 |
| 依審查意見修改後更新 PR | `git commit`、`git push` | Commit → Push | 7 |
| 合併後更新 main | `git switch main`、`git pull` | 雙擊 main → Pull | 7 |
| 把別人的 PR 抓下來測試 | `git fetch origin pull/<編號>/head:<名稱>` | — | 7 |

## tag 與發布

| 想做的事 | 指令 | 在 Sourcetree 裡 | 章節 |
|---|---|---|---|
| 打附註 tag | `git tag -a <名稱> -m "訊息"` | 工具列的 Tag | 8 |
| 列出 tag | `git tag` | 左側的 Tags | 8 |
| 推送 tag | `git push origin <名稱>` | 打 tag 時勾選 Push tag | 8 |

## 復原

| 想做的事 | 指令 | 在 Sourcetree 裡 | 章節 |
|---|---|---|---|
| 丟掉工作目錄的修改 | `git restore <檔案>` | 右鍵檔案 → Discard | 9 |
| 把檔案拿出暫存區 | `git restore --staged <檔案>` | Unstage Selected | 9 |
| 分支退回過去 | `git reset --soft/--mixed/--hard <commit>` | 右鍵 commit → Reset current branch to this commit（macOS：Reset main to this commit） | 9 |
| 新增反向的 commit | `git revert <commit>` | 右鍵 commit → Reverse commit | 9 |
| 查看 HEAD 走過的路 | `git reflog` | 按 Terminal 輸入指令 | 9 |
| 暫時收起修改 | `git stash`、`git stash pop` | 工具列的 Stash；右鍵 → Apply Stash | 9 |

## 忽略檔案、子模組與儲存庫大小

| 想做的事 | 指令 | 在 Sourcetree 裡 | 章節 |
|---|---|---|---|
| 停止追蹤，但保留檔案 | `git rm --cached <檔案>` | 右鍵檔案 → Stop Tracking | 10 |
| 查看檔案為什麼被忽略 | `git check-ignore -v <檔案>` | — | 10 |
| 加入子模組 | `git submodule add <網址> <資料夾>` | Repository → Add Submodule | 10 |
| 取得子模組 | `git submodule update --init` | — | 10 |
| 查看儲存庫的大小 | `git count-objects -vH` | — | 10 |

---

[← 附錄 B 現場行話](jargon.md) ｜ [目錄](../README.md) ｜ [附錄 D 延伸閱讀 →](further-reading.md)
