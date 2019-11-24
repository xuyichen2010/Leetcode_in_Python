# DFS
# O(n*2^n) 2^n number of subsets, every subset takes O(n)
# O(n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, result, [], 0)
        return result

    def dfs(self, nums, result, subset, startIndex):
        result.append(list(subset))
        for i in range(startIndex, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, result, subset, i + 1)
            subset.pop()