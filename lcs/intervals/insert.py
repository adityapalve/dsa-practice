def main(intervals, ni):
  res = []

  for i in range(len(intervals)):
    print(i, len(intervals))
    if ni[1]<intervals[i][0]:
      res.append(ni)
      return res + intervals[i:]
    elif ni[0]>intervals[i][1]:
      res.append(intervals[i])
    else:
      print(ni)
      ni = [min(ni[0],intervals[i][0]), max(ni[1],intervals[i][1])]
      print(ni, "line 14")
    print(res)
  res.append(ni)
  return res 

nums = [[1,3],[6,9]]
newInterval = [2,5]
output = [[1,5],[6,9]]
print(main(nums, newInterval))
nums2 = [[1,2],[3,5],[6,7],[8,10],[12,16]] 
newInterval2 = [4,8]
output2 = [[1,2],[3,10],[12,16]][[]]

