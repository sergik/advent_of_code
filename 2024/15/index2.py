from collections import deque

DIRS = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}

def scale_map(lines):
    out = []
    for row in lines:
        new = []
        for ch in row:
            if ch == '#':
                new.append('##')
            elif ch == '.':
                new.append('..')
            elif ch == 'O':
                new.append('[]')
            elif ch == '@':
                new.append('@.')
            else:
                raise ValueError(f"Unexpected char: {ch}")
        out.append(''.join(new))
    return out

def build_state(grid):
    R, C = len(grid), len(grid[0])
    walls = set()
    boxes = set()
    robot = None

    for r in range(R):
        for c in range(C):
            ch = grid[r][c]
            if ch == '#':
                walls.add((r, c))
            elif ch == '@':
                robot = (r, c)
            elif ch == '[':
                boxes.add((r, c))

    def make_cell_map(boxes_set):
        m = {}
        for (r, c) in boxes_set:
            m[(r, c)] = (r, c)
            m[(r, c + 1)] = (r, c)
        return m

    return walls, boxes, make_cell_map(boxes), robot

def try_push_boxes(dr, dc, first_box, walls, boxes, cell_to_box):
    moving = set([first_box])
    q = deque([first_box])

    while q:
        r, c = q.popleft()
        nr, nc = r + dr, c + dc

        for cell in ((nr, nc), (nr, nc + 1)):
            if cell in walls:
                return False, None
            other = cell_to_box.get(cell)
            if other and other not in moving:
                moving.add(other)
                q.append(other)

    return True, moving

def apply_push(dr, dc, moving, boxes, cell_to_box):
    for r, c in moving:
        boxes.remove((r, c))
        cell_to_box.pop((r, c), None)
        cell_to_box.pop((r, c + 1), None)

    for r, c in moving:
        nr, nc = r + dr, c + dc
        boxes.add((nr, nc))
        cell_to_box[(nr, nc)] = (nr, nc)
        cell_to_box[(nr, nc + 1)] = (nr, nc)

def solve_from_file(filename="input.txt"):
    with open(filename, "r") as f:
        raw = f.read().rstrip("\n").split("\n")

    split = raw.index("")
    map_lines = raw[:split]
    moves = "".join(raw[split + 1:]).strip()

    grid = scale_map(map_lines)
    walls, boxes, cell_to_box, (rr, rc) = build_state(grid)

    for mv in moves:
        dr, dc = DIRS[mv]
        nr, nc = rr + dr, rc + dc

        if (nr, nc) in walls:
            continue

        hit = cell_to_box.get((nr, nc))
        if not hit:
            rr, rc = nr, nc
            continue

        ok, moving = try_push_boxes(dr, dc, hit, walls, boxes, cell_to_box)
        if not ok:
            continue

        apply_push(dr, dc, moving, boxes, cell_to_box)
        rr, rc = nr, nc

    return sum(100 * r + c for r, c in boxes)

if __name__ == "__main__":
    print(solve_from_file("input.txt"))
