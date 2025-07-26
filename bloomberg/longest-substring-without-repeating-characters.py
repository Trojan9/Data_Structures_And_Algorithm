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


#################################### Another solution still on sliding window...0(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap= {} # this will hold the character and the last index it occured
        maxi = 0
        left =0 
        # so we will use sliding window method
        # both starts at 0,0, for every time we move right one step,  
        # but if the character at right existed before and the index in the map is greater than or equal to left, we then move left to the index after the previously existed one from our map
        #e.g dvdf ...starts at 0,0 index, we move right till we get to 2(second d)..now we have d existed at 0
        #hashmap[s[right]] >= left
        # we move left to 0+1
        #don't forget to find the max for every step

        #abcabcbb...here also...a,b,c..in the second a, left moves to 1, now in second b , left is on 1 and previous index of b is on 1...here hashmap[s[right]] == left, we move left 1+1 also
        for right in range(len(s)):
            if s[right] in hashmap and hashmap[s[right]] >= left:
               left = hashmap[s[right]] + 1
            hashmap[s[right]] = right



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        queue = deque()
        maxi = 0

        for i in range(len(s)):
            if s[i] not in queue:
                queue.append(s[i])
                maxi = max(maxi,len(queue))
            else:
                while s[i] in queue:
                    queue.popleft()
                queue.append(s[i])
                maxi = max(maxi,len(queue))

        return maxi




        
            maxi = max(maxi,right-left+1)

        return maxi
        
