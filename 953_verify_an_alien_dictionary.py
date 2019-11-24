# https://leetcode.com/problems/verifying-an-alien-dictionary/
# The words are sorted lexicographically if and only if adjacent words are.
# This is because order is transitive: a <= b and b <= c implies a <= c.
# To check whether a <= b for two adjacent words a and b, we can find their first difference.

# O(C) where C is the total content of words
# O(1)

class Solution:
    def isAlienSorted(self, words, order):
        dict = {}
        for i, c in enumerate(order):
            dict[c] = i
        for i in range(0, len(words ) -1):
            # Compare words next to each other
            curr = words[i]
            nex = words[i +1]
            equal = True
            for j in range(min(len(curr), len(nex))):
                if curr[j] != nex[j]:
                    equal = False
                    if dict[curr[j]] > dict[nex[j]]:
                        return False
                    break
            if equal and len(curr) > len(nex):
                return False

        return True