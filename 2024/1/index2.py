def read_two_columns(path: str):
    col1 = []
    col2 = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
            if len(parts) < 2:
                raise ValueError(f"Expected 2 values per line, got: {line!r}")
            col1.append(int(parts[0]))
            col2.append(int(parts[1]))
    return col1, col2

col1, col2 = read_two_columns("input.txt")

res = 0
matches = {}
for val in col2:
    if val in matches:
        matches[val] += 1
    else:
        matches[val] = 1

for val in col1:
    if val in matches:
        res += matches[val] * val

print(res)