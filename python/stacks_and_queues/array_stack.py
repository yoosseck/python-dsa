class Stack:
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[len(self.array)-1]

    def push(self, value):
        self.array.append(value)

    def pop(self):
        self.array.pop()


my_stack = Stack()
my_stack.push("google")
print(my_stack.peek())
my_stack.push("youtube")
print(my_stack.peek())
my_stack.push("facebook")
print(my_stack.peek())

my_stack.pop()
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
