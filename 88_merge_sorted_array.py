# https://leetcode.com/problems/merge-sorted-array/solution/

#
# Brute
# Merge and sort
# O((n+m)log(n+m)) B/c one deosn't benefit from the fact that both arrays are already sorted
# O(1)
nums1[:] = sorted(nums1[:m] + nums2)

# Two pointers (Start from beginning)
# O(n+m)
# O(m) keep the first m elements of nums1 somewhere aside

# Two pointers (Start from end)
# O(n+m)
# O(1)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if not nums1 or not nums2:
            return
        pt1 = m-1
        pt2 = n-1
        end = m+n-1
        while pt1 > -1 and pt2 > -1:
            if nums1[pt1] > nums2[pt2]:
                nums1[end] = nums1[pt1]
                pt1 -= 1
            else:
                nums1[end] = nums2[pt2]
                pt2 -= 1
            end -= 1

        # OR if pt1 < 0:
        #       nums1[:p2 + 1] = nums2[:p2 + 1]
        for i in range(pt2,-1,-1):
            nums1[end] = nums2[i]
            end -= 1