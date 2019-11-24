# https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/
# Binary Search
# O(m*log(n))


# Using Dict
# O(m + n)
# O(min(m,n))
class Solution(object):
    def intersect(self, nums1, nums2):
        dict = {}
        result = []
        for l in nums1:
            if l not in dict.keys():
                dict[l] = 1
            else:
                dict[l] += 1
        for item in nums2:
            if item not in dict.keys():
                continue
            if dict[item] > 0:
                result.append(item)
                dict[item] -= 1
        return result

# Sort then two pointer
# O(nlogn + mlogm)
# O(min(m,n)
class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0
        result = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums2[p2] > nums1[p1]:
                p1 +=1
            elif nums2[p2] < nums1[p1]:
                p2 +=1
            else:
                result.append(nums2[p2])
                p1 += 1
                p2 += 1
        return result

# Bring down space complexity to O(1)
# Use nums1 to store result
class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0
        k = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums2[p2] > nums1[p1]:
                p1 += 1
            elif nums2[p2] < nums1[p1]:
                p2 += 1
            else:
                nums1[k] = nums1[p1]
                k += 1
                p1 += 1
                p2 += 1
        return nums1[0:k]

# 1. Follow up one array is much bigger than the other
# ANS: Use the approach 1 as we hash the smaller array
# ANS: OR we can use binary search over the large array use elements in small array as key
# 2. What if array is already sorted?
# ANS: Use approach 2, gives linear time and constant memory (After modification)
# 3. What if nums2 can't fit in memory?
# ANS: Use approach1 Then sequentially load and process nums2
# 4. What if neither fit in memory?
# ANS: 1. Split the numeric range into sub-ranges that fits the memory.
#         Modify Approach 1 to collect count in one sub range at a time
#      2. Use external sort and use Approach 2
# 5. Use Binary Search to find duplicate element?
#    Every time when we find an answer, we set a lower bound to
#    Lower: ans_index + 1
#    Upper: len(array)

