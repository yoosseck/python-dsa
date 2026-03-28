import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = -math.inf
        
        def inorder(node):
            if not node:
                return True
            # Left
            if not inorder(node.left):
                return False
            # Process Node
            if node.val <= self.prev:
                return False
            self.prev = node.val
            # Right
            return inorder(node.right)
            
        return inorder(root)

# VS Code Debugging Entry Point
if __name__ == "__main__":
    # Manually creating root = [2,1,3]
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(f"Is valid BST: {Solution().isValidBST(root)}")
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(f"Is valid BST: {Solution().isValidBST(root2)}")