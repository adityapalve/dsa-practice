"""
Works but time complexity is O(n^2) and so time limit would exceed.
def maxSubarry(nums:list[int]) -> int:
  maxSum = 0
  for i in range(len(nums)):
    currSum = 0
    for j in range(i,len(nums)):
      currSum = currSum + nums[j] 
      maxSum = max(currSum, maxSum)
  return maxSum
"""
def maxSubarray(nums:list[int]) -> int:
  maxSum = nums[0] 
  currSum = 0
  for i in nums:
    if currSum<0:
      currSum = 0
    currSum = currSum+i
    maxSum = max(maxSum, currSum)
  return maxSum
 

nums = [-2,1,-3,4,-1,2,1,-5,4]
output = 6
print(maxSubarray(nums))

# if maxSubarray(nums)== output:
#   print('Test Passed', maxSubarray(nums), output)
# else:
#   print("FAILED")

