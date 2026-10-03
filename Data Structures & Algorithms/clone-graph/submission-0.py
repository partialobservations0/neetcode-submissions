"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {}
        q = deque()
        if not node:
            return node
        copy = Node(node.val)
        oldToNew[node] = copy
        q.append(node)

        while q: 
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                oldToNew[curr].neighbors.append(oldToNew[neighbor])
            
        return oldToNew[node]
