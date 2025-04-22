# Topic: Tree, Level: Medium
# Kth Smallest Integer in BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None

        def dfs(node):
            # using nonlocal is the key!
            nonlocal count, result
            if not node:
                return

            dfs(node.left)

            count += 1
            if count == k:
                result = node.val
                return

            dfs(node.right)
        
        dfs(root)