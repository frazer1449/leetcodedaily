# Count Good Nodes in Binary Tree
# Level: Medium, Topic: Tree

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            if not node:
                return 0
            
            newMax = max(maxVal, node.val)
            return int(node.val >= maxVal) + dfs(node.left, newMax) + dfs(node.right, newMax)
        
        return dfs(root, root.val)