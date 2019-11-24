# Brutal
# see comment below

# Binary Search
# Init: O(N) pick: O(log(N)) N = size of w
# Space O(N)
'''
say we have the numbers 1, 5, 2 easiest solution is to construct the following array
arr[] = {0,1,1,1,1,1,2,2}
then generate a random number between 0 and 7 and return the arr[rnd]. This is solution
is not really good though due to the space requirements it has (imagine a number beeing 2billion).

The solution here is similar but instead we construct the following array (accumulated sum)
{1, 6, 8} generate a number between 1-8 and say all numbers generated up to 1 is index 0.
all numbers generated greater than 1 and up to 6 are index 1 and all numbers greater than 6 and up to 8 are index 2.
After we generate a random number to find which index to return we use binary search.
'''
class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.n = len(w)
        for i in range(1, self.n):
            w[i] += w[i-1]
        self.s = self.w[-1]

    def pickIndex(self) -> int:
        seed = random.randint(1, self.s)
        l, r = 0, self.n-1
        while l < r:
            mid = (l+r) // 2
            if seed <= self.w[mid]:
                r = mid
            else:
                l = mid+1
        return l
