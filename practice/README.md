# 練習專案 / Practice project

`fan-controller` 是書中故事裡的韌體專案。每一章的「🧪 跟著做」都用它。

`fan-controller` is the firmware project from the book's story. Every "🧪 Hands-on" section uses it.

## 從第 2 章開始 / Start from Chapter 2

把 `fan-controller` 資料夾複製到你想放的位置，例如 `~/git-practice/fan-controller`，然後照第 2 章的「跟著做」開始。

Copy the `fan-controller` folder to a place of your choice, such as `~/git-practice/fan-controller`, and follow the Hands-on section of Chapter 2.

## 從任何一章開始 / Start from any chapter

在這本書的根目錄執行：

From the root of this repository, run:

```bash
bash practice/setup.sh 5
```

- 把 `5` 換成你要開始的章號（2～10）。
- 腳本會在 `~/git-practice/fan-controller` 建立那一章開始時的儲存庫。想放在別的地方，把路徑寫在章號後面。
- 如果資料夾已經存在，腳本會停下來，不會覆蓋你的檔案。
- Windows 請用安裝 Git 時一起裝好的 Git Bash 執行；macOS 與 Linux 用內建的終端機。
- Sourcetree 使用者執行完之後，把建立好的資料夾加進 Sourcetree 即可。

<!-- -->

- Replace `5` with the chapter you want to start from (2–10).
- The script creates the repository at `~/git-practice/fan-controller` as it is at the start of that chapter. Add a folder after the chapter number to put it somewhere else.
- If the folder already exists, the script stops and does not overwrite anything.
- On Windows, run it in Git Bash, which is installed with Git. On macOS and Linux, use the built-in terminal.
- In Sourcetree, add the new folder as an existing local repository.

## 第 6、7 章需要 GitHub / Chapters 6 and 7 need GitHub

腳本只會建立你電腦上的儲存庫。第 6、7 章要把它推到你自己的 GitHub 儲存庫，步驟寫在第 6 章的「跟著做」。

The script only creates the repository on your computer. In Chapters 6 and 7 you push it to your own GitHub repository, as described in the Hands-on section of Chapter 6.

## 關於程式碼 / About the code

程式碼刻意寫得很短，不需要開發板或編譯器也能跟上故事。註解使用英文，讓每個語言版本都能共用同一份練習專案。

The code is kept short, so you can follow the story without a board or a compiler. Comments are in English so that every language edition shares the same practice project.
