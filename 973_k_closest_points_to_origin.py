# https://leetcode.com/problems/k-closest-points-to-origin/
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)
# You may return the answer in any order.
# The answer is guaranteed to be unique (except for the order that it is in.)

# O(NlogN)
# O(N)
class Solution(object):
    def kClosest(self, points, K):
        points.sort(key=lambda P: P[0]**2 + P[1]**2)
        return points[:K]

# O(NlogK) for inserting an item we do this k time
# O(K) space for heap because we pop the furthest element each time the length reaches k
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for p in points:
            if len(heap) < K:
                heapq.heappush(heap, (-p[0] ** 2 - p[1] ** 2, p))
            else:
                if -p[0] ** 2 - p[1] ** 2 > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-p[0] ** 2 - p[1] ** 2, p))
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
# O(N) on average quick select
# O(1)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda k: points[k][0] ** 2 + points[k][1] ** 2

        def quickSelect(points, K, l, r):
            if l < r:
                k = random.randint(l, r)
                pivot = partition(points, l, r, k)
                if K < pivot - l + 1:
                    quickSelect(points, K, l, pivot - 1)
                elif K > pivot - l + 1:
                    quickSelect(points, K - (pivot - l + 1), pivot + 1, r)

        def partition(a, l, r, k):
            a[k], a[r] = a[r], a[k]
            x = dist(r)
            i = l - 1
            for j in range(l, r):
                if dist(j) <= x:
                    i += 1
                    a[j], a[i] = a[i], a[j]
            a[i + 1], a[r] = a[r], a[i + 1]
            return i + 1

        quickSelect(points, K, 0, len(points) - 1)
        return points[:K]