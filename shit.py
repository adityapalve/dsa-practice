# when im writing python and i gotta do some [1, ...[2, 3, 4]] ass shit

# shit = [1]
# for i, j in enumerate([2, 3] + [4]):
#   shit += [j]

# print("im so fuckin smart")
class Solution:
  def __init__(self, numbers, target):
    self.target = target
    self.numbers = numbers

  def twoSum(self, numbers, target):
          d = {abs(x - target): i for i, x in enumerate(numbers)}
          print(d)
          for i, e in enumerate(numbers):
            print(i, e)
            if (abs(e-target) in d):
                print(abs(e-target), d[e])
                return sorted([d[e]+1, i+1])

  def twoSum2(self, numbers, target):
    l,r = 0, len(numbers)-1

    while l < r:
      curr = numbers[l] + numbers[r]

      if curr < target:
        l += 1
      if curr > target:
        r -= 1
      return [l+1, r+1] 
# numbers = [2,3,4]
numbers = [2,7,11,15]
target = 9 
# l = [1,3]
l = [1,2]
o = Solution(numbers, target)
# print(o.twoSum(numbers, target))
print(o.twoSum2(numbers, target))
print("expected output =",l)

