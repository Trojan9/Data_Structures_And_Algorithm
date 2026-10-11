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





##############################################################

#✅ Strategy: DFS + Backtracking
#We'll:

#1. Loop through each cell in the grid

#2. When the first letter matches word[0], start DFS (Depth-First Search)

#3. Recursively try to match the next letter in the word

#4. Use backtracking to unmark visited cells after trying paths


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board), len(board[0])
        visited = set()

        def dfs(r,c,i):
            # if i is the last index of the word..then we got all our words
            if i == len(word):
                return True
            #we already know first character match..add to seen
            visited.add((r,c))
            #normal tree traversing
            for dr,dc in [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]:
                #check if point is not outside the grid
                #check if not in visited
                #and see if current word at i is equal to current point in grid
                #at first we check i=1 , then recursively check i+1, +1,+1 for the 4 point
                if 0<=dr<rows and 0<=dc<cols and (dr,dc) not in visited and board[dr][dc] == word[i]:
                    #so recursively checking if next point on grid matches word at i, remember i increases
                    #i.e for every point in grid , we check up,left,right,down to see which will match word at index i
                    if dfs(dr,dc,i+1): #recursive
                        return True
            #if all doesn't match the words..backtract by removing all r,c (remember we have called in loop)
            #what this means is that all dfs that was called in the loop will remove their r,c point in grid that was passed to them (i.e all point visited from when board[r][c] == word[0])
            visited.remove((r,c))
            return False

    #loop through each cell    
        for r in range(rows):
            for c in range(cols):
                #we start dfs only when the first value of the word matches the current index
                if board[r][c] == word[0]:
                    #since we already know the first index matches first word..we need to know the next index that we match the next character of the word at 1..so we go recursively
                    if dfs(r,c,1):
                        return True
        return False
            
    #time complexity (o*N*M*dfs)*4^len(word)
            
        
