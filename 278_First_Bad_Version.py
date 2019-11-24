# https://leetcode.com/problems/first-bad-version/

# Brute Force
# Fails when input is huge
# O(n)
# O(1)
class Solution(object):
    def firstBadVersion(self, n):
        for i in range(1, n + 1):
            if isBadVersion(i):
                return i

# Binary Search
# why start + 1 < end? Works for both last and first position of targets
# For last position of target, when start = 0 end = 1 mid = 1/2 = 0, infinite loop
# O(log(n))
# O(1)
class Solution(object):
    def firstBadVersion(self, n):
        start = 1
        end = n
        while start + 1 < end:
            mid = (start + end)//2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        if isBadVersion(start):
            return start
        else:
            return end




def isBadVersion(i):
    return i

