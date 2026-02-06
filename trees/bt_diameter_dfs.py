class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class TreeTraversal:
   
    def diameter(self, root: TreeNode):
        if not root:
            return 0
        
        diameter = 0        
        heights = {None: 0}        
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            
            if not node:
                continue
                
            if visited:
                left_h = heights[node.left]
                right_h = heights[node.right]
            
                diameter = max(diameter, left_h + right_h)
                heights[node] = 1 + max(left_h, right_h)
            
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        
        return diameter     


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
    h = TreeNode('H')
    d = TreeNode('D', h)
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

print(f"Pre-order (Root→Left→Right):  {traversal.diameter(root)}")
