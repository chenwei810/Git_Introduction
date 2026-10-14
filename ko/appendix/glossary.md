<!-- source: zh-TW/appendix/glossary.md | sha: 22760eca648a -->

# 부록 A 용어집

이 책에 나오는 주요 용어를 영어 알파벳 순서로 모았습니다. "장" 열은 그 용어가 주로 나오거나 설명되는 장의 번호입니다.

"繁體中文" 열은 번체 중국어 원문에서 쓰는 표현으로, 대만 동료와 일할 때 도움이 됩니다. commit, tag, rebase처럼 팀에서 영어 그대로 말하는 경우가 많은 용어는 원문에서도 영어로 쓰며, 이 열에는 중국어 번역어도 함께 실었습니다.

이 용어집은 책 전체 용어의 **기준**이기도 합니다. 집필하거나 번역할 때는 이 표의 용어를 따라 주세요. 언어를 추가할 때는 그 언어의 열을 더합니다. 자세한 내용은 [TRANSLATIONS.md](../../TRANSLATIONS.md)를 참고하세요.

팀에서 이 말들을 실제로 어떻게 쓰는지는 [부록 B 현장 용어](jargon.md)를 참고하세요.

| 영어 | 약어 | 한국어 | 繁體中文 | 설명 | 장 |
|---|---|---|---|---|---|
| Annotated Tag | — | 주석 태그 | 附註 tag | 작성자, 날짜, 설명이 있는 태그로, 그 자체가 하나의 객체다. 릴리스에는 이것을 쓴다 | 8 |
| Blame | — | blame | blame | 파일의 각 줄을 마지막으로 바꾼 커밋과 사람을 보여 준다 | 10 |
| Blob | — | blob | blob | 파일 하나의 내용을 저장하는 객체. 파일 이름은 없다 | 3 |
| Branch | — | 브랜치 | 分支 | 커밋에 붙어 있고, 새 커밋과 함께 앞으로 나아가는 이름 | 4 |
| Branch Protection | — | 브랜치 보호 | 分支保護 | 바로 푸시 금지, 리뷰와 자동 검사 통과 필수 같은 서비스 쪽 규칙 | 7 |
| Centralized Version Control | — | 중앙 집중형 버전 관리 | 集中式版本控制 | 전체 기록이 서버 한 대에만 있는 버전 관리 방식 | 0 |
| Clone | — | clone(클론) | clone（複製儲存庫） | 원격 저장소를 전체 기록과 함께 내 컴퓨터로 복사하는 것 | 6 |
| Code Review | — | 코드 리뷰 | 程式碼審查 | 병합하기 전에 다른 사람이 변경 내용을 확인하는 것 | 7 |
| Commit | — | 커밋 | 提交；書中多直接說 commit | 완전한 스냅숏에 작성자, 시각, 메시지, 바로 앞 커밋의 번호를 더한 것 | 2, 3 |
| Commit Message | — | 커밋 메시지 | commit 訊息 | 이 변경이 무엇을 하고 왜 하는지 설명하는 글. 첫 줄이 제목이다 | 2, 10 |
| Conflict Marker | — | 충돌 표시 | 衝突標記 | 파일 안에서 충돌 범위를 나타내는 `<<<<<<<`, `=======`, `>>>>>>>` 세 줄 | 5 |
| Continuous Integration | CI | 지속적 통합 | 持續整合 | 푸시할 때마다 자동으로 빌드하고 테스트해, 결과를 풀 리퀘스트에 보여 준다 | 7 |
| CRLF, LF | — | 줄 바꿈 문자 | 換行字元 | Windows는 CRLF, macOS와 Linux는 LF로 줄 바꿈을 나타낸다 | 1 |
| Detached HEAD | — | detached HEAD | detached HEAD | HEAD가 브랜치가 아니라 커밋을 바로 가리키는 상태 | 4, 8 |
| Directed Acyclic Graph | DAG | 방향성 비순환 그래프 | 有向無環圖 | 커밋 기록의 자료 구조. 각 커밋이 바로 앞을 가리키고, 자기 자신으로 돌아오지 않는다 | 5 |
| Distributed Version Control | — | 분산 버전 관리 | 分散式版本控制 | 각자의 컴퓨터에 전체 기록이 있는 버전 관리 방식. Git이 여기에 속한다 | 0 |
| Fast-forward | — | 빨리 감기 | 快轉 | 병합 대상에 새 커밋이 없을 때, 브랜치를 앞으로 옮기기만 하고 새 커밋을 만들지 않는 병합 | 5 |
| Feature Branch | — | 기능 브랜치 | 功能分支 | 기능이나 수정 하나를 위해 만들고, 끝나면 `main`에 병합하는 브랜치 | 8 |
| Fetch | — | fetch | fetch | 원격의 새 커밋을 내려받아 원격 추적 브랜치를 갱신하지만, 내 파일은 건드리지 않는다 | 6 |
| Garbage Collection | gc | 가비지 컬렉션 | 垃圾回收 | 어떤 브랜치, 태그, reflog도 가리키지 않는 객체를 치우는 것 | 9 |
| Git Flow | — | Git Flow | Git Flow | `main`, `develop`, 기능, release, hotfix 등 여러 브랜치를 쓰는 브랜치 전략 | 8 |
| Git LFS (Large File Storage) | LFS | Git LFS | Git LFS | 큰 파일을 다른 서버에 저장하고, 저장소에는 작은 포인터 파일만 둔다 | 10 |
| .gitignore | — | .gitignore | .gitignore | Git이 추적하지 않을 파일과 폴더를 적어 둔 파일 | 10 |
| Hash | — | 해시 값 | 雜湊值 | 내용으로 계산한 길이가 정해진 번호. 내용이 한 글자만 달라도 완전히 달라진다 | 3 |
| Hash Function | — | 해시 함수 | 雜湊函式 | 길이에 상관없는 데이터를 해시 값으로 바꾸는 함수 | 3 |
| HEAD | — | HEAD | HEAD | "지금 있는 곳"을 나타내는 포인터. 보통 현재 브랜치를 가리킨다 | 4 |
| Hotfix | — | hotfix(긴급 수정) | hotfix（緊急修正） | 릴리스한 버전에 문제가 생겼을 때, 그 버전에서 브랜치를 만들어 하는 긴급 수정 | 8 |
| Lightweight Tag | — | 가벼운 태그 | 輕量 tag | 커밋을 가리키는 이름일 뿐, 작성자와 설명이 없다 | 8 |
| Loose Object | — | 느슨한 객체 | 鬆散物件 | 따로 압축해 저장한 객체. 나중에 packfile로 묶인다 | 10 |
| Merge | — | 병합 | 合併 | 다른 브랜치의 변경을 현재 브랜치로 가져오는 것 | 5 |
| Merge Base | — | 병합 기준 | 合併基準 | 두 브랜치의 가장 가까운 공통 조상 커밋. 3-way 병합은 이것을 기준으로 비교한다 | 5 |
| Merge Commit | — | 병합 커밋 | 合併 commit | 바로 앞 커밋이 둘이고, 병합을 기록하는 커밋 | 5, 7 |
| Merge Conflict | — | 충돌 | 衝突 | 두 브랜치가 같은 곳을 고쳐서, 어느 쪽을 쓸지 Git이 정할 수 없는 상태 | 5 |
| Object | — | 객체 | 物件 | Git이 데이터를 저장하는 기본 단위. blob, tree, commit, 주석 태그가 있다 | 3 |
| origin | — | origin | origin | clone하거나 원격을 추가할 때 기본으로 쓰는 원격 이름 | 6 |
| Packfile | — | packfile | packfile | 많은 객체를 함께 압축하고, 비슷한 내용은 차이만 저장하는 파일 | 10 |
| Parent Commit | — | 부모 커밋(바로 앞 커밋) | 父 commit（上一個 commit） | 커밋이 기록하는 "앞 버전". 병합 커밋에는 둘이 있다 | 3, 5 |
| Personal Access Token | PAT | 개인 액세스 토큰 | 個人存取權杖 | 비밀번호 대신 GitHub에 신원을 증명하는 데 쓰는 문자열 | 6 |
| Pull | — | pull | pull | fetch한 뒤, 원격의 새 커밋을 현재 브랜치에 병합한다 | 6 |
| Pull Request | PR | 풀 리퀘스트 | Pull Request | 한 브랜치를 다른 브랜치에 병합해 달라는 요청. 병합 전에 논의하고 리뷰한다 | 7 |
| Push | — | push(푸시) | push（推送） | 로컬 커밋을 원격에 올린다 | 6 |
| Push Protection | — | 푸시 보호 | 推送保護 | 비밀번호나 키를 발견하면 그 푸시를 막는 서비스 쪽 기능 | 10 |
| Rebase | — | rebase(리베이스) | rebase（重新定基） | 커밋 여러 개를 새 시작점 위에서 다시 만든다. 커밋 번호가 바뀐다 | 5 |
| Rebase and Merge | — | Rebase and merge | Rebase and merge | 풀 리퀘스트 병합 방식의 하나. 브랜치의 커밋을 하나씩 대상 브랜치에 잇는다 | 7 |
| Reflog | — | reflog | reflog | HEAD와 각 브랜치가 가리켜 온 커밋의 기록. "사라진" 커밋을 되살리는 데 쓴다 | 9 |
| Release | — | release(릴리스) | release（發布版本） | 태그를 바탕으로 릴리스 노트와 파일을 붙여 서비스에서 공개하는 버전 | 8 |
| Remote | — | 원격 | 遠端 | 다른 곳에 있는 같은 저장소. 보통 GitHub에 있다 | 6 |
| Remote Repository | — | 원격 저장소 | 遠端儲存庫 | 서버에 두고, 모두가 기준으로 삼기로 한 저장소 | 6 |
| Remote-tracking Branch | — | 원격 추적 브랜치 | 遠端追蹤分支 | 원격 브랜치가 마지막으로 봤을 때 어디 있었는지 기록한다. 예: `origin/main` | 6 |
| Repository | repo | 저장소 | 儲存庫 | Git이 프로젝트의 모든 버전을 기록하는 곳. 프로젝트 폴더 안의 `.git` | 2 |
| Reset | — | reset | reset | 현재 브랜치를 어떤 커밋으로 되돌린다. 모드에 따라 스테이징 영역과 파일도 되돌릴지 정해진다 | 9 |
| Restore | — | restore | restore | 파일을 스테이징 영역이나 어떤 커밋 안의 모습으로 되돌린다 | 9 |
| Revert | — | revert | revert | 옛 커밋의 변경을 상쇄하는 반대 방향 커밋을 더한다. 기록을 고쳐 쓰지 않는다 | 9 |
| Semantic Versioning | SemVer | 유의적 버전 | 語意化版本 | "주 버전.부 버전.수 버전"으로 변경의 크기를 나타내는 버전 번호 규칙 | 8 |
| SHA-1, SHA-256 | — | SHA-1, SHA-256 | SHA-1、SHA-256 | Git이 객체 번호를 계산하는 두 가지 해시 알고리즘. 번호는 각각 40글자와 64글자다 | 3 |
| Snapshot | — | 스냅숏 | 快照 | 어떤 시점의 모든 파일의 완전한 모습 | 3 |
| Squash and Merge | — | Squash and merge | Squash and merge | 풀 리퀘스트 병합 방식의 하나. 브랜치의 모든 변경을 새 커밋 하나로 합친다 | 7 |
| SSH Key | — | SSH 키 | SSH 金鑰 | GitHub에 신원을 증명하는 데 쓰는 공개 키와 개인 키 한 쌍 | 6 |
| Staging Area | — | 스테이징 영역 | 暫存區 | 다음 커밋에 들어갈 내용. 인덱스(index)라고도 한다 | 2 |
| Stash | — | stash | stash | 커밋하지 않은 변경을 잠시 치워 두고, 작업 디렉터리를 깨끗한 상태로 돌린다 | 9 |
| Submodule | — | 서브모듈 | 子模組 | 한 저장소 안에서 다른 저장소의 특정 커밋을 고정해서 참조하는 것 | 10 |
| Tag | — | 태그 | tag（標籤） | 커밋에 붙이는 움직이지 않는 이름. 보통 버전을 나타내는 데 쓴다 | 8 |
| Terminal | — | 터미널 | 終端機 | 글자로 명령어를 입력하는 창 | 1 |
| Three-way Merge | — | 3-way 병합 | 三方合併 | 병합 기준과 두 브랜치의 버전을 비교해 양쪽 변경을 자동으로 합치는 병합 | 5 |
| Tree | — | tree | tree | 폴더를 나타내는 객체. 안의 파일 이름과 각각이 가리키는 blob이나 tree를 나열한다 | 3 |
| Trunk-Based Development | — | 트렁크 기반 개발 | 主幹開發 | `main`과 수명이 짧은 기능 브랜치만 쓰고 자주 병합하는 브랜치 전략 | 8 |
| Two-Factor Authentication | 2FA | 2단계 인증 | 兩步驟驗證 | 로그인할 때 비밀번호 외에 휴대폰에서 만든 인증 코드를 입력한다 | 1 |
| Untracked File | — | 추적하지 않는 파일 | 未追蹤的檔案 | 작업 디렉터리에 있지만 Git이 아직 기록을 시작하지 않은 파일 | 2 |
| Version Control | — | 버전 관리 | 版本控制 | 파일의 모든 버전을 기록해 비교, 복원, 병합할 수 있게 하는 방법 | 0 |
| Working Directory | — | 작업 디렉터리 | 工作目錄 | 실제로 열어서 편집하는 파일 | 2 |

---

[← 제10장 좋은 습관](../3-when-things-go-wrong/10-good-habits/README.md) ｜ [목차](../README.md) ｜ [부록 B 현장 용어 →](jargon.md)
