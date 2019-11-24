# O(N) == O(4N)
# First loop iterate the string
# Second loop union pop the stack and adds to the list
# Third loop iterate the string again
# Fourth loop convert the list to string

# O(n) using staeck, set and list

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indices_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in '()':
                continue
            if c == '(':
                stack.append(i)
            elif not stack:
                indices_to_remove.add(i)
            else:
                stack.pop()
        indices_to_remove = indices_to_remove.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in indices_to_remove:
                string_builder.append(c)
        return ''.join(string_builder)

# O(N) one pass
# O(N) string builder takes O(N)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Pass 1: remove all invalid ")"
        first_parse_chars = []
        balance = 0
        open_seen = 0
        for c in s:
            if c == '(':
                balance += 1
                open_seen += 1
            if c == ')':
                if balance == 0:
                    continue
                balance -= 1
            first_parse_chars.append(c)
        # Pass 2: Remove all rightmost "("
        result = []
        open_to_keep = open_seen - balance
        for c in first_parse_chars:
            if c == '(':
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue
            result.append(c)

        return ''.join(result)