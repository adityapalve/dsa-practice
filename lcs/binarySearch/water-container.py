# LC link: https://leetcode.com/problems/container-with-most-water/
"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, 
such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

"""
# This Solution works but is a brute force approach and gives TLE

def maxArea(height):
  max_area = 0
  for i, h in enumerate(height):
      print(i,h)
      r = len(height)-1
      while r>i:
          h2 = height[r]
          area = min(h,h2)*(r-i)
          max_area = max(area, max_area)
          print(f"h2:{h2}, area:{area}, max_area:{max_area}")
          r -= 1
  return max_area


def maxArea_fast(height):
  lp, rp = 0, len(height)-1
  max_area = 0
  while lp<rp:
      area = min(height[lp], height[rp])*(rp-lp)
      max_area = max(area, max_area)
      
      if height[lp]<height[rp]:
          lp += 1
      else:
          rp -= 1

  return max_area

height = [1,8,6,2,5,4,8,3,7]
# Output: 49
print(maxArea_fast(height))