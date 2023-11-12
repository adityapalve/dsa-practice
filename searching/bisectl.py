def bisectl(nums, target):
    lo, hi = 0, len(nums) - 1
    res = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if target < nums[mid]:
            hi = mid - 1
        elif target > nums[mid]:
            lo = mid + 1
        else:
            res = mid
            break

    return res, nums[res]


"""
lo, hi = 0, len(nums)-1
res = -1
ans = []
while(lo<=hi):
    mid = (lo+hi)//2
    if target == nums[mid]:
        res = mid
        hi = mid-1
    elif target<nums[mid]:
        hi=mid-1
    else:
        lo = mid+1
ans.append(res)
res , lo, hi = -1,0, len(nums)-1

while(lo<=hi):
    mid = (lo+hi)//2
    if target == nums[mid]:
        res = mid
        lo = mid+1
    elif target > nums[mid]:
        lo = mid+1
    else:
        hi = mid-1

ans.append(res)
    
return ans
"""

nums1 = [1, 2, 3, 4, 5, 6]
nums = [1, 2, 3, 3, 3, 4, 4, 5, 6]

nums3 = [5, 7, 7, 8, 8, 10]
target = 6
print(bisectl(nums1, 4))
