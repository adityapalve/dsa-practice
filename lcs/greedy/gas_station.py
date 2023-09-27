def main(gas, cost):
  if sum(gas)<sum(cost):
    return -1
  total = 0
  res = 0
  for i in range(len(gas)):
    total += (gas[i]-cost[i])
    if total<0:
      total = 0
      res = i+1
  return res 


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
output = 3
gas2, cost2=[2,3,4], [3,4,3]
output2 = -1
print(main(gas,cost), output)
print(main(gas2,cost2), output2)
