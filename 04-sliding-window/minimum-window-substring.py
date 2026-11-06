# Amazon SDE-I 50, #16: Minimum Window Substring (Hard)  [Sliding Window]
#
# Brief: Shortest substring of `s` containing all of `t` (counts included), or "".
# `"ADOBECODEBANC","ABC"` → `"BANC"`.
#
# In plain words: find the shortest chunk of `s` that contains every letter of `t`. Slide a
# window: grow the right end until the window has everything `t` needs, then shrink the left as
# far as you can while it's still valid, keeping the smallest. Track `have` = how many required
# letters currently have enough copies, and `need` = how many distinct letters `t` wants. Valid
# when `have == need`.
#
# Why it works: you bump `have` only when a letter's count *reaches* what's needed (`==
# countT[c]`) and drop it only when shrinking pushes it *below* (`< countT[c]`). Those crossing
# points keep `have` an accurate count of satisfied requirements. The window can hold junk letters
# not in `t`, they just add length and get shrunk away.
#
# Algorithm
# 1. Build `countT`; `need = len(countT)`. 2. Expand right; when a char hits its needed count,
#    `have += 1`. 3. While valid, record if smaller, pop left; if a char drops below need, `have
#    -= 1`.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:   # c just became satisfied
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:   # dropped below need
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""

# Complexity: Time O(n), Space O(distinct chars).
# Gotcha: use `==` (not `>=`) when bumping `have`, or extra copies over-count.
