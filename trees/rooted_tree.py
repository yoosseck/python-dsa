import string
from tree_node import TreeNode


class RootedTree:

    def __init__(self, root_data: TreeNode):
        self.root = TreeNode(root_data)

    def find_node(self, data):
        return self._find_node_recursive(self.root, data)

    def _find_node_recursive(self, current: TreeNode, data: TreeNode):
        if current.data == data:
            return current

        for child in current.children:
            result = self._find_node_recursive(child, data)

            if result:
                return result

        return

    def add_node(self, parent_data: TreeNode, child_data: TreeNode):
        parent_node = self.find_node(parent_data)
        if parent_node:
            new_child = TreeNode(child_data)
            parent_node.add_child(new_child)
            return True
        return False

    def get_height(self):
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, node: TreeNode):
        if node.is_leaf():
            return 0

        max_child_height = 0
        for child in node.children:
            child_height = self._get_height_recursive(child)
            max_child_height = max(max_child_height, child_height)

        return 1 + max_child_height

    def get_depth(self, data: TreeNode):
        node = self.find_node(data)
        if not node:
            return -1

        depth = 0
        current = node
        while current.parent:
            depth += 1
            current = current.parent

        return depth

    def get_leaves(self):
        leaves = []
        self._collect_leaves(self.root, leaves)
        return [leaf.data for leaf in leaves]

    def _collect_leaves(self, node: TreeNode, leaves: list[TreeNode]):

        if node.is_leaf():
            leaves.append(node)
        else:
            for child in node.children:
                self._collect_leaves(child, leaves)

    def print_tree(self):
        print("The whole tree structure:")
        self._print_tree_recursive(self.root, "", True)

    def _print_tree_recursive(self,
                              node: TreeNode,
                              prefix: string,
                              is_last: bool):

        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{node.data}")

        # Print children
        if node.children:
            for i, child in enumerate(node.children):
                is_last_child = (i == len(node.children) - 1)
                # Extend prefix for children
                child_prefix = prefix + ("    " if is_last else "│   ")
                self._print_tree_recursive(child, child_prefix, is_last_child)


company = RootedTree("CEO")

# Add department heads
company.add_node("CEO", "CTO")
company.add_node("CEO", "CFO")
company.add_node("CEO", "CMO")

# Add team members under CTO
company.add_node("CTO", "Dev Manager")
company.add_node("CTO", "QA Manager")
company.add_node("Dev Manager", "Frontend Dev")
company.add_node("Dev Manager", "Backend Dev")
company.add_node("QA Manager", "QA Engineer")

# Add team members under CFO
company.add_node("CFO", "Accountant")
company.add_node("CFO", "Financial Analyst")

# Display tree structure
company.print_tree()

print("\n=== TREE PROPERTIES ===")
print(f"Tree height: {company.get_height()}")
print(f"Depth of 'Frontend Dev': {company.get_depth('Frontend Dev')}")
print(f"Leaf nodes (employees): {company.get_leaves()}")
