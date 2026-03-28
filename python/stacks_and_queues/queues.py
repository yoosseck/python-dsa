class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return None if self.first is None else self.first.value

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = self.last.next

        self.length += 1

    def dequeue(self):

        if not self.first:
            return None

        if self.first == self.last:
            self.last = None

        self.first = self.first.next
        self.length -= 1

# isEmpty


my_queue = Queue()

# Joy
# Matt
# Pavel
# Samir


my_queue.enqueue("Joy")
print(my_queue.peek())
my_queue.enqueue("Matt")
print(my_queue.peek())
my_queue.enqueue("Pavel")
print(my_queue.peek())
my_queue.enqueue("Samir")
print(my_queue.peek())

my_queue.dequeue()
print(my_queue.peek())
my_queue.dequeue()
print(my_queue.peek())
my_queue.dequeue()
print(my_queue.peek())
my_queue.dequeue()
print(my_queue.peek())
