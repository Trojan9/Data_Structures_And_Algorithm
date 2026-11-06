# Amazon SDE-I 50, #15: Longest Repeating Character Replacement (Medium)  [Sliding Window]
#
# Brief: Replace up to `k` chars; longest run of one letter you can make. `"AABABBA", k=1` → `4`.
#
# In plain words: you may change up to k characters; how long a run of a single letter can you
# make? For a window, the letters you'd have to change = window length − (count of its most common
# letter). If that's ≤ k, the window is doable; if it goes over k, shrink from the left.
#
# Why it works: to make a window uniform you keep the majority letter and change the rest, so
# "window length − max letter count" is exactly the number of replacements needed. Comparing that
# to k tells you if the window is achievable.
#
# Algorithm
# 1. Track window counts and `maxf`. 2. Expand; while `(len − maxf) > k`, shrink left. 3. Track
#    best length.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:        # replacements needed exceed budget
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

# Complexity: Time O(n), Space O(1).
