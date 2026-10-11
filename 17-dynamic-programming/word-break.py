Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d= set(wordDict)
        N=len(s)

        dp=[False for _ in range(N+1)]
        dp[0]=True
        for start in range(N):
            if not dp[start]:continue
            for end in range(start+1,N+1):
                if s[start:end] in d :dp[end]=True
        return dp[-1]
            
       

####### EASY TO UNDERSTAND  #######

### USING RECURSIVE BACKTRACKING

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #make sure you add this
        @lru_cache(maxsize=None) # This adds memoization via @lru_cache, turning it into a top-down dynamic programming approach. this just cache results so you don’t recompute from the same start again
        def recursive(start):
            #if the start index is the last index of s just return we already have all words
            if start == len(s):
                return True
            for word in wordDict:
                end = start + len(word)
                #remember end not inclusive in this split
                if s[start:end] == word:
                    # we recursively check for the next start index and last index of s 
                    if recursive(end):
                        return True
            return False

        return recursive(0)
