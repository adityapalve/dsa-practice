def jump(nums:list[int])-> bool:
  j =len(nums)-1

  for i in range(len(nums)-1, -1, -1):
    if nums[i]+i >=j:
      j = i
      i = i-1
    print(i,j)
  return True if j==0 else False 

array1 = [2,3,1,1,4]
array2 = [3,2,1,0,4]
array3 = [2,0,0] 
print("Ans should be True, :", jump(array3))
# ans1 = True
# ans2 = False
# if jump(array1) == ans1:
#   print("Test Case Solved")
# if jump(array2) == ans2:
#   print("Test Case Solved")