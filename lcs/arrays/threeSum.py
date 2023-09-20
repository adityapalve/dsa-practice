def threeSum(nums):
  nums.sort()

  for l in range(len(nums)-1):
    r = len(nums)-1
    mid = l+1

    while l>0 and nums[l] == nums[l-1]:
        continue
    while mid<right:
        if nums[mid]== nums[mid+1]:
            mid = mid + 1
        else:
           break
"""
    is the previous while loop the same as 
    while mid<right and nums[mid] == nums[mid+1]:
      mid = mid + 1
"""