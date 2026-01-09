path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]


res = 0
n = len(data)
m = len(data[0])
for i in range(n):
   for j in range(m):
      if data[i][j] == 'X':
         up = ''
         ic = i
         while ic>= 0 and len(up) < 4:
            up += data[ic][j]
            ic -= 1
         if up == 'XMAS':
            res += 1
         
         down = ''
         ic = i
         while ic < n and len(down) < 4:
            down += data[ic][j]
            ic += 1
         if down == 'XMAS':
            res += 1

         left = ''
         jc = j
         while jc >= 0 and len(left) < 4:
            left += data[i][jc]
            jc -= 1
         if left == 'XMAS':
            res += 1

         right = ''
         jc = j
         while jc < m and len(right) < 4:
            right += data[i][jc]
            jc += 1
         if right == 'XMAS':
            res += 1

         left_up = ''
         jc = j
         ic = i
         while jc >= 0 and ic >= 0 and len(left_up) < 4:
            left_up += data[ic][jc]
            jc -= 1
            ic -= 1
         if left_up == 'XMAS':
            res += 1

         right_up = ''
         jc = j
         ic = i
         while jc < m and ic >= 0 and len(right_up) < 4:
            right_up += data[ic][jc]
            jc += 1
            ic -= 1
         if right_up == 'XMAS':
            res += 1

         right_down = ''
         jc = j
         ic = i
         while jc < m and ic < n and len(right_down) < 4:
            right_down += data[ic][jc]
            jc += 1
            ic += 1
         if right_down == 'XMAS':
            res += 1

         left_down = ''
         jc = j
         ic = i
         while jc >=0 and ic < n and len(left_down) < 4:
            left_down += data[ic][jc]
            jc -= 1
            ic += 1
         if left_down == 'XMAS':
            res += 1

print(res)
