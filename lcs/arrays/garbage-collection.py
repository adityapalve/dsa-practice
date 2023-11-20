def garbageCollection(garbage, travel):
  farthest_index = {"G":[0,0], "P":[0,0], "M":[0,0]}

  for i, s in enumerate(garbage):
    for g in s:
      farthest_index[g][1] += 1
      farthest_index[g][0] = i
  time = 0

  for g in farthest_index:
    index, count = farthest_index[g]
    time += count
    if index > 0:
      time += sum(travel[:index])

  return time

garbage = ["G","P","GP","GG"]
travel = [2,4,3]

print(garbageCollection(garbage, travel))