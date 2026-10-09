class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
def print_all(current):
        while current is not None:
            print(current.value)
            current = current.next

class LinkedList:
    def __init__(self):
        self.head = None
    def add_to_front(self,value):
        new_box = Node(value)
        new_box.next = self.head
        self.head = new_box
    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
    def count(self):
        total = 0
        current = self.head
        while current is not None:
            total += 1
            current = current.next
        return total

rooms = LinkedList()
rooms.add_to_front(315)
rooms.add_to_front(204)
rooms.add_to_front(101)
print_all(rooms.head)
print(rooms.contains(204))   # True
print(rooms.contains(500))   # False
print(rooms.count())   # 3