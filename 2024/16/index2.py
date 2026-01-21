from collections import deque

path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]

moves = [(0, 1), #east
         (1, 0), #south
         (0, -1), #west
         (-1, 0) #north
         ]

def getNextMoves(direction):
   next_moves = []
   next_moves.append((moves[direction], direction,  1))
   next_moves.append((moves[(direction + 1) % 4], (direction + 1) % 4,  1001))
   next_moves.append((moves[(direction + 2) % 4], (direction + 2) % 4, 2001))
   next_moves.append((moves[(direction + 3) % 4], (direction + 3) % 4,  1001))

   return next_moves

def getStartEnd(field):
   start = None
   end = None
   for i in range(len(field)):
      for j in range(len(field[i])):
         if field[i][j] == 'S':
            start = (i, j)
         if field[i][j] == 'E':
            end = (i, j)
   return (start, end)

visited = {}
q = deque()

field = data

start, end = getStartEnd(data)
q.append(((start[0], start[1], 0), 0, []))

min_score = 9999999999
all_min_paths = set()
while q:
   move, score, path = q.popleft()
   new_path = path.copy()
   new_path.append(move)
   row, col, dir = move
   if(field[row][col] == 'E'):
      if min_score >= score:
        if min_score > score:
           all_min_paths = set()
        min_score = score
        for m in new_path:
           all_min_paths.add((m[0], m[1]))
      continue
   if move in visited and visited[move] < score:
      continue
   else:
      visited[move] = score
   
   next_dir = getNextMoves(dir)
   for nm in next_dir:
      m, n_dir, score_penalty = nm
      next_r, next_col = m[0] + row, m[1] + col
      next_score = score + score_penalty
      if(field[next_r][next_col] != '#'):
         q.append(((next_r, next_col, n_dir), next_score, new_path))
      


print(len(all_min_paths))




