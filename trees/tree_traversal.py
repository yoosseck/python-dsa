class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class TreeTraversal:
    # ============ RECURSIVE IMPLEMENTATIONS ============
    def preorder_recursive(self, root: TreeNode):
        """
        Order:
            Root -> Left - Right
        Usage:
            copy
            prefix expression generation
        """
        result = []

        def traverse(node: TreeNode):
            if node:
                result.append(node.data)
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return result

    def inorder_recursive(self, root: TreeNode):
        """
        Order:
            Left -> Root - Right
        Usage:
            Binary Search Trees - places nodes in sorted order
            infix expression generation
        """
        result = []

        def traverse(node: TreeNode):
            if node:
                traverse(node.left)
                result.append(node.data)
                traverse(node.right)

        traverse(root)
        return result

    def postorder_recursive(self, root: TreeNode):
        """
        Order:
            Left -> Right -> Root
        Usage:
            delete
            calculate directory sizes
            generate postfix expressions
        """
        result = []

        def traverse(node: TreeNode):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.data)

        traverse(root)
        return result

    # ============ ITERATIVE IMPLEMENTATIONS ============
    def preorder_iterative(self, root: TreeNode):
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.data)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def inorder_iterative(self, root: TreeNode):

        result = []
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.data)

            current = current.right

        return result

    def postorder_iterative(self, root: TreeNode):
        if not root:
            return []

        result = []
        stack1 = [root]
        stack2 = []

        # if stack1:
        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            result.append(node.data)

        return result

    # ============ LEVEL ORDER TRAVERSAL ============
    def level_order(self, root: TreeNode):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def level_order_2d(self, root: TreeNode):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result


def print_tree_structure(root, level=0, prefix="Root:"):
    if root:
        print(" " * (level * 4) + prefix + str(root.data))
        if root.left or root.right:
            if root.left:
                print_tree_structure(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree_structure(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


def build_sample_tree():
    """
    Build sample tree:
            A(1)
            /    \\
        B(2)    C(3)
        /  \\    /  \\
    D(4) E(5) F(6) G(7)
    /
    H(8)
    """
    h = TreeNode(8)
    d = TreeNode(4, h, None)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    b = TreeNode(2, d, e)
    c = TreeNode(3, f, g)
    a = TreeNode(1, b, c)
    return a


root = build_sample_tree()
traversal = TreeTraversal()

print("🌳 TREE STRUCTURE:")
print_tree_structure(root)
print("\n" + "="*50)

# Demonstrate all traversals
print("\nRECURSIVE TRAVERSALS:")
print(f"Pre-order (Root→Left→Right):  {traversal.preorder_recursive(root)}")
print(f"In-order (Left→Root→Right):   {traversal.inorder_recursive(root)}")
print(f"Post-order (Left→Right→Root): {traversal.postorder_recursive(root)}")

print("\nITERATIVE TRAVERSALS:")
print(f"Pre-order iterative:  {traversal.preorder_iterative(root)}")
print(f"In-order iterative:   {traversal.inorder_iterative(root)}")
print(f"Post-order iterative: {traversal.postorder_iterative(root)}")

print("\nLEVEL ORDER TRAVERSALS:")
print(f"Level-order (BFS):     {traversal.level_order(root)}")
print(f"Level-order (2D):      {traversal.level_order_2d(root)}")

# Verify recursive vs iterative consistency
print("\nVERIFICATION:")
print(f"Pre-order match:  {traversal.preorder_recursive(root) == traversal.preorder_iterative(root)}")
print(f"In-order match:   {traversal.inorder_recursive(root) == traversal.inorder_iterative(root)}")
print(f"Post-order match: {traversal.postorder_recursive(root) == traversal.postorder_iterative(root)}")
