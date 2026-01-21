
path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]

prizes=[]
btns_a = []
btns_b = []

# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

def parseBtn(btn_string):
   print(btn_string)
   _, second = btn_string.split(':')
   x_str, y_str = second.split(',')
   x_str = x_str.replace('X', '').replace('=', '').strip()
   y_str = y_str.replace('Y', '').replace('=', '').strip()

   return (int(x_str), int(y_str))

for i in range(0, len(data), 3):
   btns_a.append(parseBtn(data[i]))
   btns_b.append(parseBtn(data[i+1]))
   prizes.append(parseBtn(data[i+2]))
   
res = 0
for i in range(len(prizes)):
   a = btns_a[i]
   b = btns_b[i]

   prize = prizes[i]
   px, py = prize

   x = 100 * a[0]
   y = 100*a[1]
   a_cnt = 100
   b_cnt = 0
   current_cost = 300
   min_cost = 99999
   
   while a_cnt >= 0 and b_cnt <= 100:      
      if x == px and y == py:
         min_cost = min(min_cost, a_cnt * 3 + b_cnt)
      if x > px or y > py:
         a_cnt -= 1
         x -= a[0]
         y -= a[1]
         continue
      
      b_cnt += 1
      x += b[0]
      y += b[1]
   
   if min_cost < 99999:
      res+= min_cost

print(res)
