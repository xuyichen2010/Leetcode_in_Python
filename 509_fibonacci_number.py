# Top to Bottom memorization
# O(N)
# O(N)
class Solution(object):
    def fib(self, N):
        self.store = {}

        def helper(N):
            if N == 1:
                return 1
            if N == 0:
                return 0
            if N in self.store:
                return self.store[N]
            self.store[N] = helper(N - 1) + helper(N - 2)
            return self.store[N]

        return helper(N)

# Bottom up
# O(N)
# O(N)
class Solution(object):
    def fib(self, N):
        if N <= 1:
            return N
        result = {0: 0, 1: 1}
        for i in range(2, N + 1):
            result[i] = result[i - 1] + result[i - 2]

        return result[N]
