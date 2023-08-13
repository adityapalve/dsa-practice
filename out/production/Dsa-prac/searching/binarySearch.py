class Solution:
    def search(self, nums: list[int], target: int)-> int:
        def binary_search(nums, target, low, high):
            # if low > high:
            #     return -1
            #
            # mid = int(low + (high-low)/2)
            #
            # if(nums[mid] > target):
            #     return binary_search(nums, target, low, mid-1)
            # elif(nums[mid] < target):
            #     return binary_search(nums, target, mid+1, high)
            # else:
            #     return mid
            if low <= high:
                mid = low+(high-low)//2
                if(nums[mid] == target):
                    return mid
                elif(nums[mid]>target):
                    return binary_search(nums, target, low, mid-1)
                else:
                    return binary_search(nums, target, mid+1, high)
            else:
                print(low, high, "line 24")
                return -1
        n = len(nums)
        return binary_search(nums, target, 0, n-1)


list = [1, 3, 5, 6, 10, 72]
sol = Solution()
print(sol.search(list, 6))