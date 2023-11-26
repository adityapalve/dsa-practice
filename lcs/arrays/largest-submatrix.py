def largestSubmatrix(matrix):
  cols = len(matrix[0])
  rows = len(matrix)
  max_area = 0

  for i in range(1, rows):
    for j in range(cols):
      if matrix[i][j] == 1:
        matrix[i][j] += matrix[i-1][j]
  
  for i in range(rows):
    sorted_heights = sorted(matrix[i], reverse=True)
    for j in range(cols):
      max_area = max(max_area, sorted_heights[j]*(j+1))

  return max_area

matrix = [[0,0,1],[1,1,1],[1,0,1]]
output = 4



matrix_1 = [[1,1,0],[1,0,1]]
output_1 = 2

print(largestSubmatrix(matrix_1))