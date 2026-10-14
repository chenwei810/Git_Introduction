#!/usr/bin/env python3
"""檢查全書的連結、章節結構、提示框格式與用語。

Check the whole book for broken links, chapter structure, box format and wording.

用法 / Usage:
    python3 scripts/check_book.py

發現錯誤時回傳 1，只有警告時回傳 0。
Exits with 1 if any error is found; warnings alone exit with 0.

連到還沒翻譯的語言版本（en/、ja/、ko/）的連結只算警告，翻譯完成後就會消失。
Links to language versions that are not translated yet only produce warnings.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
SOURCE_LANG = "zh-TW"
TRANSLATION_LANGS = {"en", "ja", "ko"}
SKIP_DIRS = {".git", "node_modules", "templates"}

LINK_RE = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
IMG_TAG_RE = re.compile(r"<img\b[^>]*\bsrc=\"([^\"]+)\"", re.IGNORECASE)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
GITHUB_ROUTE_RE = re.compile(r"^(\.\./)+(issues|pulls|discussions|wiki|releases|actions)(/|$)")
CHAPTER_RE = re.compile(r"^([a-z]{2,3}(?:-[A-Za-z0-9]+)?)/\d-[a-z0-9-]+/(\d{2})-[a-z0-9-]+/README\.md$")
ALERT_RE = re.compile(r"^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$")
LIST_ITEM_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+")

# 各語言的章節必備元素 / Required parts of a chapter, per language.
CHAPTER_RULES = {
    "zh-TW": {
        "title": "# 第 {n} 章",
        "deep_dive": "🔍 深入一點｜",
        "required": {
            "📍 **專案與修改位置**": "專案與修改位置",
            "## 🧪 跟著做": "跟著做",
            "**你應該看到**": "跟著做的「你應該看到」",
            "## 📋 本章指令": "本章指令",
            "## 本章重點": "本章重點",
            "## 延伸閱讀": "延伸閱讀",
            "[目錄](../../README.md)": "導覽列",
        },
    },
    "en": {
        "title": "# Chapter {n}:",
        "deep_dive": "🔍 Deep dive |",
        "required": {
            "📍 **Where the project and the change are**": "Where the project and the change are",
            "## 🧪 Hands-on": "Hands-on",
            "**What you should see**": "What you should see",
            "## 📋 Commands in this chapter": "Commands in this chapter",
            "## Key takeaways": "Key takeaways",
            "## Further reading": "Further reading",
            "[Contents](../../README.md)": "navigation bar",
        },
    },
    "ja": {
        "title": "# 第 {n} 章",
        "deep_dive": "🔍 もっと詳しく｜",
        "required": {
            "📍 **プロジェクトと変更の現在地**": "プロジェクトと変更の現在地",
            "## 🧪 やってみよう": "やってみよう",
            "**こうなれば成功**": "こうなれば成功",
            "## 📋 この章のコマンド": "この章のコマンド",
            "## この章のポイント": "この章のポイント",
            "## 参考文献": "参考文献",
            "[目次](../../README.md)": "ナビゲーション",
        },
    },
    "ko": {
        "title": "# 제{n}장",
        "deep_dive": "🔍 더 알아보기｜",
        "required": {
            "📍 **프로젝트와 변경의 현재 위치**": "프로젝트와 변경의 현재 위치",
            "## 🧪 따라 해 보기": "따라 해 보기",
            "**이렇게 보이면 성공**": "이렇게 보이면 성공",
            "## 📋 이 장의 명령어": "이 장의 명령어",
            "## 이 장의 핵심": "이 장의 핵심",
            "## 참고 자료": "참고 자료",
            "[목차](../../README.md)": "내비게이션",
        },
    },
}

# 台灣用語檢查：常見的非台灣用語（只發出警告）。
# Terminology check for the Traditional Chinese text (warnings only).
DISCOURAGED_TERMS = {
    "默認": "預設",
    "缺省": "預設",
    "文件夾": "資料夾",
    "倉庫": "儲存庫",
    "遠程": "遠端",
    "源代碼": "原始碼",
    "源碼": "原始碼",
    "寫代碼": "寫程式",
    "信息": "訊息",
    "用戶": "使用者",
    "數據": "資料",
    "服務器": "伺服器",
    "視頻": "影片",
    "創建": "建立",
    "運行": "執行",
    "屏幕": "螢幕",
    "界面": "介面",
    "文檔": "文件",
    "調試": "除錯",
    "回滾": "還原",
    "軟件": "軟體",
    "硬件": "硬體",
    "芯片": "晶片",
    "接口": "介面",
    "內存": "記憶體",
    "網絡": "網路",
    "質量": "品質",
    "配置文件": "設定檔",
}

# 合法的台灣用法，出現時不要誤報 / Valid Taiwanese phrases that contain a discouraged term.
ALLOWED_PHRASES: dict[str, list[str]] = {}

# 常見的簡體字（只發出警告）。只收錄在台灣的繁體中文裡幾乎不會出現的字。
# Common Simplified Chinese characters (warnings only).
SIMPLIFIED_CHARS = set(
    "们这个为与说时过发现会对产业电导体层门线术设计础规质检测试结构样书读写图标题录页问错误单联关开"
    "经语译视频网络专务简态选择应运动输环节约织组济阶处获辆军伤长东乐车马鸟鱼龙风飞广庆库张弹强归"
    "忆怀总战户挂损换摄数断无旧显晓暂杂权条来极构枪树桥档梦检楼汉汤沟没泪泽洁浅测济浓润涨渐温湿满滤"
    "灭灯灵灾炉炼烂烦烧热爱牵状独狮猎猪献环现画畅疗盐监盖盘矿码砖确碍礼祸离种积称税稳穷窃竞笔筑签"
    "简类粮紧纠红级纪纤纯纳纵纷纸纹纺纽练细终绍结绕绘给络绝统继绩续维综绿缓编缘缩缴罗罚职肃肠肤肿胀"
    "胆脑脚脱脸舰艺芜苍苏药获营虑虚补装见观规视览觉触计订认讨让训议讯记讲许论访证评识诉词试话询该详"
    "误请诸读课谁调谈谢贝负贡财责败货贩购贯费资赋赏赔赚赛赞赢赶趋跃践轨转轮软轰轻载较辅辉输边达迁迟"
    "适选递逻遗邮释钉钟钢钱铁铜铝铭银链销锁锅锋锡键镜闭闯闲间闻阀阅队阳阴阵际陆陈险随隐难静顶项顺须"
    "顾领颗颜额饭馆驱驶驾验骑鲜鸡麦黄齐齿龄掺杂兴举义乐习书买乱亏亚亲亿仅从仓优伟传伤价众优员"
)


def iter_markdown_files() -> list[Path]:
    files = []
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        files.append(path)
    return files


def strip_code(lines: list[str]) -> list[str]:
    """把程式碼區塊與行內程式碼換成空白，保留行號。"""
    out, fence = [], None
    for line in lines:
        match = FENCE_RE.match(line)
        if match:
            mark = match.group(1)
            if fence is None:
                fence = mark
                out.append("")
                continue
            if mark[0] == fence[0] and len(mark) >= len(fence) and line.strip() == mark:
                fence = None
                out.append("")
                continue
        out.append("" if fence else INLINE_CODE_RE.sub("", line))
    return out


def check_links(path: Path, lines: list[str], errors: list[str], warnings: list[str]) -> None:
    rel = path.relative_to(ROOT).as_posix()
    for no, line in enumerate(lines, 1):
        targets = LINK_RE.findall(line) + IMG_TAG_RE.findall(line)
        for target in targets:
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE) or target.startswith("#"):
                continue
            if GITHUB_ROUTE_RE.match(target):
                continue
            clean = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            if resolved.exists():
                continue
            try:
                top = resolved.relative_to(ROOT).parts[0]
            except ValueError:
                top = ""
            if top in TRANSLATION_LANGS:
                warnings.append(f"{rel}:{no}: 翻譯尚未完成 translation not available yet -> {target}")
            else:
                errors.append(f"{rel}:{no}: 連結失效 broken link -> {target}")


def check_boxes(path: Path, lines: list[str], errors: list[str]) -> None:
    """引用區塊裡連續兩行一般文字，在 GitHub 上會被合併成同一段。"""
    rel = path.relative_to(ROOT).as_posix()
    prev_text = False
    for no, line in enumerate(lines, 1):
        if not line.startswith(">"):
            prev_text = False
            continue
        content = re.sub(r"^>\s?", "", line)
        if content.strip() == "" or LIST_ITEM_RE.match(content):
            prev_text = False
            continue
        if content.startswith("[!"):
            if not ALERT_RE.match(content.strip()):
                errors.append(f"{rel}:{no}: 不支援的提示框類型 unsupported alert type -> {content.strip()}")
            prev_text = False
            continue
        if prev_text:
            errors.append(
                f"{rel}:{no}: 引用區塊中連續兩行文字會被合併，請改用清單或空行 "
                f"consecutive lines in a blockquote will be merged"
            )
        prev_text = True


def check_details(path: Path, lines: list[str], errors: list[str], label: str | None) -> None:
    """「深入一點」區塊：summary 之後與 </details> 之前都要空一行，GitHub 才會把內容當成 Markdown。"""
    rel = path.relative_to(ROOT).as_posix()
    opened = None
    for no, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped == "<details>":
            if opened is not None:
                errors.append(f"{rel}:{no}: <details> 沒有關閉 unclosed <details>")
            opened = no
            nxt = lines[no] if no < len(lines) else ""
            if not nxt.strip().startswith("<summary>") or not nxt.strip().endswith("</summary>"):
                errors.append(f"{rel}:{no + 1}: <details> 下一行要是一行完整的 <summary> one-line <summary> expected")
            elif label and label not in nxt:
                errors.append(f"{rel}:{no + 1}: 標題應包含「{label}」 summary should contain \"{label}\"")
            if no + 1 < len(lines) and lines[no + 1].strip() != "":
                errors.append(f"{rel}:{no + 2}: </summary> 之後要空一行 blank line needed after </summary>")
        elif stripped == "</details>":
            if opened is None:
                errors.append(f"{rel}:{no}: 多出來的 </details> stray </details>")
            elif lines[no - 2].strip() != "":
                errors.append(f"{rel}:{no}: </details> 之前要空一行 blank line needed before </details>")
            opened = None
    if opened is not None:
        errors.append(f"{rel}:{opened}: <details> 沒有關閉 unclosed <details>")


def chapter_lang(path: Path) -> tuple[str, int] | None:
    match = CHAPTER_RE.match(path.relative_to(ROOT).as_posix())
    if not match:
        return None
    return match.group(1), int(match.group(2))


def check_chapter(path: Path, text: str, errors: list[str]) -> None:
    rel = path.relative_to(ROOT).as_posix()
    info = chapter_lang(path)
    if info is None:
        return
    lang, number = info
    rules = CHAPTER_RULES.get(lang)
    if rules is None:
        if "](../../README.md)" not in text:
            errors.append(f"{rel}: missing navigation link to ../../README.md")
        return
    title = rules["title"].format(n=number)
    first_heading = next((l for l in text.splitlines() if l.startswith("# ")), "")
    if not first_heading.startswith(title):
        errors.append(f"{rel}: 標題應以「{title}」開頭 title should start with \"{title}\"")
    for marker, name in rules["required"].items():
        if marker not in text:
            errors.append(f"{rel}: 缺少「{name}」 missing section")
    if "```mermaid" not in text:
        errors.append(f"{rel}: 缺少歷史圖或流程圖（Mermaid） missing a Mermaid diagram")


def check_language(path: Path, lines: list[str], warnings: list[str]) -> None:
    """只檢查繁體中文原文與根目錄的專案文件。"""
    rel = path.relative_to(ROOT)
    first = rel.parts[0]
    if rel.as_posix() in {"STYLE_GUIDE.md", "README.md", "PLAN.md"}:
        return
    if len(rel.parts) > 1 and first != SOURCE_LANG and re.match(r"^[a-z]{2,3}(-[A-Za-z0-9]+)?$", first):
        return
    for no, line in enumerate(lines, 1):
        for term, preferred in DISCOURAGED_TERMS.items():
            cleaned = line
            for phrase in ALLOWED_PHRASES.get(term, []):
                cleaned = cleaned.replace(phrase, "")
            if term in cleaned:
                warnings.append(f"{rel.as_posix()}:{no}: 建議用「{preferred}」取代「{term}」")
        found = sorted({ch for ch in line if ch in SIMPLIFIED_CHARS})
        if found:
            warnings.append(f"{rel.as_posix()}:{no}: 可能是簡體字 possible Simplified Chinese -> {''.join(found)}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    files = iter_markdown_files()
    for path in files:
        text = path.read_text(encoding="utf-8")
        lines = strip_code(text.splitlines())
        info = chapter_lang(path)
        label = CHAPTER_RULES.get(info[0], {}).get("deep_dive") if info else None
        check_links(path, lines, errors, warnings)
        check_boxes(path, lines, errors)
        check_details(path, lines, errors, label)
        check_chapter(path, text, errors)
        check_language(path, lines, warnings)

    pending = sum(1 for w in warnings if "translation not available yet" in w)
    for message in warnings:
        if "translation not available yet" not in message:
            print(f"WARNING {message}")
    for message in errors:
        print(f"ERROR   {message}")
    if pending:
        print(f"\n有 {pending} 個連結指向尚未翻譯的語言版本。{pending} links point to translations that are not available yet.")
    print(f"\n檢查了 {len(files)} 個檔案：{len(errors)} 個錯誤，{len(warnings) - pending} 個警告。")
    print(f"Checked {len(files)} files: {len(errors)} errors, {len(warnings) - pending} warnings.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
