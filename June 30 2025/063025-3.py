# Lesson: Iterative DFS (Postorder L -> R -> Rt)
# Step 1: Use two stacks, "stack" and "visited" Initialize them each with stack = [root], visited = [False] 
#         (stack and visited will always have same size)
# Step 2: while stack & visited is non-empty, pop a node from "stack" and pop a bool from "visited." 
# Step 3: If popped node is marked true, process it (add it to "ans"). If popped node is marked false, add yourself with true, add right node with false, add left node with false.

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def postorder(root):
    ans = []
    
    stack = [root]
    visited = [False]

    while stack:
        node = stack.pop()
        bool = visited.pop()
        if bool:
            ans.append(node.val)
        else:
            stack.append(node)
            visited.append(True)
            if node.right:
                stack.append(node.right)
                visited.append(False)
            if node.left:
                stack.append(node.left)
                visited.append(False)
    return ans
two = TreeNode(2, TreeNode(4, None, None), None)
three = TreeNode(3, None, TreeNode(5, None, None))
one = TreeNode(1, two, three)

print(postorder(one))

# 2 False
# 3 False
# 1 True

# 4 False
# 2 True
# 3 False
# 1 True

# 4 True
# 2 True
# 3 False
# 1 True

# 3 False
# 1 True

# 5 False
# 3 True
# 1 True

# 5 True
# 3 True
# 1 True

# [4, 2, 5, 3, 1]
