
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
            
