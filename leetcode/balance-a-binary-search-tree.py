# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if not root:
            return 
        self.inorder(root.left)
        self.inorderList.append(root)
        self.inorder(root.right)

        return
    
    def BST(self,low,high):
        if low > high:
            return None
        mid = low + high >> 1
        node = self.inorderList[mid]
        node.left = self.BST(low, mid - 1)
        node.right = self.BST(mid+1, high)
        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inorderList = []
        self.inorder(root)
        return self.BST(0,len(self.inorderList)-1)
        