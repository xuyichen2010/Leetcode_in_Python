# https://leetcode.com/problems/longest-palindromic-substring/


# Brute
# Check all Substring
# O(n^3) because there are O(n^2) substrings and takes O(n) to check each
# O(1)


# DP
# O(n^2) Double for loops
# O(n^2) Building a 2D array DP

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        DP = [[0 for i in range(0, len(s))] for j in range(0, len(s))]
        n = len(s)
        max_length = 1
        start = 0
        # case when the length is 1
        for i in range(0, n):
            DP[i][i] = 1

            # case when the length is 2
        for i in range(0, n - 1):
            if s[i] == s[i + 1]:
                DP[i][i + 1] = 1
                max_length = 2
                start = i

        # case when the length is between 3 and len(s)
        for k in range(3, n + 1):
            i = 0
            while (i < n - k + 1):
                j = i + k - 1
                if s[i] == s[j] and DP[i + 1][j - 1] == 1:
                    DP[i][j] = 1
                    max_length = k
                    start = i
                i += 1
        return s[start:start + max_length]

    # Inner to Outer
    # O(n^2) Double for loops
    # O(1) start and end

    def longestPalindrome(self, s):
        max_start = 0
        max_end = 0
        for i in range(0, len(s)):
            # Odd Case like "aba"
            start, end = self.helper(s, i, i)
            if end - start + 1 > max_end - max_start + 1:
                max_start = start
                max_end = end
            # Even Case like "abba"
            start, end = self.helper(s, i, i + 1)
            if end - start + 1 > max_end - max_start + 1:
                max_start = start
                max_end = end
        return s[max_start:max_end + 1]

    # get the longest palindrome from inner to outer
    def helper(self, s, l, r):
        while l > -1 and r < len(s) and s[r] == s[l]:
            r += 1
            l -= 1
        return l + 1, r - 1
