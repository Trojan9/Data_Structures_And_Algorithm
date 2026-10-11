
#brute force solution
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        news=[]
        newt=[]
        for i in range(len(s)):
            if s[i]=="#":
                if news:
                    print(news)
                    news.pop()#will delete the right most..popleft deletes leftmost
                    print(news)
            else:
                news.append(s[i])
        for r in range(len(t)):
            if t[r]=="#":
                if newt:
                    newt.pop()
            else:
                newt.append(t[r])
        
        return newt==news

# two pointer solution  
                
        