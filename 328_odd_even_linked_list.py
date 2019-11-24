# O(n)
# O(1)

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        o_head = head
        even = head.next
        even_head = even
        while even and even.next:
            head.next = head.next.next
            head = head.next
            even.next = head.next
            even = even.next
        head.next = even_head
        return o_head