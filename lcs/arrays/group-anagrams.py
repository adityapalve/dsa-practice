def groupAnagrams(strs: list[str]):
  d = {}
  res = []

  for i in range(len(strs)):
    s = "".join(sorted(strs[i]))
    if s in d:
      d[s].append(strs[i])
    else:
      d[s] = [strs[i]]

  print(strs, d)   

  res = d.values()

  return res


# Test Case 1:
arr = ['aba','baa', 'abba', 'aab', 'abb']
res = [['aba','baa','aab'], ['abb'], ['abba']]

groupAnagrams(arr)

arr2 = [""]
res2 = [[""]]

arr3 = ["a"]
res3 = [["a"]]