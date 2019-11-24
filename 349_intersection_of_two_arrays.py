# https://leetcode.com/problems/intersection-of-two-arrays/
# NO PRINT DUPLICATES

# Brute force
# O(n*m)

# 2 sets
# O(m+n)
# O(min(m,n))

class Solution(object):
    def intersection(self, nums1, nums2):
        res = set()
        result = set()
        for i1 in nums1:
            res.add(i1)
        for i2 in nums2:
            if i2 in res:
                result.add(i2)
        return result

# Follow up 1 if one array is much larger than the other
# Binary search all the small array element in the big one
# See 350 for the other follow-ups

