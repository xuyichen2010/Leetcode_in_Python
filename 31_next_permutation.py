# Brute force
# Find every possible permutation and comapre
# O(n!)
# O(1)

# Single pass
# 1. Find first non-decending pair a[i] and a[i-1].
# Because no arrangement to the right of a[i-1] can create a larger permutaion
# 2. Find a place j to hold a[i-1], so the result is just larger than the current
#    i.e nums[j] <= nums[i-1]
# 3. Switch i-1 and j,
# 4. Switch i-1 to len(n)-1 to get the smallest possible lexicographic permutation

# O(n) One pass
# O(1) In place
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        j = len(nums) - 1
        if i != 0:
            while nums[j] <= nums[i - 1]:
                j -= 1
            print(i, j)
            nums[j], nums[i - 1] = nums[i - 1], nums[j]
        return self.rotate(nums, i, len(nums) - 1)

    def rotate(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
