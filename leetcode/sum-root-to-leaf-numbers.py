# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root, path):
            nonlocal res
            if root is None:
                return
            path.append(str(root.val))
            if not root.left and not root.right:
                res += int("".join(path))
                return 
            dfs(root.left, path.copy())
            dfs(root.right, path.copy())
            path.pop()

        dfs(root, [])
        return res
