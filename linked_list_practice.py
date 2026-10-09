class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
def print_all(head):
        current = head
        while current is not None:
            print(current.value)
            current = current.next


class LinkedList:
    def __init__(self):
        self.head = None
    def add_to_front(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

rooms = LinkedList()
rooms.add_to_front(315)
rooms.add_to_front(204)
rooms.add_to_front(101)
print_all(rooms.head)