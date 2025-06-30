# Lesson: Iterative DFS (Preorder Rt -> L -> R)
# Step 1: Immediately print / process the current node, add right to stack, move pointer to left
# Step 2: if pointer is null, move pointer to stack.pop()

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    ans = []
    stack = []
    curr = root

    while stack or curr:
        if curr:
            ans.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()
    return ans

print(preorder(root = None))
print(preorder(root = TreeNode(1, None, None)))
print(preorder(root = TreeNode(2,
    TreeNode(1, None, None),
    TreeNode(3, None, None)
)))