# Brute
# For each element find all subarray cost n^2
# Find sum is On or we can optimize to O(1)
# Total time O(n^3) or O(n^2)
# O(1)

# 2 pointers
# O(n) visit at most twice
# O(1)

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = len(nums) + 1
        window_sum = 0
        while r < len(nums):
            window_sum += nums[r]

            while window_sum >= s:
                res = min(res, r - l + 1)
                window_sum -= nums[l]
                l += 1
            r += 1

        return res if res != len(nums) + 1 else 0