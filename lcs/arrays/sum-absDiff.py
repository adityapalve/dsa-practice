def absDiff(nums):
  n = len(nums)
  prefix_sum = [0]*n
  suffix_sum = [0]*n
  res = [0]*n

  prefix_sum[0] = nums[0]
  for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]

  print("ps:",prefix_sum)
  suffix_sum[-1] = nums[-1]
  for i in range(n-2,-1,-1):
    suffix_sum[i] = suffix_sum[i+1] + nums[i]
  print("ss:",suffix_sum)

  for i in range(n):
    if i >0:
      res[i] += i*nums[i] - prefix_sum[i-1]
    if i < n-1:
      res[i] += suffix_sum[i+1] - (n-1-i)*nums[i]
  return res

nums = [2,3,5]
output = [4,3,5]

print(absDiff(nums))