
path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]

def getStart(grid)->tuple[int, int]:
   for i in range(len(grid)):
      for j in range(len(grid[i])):
         if grid[i][j] == '^':
            return (i, j)
         
   raise ValueError("No start found") 


start = getStart(data)
directions = [(-1, 0), (0, 1), (1, 0), (0,-1)]
current_direction = 0

def outOfBound(i, j, grid):
   if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
      return True
   return False


current = start
visited = set()
while True:
   dir = directions[current_direction]
   i, j = current
   visited.add((i, j))
   ni, nj = i + dir[0], j + dir[1]
   if outOfBound(ni, nj, data):
      break
   next = data[ni][nj]
   if next == '#':
      current_direction = (current_direction + 1) % 4
   else:
      current = (ni, nj)
   

print(len(visited))








