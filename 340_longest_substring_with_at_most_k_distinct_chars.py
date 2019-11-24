# Sliding window
# Keep a dictionary of the counts for each char
# While len(dict) > K
# Incrementing start until the condition is satisfied

# O(N)
# O(K) length could be K+1 at the most
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0
        char_to_count = {}
        start = 0
        for i in range(len(s)):
            if s[i] not in char_to_count:
                char_to_count[s[i]] = 1
            else:
                char_to_count[s[i]] += 1
            while len(char_to_count) > k:
                if char_to_count[s[start]] > 1:
                    char_to_count[s[start]] -= 1
                else:
                    del(char_to_count[s[start]])
                start += 1
            res = max(res, i - start + 1)
        return res