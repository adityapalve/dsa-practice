
# n,k = map(int, input().split())

d = {}
def foo(k,n,s1,s2,s3):
  for i in range(k):
    for j in range(n):
      for l in range(j+1,n):
        pass        
  pass


"""
3 4
4 1 2 3
4 1 3 2
4 2 1 3




j -> 1, k
l -> 1, k
"""
import itertools
import pprint
def foo1(k,n,vals):
  # for i in range(0,K):
  #     arr = list(map(int,input().split()))
  #     vals.append(arr)
  mult_combos = []
  K, N= k, n
  for i in range(0,K):
      combo = list(itertools.combinations(vals[i],2))
      mult_combos.append(combo)
  pprint.pprint(mult_combos)

  ans = []
  ans_count = 0
  for lst in mult_combos:
      for i in lst:
          ans.append(i)
  print("ans:", ans)
  
  for i in ans:
      c = ans.count(i)
      if c == K:
          ans_count += 1

  print(int(ans_count/K))


vals = [[4,1,2,3],
        [4,1,3,2],
        [4,2,1,3]]

foo1(3,4,vals)