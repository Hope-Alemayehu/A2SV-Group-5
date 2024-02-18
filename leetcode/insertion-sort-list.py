# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #is this really insertion sort nope
        #but it sort it doesn't it?
        
        if not head:
            return 

        temparr = []
        temp = head

        while temp:
            temparr.append(temp.val)
            temp =  temp.next
        
        temparr.sort()
        temp = head
        i = 0
        while temp:
            temp.val = temparr[i]
            i += 1
            temp = temp.next
        return head