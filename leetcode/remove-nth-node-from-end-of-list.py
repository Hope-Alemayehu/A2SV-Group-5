# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        ahead = ListNode(0,dummy)
        back = ListNode(0,dummy)

        #moving the ahead nth step
        for i in range(n):
            ahead = ahead.next
        
        #moving the back pointer with it
        while ahead and ahead.next:
            back = back.next
            ahead = ahead.next
        
        tmp = back.next.next
        back.next = tmp
        return dummy.next