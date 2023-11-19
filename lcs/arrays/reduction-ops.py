"""
This is valid solution but brute forcing the problem
and would throw a TLE.
"""
def reductionOperations(nums):
  nums.sort()
  print(nums)
  end = len(nums)-1
  count = 0
  while end>0:
    print(end, count)
    if nums[end] == nums[end-1]:
      end -= 1
    else:
      nums[end] = nums[end-1]
      count += 1
      end = len(nums)-1
      print(nums, end, count)
  return count

nums = [7,9,10,8,6,4,1,5,2,3]
print(reductionOperations(nums))