path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]
from collections import Counter

def blink_counts(counts: Counter) -> Counter:
    nxt = Counter()
    for v, cnt in counts.items():
        if v == 0:
            nxt[1] += cnt
            continue

        s = str(v)
        if len(s) % 2 == 0:
            mid = len(s) // 2
            left = int(s[:mid])
            right = int(s[mid:])   # int() removes leading zeros automatically
            nxt[left] += cnt
            nxt[right] += cnt
        else:
            nxt[v * 2024] += cnt
    return nxt

def stones_after_blinks(initial_stones, blinks: int) -> int:
    counts = Counter(initial_stones)
    for _ in range(blinks):
        counts = blink_counts(counts)
    return sum(counts.values())

print(stones_after_blinks([3028, 78, 973951, 5146801, 5, 0, 23533, 857], 75))