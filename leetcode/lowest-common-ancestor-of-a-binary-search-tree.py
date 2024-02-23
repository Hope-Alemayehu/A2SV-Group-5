# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # path1 = []
        # path2 = []
        # def search(root, v ,paths):
        #     if root.val == v:
        #         return root.val
        #     if root.val > v:
        #         paths.extend(return search(root.left , v ,paths))
        #     elif root.val < v:
        #         paths.extend(return search(root.right,v ,paths)) 
        # search(root, p, path1)
        # search(root, p, path2)

        # # path1 = set(path1)
        # # path2 = set(path2)

        # maxLen = max(len(path1), len(path2))
        # if 
        # for i in range (maxlen - 1 , )
        
        # time compelxity O(N) n being the number of nodes
        #space complexity O(d) d is the depth of recursive calls

        def search (root,p,q):
            if (root.val > p.val) and (root.val > q.val):
                return search(root.left,p,q)
            if (root.val < p.val) and (root.val < q.val):
                return search(root.right,p,q)
            else:
                return root
        return search(root,p,q)
