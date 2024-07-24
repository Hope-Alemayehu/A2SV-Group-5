# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        dummy = ListNode(0)
        move = dummy
        cur = head.next
        if not cur.next:
            return
        
        while cur and cur.next:
            summ = 0
            while cur and cur.val != 0:
                summ += cur.val
                cur = cur.next
            if summ != 0:
                move.next = ListNode(summ)
                move = move.next
            cur = cur.next
        return dummy.next
