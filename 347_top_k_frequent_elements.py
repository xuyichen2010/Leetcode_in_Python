# Naive
# Hashmap then sort
# O(NlogN)
# O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = {}
        for num in nums:
            num_to_count[num] = num_to_count.get(num, 0) + 1
        res = sorted(num_to_count, key= lambda k: -num_to_count[k])
        return res[:k]

# Optimized Version using bucket sort
# O(N)
# O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = {}
        freq_to_num = collections.defaultdict(list)
        for num in nums:
            num_to_count[num] = num_to_count.get(num, 0) + 1
        for key in num_to_count:
            frequency = num_to_count[key]
            freq_to_num[frequency].append(key)
        res = []
        for i in range(len(nums), 0, -1):
            if i not in freq_to_num:
                continue
            for j in freq_to_num[i]:
                res.append(j)
        return res[0:k]

# Using Heap
# O(NlogN) extracting N items where each takes log(N)
# O(N) for the hashmap
class Solution:
    def topKFrequent(self, nums, k):
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)