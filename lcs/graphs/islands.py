def numberOfIslands(grid):
    cols = len(grid[0]) - 1
    rows = len(grid) - 1
    count = 0

    def dfs(grid, r, c):
        if (c<0 or r<0 or c>cols or r>rows or grid[r][c] != "1"):
            return
        grid[r][c] = '#'
        dfs(grid, r+1,c)
        dfs(grid, r-1,c)
        dfs(grid, r,c+1)
        dfs(grid, r,c-1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count


grid1 = [["1","1","0"],
         ["1","0","0"],
         ["0","0","1"]
         ]

n = numberOfIslands(grid1)
print(n)

class AreaofIsland():
  """
  def maxAreaOfIsland(self, grid):
    seen = set()
    def area(r, c):
      if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
              and (r, c) not in seen and grid[r][c]):
        return 0
      seen.add((r, c))
      return (1 + area(r+1, c) + area(r-1, c) +
    area(r, c-1) + area(r, c+1))

    return max(area(r, c)
                for r in range(len(grid))
                for c in range(len(grid[0])))
  """
  def maxAreaOfIsland(self, grid):
    if not grid:
      return 0
    rows = len(grid) - 1
    cols = len(grid[0]) - 1
    count = 0

    def dfs(r, c):
      if(c<0 or r<0 or c>cols or r>rows or grid[r][c] == "0"):
        return 0
      count = 1
      grid[r][c] = "0"
      count = count + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1)+ dfs(r,c-1)
      return count

    for i in range(rows+1):
      for j in range(cols+1):
        if grid[i][j] == "1":
          count = max(count, dfs(i, j))
    return count
