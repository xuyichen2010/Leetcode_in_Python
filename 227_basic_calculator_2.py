# Using Stack
# O(N) go through the entire string
# O(N) stack space
class Solution:
    def calculate(self, s):
        def update_helper(op, val):
            if op == '+':
                stack.append(val)
            elif op == '-':
                stack.append(-val)
            elif op == '*':
                stack.append(stack.pop() * val)
            elif op == '/':
                l = stack.pop()
                r = val
                if l * r < 0 and l % r != 0:
                    stack.append(l // r + 1) # For the sake of truncate toward zero Otherwise not needed
                else:
                    stack.append(l // r)
        stack = []
        val = 0
        op = '+'
        for c in s:
            if c.isdigit():
                val = val * 10 + int(c)
            elif c in ['+', '-', '*', '/']:
                update_helper(op, val)
                op = c
                val = 0
        update_helper(op, val)
        return sum(stack)