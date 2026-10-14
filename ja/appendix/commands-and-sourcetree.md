<!-- source: zh-TW/appendix/commands-and-sourcetree.md | sha: 438d3b61b039 -->

# 付録 C　コマンドと Sourcetree の対応表

この付録は、各章の最後にある「📋 この章のコマンド」を、操作ごとにまとめ直したものです。何かをしたいのにやり方を忘れたときはここで探し、「章」の列にある章で詳しい説明を読んでください。

Sourcetree のボタンやメニューの名前は英語の画面に合わせています。Windows 版と macOS 版は画面が少し違い、違いが大きいところはかっこで macOS 版の場所を示しています。表の「—」は Sourcetree に対応するボタンがないことを表します。ツールバーの **Terminal** を押してターミナルを開き、コマンドを入力してください。

---

## 設定

| やりたいこと | コマンド | Sourcetree では | 章 |
|---|---|---|---|
| Git のバージョンを確認する | `git --version` | — | 1 |
| 名前とメールアドレスを設定する | `git config --global user.name`、`user.email` | Tools → Options → General（macOS：Settings → General） | 1 |
| 新しいリポジトリのブランチ名を main にする | `git config --global init.defaultBranch main` | — | 1 |
| 改行を設定する（macOS、Linux） | `git config --global core.autocrlf input` | — | 1 |
| global の設定を一覧表示する | `git config --global --list` | — | 1 |
| GitHub アカウントを接続する | — | Tools → Options → Authentication（macOS：Settings → Accounts） | 1 |

## リポジトリを作る、取ってくる

| やりたいこと | コマンド | Sourcetree では | 章 |
|---|---|---|---|
| フォルダをリポジトリにする | `git init` | Create（macOS：New → Create Local Repository） | 2 |
| リモートリポジトリを丸ごとコピーする | `git clone <URL>` | 新しいタブの Clone | 6 |

## 変更を記録する

| やりたいこと | コマンド | Sourcetree では | 章 |
|---|---|---|---|
| 現在の状態を見る | `git status` | 左側の File Status | 2 |
| ファイルをステージングエリアに入れる | `git add <ファイル>`、`git add .` | ファイルを選ぶ → Stage Selected、または Stage All | 2 |
| まだステージしていない変更を見る | `git diff` | Unstaged files のファイルをクリック | 2 |
| ステージした変更を見る | `git diff --staged` | Staged files のファイルをクリック | 2 |
| コミットする | `git commit -m "メッセージ"` | メッセージを入力 → Commit | 2 |
| 変更したファイルをすべてコミットする | `git commit -am "メッセージ"` | Stage All → Commit | 4 |
| 本文付きのコミットメッセージを書く | `git commit -m "件名" -m "本文"` | メッセージ欄の 1 行目に件名、1 行空けて本文 | 10 |

## 履歴を見る

| やりたいこと | コマンド | Sourcetree では | 章 |
|---|---|---|---|
| 履歴を見る | `git log` | 左側の History | 3 |
| 1 つのコミットを 1 行で | `git log --oneline` | History は最初からこの形 | 3 |
| すべてのブランチの履歴を描く | `git log --oneline --graph --all` | History で All Branches を選ぶ | 4 |
| コミットで何を変えたかを見る | `git show <番号>` | History でそのコミットをクリック | 3 |
| 変えたファイルだけを見る | `git show --stat <番号>` | History でコミットをクリックし、下のファイル一覧を見る | 3 |
| 各行を誰が変えたかを調べる | `git blame <ファイル>` | ファイルを右クリック → Blame Selected | 10 |
| オブジェクトを開く | `git cat-file -p <番号>` | — | 3 |
| いちばん近いタグを調べる | `git describe` | — | 8 |

## ブランチ

| やりたいこと | コマンド | Sourcetree では | 章 |
|---|---|---|---|
| ブランチを一覧表示する | `git branch` | 左側の Branches | 4 |
| 新しいブランチを作って切り替える | `git switch -c <名前>` | ツールバーの Branch | 4 |
| ブランチを切り替える | `git switch <名前>` | 左側のブランチ名をダブルクリック | 4 |
| タグからブランチを作る | `git switch -c <ブランチ> <タグ>` | History でそのコミットを右クリック → Branch | 8 |
| マージ済みのブランチを削除する | `git branch -d <ブランチ>` | ブランチを右クリック → Delete | 5 |

## マージ

| やりたいこと | コマンド | Sourcetree では | 章 |
|---|---|---|---|
| あるブランチをいまのブランチにマージする | `git merge <ブランチ>` | ブランチを右クリック → Merge … into current branch | 5 |
| 必ずマージコミットを作る | `git merge --no-ff <ブランチ>` | Merge で Create a new commit even if fast-forward is possible にチェック | 8 |
| コンフリクトを解決済みにする | `git add <ファイル>` | ファイルを右クリック → Resolve Conflicts → Mark Resolved | 5 |
| 既定のメッセージでマージを完了する | `git commit --no-edit` | Commit | 5 |
| このマージをやめる | `git merge --abort` | — | 5 |
| ブランチを main の先に付け直す | `git rebase main` | main を右クリック → Rebase current changes onto main | 5 |

## リモート

| やりたいこと | コマンド | Sourcetree では | 章 |
|---|---|---|---|
| リモートを追加する | `git remote add origin <URL>` | Settings → Remotes → Add | 6 |
| リモートを確認する | `git remote -v` | Settings → Remotes | 6 |
| ブランチを初めてプッシュする | `git push -u origin <ブランチ>` | Push で、ブランチと Track にチェック | 6 |
| プッシュする | `git push` | Push | 6 |
| ダウンロードだけして、ファイルは変えない | `git fetch` | Fetch | 6 |
| ダウンロードしてマージする | `git pull` | Pull | 6 |
| リモートにあって自分にないコミットを一覧する | `git log main..origin/main` | — | 6 |
| 削除されたリモートブランチを片づける | `git fetch --prune` | Fetch で Prune にチェック | 7 |

## プルリクエスト

| やりたいこと | コマンド | Sourcetree では | 章 |
|---|---|---|---|
| プルリクエストを作る | —（GitHub の Web ページで） | ブランチを右クリック → Create Pull Request | 7 |
| レビューを受けて直し、PR を更新する | `git commit`、`git push` | Commit → Push | 7 |
| マージ後に main を更新する | `git switch main`、`git pull` | main をダブルクリック → Pull | 7 |
| ほかの人の PR を取ってきてテストする | `git fetch origin pull/<番号>/head:<名前>` | — | 7 |

## タグとリリース

| やりたいこと | コマンド | Sourcetree では | 章 |
|---|---|---|---|
| 注釈付きタグを付ける | `git tag -a <名前> -m "メッセージ"` | ツールバーの Tag | 8 |
| タグを一覧表示する | `git tag` | 左側の Tags | 8 |
| タグをプッシュする | `git push origin <名前>` | タグを付けるときに Push tag にチェック | 8 |

## 取り消し

| やりたいこと | コマンド | Sourcetree では | 章 |
|---|---|---|---|
| 作業ディレクトリの変更を捨てる | `git restore <ファイル>` | ファイルを右クリック → Discard | 9 |
| ファイルをステージングエリアから出す | `git restore --staged <ファイル>` | Unstage Selected | 9 |
| ブランチを過去に戻す | `git reset --soft/--mixed/--hard <コミット>` | コミットを右クリック → Reset current branch to this commit（macOS：Reset main to this commit） | 9 |
| 逆向きのコミットを作る | `git revert <コミット>` | コミットを右クリック → Reverse commit | 9 |
| HEAD がたどった道を見る | `git reflog` | Terminal を押してコマンドを入力 | 9 |
| 変更をいったんしまう | `git stash`、`git stash pop` | ツールバーの Stash。右クリック → Apply Stash | 9 |

## ファイルの無視、サブモジュール、リポジトリの大きさ

| やりたいこと | コマンド | Sourcetree では | 章 |
|---|---|---|---|
| 追跡はやめるが、ファイルは残す | `git rm --cached <ファイル>` | ファイルを右クリック → Stop Tracking | 10 |
| ファイルが無視される理由を調べる | `git check-ignore -v <ファイル>` | — | 10 |
| サブモジュールを追加する | `git submodule add <URL> <フォルダ>` | Repository → Add Submodule | 10 |
| サブモジュールを取ってくる | `git submodule update --init` | — | 10 |
| リポジトリの大きさを調べる | `git count-objects -vH` | — | 10 |

---

[← 付録 B　現場の言い回し](jargon.md) ｜ [目次](../README.md) ｜ [付録 D　参考文献 →](further-reading.md)
