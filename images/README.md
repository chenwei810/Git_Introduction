# 圖片 / Images

全書共用的圖片都放在這個資料夾。中文版、英文版和之後的每一種語言都使用同一套圖片，所以**圖上不放文字**；需要標示時使用數字編號，在各語言的圖說中解釋。

All images are shared by every language version, so **images contain no text**. Use numbers as labels and explain them in the caption of each language.

---

## 規範 / Guidelines

| 項目 Item | 規則 Rule |
|---|---|
| 格式 Format | 優先使用 SVG / SVG preferred |
| 截圖 Screenshots | 不放 Sourcetree 或 GitHub 的截圖，改畫簡化的示意圖，用編號標出按鈕位置 / No screenshots of Sourcetree or GitHub; draw simplified diagrams with numbered callouts |
| 檔名 File name | 「章節編號-描述」，例如 `05-conflict-markers.svg` / chapter number and description |
| 文字 Text | 圖上不放文字，只用數字編號 / No text in images, numbers only |
| 顏色 Color | 在 GitHub 的淺色與深色主題下都要看得清楚，避免只靠紅綠色區分 / Readable in light and dark themes; never rely on red versus green alone |
| 授權 License | 只能使用自己繪製或授權相容的圖片 / Only images you drew yourself or that have a compatible license |

從章節引用圖片的寫法（每種語言的路徑都一樣） / Referencing an image from a chapter (the path is the same in every language):

```markdown
![替代文字 / alt text](../../../images/05-conflict-markers.svg)
```

---

## 已完成的圖 / Finished images

| 檔案 File | 用在哪裡 Used in |
|---|---|
| `cover.svg` | 首頁封面 / Cover on the home pages |
| `social-preview.png` | GitHub 社群預覽圖，在 Settings → General → Social preview 上傳。只用於社群分享，所以含有文字 / GitHub social preview, uploaded under Settings → General → Social preview. It contains text because it is only used for sharing |
| `01-sourcetree-accounts.svg` | 第 1 章，Sourcetree 的帳號設定 / Chapter 1, Sourcetree account settings |
| `02-file-status.svg` | 第 2 章，Sourcetree 的 File Status / Chapter 2, Sourcetree File Status |
| `05-resolve-conflicts.svg` | 第 5 章，衝突檔案的右鍵選單 / Chapter 5, context menu for a conflicted file |
| `07-new-pull-request.svg` | 第 7 章，GitHub 開 Pull Request 的頁面 / Chapter 7, opening a pull request on GitHub |

commit 歷史圖都用 Mermaid 的 `gitGraph` 直接寫在章節裡，不另外存成圖片。

Commit graphs are written in the chapters with Mermaid `gitGraph`, not stored as images.

---

## 待補的圖 / Figures to draw

目前沒有待補的圖。新增圖片時，先在章節裡用 `<!-- 圖：… -->` 標出位置（英文版是 `<!-- Figure: … -->`），再用下面的指令列出清單。

There are no figures left to draw. When you plan a new figure, mark it with `<!-- 圖：… -->` (`<!-- Figure: … -->` in English) and list the placeholders with:

```bash
python3 scripts/list_figures.py --markdown
```
