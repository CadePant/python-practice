from collections import deque
class Queue:
    def __init__(self):
        self.line = deque()
    def enqueue(self, item):
        self.line.append(item)
    def dequeue(self):
        try:
            return self.line.popleft()
        except IndexError:
            return None

q = Queue()
choice = 0
while choice != 3:
    print('1. Guest arrives')
    print('2. Serve next guest')
    print('3. Exit')
    try:
        choice = int(input('What can we assist you with today?'))
    except ValueError:
        print('Please enter a number.')
    else:
        if choice == 1:
            guest_name = input('What is the guests name? ')
            q.enqueue(guest_name)
        elif choice == 2:
            Next = q.dequeue()
            if Next:
                print('Now serving:' ,Next)
            elif Next == None:
                print('No guests waiting.')
        elif choice == 3:
            print('Goodbye')
        else:
            print('Invalid option')