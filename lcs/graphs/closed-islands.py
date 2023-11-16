def NumberOfClosedIslands(grid):
  count = 0
  def dfs(r, c):
    if(grid[r][c] == 1):
      return True
    if(r<=0 or c<=0 or r>=len(grid)-1 or c >=len(grid[0])-1):
        return False
    grid[r][c] = 1
    return dfs(r-1,c) and dfs(r+1,c) and dfs(r,c-1) and dfs(r,c+1)

  for i in range(1,len(grid)-1):
    for j in range(1,len(grid[0])-1):
      if(grid[i][j] == 0 and dfs(i,j)):
        count+=1

  return count

def NumberOfClosedIslands(grid):
  def dfs(r,c):
    if grid[r][c] == 1:
      return True

    grid[r][c] = 0
    dfs(r-1,c)
    dfs(r+1,c)
    dfs(r, c-1)
    dfs(r, c+1)
    
