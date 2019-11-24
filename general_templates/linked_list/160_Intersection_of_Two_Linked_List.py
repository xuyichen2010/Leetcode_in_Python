# O(n+m)
# O(1)

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curA = headA
        curB = headB
        while headA and headB:
            headA = headA.next
            headB = headB.next
        count = 0
        if headA:
            while headA:
                headA = headA.next
                count += 1
            while count > 0:
                curA = curA.next
                count -= 1
        elif headB:
            while headB:
                headB = headB.next
                count += 1
            while count > 0:
                curB = curB.next
                count -= 1
        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None