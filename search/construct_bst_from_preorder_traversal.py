from collections import deque
import json

# Standard TreeNode definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode:
        self.idx = 0
        
        def helper(upper_bound):
            # Check constraints
            if self.idx == len(preorder) or preorder[self.idx] > upper_bound:
                return None
            
            # Root creation
            root_val = preorder[self.idx]
            root = TreeNode(root_val)
            self.idx += 1
            
            # Recursive construction
            root.left = helper(root_val)
            root.right = helper(upper_bound)
            
            return root
        
        return helper(float('inf'))

# --- Debugging Boilerplate ---

def tree_to_list(root):
    """Helper to visualize the tree output in the console"""
    if not root:
        return []
    res, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    # Clean up trailing None values for readability
    while res and res[-1] is None:
        res.pop()
    return res

if __name__ == "__main__":
    # Test Case 1
    preorder_input = [8, 5, 1, 7, 10, 12]
    
    sol = Solution()
    result_root = sol.bstFromPreorder(preorder_input)
    
    print(f"Input Preorder: {preorder_input}")
    print(f"Resulting Tree (Level Order): {tree_to_list(result_root)}")