class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #get len of row ans column
        ROWS,COLS=len(board),len(board[0])
        #create a path that will hold already visited points in the board
        path=set() #so we don't have duplicate
        #create a dfs parameters of r point,c point then the point on the word
        def dfs(r,c,i):
            if i==len(word):
                #i.e we already saw all the word in the word search and they follow the rules
                return True
            if (r<0 or c<0 or r>=ROWS or c>=COLS or word[i]!=board[r][c] or (r,c) in path):
                return False
            #we add to the path if none fits all condition above
            
            path.add((r,c))
            #then we find dfs for all cardinal point...up,left,right,down..i increments in all this..in all this they must return one true else it will be false..so we use OR operator
            res=(dfs(r+1,c,i+1) or dfs(r-1,c,i+1)or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            #so we remove item so another iteration can commece..so all above is done for each words until we get res=true..if not it will perform for all point in the board
            path.remove((r,c))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                #then run dfs for all interation for every point on the board
                if board[r][c]==word[0] and dfs(r,c,0):return True
        return False
    
    #time complexity (o*N*M*dfs)*4^len(word)
            
        