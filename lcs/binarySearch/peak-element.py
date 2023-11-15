def findPeak(nums):
  lo, hi = 0, len(nums)-1

  if len(nums)<=1:
    return 0

  while(lo<=hi):
    mid = (lo+hi)//2

    if (nums[mid]>nums[mid-1] or mid==0) and (nums[mid]>nums[mid+1] or mid==len(nums)-1):
      return mid
    elif nums[mid]<nums[mid+1]:
      lo = mid+1
    else:
      hi = mid

  return mid


nums = [1,2,3,5,4,6,7,9,6]
i = findPeak(nums)
print(f"Peak element: {nums[i]} and index: {i}")