import time
from collections import Counter

def main(s1, s2):
  freq_s1 = Counter(s1)
  wc = Counter()
  for i in range(len(s2)):
    wc[s2[i]] += 1

    if i >= len(s1):
      if wc[s2[i-len(s1)]] == 1:
        del wc[s2[i-len(s1)]]
      else:
        wc[s2[i-len(s1)]] -= 1
    
    if freq_s1 == wc:
      return True
  return False 

import random, string
def random_string_generator(l):
  chars = string.ascii_lowercase 
  random_string = ''.join(random.choice(chars) for _ in range(l))
  return random_string 

start = time.time()
s = random_string_generator(10**7)
s1, s2  = "ab", s+'ba' 
output = True
stop = time.time()
print(f'execution time for string gen:{stop-start}s, start time:{start}s, stop time:{stop}s')

start1 = time.time()
main(s1, s2)
stop1 = time.time()
print(f'execution time:{stop1-start1}s, start time:{start1}s, stop time:{stop1}s')
# print(, f'Ans should be: {output}')