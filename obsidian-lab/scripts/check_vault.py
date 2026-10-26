#!/usr/bin/env python3
"""Check every link in a vault, using nothing but the files.

Obsidian's two link styles, reduced to
what they mean on disk:

* A wikilink [[Some Note]] resolves by
  NAME. It finds a Markdown file of that
  name anywhere in the vault. Headings
  after a # must exist in that file.
  An embed ![[file.png]] finds any file
  of that name anywhere in the vault.
* A Markdown link [text](Some Note.md)
  resolves by PATH, relative to the
  folder the linking note sits in.

This script applies exactly those rules
and lists what resolves and what does
not. Exit code 0 when nothing is
broken, 1 when something is.
"""
import os
import re
import sys

WIKI = re.compile(r"!?\[\[([^\]|#]+)(#[^\]|]+)?(\|[^\]]*)?\]\]")
MDLINK = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def collect(vault):
    notes = {}   # basename without .md -> path
    files = {}   # basename -> path, for embeds
    paths = []   # every markdown file, relative
    for root, dirs, names in os.walk(vault):
        dirs[:] = [d for d in dirs if d != ".obsidian"]
        for name in names:
            full = os.path.join(root, name)
            rel = os.path.relpath(full, vault)
            files[name] = rel
            if name.endswith(".md"):
                notes[name[:-3]] = rel
                paths.append(rel)
    return notes, files, sorted(paths)


def headings(path):
    found = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"#{1,6}\s+(.*)", line.strip())
            if m:
                found.append(m.group(1).strip())
    return found


def main(vault):
    notes, files, paths = collect(vault)
    broken = []
    total = 0
    for rel in paths:
        full = os.path.join(vault, rel)
        with open(full, encoding="utf-8") as f:
            text = f.read()
        for m in WIKI.finditer(text):
            total += 1
            target, heading = m.group(1).strip(), m.group(2)
            if target.endswith((".png", ".jpg", ".svg", ".pdf")):
                if target not in files:
                    broken.append(f"{rel}: embed [[{target}]] - no such file")
                continue
            if target not in notes:
                broken.append(f"{rel}: [[{target}]] - no note of that name")
                continue
            if heading:
                want = heading[1:].strip()
                have = headings(os.path.join(vault, notes[target]))
                if want not in have:
                    broken.append(f"{rel}: [[{target}{heading}]] - no such heading")
        for m in MDLINK.finditer(text):
            dest = m.group(1)
            if dest.startswith(("http://", "https://", "#", "mailto:")):
                continue
            total += 1
            dest = dest.split("#")[0].replace("%20", " ")
            here = os.path.dirname(full)
            if not os.path.exists(os.path.join(here, dest)):
                broken.append(f"{rel}: ({dest}) - no file at that path")
    print(f"vault: {vault}")
    print(f"notes: {len(paths)}  links checked: {total}")
    if broken:
        print(f"BROKEN: {len(broken)}")
        for b in broken:
            print(f"  {b}")
        return 1
    print("all links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
