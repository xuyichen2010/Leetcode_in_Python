# O(n+k) ?
# O(n+k)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        dict1 = {}
        dict2 = {}
        start = 0

        # Fill in dict1
        for c in p:
            dict1[c] = dict1.get(c, 0) + 1

        # Loop through the entire s with last pointer
        for end in range(len(s)):
            curr = s[end]
            if end - start + 1 > len(p):
                dict2[s[start]] -= 1
                if dict2[s[start]] <= 0:
                    del (dict2[s[start]])
                start += 1

            dict2[curr] = dict2.get(curr, 0) + 1
            if dict2 == dict1:
                res.append(start)
        return res

# Not comparing dictionary
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        dict1 = {}
        dict2 = {}
        start = 0

        for c in p:
            dict1[c] = dict1.get(c, 0) + 1
        formed = 0
        valid = len(dict1)

        for end in range(len(s)):
            curr = s[end]
            if end - start + 1 > len(p):
                temp = s[start]
                dict2[temp] -= 1
                if temp in dict1 and dict1[temp] == dict2[temp]:
                    formed += 1
                elif temp in dict1 and dict1[temp] == dict2[temp] + 1:
                    formed -= 1
                if dict2[temp] <= 0:
                    del (dict2[temp])
                start += 1

            dict2[curr] = dict2.get(curr, 0) + 1
            if curr in dict1 and dict1[curr] == dict2[curr]:
                formed += 1
            elif curr in dict1 and dict1[curr] < dict2[curr]:
                formed -= 1
            if formed == valid:
                res.append(start)
        return res