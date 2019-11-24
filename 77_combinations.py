# DFS
# O(n*2^n) 2^n number of subsets, every subset takes O(n)
# O(n)
class Solution(object):
    def combine(self, n, k):
        result = []
        self.dfs(range(1,n+1), result, [], 0, k)
        return result

    def dfs(self, nums, result, subset, startIndex, k):
        if len(subset) == k:
            result.append(list(subset))
        for i in range(startIndex, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, result, subset, i + 1, k)
            subset.pop()