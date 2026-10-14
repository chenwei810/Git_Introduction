<!-- source: zh-TW/appendix/glossary.md | sha: 22760eca648a -->

# Appendix A: Glossary

This glossary lists the main terms in the book in alphabetical order. The "Chapter" column gives the chapters where each term mainly appears or is explained.

The "繁體中文" column shows the wording used in the Traditional Chinese original, which is useful when you work with Chinese-speaking teammates. For terms that teams usually say in English, such as commit, tag and rebase, the Chinese original uses the English word too, and this column also gives the Chinese translation for reference.

This glossary is also the **single source** for the book's wording: when writing or translating, follow the terms in this table. To add a language, add a column for it. See [TRANSLATIONS.md](../../TRANSLATIONS.md) for details.

To see how teams actually use these words, see [Appendix B: Team Jargon](jargon.md).

| English | Abbr. | 繁體中文 | Description | Chapter |
|---|---|---|---|---|
| Annotated Tag | — | 附註 tag | A tag with an author, a date and a message, stored as an object of its own; use it for releases | 8 |
| Blame | — | blame | Shows, for each line of a file, the commit and person that last changed it | 10 |
| Blob | — | blob | An object that stores the contents of one file, without its name | 3 |
| Branch | — | 分支 | A name attached to a commit that moves forward with each new commit | 4 |
| Branch Protection | — | 分支保護 | Platform rules such as forbidding direct pushes and requiring reviews and passing checks | 7 |
| Centralized Version Control | — | 集中式版本控制 | Version control in which the complete history exists on only one server | 0 |
| Clone | — | clone（複製儲存庫） | Copying a remote repository, with its full history, to your own computer | 6 |
| Code Review | — | 程式碼審查 | Having others check a change before it is merged | 7 |
| Commit | — | 提交；書中多直接說 commit | A complete snapshot, plus the author, time, message and the ID of the previous commit | 2, 3 |
| Commit Message | — | commit 訊息 | Text explaining what a change does and why; the first line is the subject | 2, 10 |
| Conflict Marker | — | 衝突標記 | The three lines `<<<<<<<`, `=======` and `>>>>>>>` that mark a conflict in a file | 5 |
| Continuous Integration | CI | 持續整合 | Building and testing automatically on every push, with the results shown on the pull request | 7 |
| CRLF, LF | — | 換行字元 | Line endings: Windows uses CRLF, while macOS and Linux use LF | 1 |
| Detached HEAD | — | detached HEAD | The state in which HEAD points directly at a commit instead of a branch | 4, 8 |
| Directed Acyclic Graph | DAG | 有向無環圖 | The data structure of commit history: each commit points to the previous one, and nothing loops back | 5 |
| Distributed Version Control | — | 分散式版本控制 | Version control in which everyone's computer has the full history; Git is one | 0 |
| Fast-forward | — | 快轉 | When the target branch has no new commits, a merge just moves the branch forward without a new commit | 5 |
| Feature Branch | — | 功能分支 | A branch created to develop one feature or fix, merged back into `main` when done | 8 |
| Fetch | — | fetch | Downloads new commits from the remote and updates remote-tracking branches, without touching your files | 6 |
| Garbage Collection | gc | 垃圾回收 | Removing objects that no branch, tag or reflog entry points to | 9 |
| Git Flow | — | Git Flow | A branching strategy using `main`, `develop`, feature, release and hotfix branches | 8 |
| Git LFS (Large File Storage) | LFS | Git LFS | Stores large files on a separate server, keeping only a small pointer file in the repository | 10 |
| .gitignore | — | .gitignore | A file listing the files and folders Git should not track | 10 |
| Hash | — | 雜湊值 | A fixed-length ID computed from content; change one character and it is completely different | 3 |
| Hash Function | — | 雜湊函式 | A function that turns data of any length into a hash | 3 |
| HEAD | — | HEAD | A pointer meaning "where you are now," usually pointing to the current branch | 4 |
| Hotfix | — | hotfix（緊急修正） | An urgent fix made on a branch created from a released version that has a problem | 8 |
| Lightweight Tag | — | 輕量 tag | Just a name pointing to a commit, with no author or message | 8 |
| Loose Object | — | 鬆散物件 | An object compressed and stored on its own; later packed into a packfile | 10 |
| Merge | — | 合併 | Bringing another branch's changes into the current branch | 5 |
| Merge Base | — | 合併基準 | The nearest common ancestor commit of two branches; a three-way merge compares against it | 5 |
| Merge Commit | — | 合併 commit | A commit with two previous commits, recording a merge | 5, 7 |
| Merge Conflict | — | 衝突 | Two branches changed the same place, and Git cannot decide which side to use | 5 |
| Object | — | 物件 | The basic unit Git stores data in: blobs, trees, commits and annotated tags | 3 |
| origin | — | origin | The default name for a remote when you clone or add one | 6 |
| Packfile | — | packfile | A file that compresses many objects together, storing only the differences between similar contents | 10 |
| Parent Commit | — | 父 commit（上一個 commit） | The "previous version" a commit records; a merge commit has two | 3, 5 |
| Personal Access Token | PAT | 個人存取權杖 | A string of characters used instead of a password to prove your identity to GitHub | 6 |
| Pull | — | pull | Fetches, then merges the remote's new commits into the current branch | 6 |
| Pull Request | PR | Pull Request | A request to merge one branch into another, with discussion and review before merging | 7 |
| Push | — | push（推送） | Uploads local commits to the remote | 6 |
| Push Protection | — | 推送保護 | A platform feature that blocks a push when it detects passwords or keys | 10 |
| Rebase | — | rebase（重新定基） | Replays a series of commits on a new starting point; the commit IDs change | 5 |
| Rebase and Merge | — | Rebase and merge | A pull request merge method that adds the branch's commits to the target branch one by one | 7 |
| Reflog | — | reflog | Records which commits HEAD and each branch have pointed to; used to rescue "lost" commits | 9 |
| Release | — | release（發布版本） | A version on the platform, based on a tag, with release notes and attached files | 8 |
| Remote | — | 遠端 | The same repository somewhere else, usually on GitHub | 6 |
| Remote Repository | — | 遠端儲存庫 | A repository on a server that everyone agrees to treat as the official copy | 6 |
| Remote-tracking Branch | — | 遠端追蹤分支 | Records where a remote branch was last seen, such as `origin/main` | 6 |
| Repository | repo | 儲存庫 | Where Git records every version of a project: the `.git` folder inside the project folder | 2 |
| Reset | — | reset | Moves the current branch back to a commit; the mode decides whether the staging area and files change too | 9 |
| Restore | — | restore | Restores a file to how it is in the staging area or in a commit | 9 |
| Revert | — | revert | Adds an opposite commit that cancels an older commit's changes, without rewriting history | 9 |
| Semantic Versioning | SemVer | 語意化版本 | A version number rule, major.minor.patch, that shows how big a change is | 8 |
| SHA-1, SHA-256 | — | SHA-1、SHA-256 | The two hash algorithms Git uses to compute object IDs, producing 40 and 64 characters | 3 |
| Snapshot | — | 快照 | What every file looks like at a point in time | 3 |
| Squash and Merge | — | Squash and merge | A pull request merge method that squashes all of a branch's changes into one new commit | 7 |
| SSH Key | — | SSH 金鑰 | A public and private key pair used to prove your identity to GitHub | 6 |
| Staging Area | — | 暫存區 | The contents going into the next commit; also called the index | 2 |
| Stash | — | stash | Puts uncommitted changes away temporarily, leaving the working directory clean | 9 |
| Submodule | — | 子模組 | A fixed reference, from inside one repository, to one commit of another repository | 10 |
| Tag | — | tag（標籤） | A name attached to a commit that never moves, usually used to mark versions | 8 |
| Terminal | — | 終端機 | A window for typing text commands | 1 |
| Three-way Merge | — | 三方合併 | Merging both sides' changes automatically by comparing the merge base with both branches | 5 |
| Tree | — | tree | An object representing a folder, listing file names and the blob or tree each points to | 3 |
| Trunk-Based Development | — | 主幹開發 | A branching strategy using only `main` plus short-lived feature branches, merged often | 8 |
| Two-Factor Authentication | 2FA | 兩步驟驗證 | Signing in with a code generated on your phone in addition to your password | 1 |
| Untracked File | — | 未追蹤的檔案 | A file in the working directory that Git has not started recording yet | 2 |
| Version Control | — | 版本控制 | A way of recording every version of files, so you can compare, restore and merge them | 0 |
| Working Directory | — | 工作目錄 | The files you actually open and edit | 2 |

---

[← Chapter 10: Good Habits](../3-when-things-go-wrong/10-good-habits/README.md) | [Contents](../README.md) | [Appendix B: Team Jargon →](jargon.md)
