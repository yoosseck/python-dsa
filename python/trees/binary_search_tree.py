import json


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    #      9
    #   4     20
    # 1  6  15  170

    def insert(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            return

        current = self.root

        while True:
            if current.value > value:
                if current.left is None:
                    current.left = node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                current = current.right

        # current = self.root

        # if current.left is None

        # while current.left is not None and current.right is not None:
        #     if current.value < value:
        #         current = current.left
        #     else:
        #         current = current.right

        # current = node

    def lookup(self, value):

        if not self.root:
            return False

        current = self.root

        while current:
            if current.value > value:
                current = current.left
            elif current.value < value:
                current = current.right
            elif current.value == value:
                return True

        return False

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            # case 1: no child
            if not node.left and not node.right:
                return None
            # case 2: one child
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            # case 3: two children
            else:
                successor = self._min_value_node(node.right)
                node.value = successor.value
                node.right = self._remove(node.right, successor.value)

        return node

    def _min_value_node(self, node):
        # Helper: find smallest node in a subtree
        current = node
        while current.left:
            current = current.left
        return current

    def traverse(self, node):
        if node is None:
            return None

        tree = {"value": node.value}
        tree["left"] = self.traverse(node.left) if node.left else None
        tree["right"] = self.traverse(node.right) if node.right else None
        return tree


tree = BinarySearchTree()
print(tree.lookup(0))
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# tree.remove(170)
json_str = json.dumps(tree.traverse(tree.root))
print(json_str)
# print(tree.lookup(20))
# print(tree.lookup(100))

print(tree.remove(6))


json_str = json.dumps(tree.traverse(tree.root))
print(json_str)


#      9
#   4     20
# 1  6  15  170
