# 1. Check whether a input string is valid
#    Check the num of left '(' and the num of right )
#    O(n)
# 2. Compute min number of ( and ) to remove
# 3. Try all possible ways to remove ) and (
# remove RIGHT ) FIRST to make prefix valid
# REMOVE THE FIRST PARANSETHESIS ONLY TO AVOID DUPLICATE
# dfs(s, l, r):
# if l==0 and r==0 and valid:
# ans.add(s)
# Avoid duplications, remove the first paransethesis if there are more than 1

# O(2^(l+r)) # of left need to deleted
# O((l+r)^2) O(n^2) # every call needs a copy of the word

class Solution(object):
    def removeInvalidParentheses(self, s):
        l, r = 0, 0
        # Compute the Minimum number of paranthesis to remove
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
        res = []
        self.dfs(s, 0, l, r, res)
        return res

    # Check if a given string is valid
    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    def dfs(self, s, startIndex, l, r, res):
        if l == 0 and r == 0 and self.isValid(s):
            res.append(s)
            return

        for i in range(startIndex, len(s)):
            if i > 0 and s[i] == s[i - 1] and i != startIndex:
                continue
            if s[i] == '(' or s[i] == ')':
                if r > 0 and s[i] == ')':
                    curr = s[:i] + s[i + 1:]
                    self.dfs(curr, i, l, r - 1, res)
                elif l > 0 and s[i] == '(':
                    curr = s[:i] + s[i + 1:]
                    self.dfs(curr, i, l - 1, r, res)

# BFS
# O(n*2^n)
# from the first level, so there are C(n, n-1) new strings,
# each of them has n-1 characters, and for each string, we need to check whether
# it's valid or not, thus the total time complexity on this level is (n-1) x C(n, n-1

class Solution(object):
    def removeInvalidParentheses(self, s):
        if not s:
            return [""]
        res = []
        queue = collections.deque([s])
        visited = set([s])
        found = False
        while queue:
            head = queue.popleft()

            if self.isValid(head):
                res.append(head)
                found = True
            if found:
                continue
            for i in range(0, len(head)):
                if head[i] == '(' or head[i] == ')':
                    curr = head[:i] + head[i + 1:]
                    if curr not in visited:
                        queue.append(curr)
                        visited.add(curr)
        return res

    # Check if a given string is valid
    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0


