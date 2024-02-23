# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def helper(leftie , righti):
            if not leftie and not righti:
                return True
            if not leftie or not righti:
                return False
            if leftie.val != righti.val:
                return False
            return (leftie.val == righti.val and 
               (helper(leftie.left,righti.right) )and
                (helper(leftie.right,righti.left)))

        return helper(root.left,root.right)