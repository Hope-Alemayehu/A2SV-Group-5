# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def build(head, N):
            cur = head
            while N:
                tmp = cur
                cur = cur.next
                N -= 1
            tmp.next = None
        
            return head,cur

        arr = []
        res = []
        if not head:
            return [None]*k
        n = 0 #the length of the linked list
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        if n < k:
            for i in range(n):
                ans, head = build(head,1)
                res.append(ans)
                
            return res + [None]* (k - n)
        quo, rem = divmod(n, k)
        arr = [quo] * k
        idx = 0

        while rem:
            idx %= k
            arr[idx] += 1
            rem -= 1
            idx += 1

        for i in arr:
            ans, head = build(head,i)
            res.append(ans)  
          
        return res