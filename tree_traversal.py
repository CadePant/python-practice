from collections import deque
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value)
    inorder(node.right)
def preorder(node):
    if node is None:
        return
    print(node.value)
    preorder(node.left)
    preorder(node.right)
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value)
def level_order(root):
    if root is None:
        return []
    queue = deque([root])
    result = []
    while len(queue) != 0:
        node = queue.popleft()
        result.append(node.value)
        if node.left is not None:
           queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result
def bst_min(node):
    if node is None:
        return None
    if node.left is None:
        return node.value
    return bst_min(node.left)
print("Inorder:")
inorder(root)
print("Preorder:")
preorder(root)
print("Postorder:")
postorder(root)
print(level_order(root))   # expected: [8, 3, 10, 1, 6, 14]
print(level_order(None))   # expected: []
print(bst_min(root))    # expected: 20
print(bst_min(None))    # expected: None