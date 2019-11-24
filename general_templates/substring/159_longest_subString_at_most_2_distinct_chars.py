# Slide Window
# Keep a start pointer
# Keep the count of each char
# While loop if unique chars num is greater than K

# O(N) Linear
# O(1) dict can't have a size greater than 2
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = 0
        char_to_count = {}
        start = 0
        for i in range(0, len(s)):
            if s[i] not in char_to_count:
                char_to_count[s[i]] = 1
            else:
                char_to_count[s[i]] += 1
            while len(char_to_count) > 2:
                if char_to_count[s[start]] > 1:
                    char_to_count[s[start]] -= 1
                else:
                    del (char_to_count[s[start]])
                start += 1
            res = max(res, i - start + 1)
        return res
