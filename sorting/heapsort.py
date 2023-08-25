# HeapSort
def merge(left, right):
    l,r = 0,0 
    output = []

    while l< len(left) and r< len(right): 
      if left[l]<right[r]:
          output.append(left[l])
          l+=1
      else:
          output.append(right[r])          
          r+=1
    output.extend(left[l:])
    output.extend(right[r:])
    return output

def mergesort(nums: list) -> list:
    if len(nums)<=1:
        return []

    mid = len(nums)//2
    
    left  = mergesort(nums[:mid])
    right = mergesort(nums[mid:])
    return merge(left, right)

a = [3,5,24,6]
print(mergesort(a))