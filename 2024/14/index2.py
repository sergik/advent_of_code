import re

W, H = 101, 103
PERIOD = W * H  # 10403

DIR8 = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0)]
DIR4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def parse(inp: str):
    robots = []
    for line in inp.strip().splitlines():
        x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
        robots.append((x, y, vx, vy))
    return robots

def positions_at(robots, t):
    return [((x + vx * t) % W, (y + vy * t) % H) for x, y, vx, vy in robots]

def bbox(pos):
    xs = [x for x, _ in pos]
    ys = [y for _, y in pos]
    return min(xs), max(xs), min(ys), max(ys)

def render(pos, pad=0):
    s = set(pos)
    minx, maxx, miny, maxy = bbox(pos)
    minx = max(0, minx - pad); maxx = min(W - 1, maxx + pad)
    miny = max(0, miny - pad); maxy = min(H - 1, maxy + pad)

    out = []
    for y in range(miny, maxy + 1):
        row = []
        for x in range(minx, maxx + 1):
            row.append("#" if (x, y) in s else ".")
        out.append("".join(row))
    return "\n".join(out)

def connected_score(pos):
    """
    Score = number of robots that have at least one 8-neighbor.
    (Tree-like pictures maximize this strongly.)
    """
    s = set(pos)
    score = 0
    for x, y in pos:
        if any(((x + dx) % W, (y + dy) % H) in s for dx, dy in DIR8):
            score += 1
    return score

def edge_score(pos):
    """
    Alternative score: count 4-neighbor edges (each edge counted once).
    Even stronger signal sometimes.
    """
    s = set(pos)
    edges = 0
    for x, y in s:
        # count only "right" and "down" to avoid double counting
        if ((x + 1) % W, y) in s:
            edges += 1
        if (x, (y + 1) % H) in s:
            edges += 1
    return edges

def solve_part2(inp: str) -> int:
    robots = parse(inp)

    best_t = 0
    best = -1

    for t in range(PERIOD):
        pos = positions_at(robots, t)

        # Use one of the scores (try edge_score first; it’s usually very clean)
        sc = edge_score(pos)
        # sc = connected_score(pos)

        if sc > best:
            best = sc
            best_t = t

    # Print to verify visually (should look like a tree)
    pos = positions_at(robots, best_t)
    print("best_t =", best_t, "score =", best)
    print(render(pos, pad=1))

    return best_t

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        print(solve_part2(f.read()))
