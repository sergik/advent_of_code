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
col1.sort()
col2.sort()
res = 0
for i in range(len(col1)):
    res += abs(col1[i] - col2[i])

print(res)