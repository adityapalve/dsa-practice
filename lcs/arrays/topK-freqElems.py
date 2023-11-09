def topKFrequent(nums, k):
  num_count = {}

  for n in nums:
    if n in num_count:
      num_count[n] += 1
    else:
      num_count[n] = 1
  
  res = sorted(num_count, key= lambda i: num_count[i], reverse=True)

  return res[:k]  

"""
  Method 1:
  topK = sorted(num_count.items(), key= lambda v: v[1], reverse=True)[:k]
  res, _ = zip(*topK)
  return list(res)
"""
  # res = [v for v,c in topK]

arr1 = [1,2,3,1,2,24,441]
k = 2 # most frequent
print(topKFrequent(arr1,k))
res = [1,2]
