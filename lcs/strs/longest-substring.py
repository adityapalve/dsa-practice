def longestSubstring(s:str) -> int:
  l,r = 0, 1
  while r<len(s)-1:
    if s[l] != s[r]:
      r +=1
    
  return 0

s = "abcabcbb"
print(sorted(s))