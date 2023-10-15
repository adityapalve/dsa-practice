def min_process(n, task_memory, task_type, max_memory):
  grouped_tasks = {}

  for i in range(n):
    if task_type[i] in grouped_tasks:
      grouped_tasks[task_type[i]].append(task_memory[i])
    else:
      grouped_tasks[task_type[i]] = [task_memory[i]]

  req_t = 0
  for key in grouped_tasks:
    tasks = sorted(grouped_tasks[key])

    while tasks:
      largest = tasks.pop()
       
      if tasks and tasks[0]+largest<= max_memory:
        tasks.pop(0)
      req_t += 1
  
  return req_t

n= 6
task_memory = [7, 2, 3, 9,9,1]
task_type = [1, 2, 1, 3,1,1]
max_mem = 10
print(min_process(n,task_memory,task_type,max_mem))