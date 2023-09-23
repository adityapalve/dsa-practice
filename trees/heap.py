import heapq, math
def run(points, k):
  distances = []
  res = []
  dict1 = {}
  for x,y in points:
    d = math.sqrt(x**2+y**2)
    distances.append(-d)
    dict1[-d] = [x,y]

  heapq.heapify(distances)
  print(distances)

  while len(distances)>k:
    heapq.heappop(distances)
  print(distances)
  print(dict1)
  for d in distances:
    print(d)
    res.append(dict1[d])
  return print(res)

p = [[3,3],[5,-1],[-2,4]]
p = [[0,1],[1,0]]
run(p, 2)