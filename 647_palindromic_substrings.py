# The middle of the palindrome could be in one of 2N - 1 positions:
# either at letter or between two letters.
# For each center, let's count all the palindromes that have this center.

# O(N^2)
# O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        N = len(s)
        for center in range(2*N -1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

# Optimized Manacher's Algorithm
# O(N)
# O(N)
