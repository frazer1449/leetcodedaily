# Lesson: Iterative DFS (Inorder)
# Step 1: add a node to stack, then move left (do this until we reach a null)
# Step 2: if we reach a null, we pop from the stack (and set the pointer to it), add it to ans, move right from popped node

# Space Complexity: Height of Tree O(h)

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

# inorder (L -> Rt -> R) iterative DFS traversal (emulates a call-stack)
def inorder(root):
    ans = []

    stack = []
    curr = root
    while curr or stack:
        # case 1: pointer is not null
        if curr:
            stack.append(curr)
            curr = curr.left
        # case 2: pointer is null
        else:
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
    return ans

print(inorder(root = None))
print(inorder(root = TreeNode(1, None, None)))
print(inorder(root = TreeNode(2,
    TreeNode(1, None, None),
    TreeNode(3, None, None)
)))
