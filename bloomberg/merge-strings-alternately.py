class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        #we need 2 pointers to hold position of both words
        p1 = 0
        p2 = 0

        #if any of them pointers is less than theeir length
        while p1 < len(word1) or p2 < len(word2):
            if p1 < len(word1) and word1[p1]:
                res += word1[p1]
                p1 +=1
            
            if p2 < len(word2) and word2[p2]:
                res += word2[p2]
                p2 +=1
        
        return res


        

            


 
    


            
    



        
