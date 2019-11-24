# https://leetcode.com/problems/kth-largest-element-in-an-array/solution/

# Brute
# Search then access
# O(nlogn)
# O(1)

# Quick Select
# O(N) in average O(N^2) in the worst case
# O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthSmallest(nums, len(nums) - k, 0, len(nums) - 1)

    def findKthSmallest(self, nums, k, l, r):
        if l == r:
            return nums[l]
        pivot = self.partition(nums, l, r)
        if k == pivot:
            return nums[pivot]
        elif k < pivot:
            return self.findKthSmallest(nums, k, l, pivot - 1)
        else:
            return self.findKthSmallest(nums, k, pivot + 1, r)

    def partition(self, nums, l, r):
        x = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

# Increase run-time by random partion as followed
# bn
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.findKthSmallest(nums, len(nums) - k, 0, len(nums) - 1)

    def findKthSmallest(self, nums, k, l, r):
        if l == r:
            return nums[l]
        pivot_ind = random.randint(l, r)
        pivot = self.partition(nums, l, r, pivot_ind)
        if k == pivot:
            return nums[pivot]
        elif k < pivot:
            return self.findKthSmallest(nums, k, l, pivot - 1)
        else:
            return self.findKthSmallest(nums, k, pivot + 1, r)

    def partition(self, nums, l, r, pivot):
        x = nums[pivot]
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

# Using Min heap
# The idea is to init a heap "the smallest element first",
# and add all elements from the array into this heap one by one keeping the size of the heap always less or equal to k.
# That would results in a heap containing k largest elements of the array.
# The head of this heap is the answer, i.e. the kth largest element of the array.
# O(k+(n-k)lgk) time, min-heap

# The time complexity of adding an element in a heap of size k is O(logK)
# and we do it N times that means O(Nlogk) time complexity for the algorithm.
#
# In Python there is a method nlargest in heapq library which has the same O(Nlogk)
# time complexity and reduces the code to one line.
#
# This algorithm improves time complexity, but one pays with O(k) space complexity.
def findKthLargest5(self, nums, k):
    return heapq.nlargest(k, nums)[-1]