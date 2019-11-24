# BFS
# O(n^3) to O(n^2) for every starting index search continue till the end of string
# Substring in Python takes O(n)
# O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = collections.deque([0])
        visited = set()
        wordDict = set(wordDict)
        while queue:
            head = queue.popleft()
            if head not in visited:
                for i in range(head, len(s)+1):
                    if s[head:i] in wordDict:
                        queue.append(i)
                        if i == len(s):
                            return True
            visited.add(head)
        return False

# Dynamic Programming
# O(n^3) to O(n^2) depends on the string slice
# O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]

# Top-Down with memorization
# O(n^2) to O(n^3_
# O(n)
class Solution(object):
    def wordBreak(self, s, wordDict):

        def dfs(i):
            if i == len(s):
                return True
            if rec[i] != -1:
                return True if rec[i] == 1 else False
            for j in range(i, len(s)):
                if s[i:j + 1] in wordSet:
                    rec[j + 1] = 1 if dfs(j + 1) else 0
                    if rec[j + 1] == 1:
                        return True
            return False

        rec = [-1] * (len(s) + 1)
        wordSet = set(wordDict)
        return dfs(0)