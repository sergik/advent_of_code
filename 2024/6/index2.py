
path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [list(line.strip()) for line in f if line.strip()]

def getStart(grid)->tuple[int, int]:
   for i in range(len(grid)):
      for j in range(len(grid[i])):
         if grid[i][j] == '^':
            return (i, j)
         
   raise ValueError("No start found") 


start = getStart(data)
directions = [(-1, 0), (0, 1), (1, 0), (0,-1)]


def outOfBound(i, j, grid):
   if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
      return True
   return False


def imulate_movement(start, grid):
   current = start
   visited = set()
   current_direction = 0
   visited_with_dir = set()
   while True:
      dir = directions[current_direction]
      i, j = current
      visited.add((i, j))
      if (i, j, current_direction) in visited_with_dir:
         return None
      visited_with_dir.add((i, j, current_direction))
      ni, nj = i + dir[0], j + dir[1]
      if outOfBound(ni, nj, grid):
         break
      next = grid[ni][nj]
      if next == '#':
         current_direction = (current_direction + 1) % 4
      else:
         current = (ni, nj)

   return visited


visited = imulate_movement(start, data)
visited.remove(start)

res = 0
for p in visited:
   data[p[0]][p[1]] = '#'
   if imulate_movement(start, data) == None:
      res += 1
   data[p[0]][p[1]] = '.'
   

print(res)








