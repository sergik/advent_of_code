path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]

input = ''
for r in data:
   input += r


def extract_digit(start, s):
   i = start
   res = ''
   while (s[i].isdigit() and i - start < 3 and i < len(s)):
      res += s[i]
      i += 1
   
   if(len(res) == 0 or res[0] == '0'):
      return None
   
   return res   


res = 0
i = 0
while i < len(input) - 4:
  current = input[i:i+4]
  if current == 'mul(':
     i += 4
     firstArg = extract_digit(i, input)
     if firstArg != None:
        i += len(firstArg)
        if(i < len(input) and input[i] == ','):
           i += 1
           secondArg = extract_digit(i, input)
           if(secondArg != None):
               i += len(secondArg)
               if(i < len(input) and input[i] == ')'):
                  res += int(firstArg) * int(secondArg)
                  i+= 1
  else:
     i+=1 

print(res)