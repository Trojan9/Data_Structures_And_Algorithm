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
        for word in strs:
            if tuple(sorted(word)) in res:
                res[tuple(sorted(word))].append(word)
            else:
                res[tuple(sorted(word))]=[word]
        
        return [res[result] for result in res]
