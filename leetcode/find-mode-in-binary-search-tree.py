
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Step 1: Perform inorder traversal
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        inorder_list = inorder(root)
        
        # Step 2: Count occurrences of each node
        counter = Counter(inorder_list)
        
        # Step 3: Find the node(s) with the maximum count
        max_count = max(counter.values())
        modes = [num for num, count in counter.items() if count == max_count]
        
        return modes