n = int(input())
nums = list(map(int, input().split()))

def num(n, nums):
  s = sum(nums)
  expected_sum = n*(n+1)//2
  missing_n = expected_sum-s
  print(missing_n)

num(n,nums)
