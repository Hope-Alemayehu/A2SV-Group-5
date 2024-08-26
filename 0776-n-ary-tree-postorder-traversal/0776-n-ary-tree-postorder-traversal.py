"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []

        def postorder(root):
            if not root:
                return
            
            for child in root.children:
                postorder(child)
            output.append(root.val)
        postorder(root)
        return output