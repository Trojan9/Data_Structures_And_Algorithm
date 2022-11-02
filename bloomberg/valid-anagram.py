
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
            