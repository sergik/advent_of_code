
path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]

starts = []
velocities = []

max_y = 103
max_x = 101

for line in data:
   start, vel = line.split(' ')
   sx, sy = start.replace('p=', '').split(',')
   vx, vy = vel.replace('v=', '').split(',')
   starts.append((int(sx), int(sy)))
   velocities.append((int(vx), int(vy)))

first = 0
second = 0
third = 0
fourth = 0

mid_x = max_x // 2
mid_y = max_y // 2
for i in range(len(starts)):
   start= starts[i]
   vel = velocities[i]

   nx = (start[0] + vel[0] * 100) % max_x
   ny = (start[1] + vel[1] * 100) % max_y
   if nx < 0:
      nx += max_x
   if ny < 0:
      ny += max_y

   if nx < mid_x and ny < mid_y:
      first += 1
   if nx > mid_x and ny < mid_y:
      second +=1
   if nx < mid_x and ny > mid_y:
      third+=1
   if nx > mid_x and ny > mid_y:
      fourth +=1


print(first * second * third * fourth)
