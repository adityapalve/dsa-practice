def permute(nums:list[int]) -> list[list[int]]:
  res = []

  if len(nums) == 1:
    return [nums.copy()]

  for i in nums:
    n = nums.pop(0)
    perms = permute(nums)

    for perm in perms:
      perm.append(n)
    
    res.extend(perms)
    nums.append(n)

  return res 



nums = [1,2,3]
output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(permute(nums))