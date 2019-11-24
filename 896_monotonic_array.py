#https://leetcode.com/problems/monotonic-array/

# Two pass
# O(2n)
# O(1)
class Solution(object):
    def isMonotonic(self, A):
        for i in range(0, len(A) - 1):
            if A[i] > A[i + 1]:
                break
        else:
            return True
        for i in range(0, len(A) - 1):
            if A[i] < A[i + 1]:
                break
        else:
            return True
        return False


# One Pass
# O(n)
# O(1)
class Solution(object):
    def isMonotonic(self, A):
        has_deacrease = False
        has_increase = False
        for i in range(0, len(A)-1):
            if A[i] < A[i+1]:
                has_increase = True
            if A[i] > A[i+1]:
                has_deacrease = True
            if has_increase and has_deacrease:
                return False
        return True
