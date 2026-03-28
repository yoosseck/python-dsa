# 10 --> 5 --> 16

# my_linked_list = {
#     'head': {
#         'value': 10,
#         'next': {
#             'value': 5,
#             'next': {
#                 'value': 16,
#                 'next': None
#             }
#         }
#     }
# }

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = self.head
        self.length = 1

    def append(self, value):
        node = Node(value)
        # append the new node to the current tail
        self.tail.next = node
        # render the new node a new tail
        self.tail = node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        # append the current head to the new node
        node.next = self.head
        # render the new node a new head
        self.head = node
        self.length += 1

    def print_list(self):
        array = []

        current = self.head

        while current:
            array.append(current.value)
            current = current.next

        print(f'length: {self.length}, list: {array}')

    def insert(self, index, value):
        # 10 --> 5 --> 16
        if index > self.length - 1:
            raise Exception(
                'The index must not be bigger than the size of a linked list.'
                )

        # get a leader node with a pointer right before the given index
        leader = self._traverse_to_index(index - 1)
        # save a node right next to the current leader node
        pointer = leader.next
        new_node = Node(value)
        # append a new node to the leader node
        leader.next = new_node
        # append a pointer to the new node
        # keep the chain even after adding a new node
        new_node.next = pointer
        self.length += 1

        self.print_list()

    def remove(self, index):
        # get a leader node with a pointer right before the given index
        leader = self._traverse_to_index(index - 1)
        # pick up and save a node right next to the leader node
        deleted = leader.next
        # append a node right next to a deleted node
        # keep the chain after deleting a node inside of a linked list
        leader.next = deleted.next
        self.length -= 1

        self.print_list()

    def _traverse_to_index(self, index):

        # stop the execution when a given index is bigger than the size
        if index > self.length - 1:
            raise Exception(
                'The index must not be bigger than the size of a linked list.'
                )
        counter = 0
        current = self.head
        # we trail down the list until we find a node at a given index
        while counter != index:
            current = current.next
            counter += 1

        # after we find
        return current


my_linked_list = SinglyLinkedList(10)
my_linked_list.append(5)
my_linked_list.prepend(16)
my_linked_list.print_list()
my_linked_list.insert(2, 100)
my_linked_list.insert(2, 300)
my_linked_list.remove(3)
my_linked_list.remove(1)
