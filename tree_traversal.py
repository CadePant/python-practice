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

print("Inorder:")
inorder(root)
print("Preorder:")
preorder(root)
print("Postorder:")
postorder(root)