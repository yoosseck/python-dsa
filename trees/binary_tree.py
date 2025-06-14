from random import randint


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, data):

        new_node = TreeNode(data)

        if self.root is None:
            self.root = new_node
            print(f"  → {data} set as root")
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                return
            elif current.right is None:
                current.right = new_node
                return

            else:
                queue.append(current.left)
                queue.append(current.right)

    def search(self, target):
        return self._search_recursive(self.root, target)

    def _search_recursive(self, node: TreeNode, target: TreeNode):
        if node is None:
            return False

        if node.data == target:
            return True

        return (self._search_recursive(node.left, target) or
                self._search_recursive(node.right, target))

    def find_height(self):
        """Public method to get tree height without debug output"""
        if self.root is None:
            return -1
        return self._height_helper(self.root)

    def _height_helper(self, node):
        if node is None:
            return -1
        left_height = self._height_helper(node.left)
        right_height = self._height_helper(node.right)
        return 1 + max(left_height, right_height)

    def count_nodes(self):
        """Public method to count all nodes in the tree"""
        return self._count_nodes_helper(self.root)

    def _count_nodes_helper(self, node):
        """Helper method for counting nodes recursively"""
        if node is None:
            return 0
        return (1 +
                self._count_nodes_helper(node.left)
                + self._count_nodes_helper(node.right))

    def display_tree(self):

        if self.root is None:
            print("Empty Tree")
            return

        print("Tree structure: ")
        levels = []
        queue = [(self.root, 0)]

        while queue:
            node, level = queue.pop(0)

            if len(levels) <= level:
                levels.append([])

            levels[level].append(str(node.data))

            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))

        for i, level in enumerate(levels):
            print(f"level {i}: {' '.join(level)}")


binary_tree = BinaryTree()


# Insert some values
values = []

for i in range(10):
    values.append(randint(0, 100))

print(f'values: {values}')

for value in values:
    binary_tree.insert(value)

print(f'bt: {binary_tree}')

print("\n--- Tree Structure ---")
binary_tree.display_tree()

print(binary_tree.find_height())
print(binary_tree.count_nodes())

print("\n--- Search Operations ---")
search_values = [5, 8, 1]
for val in search_values:
    found = binary_tree.search(val)
    print(f"Search for {val}: {'Found' if found else 'Not found'}")
