# Topic: Tree, Level: Easy
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    # Code for Height
    # height: number of nodes on path from the root to the deepest leaf
    def height(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))