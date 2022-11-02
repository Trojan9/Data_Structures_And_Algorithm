class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #using sliding window method
        getmax=0
        hashset=set()
        l=0
        #so we loop through
        for i in range(len(s)):
            #we reduce the window by moving it to the right.."abcde" ,window becomes "bcde"
            #so it is while and not if...because the duplicate can be in beetween and out goal is to removing the duplicate by moving the window to the right
            #so for "sbcdca"...when we encounter c duplicate...l=0,remove at s[l=0],increase l by 1, c is still present...we remove s[l=1] from set
            #increase l by 1..c is still in the set..then we remove s[l=2] from the set....c is no longer present...the loop breaks
            while s[i] in hashset:
                #so what we are removing is the value of s at position l...then increase l
                #so basically ,we are always removing from the left
                #for "abcabc", l=0 at first,when we see a duplicate..we remove at l=0 of s which is a..it becomes "bc"..the we add the value at the right
                hashset.remove(s[l])
                l+=1
            #add the present to the right then get the max length
            hashset.add(s[i])
            getmax=max(getmax,len(hashset))
            
        return getmax 
            
        