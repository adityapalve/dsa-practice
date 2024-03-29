"""
This is the trivial approach to the problem. But the bottleneck in the
approach is having to sort every list of tasks. This can get expensive
quite quickly.

Optimization Thoughts: Instead of sorting we can try and use a two-pointer
approach for pairing the complements together.
"""
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

"""
The Other Complement approach could be this,
theoretically this would be O(n).
Sorting is O(nlogn). The problem is somewhat analogous to the knapsack problem. 
We want to find pairs that fit into our max_memory constraint optimally.

A more efficient approach might be using a hash table (in Python, a set or dict would be handy). 
Instead of sorting, we can process tasks in their original order for each type. 
Here's an approach using a set:

For each type group:
Create an empty set seen.
For each task in the type group:
Compute the complement as max_memory - task_memory[i].
If complement is in seen, we've found a pair. Remove complement from seen and move on.
Otherwise, add task_memory[i] to seen.
The number of pairs formed will give us the number of tasks processed in parallel. The remaining tasks in the seen set will be processed individually. 
"""
def min_time_to_process(n, task_memory, task_type, max_memory):
    from collections import defaultdict
    
    # Group tasks by type
    grouped_tasks = defaultdict(list)
    for i in range(n):
        grouped_tasks[task_type[i]].append(task_memory[i])

    time_required = 0

    # Process each type group
    for _, tasks in grouped_tasks.items():
        seen = set()
        paired = 0

        for task in tasks:
            # What if there are no complement in the memory but their sum 
            # is <max_mem wouldnt this fail in that edge case?
            complement = max_memory - task 
            if complement in seen:
                paired += 1
                seen.remove(complement)
            else:
                seen.add(task)

        time_required += paired  # Count the number of pairs
        time_required += len(seen)  # The tasks that couldn't be paired

    return time_required