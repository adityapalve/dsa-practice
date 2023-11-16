import math

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

def dist(n,x,y):
  max_dist = 0
  for i in range(n):
    for j in range(i+1,n):
      dx = abs(x[i]-x[j])
      dy = abs(y[i]-y[j])
      d = dy**2+dx**2
      max_dist = max(max_dist, math.sqrt(d))  
  
  print(round(max_dist**2))

dist(n, x, y)