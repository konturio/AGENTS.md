from pathlib import Path

SOURCE_FILE = Path('AGENTS.md')
RAW_FILE = Path('AGENTS.raw.md')

original_text = SOURCE_FILE.read_text()
RAW_FILE.write_text(original_text)

lines = original_text.splitlines()
if not lines:
    raise ValueError('AGENTS.md expected to contain data but is empty')

first_line = lines[0]

items: list[str] = []
current_header = None
for line in lines[1:]:
    if line.startswith('#'):
        current_header = line.lstrip('# ').rstrip(':')
    elif line.startswith(' - '):
        text = line[3:].strip()
        if current_header:
            items.append(f"{current_header}: {text}")
        else:
            items.append(text)
    elif line.strip():
        current_header = line.strip().rstrip(':')

if not items:
    items = [line.strip() for line in lines[1:] if line.strip()]

# trigram similarity utilities

def trigrams(s: str) -> set[str]:
    s = s.lower()
    return {s[i:i+3] for i in range(len(s) - 2)} if len(s) >= 3 else {s}


def trigram_similarity(a: str, b: str) -> float:
    ta, tb = trigrams(a), trigrams(b)
    union = ta | tb
    return len(ta & tb) / len(union) if union else 0.0


def distance(a: str, b: str) -> float:
    return 1 - trigram_similarity(a, b)


n = len(items)
if n == 0:
    Path('AGENTS.md').write_text(original_text)
    raise SystemExit

# precompute distance matrix
matrix = [[distance(ai, bj) for bj in items] for ai in items]

# pick first item least similar to the header
header_dists = [distance(first_line, it) for it in items]
first_idx = max(range(n), key=lambda i: header_dists[i])
path = [first_idx]
remaining = set(range(n)) - {first_idx}

# choose second item farthest from the first
if remaining:
    second_idx = max(remaining, key=lambda i: matrix[first_idx][i])
    path.append(second_idx)
    remaining.remove(second_idx)

while remaining:
    best_item = None
    best_end = None  # 'start' or 'end'
    best_dist = -1.0
    start_item = path[0]
    end_item = path[-1]
    for r in remaining:
        d_start = matrix[r][start_item]
        d_end = matrix[end_item][r]
        if d_start > best_dist or d_end > best_dist:
            if d_start >= d_end:
                best_dist = d_start
                best_item = r
                best_end = 'start'
            else:
                best_dist = d_end
                best_item = r
                best_end = 'end'
    if best_end == 'start':
        path.insert(0, best_item)
    else:
        path.append(best_item)
    remaining.remove(best_item)

ordered_items = [items[i] for i in path]
ordered_text = '\n'.join([first_line] + ordered_items) + '\n'
Path('AGENTS.md').write_text(ordered_text)
