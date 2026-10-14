<!-- source: zh-TW/appendix/commands-and-sourcetree.md | sha: 438d3b61b039 -->

# Appendix C: Commands and Sourcetree

This appendix gathers the "📋 Commands in this chapter" tables from every chapter, grouped by task. When you want to do something but forget how, look it up here, then go to the chapter in the "Chapter" column for the full explanation.

Sourcetree button and menu names follow the English interface. The Windows and macOS versions differ slightly; where the difference is large, the macOS location is given in parentheses. A "—" means Sourcetree has no matching button; click **Terminal** on the toolbar to open a terminal and type the command.

---

## Setup

| What you want to do | Command | In Sourcetree | Chapter |
|---|---|---|---|
| Check the Git version | `git --version` | — | 1 |
| Set your name and email | `git config --global user.name`, `user.email` | Tools → Options → General (macOS: Settings → General) | 1 |
| Name the first branch of new repositories main | `git config --global init.defaultBranch main` | — | 1 |
| Set line endings (macOS, Linux) | `git config --global core.autocrlf input` | — | 1 |
| List global settings | `git config --global --list` | — | 1 |
| Connect your GitHub account | — | Tools → Options → Authentication (macOS: Settings → Accounts) | 1 |

## Creating and getting repositories

| What you want to do | Command | In Sourcetree | Chapter |
|---|---|---|---|
| Turn a folder into a repository | `git init` | Create (macOS: New → Create Local Repository) | 2 |
| Copy a whole remote repository | `git clone <URL>` | Clone in a new tab | 6 |

## Recording changes

| What you want to do | Command | In Sourcetree | Chapter |
|---|---|---|---|
| See the current state | `git status` | File Status on the left | 2 |
| Put files in the staging area | `git add <file>`, `git add .` | Select files → Stage Selected, or Stage All | 2 |
| See changes not yet staged | `git diff` | Click a file under Unstaged files | 2 |
| See staged changes | `git diff --staged` | Click a file under Staged files | 2 |
| Commit | `git commit -m "message"` | Type a message → Commit | 2 |
| Commit every changed file | `git commit -am "message"` | Stage All → Commit | 4 |
| Write a commit message with a body | `git commit -m "subject" -m "body"` | Subject on the first line of the message box, a blank line, then the body | 10 |

## Looking at history

| What you want to do | Command | In Sourcetree | Chapter |
|---|---|---|---|
| Look at the history | `git log` | History on the left | 3 |
| One commit per line | `git log --oneline` | History shows this by default | 3 |
| Draw the history of every branch | `git log --oneline --graph --all` | History, with All Branches selected | 4 |
| See what a commit changed | `git show <ID>` | Click the commit in History | 3 |
| See only which files changed | `git show --stat <ID>` | Click the commit in History and look at the file list below | 3 |
| Find who changed each line | `git blame <file>` | Right-click the file → Blame Selected | 10 |
| Open an object | `git cat-file -p <ID>` | — | 3 |
| Find the nearest tag | `git describe` | — | 8 |

## Branches

| What you want to do | Command | In Sourcetree | Chapter |
|---|---|---|---|
| List branches | `git branch` | Branches on the left | 4 |
| Create a branch and switch to it | `git switch -c <name>` | Branch on the toolbar | 4 |
| Switch branches | `git switch <name>` | Double-click the branch name on the left | 4 |
| Create a branch from a tag | `git switch -c <branch> <tag>` | Right-click the commit in History → Branch | 8 |
| Delete a branch that has been merged | `git branch -d <branch>` | Right-click the branch → Delete | 5 |

## Merging

| What you want to do | Command | In Sourcetree | Chapter |
|---|---|---|---|
| Merge a branch into the current branch | `git merge <branch>` | Right-click the branch → Merge … into current branch | 5 |
| Always make a merge commit | `git merge --no-ff <branch>` | Tick Create a new commit even if fast-forward is possible when merging | 8 |
| Mark a conflict as resolved | `git add <file>` | Right-click the file → Resolve Conflicts → Mark Resolved | 5 |
| Finish the merge with the default message | `git commit --no-edit` | Commit | 5 |
| Give up on this merge | `git merge --abort` | — | 5 |
| Replay the branch on top of main | `git rebase main` | Right-click main → Rebase current changes onto main | 5 |

## Remotes

| What you want to do | Command | In Sourcetree | Chapter |
|---|---|---|---|
| Add a remote | `git remote add origin <URL>` | Settings → Remotes → Add | 6 |
| Look at remotes | `git remote -v` | Settings → Remotes | 6 |
| Push a branch for the first time | `git push -u origin <branch>` | Push, ticking the branch and Track | 6 |
| Push | `git push` | Push | 6 |
| Download only, without touching files | `git fetch` | Fetch | 6 |
| Download and merge | `git pull` | Pull | 6 |
| List commits the remote has that you don't | `git log main..origin/main` | — | 6 |
| Remove deleted remote branches | `git fetch --prune` | Fetch, ticking Prune | 7 |

## Pull requests

| What you want to do | Command | In Sourcetree | Chapter |
|---|---|---|---|
| Open a pull request | — (on the GitHub website) | Right-click the branch → Create Pull Request | 7 |
| Update a PR after review | `git commit`, `git push` | Commit → Push | 7 |
| Update main after the merge | `git switch main`, `git pull` | Double-click main → Pull | 7 |
| Fetch someone's PR to test it | `git fetch origin pull/<number>/head:<name>` | — | 7 |

## Tags and releases

| What you want to do | Command | In Sourcetree | Chapter |
|---|---|---|---|
| Create an annotated tag | `git tag -a <name> -m "message"` | Tag on the toolbar | 8 |
| List tags | `git tag` | Tags on the left | 8 |
| Push a tag | `git push origin <name>` | Tick Push tag when creating it | 8 |

## Undoing

| What you want to do | Command | In Sourcetree | Chapter |
|---|---|---|---|
| Throw away changes in the working directory | `git restore <file>` | Right-click the file → Discard | 9 |
| Take a file out of the staging area | `git restore --staged <file>` | Unstage Selected | 9 |
| Move the branch back in time | `git reset --soft/--mixed/--hard <commit>` | Right-click the commit → Reset current branch to this commit (macOS: Reset main to this commit) | 9 |
| Add an opposite commit | `git revert <commit>` | Right-click the commit → Reverse commit | 9 |
| See every step HEAD has taken | `git reflog` | Click Terminal and type the command | 9 |
| Put changes away for a while | `git stash`, `git stash pop` | Stash on the toolbar; right-click → Apply Stash | 9 |

## Ignoring files, submodules and repository size

| What you want to do | Command | In Sourcetree | Chapter |
|---|---|---|---|
| Stop tracking a file but keep it | `git rm --cached <file>` | Right-click the file → Stop Tracking | 10 |
| See why a file is ignored | `git check-ignore -v <file>` | — | 10 |
| Add a submodule | `git submodule add <URL> <folder>` | Repository → Add Submodule | 10 |
| Get the submodules | `git submodule update --init` | — | 10 |
| See how big the repository is | `git count-objects -vH` | — | 10 |

---

[← Appendix B: Team Jargon](jargon.md) | [Contents](../README.md) | [Appendix D: Further Reading →](further-reading.md)
