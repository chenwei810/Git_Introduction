<!-- source: zh-TW/appendix/further-reading.md | sha: c05cb50247fe -->

# Appendix D: Further Reading

This appendix collects the references cited in the chapters, plus books, official documentation and practice sites for going deeper. Use them alongside [Appendix A: Glossary](glossary.md).

---

## Introductions and overviews

| Resource | Description | Chapters |
|---|---|---|
| Scott Chacon and Ben Straub, *[Pro Git](https://git-scm.com/book/en/v2)*, 2nd edition | The most complete introduction to Git, free to read online and translated into many languages | Whole book |
| Git website: [About Git](https://git-scm.com/about) | Git's features and design ideas | 0 |
| Git documentation: [Reference](https://git-scm.com/docs) | The full description of every command; in a terminal, `git help <command>` opens it too | Whole book |

## Git internals

| Resource | Description | Chapters |
|---|---|---|
| *Pro Git*, Chapter 10, Git Internals | Objects, references, packfiles and transfer protocols; a continuation of the deep dives | 2–5, 9, 10 |
| *Pro Git*, section 7.7, Reset Demystified | Explains `reset` and `checkout` with the idea of three trees | 9 |
| Git documentation: [git-cat-file](https://git-scm.com/docs/git-cat-file), [git-reflog](https://git-scm.com/docs/git-reflog) | Opening objects and seeing where HEAD has been | 3, 9 |

## Collaboration and GitHub

| Resource | Description | Chapters |
|---|---|---|
| GitHub Docs: [About remote repositories](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories) | Connecting over HTTPS and SSH | 6 |
| GitHub Docs: [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) | Creating, reviewing and merging pull requests | 7 |
| GitHub Docs: [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) | The rules branch protection offers | 7 |
| GitHub Docs: [About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) | Publishing versions based on tags | 8 |
| GitHub Docs: [Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) | Cleaning history after a secret leaks | 10 |

## Branching strategies, versions and commit messages

| Resource | Description | Chapters |
|---|---|---|
| [Semantic Versioning 2.0.0](https://semver.org/) | The rules for major, minor and patch numbers | 8 |
| [Trunk Based Development](https://trunkbaseddevelopment.com/) | A full explanation of trunk-based development | 8 |
| Vincent Driessen, "[A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)" | The original Git Flow article; the author later added a note on when it fits | 8 |
| Chris Beams, "[How to Write a Git Commit Message](https://cbea.ms/git-commit/)" | The classic article on writing commit messages | 10 |
| [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) | A convention for organizing commit messages with prefixes such as `fix:` and `feat:` | 10 |

## Tools

| Resource | Description | Chapters |
|---|---|---|
| [Sourcetree website](https://www.sourcetreeapp.com/) | Download Sourcetree | 1 |
| [Git LFS](https://git-lfs.com/) | Managing large files with Git | 10 |
| [git filter-repo](https://github.com/newren/git-filter-repo) | A tool for rewriting history and removing leaked secrets | 10 |

## Practice

| Resource | Description | Chapters |
|---|---|---|
| [Learn Git Branching](https://learngitbranching.js.org/) | Practice branching, merging and rebasing with animations in the browser | 4, 5 |
| [GitHub Skills](https://skills.github.com/) | Interactive courses you complete step by step on GitHub | 6–8 |

---

[← Appendix C: Commands and Sourcetree](commands-and-sourcetree.md) | [Contents](../README.md) | [Back to the start: Chapter 0: The Big Picture →](../0-before-you-start/00-overview/README.md)
