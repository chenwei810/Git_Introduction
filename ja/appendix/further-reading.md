<!-- source: zh-TW/appendix/further-reading.md | sha: c05cb50247fe -->

# 付録 D　参考文献

この付録では、各章で引用した資料と、さらに詳しく知りたいときに役立つ書籍、公式ドキュメント、練習用のサイトをまとめました。英語の資料も多いので、[付録 A　用語集](glossary.md)と合わせて読んでください。

---

## 入門と総合

| 資料 | 説明 | 関連する章 |
|---|---|---|
| Scott Chacon、Ben Straub『[Pro Git](https://git-scm.com/book/ja/v2)』第 2 版 | もっとも充実した Git の入門書。オンラインで無料で読め、日本語訳もある | 全体 |
| Git 公式サイト：[About Git](https://git-scm.com/about) | Git の特徴と設計の考え方 | 0 |
| Git 公式ドキュメント：[Reference](https://git-scm.com/docs) | すべてのコマンドの詳しい説明。ターミナルで `git help <コマンド>` でも開ける | 全体 |

## Git の内部

| 資料 | 説明 | 関連する章 |
|---|---|---|
| 『Pro Git』第 10 章　Git の内側 | オブジェクト、参照、packfile、転送プロトコル。「もっと詳しく」の続き | 2～5、9、10 |
| 『Pro Git』7.7 節　リセットコマンド詳説 | 3 つのツリーという考え方で `reset` と `checkout` を説明する | 9 |
| Git 公式ドキュメント：[git-cat-file](https://git-scm.com/docs/git-cat-file)、[git-reflog](https://git-scm.com/docs/git-reflog) | オブジェクトを開く、HEAD がたどった道を見る | 3、9 |

## 共同作業と GitHub

| 資料 | 説明 | 関連する章 |
|---|---|---|
| GitHub Docs：[リモートリポジトリについて](https://docs.github.com/ja/get-started/getting-started-with-git/about-remote-repositories) | HTTPS と SSH の 2 つの接続方法 | 6 |
| GitHub Docs：[プルリクエストについて](https://docs.github.com/ja/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) | プルリクエストの作成、レビュー、マージ | 7 |
| GitHub Docs：[保護されたブランチについて](https://docs.github.com/ja/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) | ブランチ保護のさまざまなルール | 7 |
| GitHub Docs：[リリースについて](https://docs.github.com/ja/repositories/releasing-projects-on-github/about-releases) | タグをもとにバージョンを公開する | 8 |
| GitHub Docs：[リポジトリからの機微なデータの削除](https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) | 秘密情報が漏れたあとの履歴の消し方 | 10 |

## ブランチ戦略、バージョン、コミットメッセージ

| 資料 | 説明 | 関連する章 |
|---|---|---|
| [セマンティック バージョニング 2.0.0](https://semver.org/lang/ja/) | メジャー、マイナー、パッチの規則。日本語版がある | 8 |
| [Trunk Based Development](https://trunkbaseddevelopment.com/) | トランクベース開発の詳しい解説 | 8 |
| Vincent Driessen「[A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)」 | Git Flow を提案した元の記事。のちに作者が向いている場面についての注記を加えている | 8 |
| Chris Beams「[How to Write a Git Commit Message](https://cbea.ms/git-commit/)」 | コミットメッセージの書き方の定番の記事 | 10 |
| [Conventional Commits](https://www.conventionalcommits.org/ja/v1.0.0/) | `fix:`、`feat:` などの接頭辞でコミットメッセージを整理する規約。日本語版がある | 10 |

## ツール

| 資料 | 説明 | 関連する章 |
|---|---|---|
| [Sourcetree の公式サイト](https://www.sourcetreeapp.com/) | Sourcetree のダウンロード | 1 |
| [Git LFS](https://git-lfs.com/) | Git で大きなファイルを管理する | 10 |
| [git filter-repo](https://github.com/newren/git-filter-repo) | 履歴を書き換え、漏れた秘密情報を消すためのツール | 10 |

## 練習

| 資料 | 説明 | 関連する章 |
|---|---|---|
| [Learn Git Branching](https://learngitbranching.js.org/?locale=ja) | ブラウザでアニメーションを見ながら、ブランチ、マージ、rebase を練習できる。日本語の画面がある | 4、5 |
| [GitHub Skills](https://skills.github.com/) | GitHub 上で 1 歩ずつ進める対話型のコース | 6～8 |

---

[← 付録 C　コマンドと Sourcetree の対応表](commands-and-sourcetree.md) ｜ [目次](../README.md) ｜ [出発点に戻る：第 0 章　Git の全体像 →](../0-before-you-start/00-overview/README.md)
