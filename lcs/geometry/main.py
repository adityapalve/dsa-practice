def main(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  print(f'Before Tranformation {matrix}') 
  for i in range(rows):
    for j in range(i+1, cols):
     matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
  
  print(f'After Tranformation {matrix}')
  return 0


matrix = [
  [1,2,4],
  [3,9,7],
  [8,2,1]
]


def multiply(num1: str) -> int:
  x = 0
  nums =  list(num1)
  for i, n in enumerate(nums):
    # print(n, type(n))
    r = int(n)*(10**(len(nums)-i-1))
    print(r)
    x = x+r
  return x

# print(multiply("203"))
# print(main(matrix))




def getMinTime(task_memory, task_type, max_memory):
    # Write your code here
    tasks = sorted(zip(task_memory, task_type), key=lambda x: x[0])

    current_time = 0
    current_memory = 0

    for memory, type_ in tasks:

        # Check if current task can be processed
        if current_memory + memory <= max_memory:

            # Process current task
            current_memory += memory
            current_time += 1

        # Check if another task of same type can be processed
        else:

            # Find next task of same type
            i = tasks.index((memory, type_))
            next_memory, next_type = tasks[i+1]

            if next_type == type_ and current_memory + memory + next_memory <= max_memory:

                # Process current and next task
                current_memory += memory + next_memory
                current_time += 1

            else:

                # Process only current task
                current_memory += memory
                current_time += 1

            current_memory -= memory

    return current_time

