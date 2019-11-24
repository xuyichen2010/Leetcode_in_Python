# O(M + N) M N are the length of A and B
# O(M + N) the size of the answer if we taking that into account O(1) if not
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        pA = 0
        pB = 0
        ans = []
        while pA < len(A) and pB < len(B):
            end = min(A[pA][1], B[pB][1])
            start = max(A[pA][0], B[pB][0])
            if end >= start:
                ans.append([start, end])
            if A[pA][1] < B[pB][1]:
                pA += 1
            else:
                pB += 1
        return ans