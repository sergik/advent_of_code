
path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]

#data = ["2333133121414131402"]
print(len(data))
input = list(data[0])

id = 0

initial_state = []
state_compacted = []

for index, val in enumerate(input):
   if index % 2 == 0:
      state_compacted.append([(int(val), id)])
      initial_state.extend([str(id)] * int(val))
      id += 1
   else:
      state_compacted.append([(int(val), '.')])
      initial_state.extend(["."] * int(val))


for i in range(len(state_compacted) - 1, -1, -2):
   file_size, id = state_compacted[i][0]
   for j in range(1, i, 2):
      spot_size = state_compacted[j][0][0]
      if spot_size >= file_size:
         state_compacted[j-1].append((file_size, id))
         state_compacted[j][0] = (spot_size - file_size, '.')
         state_compacted[i][0] = (file_size, '.')
         break

index = 0
res = 0
for part in state_compacted:
   for pair in part:
      count, id = pair
      for i in range(0, count):
         if id != '.':
            res += id * index
         index += 1
print(res)
         


   

