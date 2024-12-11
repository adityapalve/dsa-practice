l = input()
nums = list(map(int, input().split()))
# l = 10
# test = '1000000000 1 1 1 1 1 1 1 1 1'
# ans = 8999999991

# nums = list(map(int, test.split()))

def count(l, nums):
    if l is None or l == 0:
        return 0
    ns = [nums[0]]
    count = 0
    # print(nums)
    for i in range(1, len(nums)):
        # print(ns)
        # print(nums)
        if ns[i-1]> nums[i]:
            count = count + abs(nums[i]-ns[i-1])
            ns.append(ns[i-1])
            # print(count)
        else:
            ns.append(nums[i])

    return count 
        
print(count(l, nums))