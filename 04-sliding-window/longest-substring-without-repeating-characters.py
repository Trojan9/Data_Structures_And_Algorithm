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

        
            
        