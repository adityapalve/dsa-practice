def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while(l<=r):
            mid = (l+r)//2
            if target == nums[mid]:
                return True
            
            if nums[l] == nums[mid]:
                l +=1
                continue

            # Left half is sorted
            if nums[l]<=nums[mid]:
                if target<nums[l] or target>nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if target> nums[r] or target<nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False


"""
Testcases:
[2,5,6,0,0,1,2]
0
[2,5,6,0,0,1,2]
3
"""