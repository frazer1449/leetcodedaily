# Tree
# Serialization and Deserialization (Pre-order Traversal of Tree DFS)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = []
        def preOrder(node):
            if not node:
                s.append("null")
                return
            s.append(str(node.val))
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)
        return ",".join(s)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if data[i] == "null":
                i += 1
                return None
            node = TreeNode(int(data[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()