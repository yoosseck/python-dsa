class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_min(node: TreeNode) -> TreeNode:
    """Helper to find the leftmost node in a subtree."""
    while node.left:
        node = node.left
    return node

def find_inorder_successor(root: TreeNode, target_val: int) -> TreeNode:
    """
    Finds the successor of a node with target_val.
    Trace the 'successor' variable in VS Code to see it 'remember' 
    the last left turn.
    """
    successor = None
    current = root
    
    while current:
        if target_val < current.val:
            # We are going left. This current node is a potential successor
            # because it is larger than our target.
            successor = current
            current = current.left
        elif target_val > current.val:
            # We are going right. This node is smaller than our target,
            # so it cannot be the successor.
            current = current.right
        else:
            # FOUND THE TARGET
            # If there's a right child, the successor is the min of that subtree
            if current.right:
                successor = get_min(current.right)
            break
            
    return successor

# --- TEST SETUP ---
if __name__ == "__main__":
    # Manually building the BST
    #         20
    #        /  \
    #       10   30
    #      /  \
    #     5   15
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.right = TreeNode(30)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(15)

    # Test Case 1: Node with a right child
    # Successor of 10 should be 15
    res1 = find_inorder_successor(root, 10)
    print(f"Successor of 10: {res1.val if res1 else 'None'}")

    # Test Case 2: Node without a right child
    # Successor of 15 should be 20
    res2 = find_inorder_successor(root, 15)
    print(f"Successor of 15: {res2.val if res2 else 'None'}")

    # Test Case 3: Largest node
    # Successor of 30 should be None
    res3 = find_inorder_successor(root, 30)
    print(f"Successor of 30: {res3.val if res3 else 'None'}")
    
    # Test Case 4:
    # Successor of 30 should be None
    res4 = find_inorder_successor(root, 20)
    print(f"Successor of 20: {res4.val if res4 else 'None'}")