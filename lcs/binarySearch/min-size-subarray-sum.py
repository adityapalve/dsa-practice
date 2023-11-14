"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""

def minSize(nums, target):
  start = 0
  min_length = float("inf")
  curr_sum = 0

  for end in range(len(nums)):
    curr_sum += nums[end]

    while curr_sum >= target:
      min_length = min(min_length, end-start+1)
      curr_sum -= nums[start]
      start += 1
  
  return min_length if min_length != float("inf") else 0

"""
7
-> first check if sum(arr)<target
    if true, return 0
-> check if 7 exists?
    return 1
-> find the max num in the array and
    find difference.
   proceed to find the diff.
   check: if sum of these is greater>= num
           |
[1,2,2,3,3,4]
7-4 = 


This is a very convoluted approach. A sliding window is much better here
"""
target = 7
nums = [2,3,1,2,4,3]
print(minSize(nums, target), "correct ans: 2")