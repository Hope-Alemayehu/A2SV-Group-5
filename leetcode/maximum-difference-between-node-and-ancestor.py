# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root):
        return self._maxAncestorDiff(root, root.val, root.val)

    def _maxAncestorDiff(self, root, mini, maxi):
        if not root:
            return 0
        mini = min(mini, root.val)
        maxi = max(maxi, root.val)
        l = self._maxAncestorDiff(root.left, mini, maxi)
        r = self._maxAncestorDiff(root.right, mini, maxi)
        return max(maxi - mini, l, r)