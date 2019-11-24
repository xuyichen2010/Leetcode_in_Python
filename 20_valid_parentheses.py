# O(N) traverse once
# O(N) worst case push all left parentheses to the stack
class Solution:
    def isValid(self, s: str) -> bool:
        right_to_left = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c in right_to_left:
                if not stack:
                    return False
                if right_to_left[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return True if not stack else False