# Topic: Graphs, Level: Medium
# Clone Graphs

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodeToClone = {}
        queue = deque([node])
        nodeToClone[node] = Node(node.val)

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in nodeToClone:
                    nodeToClone[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                nodeToClone[curr].neighbors.append(nodeToClone[neighbor])
        
        return nodeToClone[node]
            