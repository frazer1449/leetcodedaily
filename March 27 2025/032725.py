# Level: Easy, Topic: Tree
# Invert Binary Tree
# You are given the root of a binary tree root. Invert the binary tree and return its root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)

        root.right = left_inverted
        root.left = right_inverted

        return root

# sol = Solution()
# sol.invertTree(root)
        