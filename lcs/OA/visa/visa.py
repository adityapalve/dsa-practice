from collections import Counter
def solution(centers):
  n = len(centers)

  centers = list(map(tuple, centers))
  point_count = Counter(centers)
  output = 0
  for x,y in centers:
    for j in range(-2,3):
      for k in range(-2,3):
        if point_count[(x+j,y+k)] >0 and not (j==k==0):
          print("Found collision",(x,y),(x+j,y+k))
        output += point_count[(x+j,y+k)]
        if j==k==0:
          output -= 1
        
  return output//2

print(solution([[1,1],[1,1]]))