l = [1,2,3,4]

lp, rp = 1, 1
out = []
for i, e in enumerate(l):
    if i == 0:
        lp = 1
    else:  
      lp = lp * l[i-1]
    out.append(lp)
print(out)

for i, e in enumerate(l[::-1]):
    if i == 0:
        rp = 1
    else:  
      rp = rp * l[len(l)-i]
      # print(l[len(l)-i-1], rp)
    out[len(l)-i-1] *= rp
print(out)

"""
Alternative Method:

3 for loops
prefix = [1]*n
        suffix = [1]*n
        ans = [1]*n
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1]*nums[i+1]
        
        for i in range(n):
            ans[i] = prefix[i]*suffix[i]
"""

'''
0 3
1 2
2 1
'''