
path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]

prizes=[]
btns_a = []
btns_b = []

SHIFT = 10_000_000_000_000
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
   ax, ay = a
   bx, by = b
   PX = px + SHIFT
   PY = py + SHIFT

   D  = ax * by - ay * bx
   if D == 0:
      continue

        
   Da = PX * by - PY * bx
   Db = ax * PY - ay * PX
 
   if Da % D != 0 or Db % D != 0:
      continue

   a = Da // D
   b = Db // D
   if a < 0 or b < 0:
      continue

   res += 3 * a + b
   

print(res)
