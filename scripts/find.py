#!/usr/bin/env python3
"""跳跳物理知识库关键词检索。只用 Python 标准库。

用法：python3 scripts/find.py 关键词1 关键词2 ...   [--top 8]

查三处：概念条目（references/concepts）、知识卡和配图（references/lessons）。
关键词原样出现算 1 分；没原样出现时，把它切成两字片段，过半出现在文中算 0.5 分（「画宽」能碰上「画得过宽」）。
命中名字、别名、卡片标题、关键词的分数乘 3。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, "..", "references")


def hit(k, hay):
    if k in hay:
        return 1.0
    grams = [k[i:i + 2] for i in range(len(k) - 1)]
    if len(k) > 2 and sum(g in hay for g in grams) * 2 >= len(grams):
        return 0.5
    return 0.0


def score(kws, head, body):
    return sum(3 * hit(k, head) or hit(k, body) for k in kws)


def concepts():
    d = os.path.join(REF, "concepts")
    for f in sorted(os.listdir(d)):
        if not f.endswith(".md"):
            continue
        text = open(os.path.join(d, f), encoding="utf-8").read()
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        meta = m.group(1) if m else ""
        name = re.search(r"^concept:\s*(.*)$", meta, re.M)
        aliases = re.search(r"^aliases:\s*\[(.*)\]$", meta, re.M)
        head = " ".join(filter(None, [name and name.group(1), aliases and aliases.group(1)]))
        yield "concepts/" + f, (name.group(1) if name else f[:-3]), head, text


def lesson_sections():
    """lessons/<讲次>.md 按「## 知识卡」「## 配图」两节里的 ### 小标题切开。"""
    d = os.path.join(REF, "lessons")
    for f in sorted(os.listdir(d)):
        if not f.endswith(".md"):
            continue
        part, head, buf = "", None, []
        for line in open(os.path.join(d, f), encoding="utf-8"):
            if line.startswith("## ") or line.startswith("### "):
                if head:
                    yield "lessons/" + f, part, head, "".join(buf)
                head, buf = None, []
                if line.startswith("## "):
                    part = line[3:].strip()
                else:
                    head = line[4:].strip()
            elif head:
                buf.append(line)
        if head:
            yield "lessons/" + f, part, head, "".join(buf)


def main(argv):
    top = 8
    if "--top" in argv:
        i = argv.index("--top")
        top = int(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    kws = [k for k in argv if k.strip()]
    if not kws:
        print(__doc__)
        return 2
    crow = []
    for path, name, head, body in concepts():
        s = score(kws, head, body)
        if s:
            crow.append((s, path, name))
    crow.sort(key=lambda r: -r[0])
    print(f"== 概念条目（{len(crow)} 篇命中；先读这里，一篇汇齐老师各讲的讲法）")
    for s, path, name in crow[:top]:
        print(f"  [{s:g}] {path}  {name}")
    cards, figs = [], []
    for path, part, head, body in lesson_sections():
        first = body.strip().split("\n", 1)[0]
        s = score(kws, head + " " + first, body)
        if not s:
            continue
        if part == "知识卡":
            cards.append((s, path, head))
        elif part == "配图":
            img = re.search(r"^!\[.*$", body, re.M)
            figs.append((s, head, img.group(0) if img else ""))
    cards.sort(key=lambda r: -r[0])
    print(f"== 知识卡（{len(cards)} 条命中；到那一讲的文件里找这个小标题读全文）")
    for s, path, head in cards[:top]:
        print(f"  [{s:g}] {path}  {head}")
    figs.sort(key=lambda r: -r[0])
    print(f"== 配图（{len(figs)} 张命中；要用就原样抄后面那行图片链接）")
    for s, head, img in figs[:top]:
        print(f"  [{s:g}] {head}\n        {img}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
