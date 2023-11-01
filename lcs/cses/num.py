n = int(input())
nums = list(map(int, input().split()))
""" Very bad soln
def num(n, nums):
  d = {i:True for i in range(1,n+1)}
  
  for n in nums:
    d[n] = False
  
  number = [k for k, v in d.items() if v][0]
  print(number)
"""
# Optimal Solution:
def num(n, nums):
  s = sum(nums)
  expected_sum = n*(n+1)//2
  missing_n = expected_sum-s
  print(missing_n)


num(n,nums)
