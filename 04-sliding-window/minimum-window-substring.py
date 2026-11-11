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


# ==================== Why not just check `window == countT`? ====================
#
# It's tempting to replace have/need with "is the window's letter count equal to t's?". It doesn't
# work, because == means EXACTLY the same keys with EXACTLY the same counts:
#
#   {'a':1, 'b':2, 'c':3, 'd':1} == {'a':1, 'b':2, 'c':3}     -> False  (extra key 'd')
#   Counter(a=1, b=2, c=3, d=1) == Counter(a=1, b=2, c=3)     -> False  (same with Counter)
#   (Only exception: Counter ignores counts of 0, so Counter(a=1, d=0) == Counter(a=1) is True.)
#
# But a valid window almost always has extras:
#   - extra letters:  s = "ADOBECODEBANC", t = "ABC". The first valid window is "ADOBEC",
#                     which also has D, O, E.  ==  says False, so we'd never notice it's valid.
#   - extra copies:   t = "ABC", window "ABAC" has A twice. Valid, but == says False.
#
# What we actually need is "the window has AT LEAST what t needs", not "exactly what t has".
#
# Compare with 02-hashing/valid-anagram.py, where `Counter(s) == Counter(t)` IS right: an anagram
# must have exactly the same letters and counts, so any extra letter should make it False.
#
#   Valid Anagram:   same letters, same counts?            -> ==
#   Minimum Window:  at least every letter t needs?        -> >=  (or have == need)
#
# Python 3.10+ Counter supports >= as "every count on the left is at least the count on the right":
#
#   Counter("ADOBEC") >= Counter("ABC")    -> True   (extras are fine)
#   Counter("AABC")   >= Counter("ABC")    -> True   (extra copies are fine)
#   Counter("AB")     >= Counter("ABC")    -> False  (missing C)
#
# Note: the "Gotcha" above is a different thing. That's about comparing ONE letter's count
# (window[c] == countT[c]) when bumping `have`. This section is about comparing the WHOLE maps.

# ==================== Simpler version using Counter >= ====================
#
# Same sliding window, but instead of tracking have/need we ask the Counter directly whether the
# window covers t. Easier to write and explain; a good first answer in an interview.
#
# Cost: `window >= countT` loops over every distinct letter of t, so each check is O(k) where
# k = distinct letters in t. Total O(n * k) instead of O(n). The have/need version above is the
# upgrade: it gets the same answer with an O(1) check, because `have` only changes at the moment
# a letter reaches, or drops below, the count it needs.

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = Counter(t)                 # what we need
        window = Counter()                  # what the current window has
        res, resLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1               # grow the window to the right
            while window >= countT:         # window has AT LEAST everything t needs (not ==)
                if (r - l + 1) < resLen:    # smallest valid window so far
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1           # shrink from the left and check again
                l += 1
        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""

# Complexity: Time O(n * k) (k = distinct letters in t), Space O(distinct chars).
