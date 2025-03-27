# Level: Easy, Topic: Tree
# Maximum Depth of Binary Tree

# Given the root of a binary tree, return its depth.
# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

sol = Solution()
n4 = TreeNode(val=4, left=None,right=None)
n3 = TreeNode(val=3, left=n4, right=None)
n2 = TreeNode(val=2, left=None, right=None)
n1 = TreeNode(val=1, left=n2, right=n3)

print(sol.maxDepth(n1))