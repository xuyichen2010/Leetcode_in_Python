# Use stack and a list to keep track of time
# O(n) go through the entire list once
# O(n) stack can grow upto a depth of at most n/2
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        prev_time = 0
        stack = []
        for log in logs:
            fun, typ, time = log.split(':')
            fun, time = int(fun), int(time)
            if typ == 'start':
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(fun)
                prev_time = time
            else:
                ans[stack[-1]] += time - prev_time + 1
                stack.pop()
                prev_time = time + 1
        return ans