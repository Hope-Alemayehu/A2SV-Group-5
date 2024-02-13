# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = None

        leftprev , cur = dummy,head
        #getting to the left node
        for i in range(left - 1):
            leftprev = leftprev.next
            cur = cur.next
        
        #reversing the reqired node
        for i in range(right - left + 1):
            tmpnext = cur.next
            cur.next = prev
            prev = cur 
            cur = tmpnext
        
        #connecting the with right places
        leftprev.next.next = cur
        leftprev.next = prev
        return dummy.next