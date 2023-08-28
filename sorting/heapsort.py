# HeapSort
def quicksort(nums):
    left, right, equals = [], [], []
    if(len(nums)<1):
        return []
    mid = len(nums)//2

    for i in nums:
        if i< nums[mid]:
            left.append(i)
        elif i > nums[mid]:
            right.append(i)
        else:
            equals.append(i)

    return quicksort(left) + equals + quicksort(right)
a = [3, 5, 24, 6]
print(quicksort(a))