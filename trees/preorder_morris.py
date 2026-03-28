class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class TreeTraversal:
   
    def preorder_iterative(self, root: TreeNode):
        """
        Order:
            Root -> Left - Right
        Usage:
            copy
            prefix expression generation
        """
        if not root:
            return []

        result = []
        curr = root
        
        while curr:
            if curr.left is None:
                result.append(curr.data)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right is not curr:
                    pre = pre.right
                    
                if pre.right is None:
                    result.append(curr.data)
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    curr = curr.right

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

print(f"Pre-order (Root→Left→Right):  {traversal.preorder_iterative(root)}")
