def subarray_sum(matrix, size):
  cols = len(matrix[0])
  rows = len(matrix)
  sums = []
  submatrix_sum = 0
  for i in range(rows-size+1):
    for j in range(cols-size+1):
      submatrix_sum = sum([sum(x[j:j+size]) for x in matrix[i:i+size]])
      sums.append(submatrix_sum)

  return sums

def foo(m,s):
  for i in range(len(m)-s+1):
    for j in range(len(m[0])-s+1):
      '''Two ways to perform the computation using list comprehension are as follows.
      '''
      # matrix = [[m[i+k][j+x] for x in range(s)] for k in range(s)]
      # matrix=[[m[k][x] for x in range(j,j+s)] for k in range(i,i+s)]
      
      # Using Lambdas!!
      matrix = list(map(lambda k: list(map(lambda l: m[k][l], range(j,j+s))), range(i,i+s)))
      print(matrix)

matrix1 = [
  [1,2,2,3,4],
  [1,2,3,5,6]
]
matrix2 = [
  [2,2,3],
  [3,4,5],
  [6,6,2]
]
# print(subarray_sum(matrix1,2))
# print(subarray_sum(matrix2,2))
# foo(matrix2,2)

def foo2():
  l = [[1,2],[4,3],[5,6]]

  for i,v in enumerate(l):
    print(i,v)

# foo2()

def foo3(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  
  def dfs(r,c,matrix):
    if r<0 or c<0 or r>=rows or c>=cols or matrix[r][c]=="#":
      # print("reaching here inside the boundary condition")
      return 

    # print("Reached here right before changing matrix")
    matrix[r][c] = "#"

    print(matrix)

    dfs(r-1,c,matrix)
    dfs(r+1,c,matrix)
    dfs(r,c+1,matrix)
    dfs(r,c-1,matrix) 

  dfs(0,0,matrix)
  
  return 0

foo3(matrix2)





