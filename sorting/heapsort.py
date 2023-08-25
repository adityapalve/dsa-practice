# HeapSort
def merge(left, right):
    output = []
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            output.append(left[l])
            l += 1
        else:
            output.append(right[r])
            r += 1
    output.extend(left[l:])
    output.extend(right[r:])
    return output


def mergesort(nums: list) -> list:
    if len(nums) <= 1:
        return nums  

    mid = len(nums) // 2

    left = mergesort(nums[:mid])
    print(left)
    right = mergesort(nums[mid:])
    print(right)
    return merge(left,right) 

a = [3, 5, 24, 6]
# mid = len(a) // 2
# print(a[:mid])
# print(a[mid:])
# print(merge(a[:mid], [6,24]))
print(mergesort(a))