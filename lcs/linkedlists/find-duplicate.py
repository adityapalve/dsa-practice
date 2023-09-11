def findDuplicate(nums:list[int]) -> int:
  for e in nums:
    idx = abs(e)
    if nums[idx] < 0:
      return idx 
    nums[idx] = -nums[idx]
  return -1 

nums = [1,3,4,2,2]
print(findDuplicate(nums))