
path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]

#data = ["2333133121414131402"]
print(len(data))
input = list(data[0])

id = 0

initial_state = []

for index, val in enumerate(input):
   if index % 2 == 0:
      initial_state.extend([str(id)] * int(val))
      id += 1
   else:
      initial_state.extend(["."] * int(val))


left = 0
right = len(initial_state) - 1
while left < right:
   if initial_state[left] != '.':
      left += 1
      continue

   if initial_state[right] == '.':
      right -=1
      continue
   
   initial_state[left] = initial_state[right]
   initial_state[right] = '.'
   left +=1
   right -=1


res=0
for i in range(len(initial_state)):
   if initial_state[i] == '.':
      break
   res += i * int(initial_state[i])

print(res)

   

