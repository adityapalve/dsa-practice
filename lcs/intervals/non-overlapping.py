"""
Given an array of intervals *intervals* where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""
def main(intervals):
  intervals.sort()
  res = 0
  prev = intervals[0][1]
  for start, end in intervals[1:]:
    if start>=prev:
      prev = end
    else:
      prev= min(end, prev)
      res +=1
  return res 




intervals = [[1,2],[2,3],[3,4],[1,3]]
output = 1
print(main(intervals), output)
intervals2 = [[1,2],[1,2],[1,2]]
output2 = 2
print(main(intervals2), output2)
intervals3 = [[1,2],[2,3]]
output3 = 0
print(main(intervals3), output3)