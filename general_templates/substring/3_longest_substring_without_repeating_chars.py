# O(n)
# O(k) k = num of distinct char

# Keep a map of char to the last index
# REMEMBER to check the index we extract is greater than start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        ind = {}
        start = 0
        for i in range(0, len(s)):
            if s[i] in ind and start <= ind[s[i]]:
                start = ind[s[i]] + 1
            else:
                res = max(res, i-start+1)
            ind[s[i]] = i
        return res