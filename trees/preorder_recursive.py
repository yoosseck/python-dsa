class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class TreeTraversal:
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


    def preorder_recursive_simple(self, root: TreeNode):
        if not root:
            return []
        
        return [root.data] + self.preorder_recursive_simple(root.left) + self.preorder_recursive_simple(root.right)


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
    d = TreeNode('D')
    e = TreeNode('E')
    f = TreeNode('F')
    g = TreeNode('G')
    b = TreeNode('B', d, e)
    c = TreeNode('C', f, g)
    a = TreeNode('A', b, c)
    return a


root = build_sample_tree()
traversal = TreeTraversal()

print("🌳 TREE STRUCTURE:")
print_tree_structure(root)
print("\n" + "="*50)

# Demonstrate all traversals
print("\nRECURSIVE TRAVERSALS:")
print(f"Pre-order (Root→Left→Right):  {traversal.preorder_recursive(root)}")
