
path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]

def get_starts(grid):
   starts = []
   for i in range(len(grid)):
      for j in range(len(grid[0])):
         if grid[i][j] == '0':
            starts.append((i, j))
   return starts

starts = get_starts(data)

print(starts)

moves = [(0,1), (1, 0), (-1, 0), (0, -1)]

def move_valid(grid, n_pos, old_pos)-> bool:
   x, y = n_pos
   if x >=0 and y >=0 and x < len(grid) and y < len(grid[0]):
      return int(grid[x][y]) - int(grid[old_pos[0]][old_pos[1]]) == 1
   

def check_start(grid, start)->int:
   number = 0

   def dfs(pos):
      nonlocal number
      if grid[pos[0]][pos[1]] == '9':
         number += 1
      for m in moves:
         ni = pos[0] + m[0]
         nj = pos[1] + m[1]
         if move_valid(grid, (ni, nj), pos):
            dfs((ni, nj))  

   dfs(start)
   return number   

res = 0
for start in starts:
   res += check_start(data, start)

print(res)


   

