class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #using sliding window method
        #https://www.youtube.com/watch?v=wiGpQwVHdE0
        getmax=0
        hashset=set()
        l=0
        for i in range(len(s)):
            while s[i] in hashset:
                #this will remove the first value of the hashmap
                #as there is no removeAt function
                hashset.remove(s[l])
                l+=1
            hashset.add(s[i])
            getmax=max(getmax,len(hashset))
            
        return getmax


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #14: Longest Substring Without Repeating Characters (Medium)  [Sliding Window]
#
# Brief: Longest substring with no repeats. `"abcabcbb"` → `3`.
#
# In plain words: longest stretch with no repeated character. Keep a window (a start and end).
# Move the end forward adding characters; if a character is already in the window, slide the start
# forward past its old copy so the window stays repeat-free. Track the biggest length.
#
# Why it works: when `s[r]` duplicates something inside, the only fix is to drop everything up to
# and including that earlier copy, which shrinking from the left does. The window is always valid,
# so `r - l + 1` (its length, inclusive) is always a candidate answer.
#
# Algorithm
# 1. Set of window chars, left pointer. 2. For each `s[r]`, while it's in the set, remove `s[l]`,
#    advance l. 3. Add it, update best.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:          # shrink until the repeat is removed
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

# Complexity: Time O(n), Space O(min(n, alphabet)).


# ==================== My solution: count + map, update max when a duplicate shows up ====================
#
# KEY IDEA
#   The window s[l..r] never has a repeat. `count` = how many characters are in it
#   (same as len(countMap) and r - l + 1).
#   - New character not in the window -> add it, count += 1 (window grows).
#   - Character already in the window -> the window is about to SHRINK, so save its
#     size first (maxCount = max(count, maxCount)), then throw characters out from
#     the LEFT until the old copy is gone, then add the new one.
#   - After the loop, check once more: the last window never hit a duplicate, so it
#     was never saved (e.g. "abc" has no duplicate at all, so only the last line saves 3).

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0          # size of the current window
        maxCount = 0       # best size seen so far
        countMap = {}      # characters in the window -> their index (only the keys are used)
        l = 0              # left edge of the window

        for r in range(len(s)):                  # r = right edge, adds one character per step
            if s[r] in countMap:                 # duplicate: the window must shrink
                maxCount = max(count, maxCount)  # save the size BEFORE shrinking
                while s[r] in countMap:          # throw out from the left until the old copy of s[r] is gone
                    del countMap[s[l]]           # remove the leftmost character
                    l += 1                       # move the left edge right
                    count -= 1                   # window got smaller

            countMap[s[r]] = r                   # add the new character (now it is unique in the window)
            count += 1                           # window got bigger

        maxCount = max(count, maxCount)          # the last window was never saved inside the loop
        return maxCount

# Why it is enough to update maxCount only at a duplicate and at the end:
#   count only goes UP between duplicates, so its biggest value is right before a shrink
#   (we save it there) or at the end of the string (we save it after the loop).
#
# DRY RUN 1: s = "pwwkew"  -> 3 ("wke")
#
#   r  s[r]  duplicate?  what happens                                window   count  maxCount
#   -  ----  ----------  ------------------------------------------  -------  -----  --------
#   0  p     no          add p                                        p        1      0
#   1  w     no          add w                                        pw       2      0
#   2  w     YES         save 2 -> maxCount 2                                         2
#                        del s[0]=p, l=1 (w still in)                 w        1
#                        del s[1]=w, l=2 (w gone, stop)               (empty)  0
#                        add w                                        w        1
#   3  k     no          add k                                        wk       2      2
#   4  e     no          add e                                        wke      3      2
#   5  w     YES         save 3 -> maxCount 3                                         3
#                        del s[2]=w, l=3 (w gone, stop)               ke       2
#                        add w                                        kew      3
#   end                  max(3, 3)                                                    3   <- answer
#
# DRY RUN 2: s = "abcabcbb"  -> 3
#
#   r  s[r]  duplicate?  what happens                                window   count  maxCount
#   -  ----  ----------  ------------------------------------------  -------  -----  --------
#   0  a     no          add a                                        a        1      0
#   1  b     no          add b                                        ab       2      0
#   2  c     no          add c                                        abc      3      0
#   3  a     YES         save 3; del a (l=1); add a                   bca      3      3
#   4  b     YES         save 3; del b (l=2); add b                   cab      3      3
#   5  c     YES         save 3; del c (l=3); add c                   abc      3      3
#   6  b     YES         save 3; del a (l=4), del b (l=5); add b      cb       2      3
#   7  b     YES         save 2; del c (l=6), del b (l=7); add b      b        1      3
#   end                  max(1, 3)                                                    3   <- answer
#
# DRY RUN 3: s = "abc" -> 3. No duplicate ever, so maxCount stays 0 in the loop;
#   the line after the loop saves count = 3. Without that line the answer would be 0.
#
# Notes
#   - The index stored in countMap (= r) is never read, so a set works the same.
#     If you DO use the index, you can jump l straight past the old copy instead of
#     deleting one by one: see the second solution in
#     longest-substring-without-repeating-characters-bloomberg.py.
#   - Time O(n): each character is added once and deleted at most once.
#     Space O(min(n, alphabet)).
