# Trees
# Binary Tree Maximum Path Sum
# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

# The path sum of a path is the sum of the node's values in the path.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float("inf")
        # returns maximum path (not combining left & right) that includes that node
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            leftGain = max(0, dfs(node.left))
            rightGain = max(0, dfs(node.right))

            # for the result, we are allowed to combine left and right
            res = max(res, node.val + leftGain + rightGain)
            # choose between left path or right path (or 0)
            return (node.val + max(leftGain, rightGain))
        dfs(root)
        return res 
            
            
