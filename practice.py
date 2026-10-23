class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(5)
head.next = Node(10)
head.next.next = Node(15)

def contains(head, target):
    current = head
    while current is not None:
        if current.value == target:
            return True
        current = current.next
    return False

print(contains(head, 15))  # expected: True
print(contains(head, 99))  # expected: False