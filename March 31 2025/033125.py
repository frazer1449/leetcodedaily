# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        # Standard dfs for finding max height
        # def dfs(root):
        #     if not root:
        #         return 0
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     return 1 + max(left, right)

        # Now, as we traverse through the array, we need to update res.
        # dfs returns the HEIGHT of the current node
        # in the same time, during each iteration, it updates res.
        def dfs(root):
            nonlocal res
            
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return res

# MAKE SURE YOU UNDERSTAND THE DIFFERENCE
# Depth of a node = distance from root to that node.
# Height of a node = distance from that node to its deepest leaf.

# Code for Depth:
# BFS is used to find depth!

from collections import deque

# stores the depth of each node in tree.
depthMap = {}
def bfs(root):
    if not root:
        return
    
    depth = 0
    q = deque([root])
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            depthMap[node] = depth
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1
    
    


        
    