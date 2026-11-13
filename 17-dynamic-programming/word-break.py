# LeetCode 139: Word Break (Medium)  [Dynamic Programming]
#
from typing import List
from functools import lru_cache

# Brief: can s be split into a sequence of words from wordDict? Words can be reused.
#
#   s = "leetcode",      wordDict = ["leet", "code"]                       -> True  ("leet code")
#   s = "applepenapple", wordDict = ["apple", "pen"]                       -> True  ("apple pen apple")
#   s = "catsandog",     wordDict = ["cats", "dog", "sand", "and", "cat"]  -> False
#
# ---------------------------------------------------------------------------------------------
# Intuition (bottom-up DP)
# ---------------------------------------------------------------------------------------------
# dp[i] answers ONE question: "can the first i characters of s be split into dictionary words?"
#
#   dp[0] = True    -> the empty string (first 0 characters) is always splittable. It's the
#                      starting point every split is built on.
#   dp[i] = True    -> there is some earlier position j where
#                        1. dp[j] is True            (everything BEFORE j is already split into words)
#                        2. s[j:i] is in wordDict    (the piece from j up to i is one more word)
#
# So the dp array is one longer than s (n = len(s) + 1). Index i in dp means "the cut AFTER
# i characters", not "character i":
#
#       dp index:    0     1     2     3     4
#                    |  f  |  o  |  u  |  r  |
#       s index:        0     1     2     3
#
# That's why the piece between two cuts j and i is s[j:i]. Python slices exclude the end, so
# s[j:i] is the characters at positions j, j+1, ..., i-1. Example: s[0:1] = "f" (position 1 is
# NOT included), and s[1:4] = "our". The slice is taken off s, the True/False check is taken off
# dp, and the two line up because of that "+1".
#
# Answer = dp[-1] = dp[len(s)]: "can the WHOLE string be split?"
#
# Why we need dp[j] AND the word check: a word on its own isn't enough, the part before it must
# also be fully split. In "helloworld" below, "world" is a word, but dp[5] ("hello") is False, so
# "world" can't be used to finish the string.

# ---------------------------------------------------------------------------------------------
# Solution 1: check every split point j
# ---------------------------------------------------------------------------------------------
# 1. wordDict -> set, so "is this a word?" is O(1) instead of scanning a list.
# 2. dp = [False] * (len(s) + 1), dp[0] = True.
# 3. For every end i from 1 to len(s):
#      for every start j from 0 to i - 1:
#        if dp[j] is True and s[j:i] is a word:
#          dp[i] = True
#          break             (one way to split is enough, no need to look at other j)
# 4. Return dp[-1].

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):              # i = end cut (exclusive)
            for j in range(i):             # j = start cut, every earlier position
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

# Complexity: Time O(n^2 · m) (n^2 pairs of (j, i), each slice + hash costs up to m = word length),
# Space O(n) for dp.

# ---------------------------------------------------------------------------------------------
# Dry run 1: s = "helloworld", wordDict = {"world", "ello", "he", "lo", "ll"}
# ---------------------------------------------------------------------------------------------
#       dp index:   0     1     2     3     4     5     6     7     8     9    10
#       piece:         h     e     l     l     o     w     o     r     l     d
#
#   i = 1:  j=0 "h"     not a word                                   dp[1] = False
#   i = 2:  j=0 "he"    dp[0] True, "he" is a word                   dp[2] = True
#   i = 3:  j=0 "hel" no, j=1 dp[1] False (skip), j=2 "l" no         dp[3] = False
#   i = 4:  j=0 "hell" no, j=1 skip, j=2 "ll" yes (dp[2] True)       dp[4] = True
#   i = 5:  j=0 "hello" no, j=1 skip ("ello" IS a word, but dp[1] is False: "h" isn't a word),
#           j=2 "llo" no, j=3 skip ("lo" is a word, but dp[3] False), j=4 "o" no
#                                                                    dp[5] = False
#   i = 6..9: no j with dp[j] True gives a word                      all False
#   i = 10: j=5 "world" IS a word, but dp[5] is False                dp[10] = False
#
#   dp = [True, False, True, False, True, False, False, False, False, False, False]
#   return dp[-1] = False
#
#   Notice how much work is wasted: for every i we try every j, even though only j = 0, 2, 4
#   were ever True. That's what Solution 2 fixes.

# ---------------------------------------------------------------------------------------------
# Solution 2 (optimised): only try the j's that are already True
# ---------------------------------------------------------------------------------------------
# In Solution 1 the inner loop goes over EVERY j, then throws most of them away with `dp[j]`.
# But a j with dp[j] False can never help. So keep a list `trues` of the positions where dp is
# True, and only loop over those.
#
# 1. Same set, same dp, dp[0] = True.
# 2. trues = [0]   (position 0 is True)
# 3. For every end i from 1 to len(s):
#      for every j in trues:          (only the cuts we KNOW are reachable)
#        if s[j:i] is a word:         (no dp[j] check needed, every j here is True)
#          dp[i] = True
#          trues.append(i)            (i is now reachable, later ends can start from it)
#          break                      (IMPORTANT: also stops i being appended twice)
# 4. Return dp[-1].
#
# Is it safe to append to `trues` while looping over it? Yes here: we break straight after the
# append, so the loop never continues over the changed list.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True
        trues = [0]                        # every index where dp is True
        for i in range(1, n):
            for j in trues:                # only reachable start cuts
                if s[j:i] in wordDict:
                    dp[i] = True
                    trues.append(i)
                    break
        return dp[-1]

# Complexity: same worst case as Solution 1, Time O(n^2 · m), Space O(n) (all positions can be
# True, e.g. s = "aaaa", wordDict = ["a"]). In practice it's much faster, because usually only a
# few positions are True and the inner loop only visits those.

# ---------------------------------------------------------------------------------------------
# Dry run 2: s = "four", wordDict = {"f", "our", "oompaloompa"}, n = 5
# ---------------------------------------------------------------------------------------------
#       dp index:   0     1     2     3     4
#       piece:         f     o     u     r
#
#   start:  dp = [True, False, False, False, False]   trues = [0]
#
#   i = 1:  j=0  s[0:1] = "f"    word                 dp[1] = True, trues = [0, 1]
#   i = 2:  j=0  s[0:2] = "fo"   no
#           j=1  s[1:2] = "o"    no                   dp[2] = False
#   i = 3:  j=0  s[0:3] = "fou"  no
#           j=1  s[1:3] = "ou"   no                   dp[3] = False
#   i = 4:  j=0  s[0:4] = "four" no
#           j=1  s[1:4] = "our"  word                 dp[4] = True, trues = [0, 1, 4]
#
#   dp = [True, True, False, False, True]   -> return dp[-1] = True   ("f" + "our")
#
#   Solution 1 would also have tried j = 2 and j = 3 at i = 3 and i = 4 and thrown them away.
#   Solution 2 never looks at them.

# ---------------------------------------------------------------------------------------------
# Other ways (kept from before)
# ---------------------------------------------------------------------------------------------

# Same DP but "pushing forward": from every reachable start, mark every end that a word reaches.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        N = len(s)

        dp = [False for _ in range(N + 1)]
        dp[0] = True
        for start in range(N):
            if not dp[start]:
                continue
            for end in range(start + 1, N + 1):
                if s[start:end] in d:
                    dp[end] = True
        return dp[-1]


####### EASY TO UNDERSTAND  #######

### USING RECURSIVE BACKTRACKING

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #make sure you add this
        @lru_cache(maxsize=None) # This adds memoization via @lru_cache, turning it into a top-down dynamic programming approach. this just cache results so you don't recompute from the same start again
        def recursive(start):
            #if the start index is the last index of s just return we already have all words
            if start == len(s):
                return True
            for word in wordDict:
                end = start + len(word)
                #remember end not inclusive in this split
                if s[start:end] == word:
                    # we recursively check for the next start index and last index of s
                    if recursive(end):
                        return True
            return False

        return recursive(0)
