def longestPalindromicSubstring(s):
    if len(s) < 2:
        return s
    maxLen = 1
    start = 0
    for i in range(len(s)):
      print(s[i-maxLen-1:i+1], s[i-maxLen-1:i+1][::-1], 'line 7')
      if i - maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
          start = i - maxLen - 1
          maxLen += 2
          continue
      if i - maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
          start = i - maxLen
          maxLen += 1
    return s[start:start+maxLen]

print(longestPalindromicSubstring('babad'))
