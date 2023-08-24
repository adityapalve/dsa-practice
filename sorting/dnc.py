def quicksort(nums):
    left, right, equals = [], [], []
    if nums == []:
      return nums

    pivot = nums[len(nums) // 2]

    for i in nums:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equals.append(i)
    # What error would the below return statement cause?
    # return quicksort(left).append(pivot) + quicksort(right)
    # print(left, right, pivot)
    # l = quicksort(left)
    # l.append(pivot) 
    # r = quicksort(right)
    # print(l, r)
    return quicksort(left) + equals + quicksort(right)

def merge(left, right):
    output = []
    l, r = 0, 0

    while(l< len(left) and r < len(right)):
      if left[l]< right[r]:
          output.append(left[l])
          l += 1
      else:
          output.append(right[r])
          r += 1
    output.extend(left[l:])
    output.extend(right[r:])
    return output

def sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2

    left = sort(nums[:mid])
    right = sort(nums[mid:])

    return merge(left, right)


# print(quicksort())
# a = [7,6,8,3,10,2,3,3]
# print(quicksort(a))
# print(sort(a))

a = (0 + 1)//2
print(a)