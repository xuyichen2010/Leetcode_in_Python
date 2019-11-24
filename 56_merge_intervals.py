# Two intervals i1, i2 overlap if the following requirements are satisfied:
#
# requirement 1: i1.end >= i2.start
# requirement 2: i1.start <= i2.end
# We preprocess the list by sorting intervals by starts increasingly.
# In this way, requirement 2 i1.start <= i2.start < i2.start is promised.
# We only have to compare i1.end with i2.start to see if requirement 1 is satisfied.

# O(nlogn) sorting
# O(1) to O(n) python use timsort which requires as many as 2N extra bytes depends on the data is sorted or not
class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key=lambda k: k[0])
        res = []
        for cur in intervals:
            if len(res) == 0:
                res.append(cur)
            else:
                prev = res[-1]
                if prev[1] >= cur[0]:  # Overlapped intervals.
                    prev[1] = max(prev[1], cur[1])
                else:
                    res.append(cur)

        return res