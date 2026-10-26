#!/usr/bin/env python3
"""Read every note's properties (front matter) with a plain
YAML parser, and parse every .obsidian settings file with a
plain JSON parser. Evidence that both are ordinary text
formats any tool can read."""
import json
import os
import sys

import yaml

vault = sys.argv[1]

print("== properties (YAML front matter) ==")
for root, dirs, names in os.walk(vault):
    dirs[:] = [d for d in dirs if d != ".obsidian"]
    for name in sorted(names):
        if not name.endswith(".md"):
            continue
        full = os.path.join(root, name)
        with open(full, encoding="utf-8") as f:
            text = f.read()
        if not text.startswith("---\n"):
            continue
        block = text.split("---\n", 2)[1]
        data = yaml.safe_load(block)
        rel = os.path.relpath(full, vault)
        print(f"{rel}: {data}")

print()
print("== .obsidian settings (JSON) ==")
conf = os.path.join(vault, ".obsidian")
if not os.path.isdir(conf):
    print("(no .obsidian folder in this vault)")
    sys.exit(0)
for name in sorted(os.listdir(conf)):
    if not name.endswith(".json"):
        continue
    with open(os.path.join(conf, name), encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict):
        print(f"{name}: a JSON object with {len(data)} keys: "
              f"{', '.join(list(data)[:6])}")
    else:
        print(f"{name}: a JSON {type(data).__name__} of {len(data)} entries")
