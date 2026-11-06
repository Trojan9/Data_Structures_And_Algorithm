Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.




class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        #what we are going to do is sort the words acording to unicode 
        #remember we can use sorted with list or tuple
        #all anagrams will be sorted to becom same words, we will just appen this to a list of their dict

        #sorted() returns a list and list cannot be a key to a dictionary
        #we convert to a tuple which is immutable and can be used as a key
        for word in strs:
            if tuple(sorted(word)) in res:
                res[tuple(sorted(word))].append(word)
            else:
                res[tuple(sorted(word))]=[word]
        
        return [res[result] for result in res]


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #4: Group Anagrams (Medium)  [Arrays and Hashing]
#
from typing import List
from collections import defaultdict

# Brief: Group strings that are anagrams. `["eat","tea","tan","ate"]` →
# `[["eat","tea","ate"],["tan"]]`.
#
# In plain words: bucket words that are rearrangements of each other. Give each word a
# "fingerprint" that's identical for anagrams, counting its 26 letters works (`"eat"` and `"tea"`
# have the same counts). Use the fingerprint as a key and drop each word in its bucket.
#
# Why it works: anagrams share letters so they share a fingerprint; non-anagrams differ in at
# least one letter count. Counting beats sorting because it skips the per-word sort cost.
#
# Algorithm
# 1. Map signature → words. 2. For each word build a tuple of 26 counts. 3. Append under that key.
#    4. Return values.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)      # tuple is hashable → usable as a key
        return list(res.values())

# Complexity: Time O(n·k) (n words, length k), Space O(n·k).
