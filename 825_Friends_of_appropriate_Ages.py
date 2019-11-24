# O(A^2+N) A = number of ages N = number of People
# O(A) space for dictionary
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_to_count = [0] * 121
        for age in ages:
            age_to_count[age] += 1
        ans = 0
        for ageA, countA in enumerate(age_to_count):
            for ageB, countB in enumerate(age_to_count):
                if (ageB <= 0.5 * ageA + 7) or (ageB > ageA) or (ageB > 100 and ageA < 100):
                    continue
                ans += countA * countB
                if ageA == ageB:
                    ans -= countA
        return ans