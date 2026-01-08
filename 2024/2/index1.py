def read_rows_as_lists(path: str) -> List[List[int]]:
    rows: List[List[int]] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            rows.append([int(x) for x in parts])
    return rows

rows = read_rows_as_lists("input.txt")

safe_reports_number = len(rows)
for r in rows:
    prev_diff = r[0] - r[1]
    for i in range(0, len(r) - 1):
        diff = r[i] - r[i+1]
        if abs(diff) > 3 or diff == 0 or diff * prev_diff < 0:
            safe_reports_number -= 1
            break
        prev_diff = diff


print(safe_reports_number)