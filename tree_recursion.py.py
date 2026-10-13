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

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right) 

def count_nodes(node):
    if node is None:
        return 0
    return count_nodes(node.left) + count_nodes(node.right) + 1

def sum_tree(node):
    if node is None:
        return 0
    return sum_tree(node.left) + sum_tree(node.right) + node.value

print(count_nodes(root))       # 5
print(count_nodes(root.left))  # 3
print(count_nodes(None))       # 0
print(sum_tree(root))       # 210
print(sum_tree(root.left))  # 90
print(sum_tree(None))       # 0
print(count_leaves(root))       # 3  (20, 40, 70)
print(count_leaves(root.left))  # 2
print(count_leaves(None))       # 0