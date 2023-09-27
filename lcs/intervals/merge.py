def merge(intervals):
  res = []
  ni = intervals[0]
  for i in range(1, len(intervals)):
    # print("line 4:",i, intervals, len(intervals))
    # if intervals[i][0]>intervals[i-1][1]:
    #   res.append(intervals[i-1])
    # else:
    #   ni = [intervals[i-1][0], max(intervals[i-1][1],intervals[i][1])]
    #   print("line 11:",intervals, i)
    print(i, len(intervals))
    if ni[1]<intervals[i][0]:
      print(res, ni, "line 15")
      res.append(ni)
      ni = intervals[i]
      print("line 19:", ni)
    else:
      ni = [ni[0], max(ni[1],intervals[i][1])]
      print(res, ni)
  res.append(ni)
  return res 




intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
print(merge(intervals))
output =[[1,6],[8,10],[15,18]] 