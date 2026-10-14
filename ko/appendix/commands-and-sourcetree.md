<!-- source: zh-TW/appendix/commands-and-sourcetree.md | sha: 438d3b61b039 -->

# 부록 C 명령어와 Sourcetree 대응표

이 부록은 각 장 끝에 있는 "📋 이 장의 명령어"를 작업별로 다시 모은 것입니다. 무언가를 하고 싶은데 방법이 생각나지 않으면 여기서 찾고, "장" 열에 있는 장에서 자세한 설명을 읽으세요.

Sourcetree의 버튼과 메뉴 이름은 영어 화면을 기준으로 합니다. Windows용과 macOS용은 화면이 조금 다르고, 차이가 큰 곳은 괄호 안에 macOS용 위치를 적었습니다. 표의 "—"는 Sourcetree에 해당하는 버튼이 없다는 뜻입니다. 도구 모음의 **Terminal**을 눌러 터미널을 열고 명령어를 입력하세요.

---

## 설정

| 하고 싶은 일 | 명령어 | Sourcetree에서는 | 장 |
|---|---|---|---|
| Git 버전 확인하기 | `git --version` | — | 1 |
| 이름과 이메일 설정하기 | `git config --global user.name`, `user.email` | Tools → Options → General(macOS: Settings → General) | 1 |
| 새 저장소의 브랜치 이름을 main으로 | `git config --global init.defaultBranch main` | — | 1 |
| 줄 바꿈 설정하기(macOS, Linux) | `git config --global core.autocrlf input` | — | 1 |
| global 설정 나열하기 | `git config --global --list` | — | 1 |
| GitHub 계정 연결하기 | — | Tools → Options → Authentication(macOS: Settings → Accounts) | 1 |

## 저장소 만들기와 가져오기

| 하고 싶은 일 | 명령어 | Sourcetree에서는 | 장 |
|---|---|---|---|
| 폴더를 저장소로 만들기 | `git init` | Create(macOS: New → Create Local Repository) | 2 |
| 원격 저장소를 통째로 복사하기 | `git clone <주소>` | 새 탭의 Clone | 6 |

## 변경 기록하기

| 하고 싶은 일 | 명령어 | Sourcetree에서는 | 장 |
|---|---|---|---|
| 현재 상태 보기 | `git status` | 왼쪽의 File Status | 2 |
| 파일을 스테이징 영역에 넣기 | `git add <파일>`, `git add .` | 파일 선택 → Stage Selected, 또는 Stage All | 2 |
| 아직 스테이징하지 않은 변경 보기 | `git diff` | Unstaged files의 파일 클릭 | 2 |
| 스테이징한 변경 보기 | `git diff --staged` | Staged files의 파일 클릭 | 2 |
| 커밋하기 | `git commit -m "메시지"` | 메시지 입력 → Commit | 2 |
| 바뀐 파일을 모두 커밋하기 | `git commit -am "메시지"` | Stage All → Commit | 4 |
| 본문이 있는 커밋 메시지 쓰기 | `git commit -m "제목" -m "본문"` | 메시지 입력란 첫 줄에 제목, 한 줄 비우고 본문 | 10 |

## 기록 보기

| 하고 싶은 일 | 명령어 | Sourcetree에서는 | 장 |
|---|---|---|---|
| 기록 보기 | `git log` | 왼쪽의 History | 3 |
| 커밋 하나를 한 줄로 | `git log --oneline` | History는 기본으로 이렇게 보인다 | 3 |
| 모든 브랜치의 기록 그리기 | `git log --oneline --graph --all` | History에서 All Branches 선택 | 4 |
| 커밋이 무엇을 바꿨는지 보기 | `git show <번호>` | History에서 그 커밋 클릭 | 3 |
| 바뀐 파일만 보기 | `git show --stat <번호>` | History에서 커밋을 클릭하고 아래 파일 목록 보기 | 3 |
| 각 줄을 누가 바꿨는지 찾기 | `git blame <파일>` | 파일 오른쪽 클릭 → Blame Selected | 10 |
| 객체 열기 | `git cat-file -p <번호>` | — | 3 |
| 가장 가까운 태그 찾기 | `git describe` | — | 8 |

## 브랜치

| 하고 싶은 일 | 명령어 | Sourcetree에서는 | 장 |
|---|---|---|---|
| 브랜치 나열하기 | `git branch` | 왼쪽의 Branches | 4 |
| 새 브랜치를 만들고 전환하기 | `git switch -c <이름>` | 도구 모음의 Branch | 4 |
| 브랜치 전환하기 | `git switch <이름>` | 왼쪽의 브랜치 이름 더블클릭 | 4 |
| 태그에서 브랜치 만들기 | `git switch -c <브랜치> <태그>` | History에서 그 커밋 오른쪽 클릭 → Branch | 8 |
| 병합이 끝난 브랜치 지우기 | `git branch -d <브랜치>` | 브랜치 오른쪽 클릭 → Delete | 5 |

## 병합

| 하고 싶은 일 | 명령어 | Sourcetree에서는 | 장 |
|---|---|---|---|
| 어떤 브랜치를 현재 브랜치에 병합하기 | `git merge <브랜치>` | 브랜치 오른쪽 클릭 → Merge … into current branch | 5 |
| 반드시 병합 커밋 만들기 | `git merge --no-ff <브랜치>` | Merge할 때 Create a new commit even if fast-forward is possible 체크 | 8 |
| 충돌을 해결됨으로 표시하기 | `git add <파일>` | 파일 오른쪽 클릭 → Resolve Conflicts → Mark Resolved | 5 |
| 기본 메시지로 병합 마치기 | `git commit --no-edit` | Commit | 5 |
| 이번 병합 그만두기 | `git merge --abort` | — | 5 |
| 브랜치를 main 끝에 다시 붙이기 | `git rebase main` | main 오른쪽 클릭 → Rebase current changes onto main | 5 |

## 원격

| 하고 싶은 일 | 명령어 | Sourcetree에서는 | 장 |
|---|---|---|---|
| 원격 추가하기 | `git remote add origin <주소>` | Settings → Remotes → Add | 6 |
| 원격 확인하기 | `git remote -v` | Settings → Remotes | 6 |
| 브랜치를 처음 푸시하기 | `git push -u origin <브랜치>` | Push에서 브랜치와 Track 체크 | 6 |
| 푸시하기 | `git push` | Push | 6 |
| 파일은 건드리지 않고 내려받기만 하기 | `git fetch` | Fetch | 6 |
| 내려받고 병합하기 | `git pull` | Pull | 6 |
| 원격에는 있고 나에게는 없는 커밋 나열하기 | `git log main..origin/main` | — | 6 |
| 지워진 원격 브랜치 정리하기 | `git fetch --prune` | Fetch에서 Prune 체크 | 7 |

## 풀 리퀘스트

| 하고 싶은 일 | 명령어 | Sourcetree에서는 | 장 |
|---|---|---|---|
| 풀 리퀘스트 만들기 | —(GitHub 웹 페이지에서) | 브랜치 오른쪽 클릭 → Create Pull Request | 7 |
| 리뷰를 반영해 PR 갱신하기 | `git commit`, `git push` | Commit → Push | 7 |
| 병합 후 main 갱신하기 | `git switch main`, `git pull` | main 더블클릭 → Pull | 7 |
| 다른 사람의 PR을 가져와 테스트하기 | `git fetch origin pull/<번호>/head:<이름>` | — | 7 |

## 태그와 릴리스

| 하고 싶은 일 | 명령어 | Sourcetree에서는 | 장 |
|---|---|---|---|
| 주석 태그 붙이기 | `git tag -a <이름> -m "메시지"` | 도구 모음의 Tag | 8 |
| 태그 나열하기 | `git tag` | 왼쪽의 Tags | 8 |
| 태그 푸시하기 | `git push origin <이름>` | 태그를 붙일 때 Push tag 체크 | 8 |

## 되돌리기

| 하고 싶은 일 | 명령어 | Sourcetree에서는 | 장 |
|---|---|---|---|
| 작업 디렉터리의 변경 버리기 | `git restore <파일>` | 파일 오른쪽 클릭 → Discard | 9 |
| 파일을 스테이징 영역에서 빼기 | `git restore --staged <파일>` | Unstage Selected | 9 |
| 브랜치를 과거로 되돌리기 | `git reset --soft/--mixed/--hard <커밋>` | 커밋 오른쪽 클릭 → Reset current branch to this commit(macOS: Reset main to this commit) | 9 |
| 반대 방향 커밋 만들기 | `git revert <커밋>` | 커밋 오른쪽 클릭 → Reverse commit | 9 |
| HEAD가 지나온 길 보기 | `git reflog` | Terminal을 눌러 명령어 입력 | 9 |
| 변경을 잠시 치워 두기 | `git stash`, `git stash pop` | 도구 모음의 Stash, 오른쪽 클릭 → Apply Stash | 9 |

## 파일 무시, 서브모듈, 저장소 크기

| 하고 싶은 일 | 명령어 | Sourcetree에서는 | 장 |
|---|---|---|---|
| 추적은 멈추되 파일은 남기기 | `git rm --cached <파일>` | 파일 오른쪽 클릭 → Stop Tracking | 10 |
| 파일이 왜 무시되는지 보기 | `git check-ignore -v <파일>` | — | 10 |
| 서브모듈 추가하기 | `git submodule add <주소> <폴더>` | Repository → Add Submodule | 10 |
| 서브모듈 가져오기 | `git submodule update --init` | — | 10 |
| 저장소 크기 보기 | `git count-objects -vH` | — | 10 |

---

[← 부록 B 현장 용어](jargon.md) ｜ [목차](../README.md) ｜ [부록 D 참고 자료 →](further-reading.md)
