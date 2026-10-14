<!-- source: zh-TW/1-on-your-computer/02-three-areas/README.md | sha: 03509c355ea7 -->

# 제2장 세 가지 영역: 작업 디렉터리, 스테이징 영역, 저장소

> 📍 **프로젝트와 변경의 현재 위치**
>
> - 프로젝트: `fan-controller`는 아직 평범한 폴더다. 이 장에서 저장소로 만들고 첫 커밋을 한다
> - 이전 단계: 버그를 발견했고, Git과 Sourcetree도 설치했다
> - **이 장: 수정을 작성해 스테이징 영역에 넣는다**
> - 다음 단계: 커밋을 열어, 커밋하고 나면 무엇이 되는지 본다

---

## 왜 세 가지 영역으로 나뉠까

Git으로 관리하는 파일은 세 곳에 머뭅니다. 택배를 보내는 상황에 비유하면 가장 이해하기 쉽습니다.

- **작업 디렉터리**(Working Directory)는 책상입니다. 파일이 그 위에 있고, 언제든 고칠 수 있습니다.
- **스테이징 영역**(Staging Area)은 보낼 준비를 하는 상자입니다. 책상 위에서 이번에 보낼 것을 골라 상자에 넣습니다.
- **저장소**(Repository)는 발송 기록입니다. 상자를 봉해서 보내면 안에 든 것이 영구히 기록됩니다. 이 동작을 **커밋**(Commit)이라고 합니다.

```mermaid
flowchart LR
    W["작업 디렉터리"] -- "git add" --> S["스테이징 영역"]
    S -- "git commit" --> R["저장소"]
```

왜 굳이 상자가 하나 더 있을까요? 여러 가지를 동시에 고치는 일이 많기 때문입니다. 예를 들어 온도 환산을 고치면서 `main.c`에 디버그용 출력도 몇 줄 넣었다고 합시다. 기록하고 싶은 것은 수정뿐이고, 디버그 코드는 필요 없습니다. 스테이징 영역이 있으면 이번에 기록할 변경을 고르고, 나머지는 책상 위에 남겨 둘 수 있습니다.

> [!NOTE]
> **📖 용어｜저장소（儲存庫）**
>
> - **정의**: Git이 프로젝트의 모든 버전을 기록하는 곳이다. 프로젝트 폴더 안의 숨김 폴더 `.git`이 바로 그것이다.
> - **현장에서는**: 보통 "레포"나 "repo"라고 부른다. 예를 들어 "이 레포는 펌웨어용이고, 하드웨어 도면은 다른 레포에 있어요".
> - **관련 용어**: 작업 디렉터리, 스테이징 영역, 원격 저장소
> - **흔한 혼동**: 프로젝트 폴더가 곧 저장소는 아니다. `.git`을 지워도 폴더의 파일은 남지만, 기록은 모두 사라진다.

---

## 저장소 만들기: git init

프로젝트 폴더에서 `git init`을 실행하면 Git이 `.git` 폴더를 만들고 프로젝트 관리를 시작합니다.

```bash
cd ~/git-practice/fan-controller
git init
```

**Sourcetree에서는**: **새 탭의 Create → fan-controller 폴더 선택 → Create**(macOS용은 **New → Create Local Repository**). 폴더가 이미 있다는 경고가 나오면 계속을 고르면 됩니다.

> [!TIP]
> **🔧 노하우｜git init 전에 지금 있는 폴더를 확인한다**
>
> - **상황**: 터미널을 열자마자 `git init`을 입력한다.
> - **방법**: 먼저 `pwd`로 지금 위치를 확인하고, 프로젝트 폴더가 맞을 때 실행한다.
> - **이유**: 터미널은 보통 홈 폴더에서 시작한다. 거기서 `git init`을 실행하면 홈 폴더 전체가 하나의 프로젝트가 된다.
> - **안 하면 어떻게 되나**: `git status`에 파일 수천 개가 줄줄이 나오고, 어느 하위 폴더에서 작업하든 그 저장소를 잘못 쓰게 된다. 되돌리려면 홈 폴더의 `.git`을 지워야 한다.
> - **관련 장**: [제1장 도구 준비](../../0-before-you-start/01-setup/README.md)

<details>
<summary><strong>🔍 더 알아보기｜.git 폴더 안에는 무엇이 있을까</strong></summary>

Git의 모든 것은 `.git` 안에 있습니다. 특히 중요한 항목을 소개합니다. 뒤의 장에서 다시 만납니다.

```text
HEAD       지금 어느 브랜치에 있는지(제4장)
config     이 저장소만의 설정(제1장)
index      스테이징 영역(이 장)
objects/   모든 버전의 내용(제3장)
refs/      브랜치와 태그(제4, 8장)
```

모두 평범한 파일입니다. `HEAD`를 열면 `ref: refs/heads/main` 한 줄만 있는데, "지금 main 브랜치에 있다"는 뜻입니다.

</details>

---

## 상태 보기: git status

`git status`는 각 파일이 지금 어느 영역에 있는지 알려 줍니다. 가장 자주 쓰는 명령어이고, 무슨 일이 일어나고 있는지 모를 때는 일단 이것부터 입력하면 됩니다.

`git init`을 막 실행했을 때는 Git이 아직 어떤 파일도 추적하지 않으므로, 모든 파일이 "추적하지 않음"(Untracked files) 아래에 나옵니다.

| `git status`의 제목 | 뜻 |
|---|---|
| Untracked files | Git이 한 번도 기록한 적 없는 새 파일 |
| Changes not staged for commit | 고쳤지만 아직 책상 위에 있다 |
| Changes to be committed | 이미 상자에 들어 있고, 다음 커밋 때 기록된다 |

**Sourcetree에서는**: 왼쪽의 **File Status**. 아래쪽의 Unstaged files가 책상, 위쪽의 Staged files가 상자입니다.

![Sourcetree File Status 화면의 개략도](../../../images/02-file-status.svg)

*그림: ① Staged files. 상자에 해당한다 ② Unstaged files. 책상에 해당한다 ③ Stage All. 책상 위의 변경을 모두 상자에 넣는다 ④ 메시지 입력란 ⑤ Commit 버튼. 오른쪽에는 선택한 파일의 차이가 나온다.*

---

## 스테이징하고 커밋하기: git add, git commit

**파일 고르기 → git add → git commit**

1. **git add**: 파일을 스테이징 영역에 넣습니다. `git add .`는 현재 폴더의 모든 파일을 뜻합니다.
2. **git commit**: 스테이징 영역의 내용을 하나의 버전으로 기록합니다. `-m` 뒤에는 이 버전의 설명을 씁니다.

```bash
git add .
git commit -m "Initial commit"
```

**Sourcetree에서는**: **Stage All → 아래쪽에 메시지 입력 → Commit**.

프로젝트의 첫 커밋이 탄생했습니다. 지금 기록에는 점이 하나뿐입니다.

```mermaid
gitGraph
    commit id: "프로젝트 생성"
```

> [!NOTE]
> **📖 용어｜스테이징 영역（暫存區）**
>
> - **정의**: 다음 커밋에 들어갈 내용이다. 커밋할 때 Git은 스테이징 영역에 있는 것만 기록한다.
> - **현장에서는**: 동사로는 "스테이징하다", "add하다"라고 한다. 예를 들어 "그 파일은 아직 스테이징 안 해서 커밋에 안 들어갔어요".
> - **관련 용어**: 작업 디렉터리, `git add`, 인덱스
> - **흔한 혼동**: 스테이징 영역은 인덱스(index)라고도 하며, 둘은 같은 것이다. 제9장의 `git stash`(변경을 잠시 치워 두기)와는 전혀 다르다.

---

## 버그 고치기: git diff

이제 온도 환산을 고칩니다. `sensor.c`를 열면 주석에는 센서가 0 °C에서 500 mV를 출력한다고 적혀 있는데, 코드는 `(mv - 600)`으로 되어 있습니다. 600을 500으로 바꿔 저장하면 `sensor.c`는 "고쳤지만 아직 책상 위에 있는" 상태가 됩니다. 상자에 넣기 전에 `git diff`로 무엇을 고쳤는지 확인합니다.

```bash
git diff             # 책상 위와 상자 안의 차이를 본다
git add sensor.c
git diff --staged    # 상자 안과 마지막 커밋의 차이를 본다
```

**Sourcetree에서는**: File Status에서 파일을 클릭하면 오른쪽에 차이가 나옵니다. 빨간색은 지운 줄, 초록색은 추가한 줄입니다.

스테이징 영역이 기록하는 것은 `git add`를 한 그 순간의 내용입니다. add한 뒤에 같은 파일을 또 고치면 `git status`는 두 제목 아래에 모두 그 파일을 보여 줍니다. 새 변경을 상자에 넣으려면 다시 add해야 합니다.

> [!TIP]
> **🔧 노하우｜커밋하기 전에 git diff --staged를 본다**
>
> - **상황**: 파일 여러 개를 고쳤고, 이제 커밋하려고 한다.
> - **방법**: 먼저 `git diff --staged`를 실행해 상자 안의 것이 모두 기록하고 싶은 것인지 한 줄씩 확인한다.
> - **이유**: `git add .`는 폴더에서 고친 파일을 모두 상자에 넣는다. 디버그용 출력이나 잠시 바꿔 둔 설정값까지 포함해서.
> - **안 하면 어떻게 되나**: 디버그 코드가 정식 버전에 기록되고, 그대로 제품에 올라가기까지 한다. 나중에 그것을 들여온 커밋을 찾느라 시간이 더 든다.
> - **관련 장**: [제10장 좋은 습관](../../3-when-things-go-wrong/10-good-habits/README.md)

<details>
<summary><strong>🔍 더 알아보기｜스테이징 영역의 정체는 파일 하나</strong></summary>

스테이징 영역의 정체는 `.git/index`라는 바이너리 파일입니다. 각 파일의 경로, 권한, 내용의 해시 값을 기록합니다. 다음 명령어로 그 내용을 볼 수 있습니다.

```text
$ git ls-files --stage
100644 6305a5e833282a7ac1c6fa02a0c455706b169145 0	Makefile
100644 c50b3ace27f06cf09657fbd19635ee6d06f268ed 0	README.md
```

가운데의 40글자가 파일 내용의 해시 값입니다. `git add`가 실제로 하는 일은 파일 내용을 `.git/objects/`에 저장하고, 그 해시 값을 index에 적는 것입니다. 그래서 add하는 순간 내용은 이미 Git에 저장됩니다. add한 뒤에 파일을 고쳐도 상자 안의 것이 바뀌지 않는 이유가 이것입니다. 제3장에서 이 객체들을 열어 봅니다.

</details>

---

## 자주 겪는 문제

| 상황 | 원인 | 해결 |
|---|---|---|
| `fatal: not a git repository` | 지금 있는 폴더가 저장소가 아니다 | `cd`로 프로젝트 폴더에 들어간다 |
| `Author identity unknown` | 이름과 이메일을 설정하지 않았다 | 제1장대로 `user.name`과 `user.email`을 설정한다 |
| `LF will be replaced by CRLF` | Windows와 다른 시스템의 줄 바꿈 문자가 다르다 | 알림일 뿐이니 무시해도 된다. 제1장 참고 |

---

## 🧪 따라 해 보기

**시작하기 전에**: 이 책의 루트 폴더에서 `bash practice/setup.sh 2`를 실행해 연습 프로젝트를 `~/git-practice/fan-controller`로 복사합니다. 이때는 아직 저장소가 아닙니다.

1. 저장소를 만들고 첫 커밋을 합니다.

   ```bash
   cd ~/git-practice/fan-controller
   git init
   git status          # 모든 파일이 Untracked files 아래에 있다
   git add .
   git commit -m "Initial commit"
   ```

   Sourcetree에서는: 새 탭의 Create로 이 폴더를 고른 뒤 **Stage All → 메시지 입력 → Commit**.

2. 편집기로 `sensor.c`를 열고 `(mv - 600)`을 `(mv - 500)`으로 바꿔 저장합니다.
3. 차이를 본 다음 수정을 스테이징 영역에 넣습니다. 단, **아직 커밋하지 마세요**.

   ```bash
   git diff
   git add sensor.c
   git status
   ```

**이렇게 보이면 성공**: 마지막 `git status`의 첫 줄이 `On branch main`이고, Changes to be committed 아래에 `modified: sensor.c`가 나옵니다. 첫 줄이 `On branch master`라면 제1장대로 기본 브랜치를 설정하고 `.git` 폴더를 지운 뒤 다시 하세요. 이 수정은 제4장에서 새 브랜치에 커밋합니다.

---

## 📋 이 장의 명령어

| 하고 싶은 일 | 명령어 | Sourcetree에서는 |
|---|---|---|
| 폴더를 저장소로 만들기 | `git init` | Create(macOS: New → Create Local Repository) |
| 현재 상태 보기 | `git status` | 왼쪽의 File Status |
| 파일을 스테이징 영역에 넣기 | `git add <파일>`, `git add .` | 파일 선택 → Stage Selected, 또는 Stage All |
| 커밋하기 | `git commit -m "메시지"` | 메시지 입력 → Commit |
| 아직 스테이징하지 않은 변경 보기 | `git diff` | Unstaged files의 파일 클릭 |
| 스테이징한 변경 보기 | `git diff --staged` | Staged files의 파일 클릭 |

---

## 이 장의 핵심

1. 파일은 세 곳에 머문다. 작업 디렉터리(책상), 스테이징 영역(상자), 저장소(발송 기록).
2. `git add`는 변경을 스테이징 영역에 넣고, `git commit`은 스테이징 영역을 하나의 버전으로 기록한다.
3. 스테이징 영역 덕분에 이번에 기록할 변경을 고를 수 있다. 커밋 하나에는 관련 있는 것만 넣는다.
4. 상황을 모르겠으면 먼저 `git status`, 커밋하기 전에는 `git diff --staged`를 본다.

---

## 참고 자료

- Scott Chacon, Ben Straub, 『[Pro Git](https://git-scm.com/book/ko/v2)』 2판, 2장(Git의 기초. 온라인에서 무료로 읽을 수 있습니다)
- Git 공식 문서: [git-status](https://git-scm.com/docs/git-status), [git-add](https://git-scm.com/docs/git-add), [git-commit](https://git-scm.com/docs/git-commit)

---

[← 제1장 도구 준비](../../0-before-you-start/01-setup/README.md) ｜ [목차](../../README.md) ｜ [제3장 커밋의 정체 →](../03-commits/README.md)
