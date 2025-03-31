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
        # dfs still returns the HEIGHT of the current node = happens to equal left maxHeight
        # but, during each iteration, it updates res.
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
        
        
    