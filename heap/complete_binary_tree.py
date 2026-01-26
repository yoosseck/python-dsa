class TreeNode:
    """Node class for the binary tree."""
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class CompleteBinaryTree:
    """Complete Binary Tree implementation using array-based approach."""

    def __init__(self):
        self.tree = []  # Array to store tree nodes

    def insert(self, val):
        """
        Insert a value maintaining complete binary tree property.
        Time Complexity: O(1)
        """
        self.tree.append(val)
        print(f"Inserted {val} at index {len(self.tree)-1}")

    def delete_last(self):
        """
        Delete the last inserted node (rightmost node in last level).
        Time Complexity: O(1)
        """
        if not self.tree:
            print("Tree is empty")
            return None

        deleted_val = self.tree.pop()
        print(f"Deleted {deleted_val}")
        return deleted_val

    def get_parent_index(self, i):
        """Get parent index for node at index i."""
        if i == 0:
            return None
        return (i - 1) // 2

    def get_left_child_index(self, i):
        """Get left child index for node at index i."""
        left_idx = 2 * i + 1
        return left_idx if left_idx < len(self.tree) else None

    def get_right_child_index(self, i):
        """Get right child index for node at index i."""
        right_idx = 2 * i + 2
        return right_idx if right_idx < len(self.tree) else None

    def get_parent(self, i):
        """Get parent value for node at index i."""
        parent_idx = self.get_parent_index(i)
        return self.tree[parent_idx] if parent_idx is not None else None

    def get_left_child(self, i):
        """Get left child value for node at index i."""
        left_idx = self.get_left_child_index(i)
        return self.tree[left_idx] if left_idx is not None else None

    def get_right_child(self, i):
        """Get right child value for node at index i."""
        right_idx = self.get_right_child_index(i)
        return self.tree[right_idx] if right_idx is not None else None

    def level_order_traversal(self):
        """
        Traverse tree level by level (breadth-first).
        Time Complexity: O(n)
        """
        if not self.tree:
            return []

        result = []
        for val in self.tree:
            result.append(val)
        return result

    def inorder_traversal(self, i=0):
        """
        Inorder traversal: Left -> Root -> Right
        Time Complexity: O(n)
        """
        if i >= len(self.tree):
            return []

        result = []

        # Left subtree
        left_idx = self.get_left_child_index(i)
        if left_idx is not None:
            result.extend(self.inorder_traversal(left_idx))

        # Root
        result.append(self.tree[i])

        # Right subtree
        right_idx = self.get_right_child_index(i)
        if right_idx is not None:
            result.extend(self.inorder_traversal(right_idx))

        return result

    def preorder_traversal(self, i=0):
        """
        Preorder traversal: Root -> Left -> Right
        Time Complexity: O(n)
        """
        if i >= len(self.tree):
            return []

        result = []

        # Root
        result.append(self.tree[i])

        # Left subtree
        left_idx = self.get_left_child_index(i)
        if left_idx is not None:
            result.extend(self.preorder_traversal(left_idx))

        # Right subtree
        right_idx = self.get_right_child_index(i)
        if right_idx is not None:
            result.extend(self.preorder_traversal(right_idx))

        return result

    def postorder_traversal(self, i=0):
        """
        Postorder traversal: Left -> Right -> Root
        Time Complexity: O(n)
        """
        if i >= len(self.tree):
            return []

        result = []

        # Left subtree
        left_idx = self.get_left_child_index(i)
        if left_idx is not None:
            result.extend(self.postorder_traversal(left_idx))

        # Right subtree
        right_idx = self.get_right_child_index(i)
        if right_idx is not None:
            result.extend(self.postorder_traversal(right_idx))

    # Root
        result.append(self.tree[i])

        return result

    def get_height(self):
        """
        Calculate height of the tree.
        Height = number of edges in longest path from root to leaf.
        """
        if not self.tree:
            return -1

        import math
        return math.floor(math.log2(len(self.tree)))

    def get_max_nodes_at_level(self, level):
        """Get maximum possible nodes at a given level."""
        return 2 ** level

    def is_complete(self):
        """
        Check if the tree is complete.
        In array representation, a complete tree has no gaps.
        """
        return len(self.tree) > 0  # Array representation ensures completeness

    def _display_simple_tree(self):
        """Display a simple ASCII tree representation."""
        if not self.tree:
            return

        def print_tree_recursive(i, level=0, prefix="Root: "):
            if i >= len(self.tree):
                return

            print(" " * (level * 4) + prefix + str(self.tree[i]))

            left_idx = self.get_left_child_index(i)
            right_idx = self.get_right_child_index(i)
            if left_idx is not None:
                print_tree_recursive(left_idx, level + 1, "L--- ")
            if right_idx is not None:
                print_tree_recursive(right_idx, level + 1, "R--- ")

        print_tree_recursive(0)

    def display_tree_structure(self):
        """Display tree structure level by level with better formatting."""
        if not self.tree:
            print("Tree is empty")
            return

        print("\nTree Structure:")
        print("=" * 50)

        height = self.get_height()
        if height < 0:
            print("Tree is empty")
            return

        level = 0
        i = 0

        while i < len(self.tree):
            level_size = min(2 ** level, len(self.tree) - i)
            level_nodes = self.tree[i:i + level_size]

            # Calculate spacing for visual alignment
            spaces_before = " " * (2 ** (height - level) - 1)
            spaces_between = " " * (2 ** (height - level + 1) - 1)

            print(f"Level {level}: {spaces_before}", end="")
            for j, node in enumerate(level_nodes):
                print(f"{node:2d}", end="")
                if j < len(level_nodes) - 1:
                    print(spaces_between, end="")
            print()

            i += level_size
            level += 1

        # Also display a simpler tree view
        print("\nSimple Tree View:")
        print("-" * 30)
        self._display_simple_tree()

    def display_array_representation(self):
        """Display the array representation with indices."""
        if not self.tree:
            print("Tree is empty")
            return

        print("\nArray Representation:")
        print("=" * 50)
        print("Index: ", end="")
        for i in range(len(self.tree)):
            print(f"{i:2d} ", end="")
        print()

        print("Value: ", end="")
        for val in self.tree:
            print(f"{val:2d} ", end="")
        print()

        print("\nParent-Child Relationships:")
        for i in range(len(self.tree)):
            parent = self.get_parent(i)
            left = self.get_left_child(i)
            right = self.get_right_child(i)

            print(f"Node {self.tree[i]} (idx {i}): ", end="")
            if parent is not None:
                print(f"parent={parent}, ", end="")
            if left is not None:
                print(f"left={left}, ", end="")
            if right is not None:
                print(f"right={right}", end="")
            print()


# Demonstration
print("Complete Binary Tree Implementation Demo")
print("=" * 60)

# Create and populate tree
cbt = CompleteBinaryTree()

print("\n1. Inserting nodes: 1, 2, 3, 4, 5, 6, 7")
for val in [1, 2, 3, 4, 5, 6, 7]:
    cbt.insert(val)

# Display tree structure
cbt.display_tree_structure()
cbt.display_array_representation()

print(f"\nTree height: {cbt.get_height()}")
print(f"Is complete: {cbt.is_complete()}")

print("\n2. Tree Traversals:")
print(f"Level-order: {cbt.level_order_traversal()}")
print(f"Inorder:     {cbt.inorder_traversal()}")
print(f"Preorder:    {cbt.preorder_traversal()}")
print(f"Postorder:   {cbt.postorder_traversal()}")

print("\n3. Adding more nodes: 8, 9")
cbt.insert(8)
cbt.insert(9)

cbt.display_tree_structure()
print(f"Updated level-order: {cbt.level_order_traversal()}")

print("\n4. Deleting last node:")
cbt.delete_last()
cbt.display_array_representation()

print("\n5. Node relationship examples:")
print(f"Node at index 0: value={cbt.tree[0]}, left={cbt.get_left_child(0)}, right={cbt.get_right_child(0)}")
print(f"Node at index 1: value={cbt.tree[1]}, parent={cbt.get_parent(1)}, left={cbt.get_left_child(1)}, right={cbt.get_right_child(1)}")
print(f"Node at index 4: value={cbt.tree[4]}, parent={cbt.get_parent(4)}")