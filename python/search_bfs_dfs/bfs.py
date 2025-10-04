from json import dumps


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return self
        currentNode = self.root
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = newNode
                    return self
                currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = newNode
                    return self
                currentNode = currentNode.right

    def lookup(self, value):
        currentNode = self.root
        while currentNode:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return currentNode
        return None

    def remove(self, value):
        if self.root is None:
            return False

        currentNode = self.root
        parentNode = None

        while currentNode:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # --- Case 1: no right child
                if currentNode.right is None:
                    if parentNode is None:
                        self.root = currentNode.left
                    elif currentNode.value < parentNode.value:
                        parentNode.left = currentNode.left
                    else:
                        parentNode.right = currentNode.left

                # --- Case 2: right child with no left child
                elif currentNode.right.left is None:
                    currentNode.right.left = currentNode.left
                    if parentNode is None:
                        self.root = currentNode.right
                    elif currentNode.value < parentNode.value:
                        parentNode.left = currentNode.right
                    else:
                        parentNode.right = currentNode.right

                # --- Case 3: right child with a left child
                else:
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right
                    while leftmost.left:
                        leftmostParent = leftmost
                        leftmost = leftmost.left

                    # rewire
                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right

                    if parentNode is None:
                        self.root = leftmost
                    elif currentNode.value < parentNode.value:
                        parentNode.left = leftmost
                    else:
                        parentNode.right = leftmost
                return True
        return False

    def breadth_first_search(self):
        current_node = self.root
        items = []
        queue = [current_node]

        while len(queue) > 0:
            current_node = queue.pop(0)
            items.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return items

    def breadth_first_search_recursive(self, queue, list):
        if len(queue) == 0:
            return list

        current_node = queue.pop(0)
        list.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

        return self.breadth_first_search_recursive(queue, list)


def traverse(node):
    if node is None:
        return None
    return {
        'value': node.value,
        'left': traverse(node.left),
        'right': traverse(node.right)
    }


# Example usage
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

tree.remove(170)

print("BFS:", tree.breadth_first_search())
print("BFS recursive:", tree.breadth_first_search_recursive([tree.root], []))
print("Lookup 20:", tree.lookup(20).value if tree.lookup(20) else None)
print("Tree JSON:", dumps(traverse(tree.root), indent=2))
