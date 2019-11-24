# Non-random partition Pivot at last position
# O(n^2) Worst case when the array is already sorted
# O(nlgn) Best case when we split the array into two eqaul subarrays every iteration
# The average run time is much closer to the best case than to the worst case


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, l, r):
        if l < r:
            pivot = self.partition(nums, l, r)
            self.quickSort(nums, l, pivot - 1)
            self.quickSort(nums, pivot + 1, r)

    def partition(self, a, l, r):
        x = a[r]
        i = l - 1
        for j in range(l, r):
            if a[j] <= x:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[r] = a[r], a[i + 1]
        return i + 1

# Random partition version
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, l, r):
        if l < r:
            k = random.randint(l, r)
            pivot = self.partition(nums, l, r, k)
            self.quickSort(nums, l, pivot - 1)
            self.quickSort(nums, pivot + 1, r)

    def partition(self, a, l, r, k):
        a[k], a[r] = a[r], a[k]
        x = a[r]
        i = l - 1
        for j in range(l, r):
            if a[j] <= x:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[r] = a[r], a[i + 1]
        return i + 1