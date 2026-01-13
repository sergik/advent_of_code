
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

def get_number_of_sides(plants: set[tuple[int, int]], grid):
   min_x, max_x, min_y, max_y = 999999999, -1 , 99999999, -1

   for p in plants:
      min_y = min(min_y, p[0])
      max_y = max(max_y, p[0])
      min_x = min(min_x, p[1])
      max_x = max(max_x, p[1])

   number_of_rows = max_y - min_y + 3
   number_of_cols = max_x - min_x + 3

   figure = [['.'] * number_of_cols for i in range(0, number_of_rows)]
   for p in plants:
      figure[p[0] - min_y + 1][p[1] - min_x + 1] = 'X'
   
   res = 0
  
   for i in range(len(figure)):
      for j in range(len(figure[0])):
         if(figure[i][j] == '.'):
            top_left = (i-1, j - 1)
            top_right = (i-1, j + 1)
            bottom_right = (i + 1, j+1)
            bottom_left = (i + 1, j-1)

            if in_bound(figure, top_left):
               if figure[i][j-1] == (figure[i-1][j]) and figure[top_left[0]][top_left[1]] == 'X':
                  res += 1
               elif figure[i][j-1] == 'X' and figure[i-1][j] == 'X':
                  res += 1
            if in_bound(figure, top_right):
               if figure[i][j+1] == (figure[i-1][j]) and figure[top_right[0]][top_right[1]] == 'X':
                  res += 1
               elif figure[i][j+1] == 'X' and figure[i-1][j] == 'X':
                  res+=1
            
            if in_bound(figure, bottom_right):
               if figure[i][j+1] == figure[i+1][j] and figure[bottom_right[0]][bottom_right[1]] == 'X':
                  res += 1
               elif figure[i][j+1] == 'X' and figure[i+1][j] == 'X':
                  res += 1

            if in_bound(figure, bottom_left):
               if figure[i][j-1] == figure[i+1][j]  and figure[bottom_left[0]][bottom_left[1]] == 'X':
                  res += 1
               elif figure[i][j-1] == 'X' and figure[i+1][j] == 'X':
                  res+=1
   print(res)
   return res


   



visited = set()
res = 0
for i in range(len(data)):
   for j in range(len(data[0])):
      if (i,j) not in visited:
         next_plants_field = get_next_area(data, (i, j))
         next_area = len(next_plants_field)
         number_of_sides = get_number_of_sides(next_plants_field, data)
         res += next_area * number_of_sides
         visited.update(next_plants_field)

print(res)


         


