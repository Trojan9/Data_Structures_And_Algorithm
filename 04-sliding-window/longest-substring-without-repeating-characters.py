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
