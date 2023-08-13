def groupAnagrams(strs):
  n = len(strs)
  word_dict = {}

  for word in strs:
    tmp = "".join(sorted(word))

    return ans


# dict = {[] for i in range(4)}

dict = {}

tmp = tuple(sorted("eat"))

dict[tmp] = list()
list().append("eat")
# dict[tmp].append("eat")
print(dict)

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}

        for word in str:
            tmp = tuple(sorted(word))

            word_dict[tmp].append(word)
"""