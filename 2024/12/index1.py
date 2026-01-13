
path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]

moves = [(0,1), (0,-1), (-1, 0), (1,0)]
def in_bound(grid, pos):
   x, y = pos
   return x >= 0 and y >=0 and x < len(grid) and y < len(grid[0])

def get_next_area(grid, start):
   area = set()

   def get_next_area_rec(pos):
      if pos in area:
         return
      area.add(pos)
      x, y = pos
      plant = grid[x][y]
      next = [(x + m[0],y + m[1]) for m in moves]
      for n in next:
         nx, ny = n
         if n not in area and in_bound(grid, n) and grid[nx][ny] == plant:
            get_next_area_rec(n)
   get_next_area_rec(start)
   return area

def get_next_perimiter(plants: set[tuple[int, int]], grid):
   perimiter = 0
   for plant in plants:
      x, y = plant
      neighbours = [(x + m[0],y + m[1]) for m in moves]
      for n in neighbours:
         nx, ny = n
         if not in_bound(grid, n) or grid[nx][ny] != grid[x][y]:
            perimiter+= 1
   return perimiter


visited = set()
res = 0
for i in range(len(data)):
   for j in range(len(data[0])):
      if (i,j) not in visited:
         next_plants_field = get_next_area(data, (i, j))
         next_area = len(next_plants_field)
         next_perimiter = get_next_perimiter(next_plants_field, data)
         res += next_area * next_perimiter
         visited.update(next_plants_field)

print(res)


         


