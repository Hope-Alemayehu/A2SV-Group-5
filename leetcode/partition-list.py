# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_node = ListNode(0)
        greater_node = ListNode(0)
        dummy1 = ListNode(0,less_node)    #to get the reference of less node
        dummy2 = ListNode(0,greater_node)    #to store the reference of greater node

        cur = head
        while cur:
            if cur.val < x:
                less_node.next = cur
                less_node = cur
                tmp = cur.next
                less_node.next = None

            else:
                greater_node.next = cur
                greater_node = cur
                tmp = cur.next
                greater_node.next = None
            cur = tmp
        less_node.next = dummy2.next.next
        return dummy1.next.next

