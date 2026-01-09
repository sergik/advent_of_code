path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]


res = 0
n = len(data)
m = len(data[0])
for i in range(1, n - 1):
   for j in range(1, m - 1):
     if data[i][j] == 'A':
        first = data[i-1][j-1] + data[i][j] + data[i+1][j+1]
        second = data[i+1][j-1] + data[i][j] + data[i-1][j+1]

        if (first == 'MAS' or first == 'SAM') and (second == 'MAS' or second == 'SAM'):
           res += 1

print(res)
