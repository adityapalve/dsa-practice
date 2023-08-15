l = [1, 2, 3, 4, 5, 6]
'''
Exposition of the Peak Finding Algorithm

'''
def compute(l):
  peak, peak_i = 0, 0
  for i,v in enumerate(l):
    if (v == 0 or v > peak):
      peak = v
      peak_i = i
  return peak_i, peak

print(compute(l))