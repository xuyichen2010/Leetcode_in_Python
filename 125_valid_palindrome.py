# https://leetcode.com/problems/valid-palindrome/
# ASK CLARIFYING QUESTIONS FOR INPUT!!!!!!!!!!!!!!!!!!!!!
# alphanumeric = character or number
# ignore space or other symbols

# O(n)
# O(1)


class Solution(object):
    def is_palindrome(self, s):
        s = s.lower()
        l = 0
        r = len(s)-1
        while l <= r:
            while l < r and not s[l].isalnum():
                l +=1
            while l < r and not s[r].isalnum():
                r -=1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
