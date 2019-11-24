# O(N) memory, O(N) init, O(1) pick.
#
# Reservoir Sampling. O(1) init, O(1) memory, but O(N) to pick.
#
# binary search: O(N) memory, O(N lg N) init, O(lg N) pick.

# Reservoir Sampling solution
# O(n) pick
# O(1) space and initializing

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res = 0
        for i, curr in enumerate(self.nums):
            if curr != target:
                continue
            if random.randint(0, count) == 0:
                res = i
            count += 1
        return res
