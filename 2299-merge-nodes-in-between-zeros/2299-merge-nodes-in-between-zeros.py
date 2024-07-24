# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        right = head.next
        summ = 0

        while right:
            if right.val == 0:
                left = left.next
                left.val = summ
                summ = 0
            else:
                summ += right.val
            
            right = right.next
        
        left.next = None
        return head.next