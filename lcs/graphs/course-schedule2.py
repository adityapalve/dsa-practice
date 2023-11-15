def findOrder(numCourses, prerequisites):
  preqs = {c: [] for c in range(numCourses)}

  for crs, preq in prerequisites:
    preqs[crs].append(preq)

  visit, cycle = set(), set()
  output = []

  def dfs(crs):
    if crs in cycle:
      return False
    if crs in visit:
      return True
    
    cycle.add(crs)
    for pre in preqs[crs]:
      if dfs(pre) == False:
        return False
    cycle.remove(crs)
    visit.add(crs)
    output.append(crs)
    return True
  
  for c in range(numCourses):
    if dfs(c) == False:
      return []
  return output

# Test Case 1:
# numCourses = 2
# prerequisites = [[1,0]]
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(numCourses, prerequisites))