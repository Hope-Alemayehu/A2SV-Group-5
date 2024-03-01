# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(left,right):
            #base case
            if left > right:
                return None
            mid = (left+right)//2
            #creating the node
            root = TreeNode(nums[mid])

            #building the left part
            root.left = build(left, mid -1)
            #building the right part
            root.right = build(mid + 1,right)
            return root
            
        return build(0,len(nums)-1)