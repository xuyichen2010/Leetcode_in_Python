#
# O(number of answers * time need for each answer)
# O(n! * n)
# O(n)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        visited = [False] * len(nums)
        self.dfs(nums, [], res, visited)
        return res

    def dfs(self, nums, permutation, results, visited):
        if len(permutation) == len(nums):
            results.append(list(permutation))
            return
        for i in range(len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            permutation.append(nums[i])
            self.dfs(nums, permutation, results, visited)
            permutation.pop()
            visited[i] = False

