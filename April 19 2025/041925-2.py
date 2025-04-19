# Valid Binary Search Tree => set ranges and pass it through dfs
# Topic: Tree, Level: Medium

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, lbound, ubound) -> bool:
            if not node:
                return True
            if node.val <= lbound:
                return False
            if node.val >= ubound:
                return False
            
            return dfs(node.left, lbound, node.val) and dfs(node.right, node.val, ubound)

        return dfs(root, -9999, 9999)