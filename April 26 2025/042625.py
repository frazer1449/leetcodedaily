# Level: Medium, Topic: Tree
# Construct Binary Tree from Preorder and Inorder Traversal

# You are given two integer arrays preorder and inorder.

# preorder: root -> left -> right
# inorder: left -> root -> right
# postorder: left -> right -> root

# preorder is the preorder traversal of a binary tree
# inorder is the inorder traversal of the same tree
# Both arrays are of the same size and consist of unique values.
# Rebuild the binary tree from the preorder and inorder traversals and return its root.

# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        i = inorder.index(root_val)

        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return root



# [3, 9, 5, 6, 20, 15, 7]
# [5, 9, 6, 3, 15, 20, 7]

# [9, 5, 6]
# [5, 9, 6]

# [5]
# [5]
        