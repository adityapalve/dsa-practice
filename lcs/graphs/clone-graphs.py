from typing import Optional
def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
  if not node: return node
  q, clones = deque([node]), {node.val: Node(node.val, [])}

  while q:
    curr = q.popleft()
    curr_clone = clones[curr.val]

    for ngbr in curr.neighbors:
      if ngbr.val not in clones:
          clones[ngbr.val] = Node(ngbr.val, [])
          q.append(ngbr)
      curr_clone.neighbors.append(clones[ngbr.val])
        
    return clones[node.val]