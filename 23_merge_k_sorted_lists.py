# Brute Force
# Traverse all to array and sort
# NlogN sorting

# Divide and Conquer
# O(Nlogk) where k is num of liked list
# Merging cost n time where n is nodes in two lists
# sum up the merge we get O(Nlogk)
# O(1) space

class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left_lists = self.mergeKLists(lists[0:mid])
        right_lists = self.mergeKLists(lists[mid:len(lists)])
        return self.merge(left_lists, right_lists)

    def merge(self, l, r):
        dummy = curr = ListNode(-1)
        while l and r:
            if l.val < r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next
        if l:
            curr.next = l
        else:
            curr.next = r
        return dummy.next


# O(Nlogk)
# O(n) for creating new linked list
# O(k) space for the priority queue
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next