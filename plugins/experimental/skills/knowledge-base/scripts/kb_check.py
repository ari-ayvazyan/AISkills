#!/usr/bin/env python3
"""Check the knowledge tree. Reading the tree never needs this script.

usage: kb_check.py <root> [--stale-days N] [--today YYYY-MM-DD]
exit code 0 = no errors, 1 = errors. Stale files are reported, not errors.
"""
import argparse
import datetime as dt
import re
import sys
from pathlib import Path

MAX_ENTRIES = 30
MAX_BULLETS = 30
MAX_ENTRY_WORDS = 25
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FILE_ENTRY = re.compile(r"^- \[\[([^\]]+)\]\]")
FOLDER_ENTRY = re.compile(r"^- \[([^\]]+)/\]\(([^)]+)\)")
# only slug-shaped text is a link; bullets may quote syntax such as bash [[ $a ]]
LINK = re.compile(r"\[\[([A-Za-z0-9_-]+)\]\]")
UPDATED = re.compile(r"^updated:\s*(\S+)\s*$", re.M)


def split_frontmatter(text):
    """Returns (frontmatter, body); frontmatter is None when absent."""
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end < 0:
        return None, text
    return text[4:end], text[end + 4:]


def check_index(folder, errors):
    index = folder / "_index.md"
    if not index.exists():
        errors.append(f"{folder}: missing _index.md")
        return
    listed_files, listed_dirs = set(), set()
    entries = 0
    for line in index.read_text(encoding="utf-8").splitlines():
        if line.startswith("- ") and len(line.split()) > MAX_ENTRY_WORDS:
            errors.append(f"{index}: entry over {MAX_ENTRY_WORDS} words: {line[:60]}")
        if m := FILE_ENTRY.match(line):
            listed_files.add(m.group(1))
            entries += 1
        elif m := FOLDER_ENTRY.match(line):
            listed_dirs.add(m.group(1))
            entries += 1
            if not (folder / m.group(2)).exists():
                errors.append(f"{index}: dead folder link {m.group(2)}")
    if entries > MAX_ENTRIES:
        errors.append(f"{index}: {entries} entries, limit {MAX_ENTRIES}")
    files = {p.stem for p in folder.glob("*.md") if not p.name.startswith("_")}
    dirs = {p.name for p in folder.iterdir() if p.is_dir() and not p.name.startswith(".")}
    for name in sorted(files - listed_files):
        errors.append(f"{index}: topic file {name} not listed")
    for name in sorted(listed_files - files):
        errors.append(f"{index}: lists missing topic file {name}")
    for name in sorted(dirs - listed_dirs):
        errors.append(f"{index}: folder {name}/ not listed")
    for name in sorted(listed_dirs - dirs):
        errors.append(f"{index}: lists missing folder {name}/")


def check_topic(path, slugs, today, stale_days, errors, stale):
    if not SLUG.match(path.stem):
        errors.append(f"{path}: invalid slug")
    front, body = split_frontmatter(path.read_text(encoding="utf-8"))
    m = UPDATED.search(front) if front is not None else None
    if not m:
        errors.append(f"{path}: no updated date in frontmatter")
    else:
        try:
            updated = dt.date.fromisoformat(m.group(1))
        except ValueError:
            errors.append(f"{path}: invalid updated date {m.group(1)}")
        else:
            if updated > today:
                errors.append(f"{path}: updated date lies in the future")
            elif stale_days is not None and (today - updated).days > stale_days:
                stale.append(f"{path}: updated {updated}")
    bullets = sum(line.startswith("- ") for line in body.splitlines())
    if bullets > MAX_BULLETS:
        errors.append(f"{path}: {bullets} bullets, limit {MAX_BULLETS}")
    for link in LINK.findall(body):
        if link not in slugs:
            errors.append(f"{path}: broken link [[{link}]]")


def check(root, today, stale_days=None):
    errors, stale = [], []
    root = Path(root)
    topics = [p for p in root.rglob("*.md") if not p.name.startswith("_") and not any(s.startswith(".") for s in p.relative_to(root).parts)]
    seen = {}
    for p in topics:
        if p.stem in seen:
            errors.append(f"duplicate slug {p.stem}: {seen[p.stem]} and {p}")
        seen[p.stem] = p
    for folder in [root, *[p for p in root.rglob("*") if p.is_dir() and not any(s.startswith(".") for s in p.relative_to(root).parts)]]:
        check_index(folder, errors)
    for p in topics:
        check_topic(p, seen, today, stale_days, errors, stale)
    return errors, stale, len(topics)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--stale-days", type=int)
    ap.add_argument("--today", type=dt.date.fromisoformat, default=dt.date.today())
    a = ap.parse_args()
    errors, stale, n = check(a.root, a.today, a.stale_days)
    for e in errors:
        print("ERROR", e)
    for s in stale:
        print("STALE", s)
    print(f"{n} topic files, {len(errors)} errors, {len(stale)} stale")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
