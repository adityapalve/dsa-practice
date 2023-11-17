def minPairSum(nums):
  nums.sort()
  lp, rp =  0, len(nums)-1
  max_sum = 0
  pairs = []
  while lp<rp:
      pairs.append((nums[lp],nums[rp]))
      lp += 1
      rp -= 1
  
  # sums = [sum(s) for s in pairs]
  sums = list(map(lambda s : sum(s), pairs))
  return max(sums)

nums= [3,5,4,2,4,6]
output = 8
print(minPairSum(nums))