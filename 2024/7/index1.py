
path = 'input.txt'
with open(path, "r", encoding="utf-8") as f:
   data = [line.strip() for line in f if line.strip()]

results = []
numbers = []
for line in data:
   first, second = line.split(": ")
   results.append(int(first))
   numbers.append(list(map(int, second.split(" "))))

def generateExpressions(input):
   sub_expressions = [[input[0]]]
   for i in range(1, len(input)):
      new_sub_expressions = []
      for sub_expression in sub_expressions:
         new_plus_expr = sub_expression.copy()
         new_plus_expr.append('+')
         new_plus_expr.append(input[i])
         new_sub_expressions.append(new_plus_expr)

         new_mult_expr = sub_expression.copy()
         new_mult_expr.append('*')
         new_mult_expr.append(input[i])
         new_sub_expressions.append(new_mult_expr)
      sub_expressions = new_sub_expressions

   return sub_expressions
# def solve_expression(expression):
#    stack = []
#    op = '+'
#    for el in expression:
#       if len(stack) == 0:
#          stack.append(el)
#          continue
#       if el == '+' or el == '*':
#          op = el
#          continue
      
#       if op == '*':
#          prev = stack.pop()
#          stack.append(prev * el)
#       else:
#          stack.append(el)
      
#    return sum(stack)

def solve_expression(expression):
   op = '+'
   res = expression[0]
   for i in range(1, len(expression)):
      el = expression[i]
      if el == '+' or el == '*':
         op = el
         continue

      if op == '+':
         res += el
      else:
         res *= el
      
   return res

res = 0
print(solve_expression([11, '+', 6, '*', 16, '+', 20]))
for i in range(len(numbers)):
   num = numbers[i]
   expressions = generateExpressions(num)
   for ex in expressions:     
      if solve_expression(ex) == results[i]:
         res += results[i]
         break

print(res)
