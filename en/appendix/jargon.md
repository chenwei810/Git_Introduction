<!-- source: zh-TW/appendix/jargon.md | sha: b2877c32df07 -->

# Appendix B: Team Jargon

Everyday talk on a software team is full of shorthand, as in "Rebase before you open the PR." The first time newcomers hear it, they are often lost.

This appendix collects phrases you will often hear on a team, with example sentences. Habits differ from team to team; these are the common ones. For formal definitions, see [Appendix A: Glossary](glossary.md).

---

## Everyday commits

| Phrase | Meaning | Example |
|---|---|---|
| Commit it | Record the current changes as a version | "Commit whenever you reach a stopping point, not once at the end of the day." |
| Stage | Put changes in the staging area, that is, `git add` | "Only stage the file with the fix; leave the debug prints out." |
| Dirty working tree | There are uncommitted changes | "Your working tree is dirty. Commit or stash before you switch branches." |
| Clean | No uncommitted changes at all | "`git status` says it's clean, so you can switch." |
| SHA, hash | A commit's ID, usually only the first 7 characters | "Include the SHA when you report a bug; the first seven characters are enough." |
| Write a proper message | A commit message should say what changed and why | "`fix` isn't enough. Write a proper message." |

## Branches and merging

| Phrase | Meaning | Example |
|---|---|---|
| Cut a branch, branch off | Create a new branch from the current commit | "Cut a branch for this feature; don't change main directly." |
| Switch over | Switch to another branch | "Switch back to main and pull the latest before you branch." |
| Merge it back | Merge a branch back into `main` | "Merge it back into main once it's tested." |
| Merge main in | Merge new commits from `main` into your branch to stay in sync | "Your branch is way behind. Merge main in first." |
| Rebase onto main | Replay your commits on top of the latest `main` | "Rebase onto main before you open the PR; the history will be cleaner." |
| Resolve conflicts | Deal with conflicts during a merge | "These two PRs touch the same file, so whoever merges second has to resolve conflicts." |
| It'll fast-forward | The merge only moves the branch forward | "Nothing new on main, so it'll just fast-forward." |
| Long-lived branch | A branch kept open for a long time without merging | "Long-lived branches are always painful to merge. Try to merge within a day or two." |

## Remotes

| Phrase | Meaning | Example |
|---|---|---|
| Push it up | `git push` | "Push it up when it's ready and I'll take a look." |
| Pull it down | `git pull` | "Pull first thing in the morning, then start coding." |
| Do a fetch | Download only, without merging, to see what's new on the remote | "Do a fetch and see whether anyone has touched origin." |
| Behind, ahead | Your branch has fewer or more commits than the remote | "Your main is three commits behind origin." |
| Force push | Overwrite the remote history with `git push --force` | "Never force push a branch that has already been shared." |
| Spin up a repo | Create a new repository on GitHub | "Spin up a separate repo for this tool." |

## Pull requests and review

| Phrase | Meaning | Example |
|---|---|---|
| Open a PR, put up a PR | Create a pull request | "Put up a PR when it's fixed and assign me as reviewer." |
| Review | Check someone else's changes | "Who has time to review this PR?" |
| Approve | The review passes | "It needs two approvals before it can be merged." |
| LGTM | Looks Good To Me | "LGTM, go ahead and merge." |
| Nit | A minor suggestion; fine to leave as is | "Nit: this variable name could be clearer." |
| Changes requested | The reviewer wants changes before merging | "My PR got changes requested. I'll push again once it's fixed." |
| CI is red, CI failed | The automated checks did not pass | "CI is red. Let's see which test failed first." |
| Squash | Combine several commits into one | "Squash the small commits into one before merging." |
| Draft PR | An unfinished PR, opened early to show the direction | "Open a draft PR so we can discuss the approach." |
| Merge the PR | Click the merge button | "CI passed and it's approved, so I'll merge the PR." |

## Releases

| Phrase | Meaning | Example |
|---|---|---|
| Tag it | Put a version tag on a commit | "Has v1.0.0 been tagged?" |
| Ship, cut a release | Officially release a version | "We ship on Friday; from Thursday on, fixes only." |
| Hotfix | An urgent fix for a released version | "The shipped version has a problem. Branch a hotfix off v1.0.0." |
| Code freeze | No new features before a release | "Code freeze next week; new features go into the next version." |
| Bump the version | Change the version number following semantic versioning | "We changed the settings format and it's not compatible, so bump the major version." |

## When things go wrong

| Phrase | Meaning | Example |
|---|---|---|
| Revert it | Undo a commit with `git revert` | "It's already pushed. Revert it; don't reset." |
| Reset back | Move a branch back with `git reset` | "If you haven't pushed, just reset back to the previous commit." |
| Stash it | Put uncommitted changes away for a while | "Stash your half-done work and switch over to fix the bug." |
| Check the reflog | Find "lost" commits with `git reflog` | "Commit disappeared? Don't panic, check the reflog." |
| Blame it | Find which commit changed a line with `git blame` | "Blame that line and see why it was changed." |
| Secrets got committed | A secret was committed to the history | "A password got committed. Change it first, then deal with the history." |

"Blame" literally means to hold someone responsible, but on a team it is only used to find where a change came from and why. Good teams use it to understand context, not to find someone to blame.

---

[← Appendix A: Glossary](glossary.md) | [Contents](../README.md) | [Appendix C: Commands and Sourcetree →](commands-and-sourcetree.md)
