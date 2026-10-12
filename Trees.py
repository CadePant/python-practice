class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
def bst_contains(root,value):
    current = root
    while current is not None:
        if current.value == value:
            return True
        elif value < current.value:
            current = current.left
        elif value > current.value:
            current = current.right
    return False
def bst_insert(root, value):
    current = root
    while current is not None:
        if value < current.value:          # going LEFT
            if current.left is None:
                current.left = TreeNode(value)  # attach to the empty left spot
                return
            else:
                current = current.left          # move left
        else:                               # going RIGHT
            if current.right is None:
                current.right = TreeNode(value)  # attach to the empty right spot
                return
            else:
                current = current.right          # move right
a = TreeNode(50)
b = TreeNode(30)
c = TreeNode(70)
d = TreeNode(20)
e = TreeNode(40)
f = TreeNode(80)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
print(a.left.right.value)
print(a.right.right.value)
print(bst_contains(a, 40))   # True
print(bst_contains(a, 80))   # True
print(bst_contains(a, 65))   # False
bst_insert(a, 65)
print(a.right.left.value)      # 65
print(bst_contains(a, 65))     # True