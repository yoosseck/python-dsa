class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:

    # keep 2-way links between each of 2 nodes
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        # prepend the current tail to the new node
        new_node.prev = self.tail
        # append the new node to the current tail
        self.tail.next = new_node
        # render the new node a new tail
        self.tail = new_node
        self.length += 1

        self.print_list()

    def prepend(self, value):
        new_node = Node(value)
        # append the current head to the new node
        new_node.next = self.head
        # prepend the new node to the current head
        self.head.prev = new_node
        # render the new node a new head
        self.head = new_node
        self.length += 1

        self.print_list()

    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise Exception("Index out of bounds")

        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)

        # locate the pointer
        curr = self.traverse_index(index)   # node currently at index
        new_node = Node(value)

        # save a node (previous node) right before the pointer
        prev_node = curr.prev
        # prepend the previous node to the new node
        new_node.prev = prev_node
        # append the leader to the new node
        new_node.next = curr
        # append the new node to the previous node
        prev_node.next = new_node
        # prepend the new node to the pointer
        curr.prev = new_node

        self.length += 1

        self.print_list()

    def remove(self, index):

        if index > self.length - 1:
            raise Exception('A size of a given index is too large!')

        # locate the pointer
        pointer = self.traverse_index(index)
        deleted = pointer.value

        # connect the previous node (pointer.prev) and next node (pointer.next)
        # keep chain after dropping the pointer node

        if pointer.prev:   # not head
            # append the next node to the previous node
            pointer.prev.next = pointer.next
        else:  # head
            # render the next node a new head
            self.head = pointer.next  # removing head

        if pointer.next:   # not tail
            # prepend the previous node to the next node
            pointer.next.prev = pointer.prev
        else:  # tail
            # render the previous node a new tail
            self.tail = pointer.prev  # removing tail

        self.length -= 1
        self.print_list()

        return deleted

    def traverse_index(self, index):
        counter = 0
        current = self.head

        while counter != index:
            current = current.next
            counter += 1

        return current

    def reverse(self):

        if not self.head.next:
            return self.head

        first = self.head
        self.tail = self.head
        second = first.next

        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp

        self.head.next = None
        self.head = first

        self.print_list()

    # def reverse2(self):
    #     if self.length <= 1:
    #         return self.head

    #     current = self.head
    #     self.tail = current  # old head will become the new tail
    #     prev_node = None

    #     while current:
    #         prev_node = current
    #         current.prev, current.next = current.next, current.prev
    #         current = current.prev  # since we swapped,
    # "prev" is the next node to visit

    #     self.head = prev_node  # last processed node is the new head
    #     self.print_list()

    def print_list(self):
        array = []
        current = self.head

        while current:
            array.append(current.value)
            current = current.next

        print(f'length: {self.length}, list: {array}')


my_linked_list = DoublyLinkedList(1)
my_linked_list.append(3)
my_linked_list.append(5)
my_linked_list.append(10)
my_linked_list.prepend(9)
my_linked_list.prepend(30)
my_linked_list.insert(3, 30)
my_linked_list.remove(4)
my_linked_list.reverse()
