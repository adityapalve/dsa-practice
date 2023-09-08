def dTemp(temperature:list[int]) -> list[int]:
  res = [0]*len(temperature)
  stack:(int,int) = []

  for i,t in enumerate(temperature):
    while stack and t > stack[-1][0]:
      print(stack)
      stack_t, stack_i = stack.pop()
      print(i, stack_i, stack_t)
      res[stack_i] = i - stack_i

    stack.append((t,i))

  return res

t1 = [73,74,75,71,69,72,76,73]
t2 = [30,40,50,60]
t3 = [30,60,90]

print(dTemp(t1))