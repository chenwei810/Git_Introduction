# 附錄 D　延伸閱讀

本附錄整理書中各章引用的參考資料，以及想深入了解時可以參考的書籍、官方文件與練習網站。這些資料大多是英文，閱讀時可以搭配[附錄 A 術語總表](glossary.md)。

---

## 入門與綜合

| 資料 | 說明 | 相關章節 |
|---|---|---|
| Scott Chacon、Ben Straub，《[Pro Git](https://git-scm.com/book/zh-tw/v2)》第二版 | 最完整的 Git 入門書，可以免費線上閱讀，也有繁體中文翻譯 | 全書 |
| Git 官方網站：[About Git](https://git-scm.com/about) | Git 的特色與設計理念 | 0 |
| Git 官方文件：[Reference](https://git-scm.com/docs) | 每個指令的完整說明，也可以在終端機用 `git help <指令>` 打開 | 全書 |

## Git 內部

| 資料 | 說明 | 相關章節 |
|---|---|---|
| 《Pro Git》第 10 章 Git 內部原理 | 物件、參考、packfile 與傳輸協定，是「深入一點」的延伸 | 2～5、9、10 |
| 《Pro Git》7.7 節 重置揭密 | 用三棵樹的觀念解釋 `reset` 與 `checkout` | 9 |
| Git 官方文件：[git-cat-file](https://git-scm.com/docs/git-cat-file)、[git-reflog](https://git-scm.com/docs/git-reflog) | 打開物件、查看 HEAD 走過的路 | 3、9 |

## 協作與 GitHub

| 資料 | 說明 | 相關章節 |
|---|---|---|
| GitHub 官方文件：[About remote repositories](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories) | HTTPS 與 SSH 兩種連線方式 | 6 |
| GitHub 官方文件：[About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) | Pull Request 的建立、審查與合併 | 7 |
| GitHub 官方文件：[About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) | 分支保護的各種規則 | 7 |
| GitHub 官方文件：[About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) | 以 tag 為基礎發布版本 | 8 |
| GitHub 官方文件：[Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) | 機密外洩後如何清除歷史 | 10 |

## 分支策略、版本與 commit 訊息

| 資料 | 說明 | 相關章節 |
|---|---|---|
| [語意化版本 2.0.0](https://semver.org/lang/zh-TW/) | 主版號、次版號、修訂號的規則，有繁體中文版 | 8 |
| [Trunk Based Development](https://trunkbaseddevelopment.com/) | 主幹開發的完整說明 | 8 |
| Vincent Driessen，〈[A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)〉 | 提出 Git Flow 的原始文章，作者後來也補充了它的適用範圍 | 8 |
| Chris Beams，〈[How to Write a Git Commit Message](https://cbea.ms/git-commit/)〉 | commit 訊息寫法的經典文章 | 10 |
| [約定式提交（Conventional Commits）](https://www.conventionalcommits.org/zh-hant/v1.0.0/) | 用 `fix:`、`feat:` 等前綴整理 commit 訊息的規範 | 10 |

## 工具

| 資料 | 說明 | 相關章節 |
|---|---|---|
| [Sourcetree 官方網站](https://www.sourcetreeapp.com/) | 下載 Sourcetree | 1 |
| [Git LFS](https://git-lfs.com/) | 用 Git 管理大檔案 | 10 |
| [git filter-repo](https://github.com/newren/git-filter-repo) | 改寫歷史、清除外洩機密的工具 | 10 |

## 練習

| 資料 | 說明 | 相關章節 |
|---|---|---|
| [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_TW) | 在瀏覽器裡用動畫練習分支、合併與 rebase，有繁體中文介面 | 4、5 |
| [GitHub Skills](https://skills.github.com/) | 在 GitHub 上一步一步完成的互動課程 | 6～8 |

---

[← 附錄 C 指令與 Sourcetree 對照表](commands-and-sourcetree.md) ｜ [目錄](../README.md) ｜ [回到起點：第 0 章 Git 全景 →](../0-before-you-start/00-overview/README.md)
