def main(nums):
  ans = 0
  count = {}
  for n in nums:
      if n in count:
          ans += count[n]
          count[n] += 1
      else:
          count[n] = 1
  return ans


nums = [1,2,3,1,1,1,3,3]
output = 9 

print(main(nums),f'output={output}')