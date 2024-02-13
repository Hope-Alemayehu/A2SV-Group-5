# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        odd = dummy1
        even = dummy2
        
        cur = head
        flag = True
        if cur.val %2 == 0:
            flag = True
        else:
            flag = False
        i = 1
        while cur:
            if i % 2 == 0:
                even.next = ListNode(cur.val)
                even = even.next
            else:
                odd.next = ListNode(cur.val)
                odd = odd.next
            cur = cur.next
            i += 1
        
        odd.next = dummy2.next
        return dummy1.next
