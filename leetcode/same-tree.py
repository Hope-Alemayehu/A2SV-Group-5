# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #time complexity O(N + M) we are traversing n nodes of tree p and m nodes of tree q
        #space complexity the call stack O(D) d being the depth
        def check(p,q):
            if p and q:
                return ((p.val == q.val) and (check(p.left,q.left)) and 
                    check(p.right,q.right))
            else:
                return p == q
        return check(p,q)