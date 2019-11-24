# https://leetcode.com/problems/minimum-window-substring/
# Brute force
# Iterate through all possible substring and check if it have all chars of template return if you find one
# O(s^2*T)
# O(1)

# Sliding Window
#  One right pointer whose job is to expand the current window and then
#  we have the left pointer whose job is to contract a given window.
# We keep expanding the window by moving the right pointer.
# When the window has all the desired characters,
# we contract (if possible) and save the smallest window till now.

# O(S+T) worst case visiting every element of S twice once by left pointer once by right
# Precisely 2 * S + T
# O(S+T) S when window is entire string T when T has all unique characters
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        valid = len(count_t)

        formed = 0
        count_s = {}
        min_len = float('inf')
        res = ""

        while r < len(s):
            new_char = s[r]
            count_s[new_char] = count_s.get(new_char, 0) + 1
            if new_char in count_t and count_t[new_char] == count_s[new_char]:
                formed += 1
            while l <= r and formed == valid:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = s[l:r + 1]
                del_char = s[l]
                count_s[del_char] -= 1
                l += 1
                if del_char in count_t and count_s[del_char] < count_t[del_char]:
                    formed -= 1
            r += 1
        return "" if min_len == float('inf') else res

#  Optimized Sliding Window
# Still O(S + T)
# Precisely 2*|filtered_S| + |S| + |T|
# Therefore, complexity would reduced when |filtered_S| <<< ∣S∣
# Space is still O(S+T)
def minWindow(self, s, t):
    if not t or not s:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    # Filter all the characters from s into a new list along with their index.
    # The filtering criteria is that the character should be present in t.
    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))

    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
    # Hence, we follow the sliding window approach on as small list.
    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1

        if window_counts[character] == dict_t[character]:
            formed += 1

        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while l <= r and formed == required:
            character = filtered_s[l][1]

            # Save the smallest window until now.
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1

        r += 1
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
