class PriorityQueue:
    def __init__(self):
        # Heap stores tuples: (priority, value)
        self.heap = []

    # -----------------------------
    # HELPER FUNCTIONS
    # -----------------------------

    def _parent(self, index):
        return (index - 1) // 2 if index > 0 else None

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # -----------------------------
    # CORE OPERATIONS
    # -----------------------------

    def push(self, priority, value):
        """
        Insert (priority, value) into queue.
        """
        self.heap.append((priority, value))
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty priority queue")

        self._swap(0, len(self.heap) - 1)
        min_item = self.heap.pop()
        self._heapify_down(0)
        return min_item

    def peek(self):
        if not self.heap:
            raise IndexError("peek from empty priority queue")
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    # -----------------------------
    # HEAPIFY OPERATIONS
    # -----------------------------

    def _heapify_up(self, index):
        parent = self._parent(index)
        while parent is not None and self.heap[index][0] < self.heap[parent][0]:
            self._swap(index, parent)
            index = parent
            parent = self._parent(index)

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            smallest = index

            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break


pq = PriorityQueue()

# (priority, value)
pq.push(3, "low priority task")
pq.push(1, "high priority task")
pq.push(2, "medium priority task")

print(pq.peek())   # (1, 'high priority task')
print(pq.pop())    # (1, 'high priority task')
print(pq.pop())    # (2, 'medium priority task')
print(pq.pop())    # (3, 'low priority task')
