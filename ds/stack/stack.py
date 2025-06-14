class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("cannot peek from empty stack")

    def size(self):
        return len(self.items)


stack = Stack()

for i in range(10):
    stack.push(i)

for i in range(10):
    print("Pop from stack:", i, stack.pop())
