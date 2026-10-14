# 工具腳本 / Scripts

這些腳本只需要 Python 3，不需要安裝任何套件。請在專案根目錄執行。

These scripts only need Python 3. Run them from the repository root.

| 腳本 Script | 用途 Purpose |
|---|---|
| `python3 scripts/check_book.py` | 檢查連結、章節結構、提示框格式與用語。GitHub 會在每次 push 和 Pull Request 時自動執行。 Checks links, chapter structure, box format and wording. Runs automatically on GitHub. |
| `python3 scripts/check_translations.py [語言代碼]` | 找出過期、缺少或孤立的翻譯檔。 Finds outdated, missing or orphaned translations. |
| `python3 scripts/check_translations.py --stamp <檔案或語言>` | 翻譯或同步完成後，更新來源標記中的指紋。 Updates the fingerprint in the source marker after translating or syncing. |
| `python3 scripts/list_figures.py [--markdown]` | 列出中文原文中所有待補的圖。 Lists all figure placeholders in the original. |
