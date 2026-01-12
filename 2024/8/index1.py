
path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]


antena_locations = {}
for i in range(len(data)):
   for j in range(len(data[i])):
      if data[i][j] != '.':
         antena = data[i][j]
         if antena not in antena_locations:
            antena_locations[antena] = []
         antena_locations[antena].append((i,j))

def in_bound(grid, loc):
   i, j = loc
   return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

res = set()
for locations in antena_locations.values():
   for i in range(len(locations)):
      for j in range(i +1 , len(locations)):
         l1_x, l1_y = locations[i]
         l2_x, l2_y = locations[j]

         x_dif = l1_x - l2_x
         y_dif = l1_y - l2_y

         antenoid1 = (l1_x + x_dif, l1_y + y_dif)
         antenoid2 = (l2_x - x_dif, l2_y - y_dif)
         if in_bound(data, antenoid1):
            res.add(antenoid1)
         if in_bound(data, antenoid2):
            res.add(antenoid2)



print(len(res))