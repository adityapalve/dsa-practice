def prefixSum(nums):
  arr = [0]*len(nums)
  arr1 = [0]*len(nums)
  for i in range(len(nums)-1):
    arr[i] = nums[i+1]

  for i in range(len(nums)-1, 0, -1):
    arr1[i] = nums[i-1]
  print(arr)
  print(arr1)

nums = [2,3,1,4,5,6]
prefixSum(nums)