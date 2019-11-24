# https://leetcode.com/problems/search-in-rotated-sorted-array/

# O(log(n))
# O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums)-1
        while start+1 < end:
            mid = (start + end)//2
            if nums[mid] <= nums[len(nums)-1]:
                if target >= nums[mid] and target <= nums[len(nums)-1]:
                    start = mid
                else:
                    end = mid
            else:
                if target >= nums[0] and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1