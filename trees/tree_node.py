class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def is_leaf(self):
        return len(self.children) == 0

    def is_root(self):
        return self.parent is None
