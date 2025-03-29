
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# It is impossible to create the map while iterating through the set.

# Step 1: Create New Nodes & Use HashMap to Create Correspondences

# Step 2: To send the location of newNode2 to newNode1, we use a 3-way mapping process.

from typing import Optional

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # HashMap mapping old nodes to new nodes
        oldToNew = {}

        # Step 1: Create New Nodes and Map Corresponding Elements
        node = head
        while node:
            oldToNew[node] = Node(node.val)
            node = node.next
        
        # Step 2: 
        node = head
        while node:
            oldToNew[node].next = None if not node.next else oldToNew[node.next]
            oldToNew[node].random = None if not node.random else oldToNew[node.random]
            node = node.next
        
        return None if not head else oldToNew[head]