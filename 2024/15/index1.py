path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]

field = []
moves = ''
for line in data:
   if line.startswith('#'):
      field.append(list(line))
   elif len(line) > 0:
      moves += line

moves_map = {
   '<': (0, -1),
   'v': (1, 0),
   '^': (-1, 0),
   '>': (0, 1)
}

def getRobotPosition(field)->tuple[int, int]:
   for i in range(1, len(field)):
      for j in range(1, len(field[0]) - 1):
         if(field[i][j] == '@'):
            return (i,j)
         
def getCordsSum(field):
   res = 0
   for i in range(1, len(field) - 1):
      for j in range(1, len(field[0]) - 1):
         if field[i][j] == 'O':
            res += 100 * i + j

   return res

robot_position = getRobotPosition(field)
for move in moves:
   dir = moves_map[move]

   position = robot_position
   while True:
      position = (position[0] + dir[0], position[1] + dir[1])
      x, y = position
      if field[x][y] == '.':
         while position != robot_position:
            current = position
            position = (position[0] - dir[0], position[1] - dir[1])
            field[current[0]][current[1]] = field[position[0]][position[1]]
         field[robot_position[0]][robot_position[1]] = '.'
         robot_position = (robot_position[0] + dir[0], robot_position[1] + dir[1])
         break
      elif field[x][y] == '#':
         break


sum = getCordsSum(field)
print(sum)



