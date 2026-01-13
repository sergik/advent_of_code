
path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]


res = []
current = data[0].split(' ')


calculated = [-1]*100
def zero_stone_blinks(blinks):
   if calculated[blinks] != -1:
      return calculated[blinks]
   if blinks == 0:
      return 1
   if blinks == 1:
      return 1
   if blinks == 2:
      return 1
   if blinks == 3:
      return 2
   if blinks == 4:
      return 4
   if blinks > 4:
      calculated[blinks]= zero_stone_blinks(blinks - 4) + non_zero_stone_blinks(blinks-4, ['2', '2', '4'])
      return calculated[blinks]
   
calculated_stones = [[-1]*100 for i in range(11)]
def calculate_stone(blinks, stone):
   if calculated_stones[int(stone)][blinks] == -1:
      calculated_stones[int(stone)][blinks] = non_zero_stone_blinks(blinks -1, [str(int(stone) * 2024)])
   return calculated_stones[int(stone)][blinks]

   

def non_zero_stone_blinks(blinks, stones):
   if blinks == 0:
      return len(stones)
   next_stones = []
   res  = 0
   for el in stones:
      if el == '0':
         res += zero_stone_blinks(blinks)
      elif len(el) == 1:
         res += calculate_stone(blinks, el)
      elif len(el) % 2 == 0:
         first = el[: len(el) // 2]
         second = el[len(el)// 2:]
         second = second.lstrip('0')
         if len(second) == 0:
            second = '0'
         next_stones.append(first)
         next_stones.append(second)
      else:
         next_stones.append(str(int(el) * 2024))
   return res + non_zero_stone_blinks(blinks-1, next_stones) 

print(current)
res = non_zero_stone_blinks(75, current)

print(res)

# for i in range(10):
#    next= []
#    for el in current:
#       if el == '0':
#          next.append('1')
#       elif len(el) % 2 == 0:
#          first = el[: len(el) // 2]
#          second = el[len(el)// 2:]
#          second = second.lstrip('0')
#          if len(second) == 0:
#             second = '0'
#          next.append(first)
#          next.append(second)
#       else:
#          next.append(str(int(el) * 2024))
#    print(next))
#    current = next


         


