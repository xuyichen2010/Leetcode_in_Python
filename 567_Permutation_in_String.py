# Brute Force
# Generate all permutation of template and match with all substring
# O(n!)
# O(n^2) depth of recursion tree

# Sorting
# For all substring of s2 sort and compare
# O(k + 26*(n-k)) n = num of chars in s, k = num of chars in p, 26 = dictonary length
# O(1) at most 26 items in each dict
# OPTIMIZATION instead of comparing dict every time, we can keep a counter formed to record the matched char

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = {}
        s2_chars = {}
        start = 0
        for s in s1:
            s1_chars[s] = s1_chars.get(s, 0) + 1

        for end in range(0, len(s2)):
            if end - start + 1 > len(s1):
                s2_chars[s2[start]] -= 1
                if s2_chars[s2[start]] <= 0:
                    del (s2_chars[s2[start]])
                start += 1

            s2_chars[s2[end]] = s2_chars.get(s2[end], 0) + 1
            if s2_chars == s1_chars:
                return True

        return False