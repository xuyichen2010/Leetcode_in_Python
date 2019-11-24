# https://leetcode.com/problems/valid-palindrome-ii/solution/

# Brute
# for each index remove the char and check if the resulting string is a palindrome
# O(N^2) Create a string of length N and iterate through it [::-1] takes N time
# O(n) space used by candidate answer
class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            t = s[:i] + s[i+1:]
            if t == t[::-1]:return True
        return s == s[::-1]

# Two pointers
# Iterate from left and right
# When encounter a different char we create two substrings of the remanning middle sessions
# First with deleting left and second with deleting right
# return if either one of them is a palindrome
# O(n) because [::-1] only get excuted once
# O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                del_left = s[l+1:r+1]
                del_right = s[l:r]
                return del_left == del_left[::-1] or del_right == del_right[::-1]
            l += 1
            r -= 1
        return True

    # Method for O(1) space for the above method
    class Solution:
        def validPalindrome(self, s: str) -> bool:
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return self.helper(s, l, r - 1) or self.helper(s, l + 1, r)
                l += 1
                r -= 1
            return True

        def helper(self, s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True