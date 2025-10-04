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
                if not currentNode.left:
                    currentNode.left = newNode
                    return self
                currentNode = currentNode.left
            else:
                if not currentNode.right:
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
        if not self.root:
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
                # Option 1: No right child
                if currentNode.right is None:
                    if parentNode is None:
                        self.root = currentNode.left
                    elif currentNode.value < parentNode.value:
                        parentNode.left = currentNode.left
                    else:
                        parentNode.right = currentNode.left

                # Option 2: Right child has no left child
                elif currentNode.right.left is None:
                    currentNode.right.left = currentNode.left
                    if parentNode is None:
                        self.root = currentNode.right
                    elif currentNode.value < parentNode.value:
                        parentNode.left = currentNode.right
                    else:
                        parentNode.right = currentNode.right

                # Option 3: Right child has a left child
                else:
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right
                    while leftmost.left:
                        leftmostParent = leftmost
                        leftmost = leftmost.left
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
        currentNode = self.root
        result = []
        queue = [currentNode]

        while len(queue) > 0:
            currentNode = queue.pop(0)
            result.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return result

    def breadth_first_search_recursive(self, queue, result):
        if len(queue) == 0:
            return result

        currentNode = queue.pop(0)
        result.append(currentNode.value)

        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

        return self.breadth_first_search_recursive(queue, result)

    def dfs_in_order(self):
        return self.traverse_in_order(self.root, [])

    def dfs_post_order(self):
        return self.traverse_post_order(self.root, [])

    def dfs_pre_order(self):
        return self.traverse_pre_order(self.root, [])

    def traverse_in_order(self, node, result):
        if node.left:
            self.traverse_in_order(node.left, result)
        result.append(node.value)
        if node.right:
            self.traverse_in_order(node.right, result)
        return result

    def traverse_pre_order(self, node, result):
        result.append(node.value)
        if node.left:
            self.traverse_pre_order(node.left, result)
        if node.right:
            self.traverse_pre_order(node.right, result)
        return result

    def traverse_post_order(self, node, result):
        if node.left:
            self.traverse_post_order(node.left, result)
        if node.right:
            self.traverse_post_order(node.right, result)
        result.append(node.value)
        return result


def traverse(node):
    if node is None:
        return None
    return {
        'value': node.value,
        'left': traverse(node.left),
        'right': traverse(node.right)
    }


# Example Tree:
#      9
#   4     20
# 1  6  15  170

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

print("BFS:", tree.breadth_first_search())
print("BFS Recursive:", tree.breadth_first_search_recursive([tree.root], []))
print("DFS In Order:", tree.dfs_in_order())
print("DFS Pre Order:", tree.dfs_pre_order())
print("DFS Post Order:", tree.dfs_post_order())
