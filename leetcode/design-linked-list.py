class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        self.head = Node()

    def get(self, index: int) -> int:
        idx = 0
        cur = self.head.next  # Start from the first node
        while cur and idx < index:
            cur = cur.next
            idx += 1
        if not cur:  # Index out of bounds
            return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        tmp = self.head.next
        self.head.next = new_node
        new_node.next = tmp

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        idx = 0
        cur = self.head
        while cur and idx < index:
            cur = cur.next
            idx += 1
        if not cur:  # Index out of bounds
            return
        new_node = Node(val)
        tmp = cur.next
        cur.next = new_node
        new_node.next = tmp

    def deleteAtIndex(self, index: int) -> None:
        idx = 0
        cur = self.head
        while cur and idx < index:
            cur = cur.next
            idx += 1
        if not cur or not cur.next:  # Index out of bounds
            return
        cur.next = cur.next.next
