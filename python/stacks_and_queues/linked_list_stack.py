class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return None if self.top is None else self.top.value

    def push(self, value):
        node = Node(value)

        if self.is_empty(self.top):
            self.top = node
            self.bottom = node
        else:
            pointer = self.top
            self.top = node
            self.top.next = pointer

        self.length += 1

        return self

    def pop(self):

        if self.is_empty(self.top):
            return None

        if self.top == self.bottom:
            self.bottom = None

        self.top = self.top.next
        self.length -= 1

        return self

    def is_empty(self, node):
        return node is None


my_stack = Stack()
print(my_stack.push("google"))
print(my_stack.peek())
print(my_stack.push("youtube"))
print(my_stack.peek())
print(my_stack.push("facebook"))
print(my_stack.peek())

print(my_stack.pop())
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.peek())
