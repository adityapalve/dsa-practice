"""
This is valid solution but brute forcing the problem
and would throw a TLE.
"""
def reductionOperations_BF(nums):
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


"""
The optimal solution.
"""

def reductionOperations(nums):
  nums.sort(reverse=True)
  count = 0
  # for i in range(1,len(nums)):
  #   if nums[i] != nums[i-1]:
  #     count += i
  ans = 0
  up = 0
  for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
      up += 1
      print(ans,up)
    ans += up
    print(ans,up, i)
  return count

nums = [7,9,10,8,6,4,1,5,2,3]
print(reductionOperations(nums))