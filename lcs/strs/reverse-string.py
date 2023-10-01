def split(s:str):
  l = list(s.split()) 
  print(l)
  res = []
  for i in l:
    r = ''.join(list(i)[::-1]) 
    
    res.append(r)
  
  o = ' '.join(res)
  print(o)
  # print(res)
  return 0


split("Let's take LeetCode contest")
# print("Correct Ans: s'teL ekat edoCteeL tsetnoc")
