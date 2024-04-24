from _collections import deque

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.it_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return '[' + ', '.join(str(item) for item in self.items[::-1]) + ']'


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def deque(self):
        if not self.is_empty():
            return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return '['+', '.join(str(item) for item in self.items) + ']'



if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print("Stack:", stack)

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue:", queue)
