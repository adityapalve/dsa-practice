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

'''
0 3
1 2
2 1
'''