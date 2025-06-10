class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("cannot peek from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("cannot peek from empty queue")

    def size(self):
        return len(self.items)


# if __name__ == "__main__":
#     queue = Queue()

#     for i in range(7, 17):
#         queue.enqueue(i)

#     for i in range(10):
#         print('dequeue: ', i, queue.dequeue())
