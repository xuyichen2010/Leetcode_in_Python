# 1. Split in half
# 2. Reverse the second half
# 3. Merge the two

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# O(N)
# O(1) if use iteration reverse

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        a, b = self.findMiddle(head)
        b = self._reverseList(b)
        head = self._mergeLists(a, b)

    def _mergeLists(self, a, b):
        tail = a
        head = a

        a = a.next
        while b:
            tail.next = b
            tail = tail.next
            b = b.next
            if a:
                a, b = b, a

        return head

    def findMiddle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None

        return head, middle

    def _reverseList(self, head):
        if head is None or head.next is None:
            return head
        p = self._reverseList(head.next)
        head.next.next = head
        head.next = None
        return p