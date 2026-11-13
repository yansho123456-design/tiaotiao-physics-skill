#!/usr/bin/env python3
"""跳跳物理知识库关键词检索。只用 Python 标准库。

用法：python3 scripts/find.py 关键词1 关键词2 ... [--top 8]
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, "..", "references")
SOURCE_RE = re.compile(
    r"<!-- SOURCE: ([^ ]+\.md) -->\n<!-- BEGIN [^>]+ -->\n(.*?)\n<!-- END [^>]+ -->",
    re.S,
)


def hit(k, hay):
    if k in hay:
        return 1.0
    grams = [k[i:i + 2] for i in range(len(k) - 1)]
    if len(k) > 2 and sum(g in hay for g in grams) * 2 >= len(grams):
        return 0.5
    return 0.0


def score(kws, head, body):
    return sum(3 * hit(k, head) or hit(k, body) for k in kws)


def source_sections(kind):
    directory = os.path.join(REF, kind)
    for filename in sorted(os.listdir(directory)):
        if not filename.endswith(".md"):
            continue
        text = open(os.path.join(directory, filename), encoding="utf-8").read()
        for source, body in SOURCE_RE.findall(text):
            yield f"{kind}/{filename}", source, body


def concepts():
    for volume, source, text in source_sections("concepts"):
        match = re.match(r"---\n(.*?)\n---\n", text, re.S)
        meta = match.group(1) if match else ""
        name = re.search(r"^concept:\s*(.*)$", meta, re.M)
        aliases = re.search(r"^aliases:\s*\[(.*)\]$", meta, re.M)
        head = " ".join(filter(None, [name and name.group(1), aliases and aliases.group(1)]))
        label = name.group(1) if name else os.path.basename(source)[:-3]
        yield volume, source, label, head, text


def lesson_sections():
    for volume, source, text in source_sections("lessons"):
        part, head, buf = "", None, []
        for line in text.splitlines(keepends=True):
            if line.startswith("## ") or line.startswith("### "):
                if head:
                    yield volume, source, part, head, "".join(buf)
                head, buf = None, []
                if line.startswith("## "):
                    part = line[3:].strip()
                else:
                    head = line[4:].strip()
            elif head:
                buf.append(line)
        if head:
            yield volume, source, part, head, "".join(buf)


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

    rows = []
    for volume, source, name, head, body in concepts():
        value = score(kws, head, body)
        if value:
            rows.append((value, volume, source, name))
    rows.sort(key=lambda row: -row[0])
    print(f"== 概念条目（{len(rows)} 篇命中；先读这里）")
    for value, volume, source, name in rows[:top]:
        print(f"  [{value:g}] {volume}  SOURCE: {source}  {name}")

    cards, figures = [], []
    for volume, source, part, head, body in lesson_sections():
        first = body.strip().split("\n", 1)[0]
        value = score(kws, head + " " + first, body)
        if not value:
            continue
        if part == "知识卡":
            cards.append((value, volume, source, head))
        elif part == "配图":
            image = re.search(r"^!\[.*$", body, re.M)
            figures.append((value, volume, source, head, image.group(0) if image else ""))

    cards.sort(key=lambda row: -row[0])
    print(f"== 知识卡（{len(cards)} 条命中）")
    for value, volume, source, head in cards[:top]:
        print(f"  [{value:g}] {volume}  SOURCE: {source}  {head}")

    figures.sort(key=lambda row: -row[0])
    print(f"== 配图（{len(figures)} 张命中）")
    for value, volume, source, head, image in figures[:top]:
        print(f"  [{value:g}] {volume}  SOURCE: {source}  {head}\n        {image}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
