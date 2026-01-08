def read_rows_as_lists(path: str) -> List[List[int]]:
    rows: List[List[int]] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            rows.append([int(x) for x in parts])
    return rows

rows = read_rows_as_lists("input.txt")

def remove_at_index(arr, idx):
    return arr[:idx] + arr[idx+1:]

def check_report(report: List[int], can_drop: bool) -> bool:
    prev_diff = report[0] - report[1]
    for i in range(0, len(report) - 1):
        diff = report[i] - report[i+1]
        if abs(diff) > 3 or diff == 0 or diff * prev_diff < 0:
            if can_drop:
                res = False
                for j in range(0, len(report)):
                    new_report = remove_at_index(report, j)
                    print(new_report)
                    res = check_report(new_report, False) or res
                return res
            return False
        prev_diff = diff
    return True

res = 0
for r in rows:
   if(check_report(r, True)):
       res += 1


print(res)