from collections import deque
path = 'input.txt'
rels = []
with open(path, "r", encoding="utf-8") as f:
   data = [line for line in f]

i = 0
while i < len(data):
   line = data[i]
   if '|' in line:
      first, second = line.split('|')
      rels.append((int(first), int(second)))
      i += 1
   else:
      break

i += 1

inputs = []
while i < len(data):
   line = data[i]
   inputs.append(list(map(int,line.split(','))))
   i += 1

def buildDepsMap(rels):
   graph = {}
   res = {}
   keys = set()
   for rel in rels:
      keys.add(rel[0])
      keys.add(rel[1])
      if rel[0] not in graph:
         graph[rel[0]] = set()
      graph[rel[0]].add(rel[1])
      if rel[0] not in res:
         res[rel[0]] = 0
      if rel[1] not in res:
         res[rel[1]] = 0
      res[rel[1]] += 1

   return (graph, res)

graph, depsMap = buildDepsMap(rels)

def topoligicalSort(depsMap, graph):
   zero_keys = [k for k, v in depsMap.items() if v == 0]
   queue = deque()
   for k in zero_keys:
      queue.append((k, 1))
   res = {}
   while len(queue) > 0:
      key, rang = queue.popleft()
      refs = graph.get(key, set())
      res[key] = rang
      for ref in refs:
         depsMap[ref] -= 1
         if depsMap[ref] == 0:
            queue.append((ref, rang + 1))
   
   return res

rankMap = topoligicalSort(depsMap, graph)


def inputValid(input, rankMap):
   for i in range(0, len(input) - 1):
      if rankMap[input[i]] > rankMap[input[i+1]]:
         return False
   return True


res = 0
for input in inputs:
   input_chars = set(input)
   instructions = [rel for rel in rels if rel[0] in input_chars and rel[1] in input_chars]
  
   graph, depsMap = buildDepsMap(instructions)
   rankMap = topoligicalSort(depsMap, graph)
   if not inputValid(input, rankMap):
      sorted_items = sorted(input, key=lambda k: rankMap[k])
      res += sorted_items[len(sorted_items) // 2]


print(res)






