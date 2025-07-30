import os
import re
from pathlib import Path

SOURCE_FILE = Path('AGENTS.md')
RAW_FILE = Path('AGENTS.raw.md')

original_text = SOURCE_FILE.read_text()
RAW_FILE.write_text(original_text)

# parse headers and items from RAW_FILE
lines = original_text.splitlines()
if not lines:
    raise SystemExit('AGENTS.md is empty')
first_line = lines[0]

items = []
current_header = None
for line in lines:
    if line.startswith('#'):
        # treat header as is
        current_header = line.lstrip('# ').rstrip(':')
    elif line.startswith(' - '):
        text = line[3:].strip()
        if current_header:
            items.append(f"{current_header}: {text}")
        else:
            items.append(text)
    elif line.strip():
        # treat as plain line
        current_header = line.strip().rstrip(':')

if not items:
    items = [line.strip() for line in lines if line.strip()]

# trigram similarity
def trigrams(s):
    return {s[i:i+3] for i in range(len(s) - 2)} if len(s) >= 3 else {s}

def trigram_similarity(a, b):
    ta, tb = trigrams(a), trigrams(b)
    union = ta | tb
    if not union:
        return 0.0
    return len(ta & tb) / len(union)

ordered = [first_line]
remaining = items
if remaining:
    ordered.append(remaining[0])
    remaining = remaining[1:]
while remaining:
    scores = []
    for item in remaining:
        score = sum(trigram_similarity(item, prev) for prev in ordered)
        scores.append((score, item))
    scores.sort()
    ordered.append(scores[0][1])
    remaining.remove(scores[0][1])

# write result
Path('AGENTS.md').write_text('\n'.join(ordered) + '\n')
