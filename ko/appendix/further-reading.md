<!-- source: zh-TW/appendix/further-reading.md | sha: c05cb50247fe -->

# 부록 D 참고 자료

이 부록은 각 장에서 인용한 자료와, 더 깊이 알고 싶을 때 참고할 만한 책, 공식 문서, 연습 사이트를 모은 것입니다. 영어 자료가 많으니 [부록 A 용어집](glossary.md)과 함께 보세요.

---

## 입문과 종합

| 자료 | 설명 | 관련 장 |
|---|---|---|
| Scott Chacon, Ben Straub, 『[Pro Git](https://git-scm.com/book/ko/v2)』 2판 | 가장 충실한 Git 입문서. 온라인에서 무료로 읽을 수 있고, 한국어 번역도 있다 | 전체 |
| Git 공식 사이트: [About Git](https://git-scm.com/about) | Git의 특징과 설계 철학 | 0 |
| Git 공식 문서: [Reference](https://git-scm.com/docs) | 모든 명령어의 자세한 설명. 터미널에서 `git help <명령어>`로도 열 수 있다 | 전체 |

## Git의 내부

| 자료 | 설명 | 관련 장 |
|---|---|---|
| 『Pro Git』 10장 Git의 내부 | 객체, 참조, packfile, 전송 프로토콜. "더 알아보기"의 연장 | 2～5, 9, 10 |
| 『Pro Git』 7.7절 Reset 명확히 알고 가기 | 세 개의 트리라는 개념으로 `reset`과 `checkout`을 설명한다 | 9 |
| Git 공식 문서: [git-cat-file](https://git-scm.com/docs/git-cat-file), [git-reflog](https://git-scm.com/docs/git-reflog) | 객체 열기, HEAD가 지나온 길 보기 | 3, 9 |

## 협업과 GitHub

| 자료 | 설명 | 관련 장 |
|---|---|---|
| GitHub Docs: [원격 리포지토리 정보](https://docs.github.com/ko/get-started/getting-started-with-git/about-remote-repositories) | HTTPS와 SSH 두 가지 연결 방식 | 6 |
| GitHub Docs: [끌어오기 요청 정보](https://docs.github.com/ko/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) | 풀 리퀘스트 만들기, 리뷰, 병합 | 7 |
| GitHub Docs: [보호된 분기 정보](https://docs.github.com/ko/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) | 브랜치 보호의 여러 규칙 | 7 |
| GitHub Docs: [릴리스 정보](https://docs.github.com/ko/repositories/releasing-projects-on-github/about-releases) | 태그를 바탕으로 버전을 공개하기 | 8 |
| GitHub Docs: [리포지토리에서 중요한 데이터 제거](https://docs.github.com/ko/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) | 비밀 정보가 유출된 뒤 기록을 지우는 방법 | 10 |

## 브랜치 전략, 버전, 커밋 메시지

| 자료 | 설명 | 관련 장 |
|---|---|---|
| [유의적 버전 2.0.0](https://semver.org/lang/ko/) | 주 버전, 부 버전, 수 버전의 규칙. 한국어판이 있다 | 8 |
| [Trunk Based Development](https://trunkbaseddevelopment.com/) | 트렁크 기반 개발의 자세한 설명 | 8 |
| Vincent Driessen, "[A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)" | Git Flow를 제안한 원래 글. 작성자가 나중에 알맞은 경우에 대한 메모를 덧붙였다 | 8 |
| Chris Beams, "[How to Write a Git Commit Message](https://cbea.ms/git-commit/)" | 커밋 메시지 쓰는 법에 관한 대표적인 글 | 10 |
| [Conventional Commits](https://www.conventionalcommits.org/ko/v1.0.0/) | `fix:`, `feat:` 같은 접두어로 커밋 메시지를 정리하는 규약. 한국어판이 있다 | 10 |

## 도구

| 자료 | 설명 | 관련 장 |
|---|---|---|
| [Sourcetree 공식 사이트](https://www.sourcetreeapp.com/) | Sourcetree 내려받기 | 1 |
| [Git LFS](https://git-lfs.com/) | Git으로 큰 파일 관리하기 | 10 |
| [git filter-repo](https://github.com/newren/git-filter-repo) | 기록을 고쳐 쓰고 유출된 비밀 정보를 지우는 도구 | 10 |

## 연습

| 자료 | 설명 | 관련 장 |
|---|---|---|
| [Learn Git Branching](https://learngitbranching.js.org/?locale=ko) | 브라우저에서 애니메이션으로 브랜치, 병합, rebase를 연습한다. 한국어 화면이 있다 | 4, 5 |
| [GitHub Skills](https://skills.github.com/) | GitHub에서 한 단계씩 진행하는 대화형 강좌 | 6～8 |

---

[← 부록 C 명령어와 Sourcetree 대응표](commands-and-sourcetree.md) ｜ [목차](../README.md) ｜ [처음으로: 제0장 Git의 전체 그림 →](../0-before-you-start/00-overview/README.md)
