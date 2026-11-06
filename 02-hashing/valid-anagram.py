
#brute force solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create two counters
        countt=Counter(t)
        counts=Counter(s)
        #if the lengths are not the same they definately aren't anagrams
        if len(t)!=len(s):
            return False
        for i in t:
            #if a value is not in s..its not an anagram
            if i not in counts:
                return False
            #if this value count is not the same..its not an anagram also
            elif countt[i]!=counts[i]:
                return False
        #means it passes this return true
        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create a map with each letter count...if the maps are same, then it's an anagram
        s_dict = {} 
        t_dict = {}
        
        for letter in s:
            if letter in s_dict:
                s_dict[letter] +=1
            else:  
                s_dict[letter] =1 
                
        for letter in t:
            if letter in t_dict:
                t_dict[letter] +=1
            else:  
                t_dict[letter] =1 
        
        return s_dict == t_dict


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #3: Valid Anagram (Easy)  [Arrays and Hashing]
#
from collections import Counter

# Brief: Return `True` if `t` is an anagram of `s`. `"listen","silent"` → True.
#
# In plain words: is one word just the other's letters rearranged? Count each letter in both
# words; if the counts match exactly, they're anagrams, because rearranging doesn't change which
# letters you have or how many.
#
# Why it works: equal letter-count maps capture "same letters, same quantities", which is all an
# anagram is.
#
# Algorithm
# 1. Lengths differ → False. 2. Count both. 3. Return counts equal.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

# Complexity: Time O(n), Space O(1) (26 letters).
