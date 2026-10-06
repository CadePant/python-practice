class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return None

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        empty = False
        if len(self.items) == 0:
            empty = True
        return empty


s = Stack()
s.push('A')
s.push('B')
print(s.peek())      # B
print(s.pop())       # B
print(s.is_empty())  # False
print(s.pop())       # A
print(s.is_empty())  # True
print(s.pop())       # None
print(s.peek())      # None