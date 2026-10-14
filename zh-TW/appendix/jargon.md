# 附錄 B　現場行話

軟體團隊的日常溝通，常常是中文夾雜英文，例如「你先 rebase 一下再發 PR」。剛加入團隊的人第一次聽到，常常一頭霧水。

本附錄收錄團隊裡常聽到的說法，並附上例句。各團隊的習慣用語不完全相同，這裡整理的是普遍的講法。正式的術語定義請見[附錄 A 術語總表](glossary.md)。

---

## 日常提交

| 行話 | 意思 | 例句 |
|---|---|---|
| commit 一下 | 把目前的修改記成一個版本 | 「改到一個段落就先 commit 一下，不要整天都不存。」 |
| stage | 把修改放進暫存區，也就是 `git add` | 「只 stage 修 bug 的那個檔案，除錯的輸出先不要。」 |
| 工作目錄是髒的 | 有還沒 commit 的修改（dirty） | 「你的工作目錄是髒的，先 commit 或 stash 再切分支。」 |
| 乾淨 | 沒有任何還沒 commit 的修改（clean） | 「`git status` 顯示乾淨了，可以切過去。」 |
| commit 編號、hash | commit 的雜湊值，通常只講前 7 碼 | 「回報問題時附上 commit 編號，前七碼就夠了。」 |
| 訊息寫清楚 | commit 訊息要說明做了什麼、為什麼 | 「`fix` 兩個字不夠，訊息寫清楚一點。」 |

## 分支與合併

| 行話 | 意思 | 例句 |
|---|---|---|
| 開分支、拉分支 | 從目前的 commit 建立一條新分支 | 「這個功能拉一條分支出來做，不要直接改 main。」 |
| 切過去 | 切換到另一條分支 | 「先切回 main，pull 最新的再開分支。」 |
| merge 回去 | 把分支合併回 `main` | 「測完就 merge 回 main。」 |
| 先把 main merge 回來 | 把 `main` 的新 commit 合併進自己的分支，保持同步 | 「你的分支落後很多，先把 main merge 回來。」 |
| rebase 一下 | 把自己的 commit 接到最新的 `main` 後面 | 「rebase 一下再發 PR，歷史會比較乾淨。」 |
| 解衝突 | 處理合併時的衝突 | 「這兩個 PR 改到同一個檔案，後合的人要解衝突。」 |
| 快轉過去 | 合併時只是把分支往前移（fast-forward） | 「main 沒有新東西，直接快轉過去就好。」 |
| 長命分支 | 開很久、一直沒合併的分支 | 「長命分支最後合併都很痛苦，盡量一兩天就合。」 |

## 遠端

| 行話 | 意思 | 例句 |
|---|---|---|
| 推上去 | `git push` | 「改好推上去，我再看。」 |
| 拉下來 | `git pull` | 「早上先拉下來，再開始寫。」 |
| fetch 一下 | 只下載、不合併，先看看遠端有什麼新東西 | 「fetch 一下，看 origin 上有沒有人動過。」 |
| 落後、領先 | 本機分支比遠端少了或多了幾個 commit（behind、ahead） | 「你的 main 落後 origin 三個 commit。」 |
| force push、強推 | 用 `git push --force` 蓋掉遠端的歷史 | 「已經分享出去的分支，絕對不要 force push。」 |
| 開 repo | 在 GitHub 上建立一個新的儲存庫 | 「這個工具另外開一個 repo 放。」 |

## Pull Request 與審查

| 行話 | 意思 | 例句 |
|---|---|---|
| 發 PR、開 PR | 建立 Pull Request | 「修完發個 PR，指定我 review。」 |
| review | 審查別人的修改 | 「這個 PR 誰有空幫忙 review？」 |
| approve、給過 | 審查通過 | 「要兩個人 approve 才能合。」 |
| LGTM | Looks Good To Me，看起來沒問題 | 「LGTM，可以合了。」 |
| nit | 小建議，不改也沒關係 | 「nit：這個變數名稱可以再清楚一點。」 |
| 被 request changes | 審查者要求修改後才能合併 | 「PR 被 request changes 了，改完再推一次。」 |
| CI 掛了、CI 紅了 | 自動檢查沒有通過 | 「CI 掛了，先看是哪個測試沒過。」 |
| squash | 把好幾個 commit 壓成一個 | 「零碎的 commit squash 成一個再合。」 |
| draft PR | 還沒完成、先給大家看方向的 PR | 「先開 draft PR，方便討論做法。」 |
| 合 PR | 按下合併按鈕 | 「CI 過了、也 approve 了，我來合 PR。」 |

## 發布

| 行話 | 意思 | 例句 |
|---|---|---|
| 打 tag | 在某個 commit 上建立版本標籤 | 「v1.0.0 的 tag 打了嗎？」 |
| release、發版 | 正式發布一個版本 | 「這週五發版，週四以後只收修正。」 |
| hotfix | 已發布的版本出問題時的緊急修正 | 「出貨的版本有問題，從 v1.0.0 開 hotfix 分支修。」 |
| code freeze | 發布前停止加入新功能 | 「下週 code freeze，新功能排到下一版。」 |
| 版號往上跳 | 依語意化版本調整版本號 | 「改了設定格式，不相容，主版號要往上跳。」 |

## 出事的時候

| 行話 | 意思 | 例句 |
|---|---|---|
| revert 掉 | 用 `git revert` 撤回某個 commit | 「已經推了，用 revert，不要 reset。」 |
| reset 回去 | 用 `git reset` 把分支移回過去 | 「還沒推的話，reset 回上一個 commit 就好。」 |
| stash 起來 | 暫時收起還沒 commit 的修改 | 「改到一半的先 stash 起來，切過去修 bug。」 |
| 翻 reflog | 用 `git reflog` 找回「消失」的 commit | 「commit 不見了？先別慌，翻一下 reflog。」 |
| blame 一下 | 用 `git blame` 查某一行是哪個 commit 改的 | 「blame 一下，看這行是為什麼改的。」 |
| 密碼被 commit 進去 | 機密被提交進歷史 | 「密碼被 commit 進去了，先換密碼，再處理歷史。」 |

「blame」字面上是「責怪」，但在團隊裡它只是用來查修改的來源和原因。好的團隊用它找出脈絡，不是用來找人負責。

---

[← 附錄 A 術語總表](glossary.md) ｜ [目錄](../README.md) ｜ [附錄 C 指令與 Sourcetree 對照表 →](commands-and-sourcetree.md)
