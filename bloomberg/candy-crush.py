class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        #step 1 is to return board if empty
        if not board:
            board
        #have a variable to check if stable
        
        stable=True
        
        #step 2 is to crush rows
        #..we do this by changing values that fall into the crushable categories into -ve
        
        for r in range(len(board)):
            #since they would be same length..and we need to take this values 3 by 3 sliding to the left..so definately were we stop +2 will cover the row..e.g(1,2,3,4,5)..the loop will stop at "3"..+2 index in our slider will cover to "5"..so reaching the last index will make the 3by3 slider out of place
            for c in range(len(board[r])-2):
                #take absolute of them cuz some values might have being turned to -ve cuz we touched them before
                num1=abs(board[r][c])
                num2=abs(board[r][c+1])
                num3=abs(board[r][c+2])
                if num1==num2 and num2==num3 and num1!=0: #since 0 means empty
                    #if they are same turn them to negative
                    board[r][c]=-num1
                    board[r][c+1]=-num2
                    board[r][c+2]=-num3
                    stable=False
                    
                    
        #step 3 is to crush the column also...its similar to the row crushing
        for r in range(len(board)-2):
            for c in range(len(board[r])):
                #take absolute of them cuz some values might have being turned to -ve cuz we touched them before
                num1=abs(board[r][c])
                num2=abs(board[r+1][c])
                num3=abs(board[r+2][c])
                if num1==num2 and num2==num3 and num1!=0: #since 0 means empty
                    #if they are same turn them to negative
                    board[r][c]=-num1
                    board[r+1][c]=-num2
                    board[r+2][c]=-num3
                    stable=False
        
        #step 4 is to run gravity using the pushing zeros idea
        if not stable:
            #now we need to go column by column
            #so start at bottom to up i.e start at len(arr)-1, end at -1 exclusive..so it ends at 0..in -1 step wise
            #don't miss it..c comes first
            #so for each column
            for c in range(len(board[0])):
                #start from the buttom row
                #so ind hold the position above the last block seen
                ind=len(board)-1
                #since its applys to only vertical...the columns
                #so we check from buttom upwards
                for r in range(len(board)-1,-1,-1):
                    #if there is a block there, we move this to the position of the ind where we expect there should be block
                    #there moment there is an empty space this guy below will not run, and now the present position will be one ahead the index we need blocks
                    #so the present block will move to the one below it
                    if board[r][c]>0:
                        #here if [ind][c] are same position, it just re-equate to itself
                        board[ind][c]=board[r][c]
                        #holds the position above the last block seen
                        ind -=  1
                #so we moved the blocks above the empty space to the empty spaces
                #now we need to replace the positions we moved this block from with 0
                for i in range(ind,-1,-1):
                    board[i][c]=0
        return board if stable else self.candyCrush(board)






class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        #so we gonna make use of recursive operation
        if not board:
            return board
        rows = len(board)
        cols = len(board[0])
        stable = True

        for r in range(rows):
            for c in range (cols-2):
                num1 = abs(board[r][c])
                num2 = abs(board[r][c+1])
                num3 = abs(board[r][c+2])
            
                if num1 == num2 and num1 == num3 and num1 != 0:
                    board[r][c] = -1 * num1
                    board[r][c+1] = -1 * num2
                    board[r][c+2] = -1 * num3
                    stable = False
        
        for r in range(rows-2):
            for c in range(cols):
                num1 = abs(board[r][c])
                num2 = abs(board[r+1][c])
                num3 = abs(board[r+2][c])
            
                if num1 == num2 and num1 == num3 and num1 != 0:
                    board[r][c] = -1 * num1
                    board[r+1][c] = -1 * num2
                    board[r+2][c] = -1 * num3
                    stable = False
        
        if not stable:
            #now we need to go col by column
            for c in range(cols):
                #hold the position of last empty space, we start looking from bottom to up, so that we need to fill up the space also
                lastEmptyIndex = rows - 1
                # so we move from down to the top
                for r in reversed(range(rows)):
                    #if position is greater than 0, it has a block
                    if board[r][c] > 0:
                        board[lastEmptyIndex][c] = board[r][c]
                        lastEmptyIndex -= 1

                #now replace all the moved blocks with nothing to fill them up with 0
                for i in range(lastEmptyIndex,-1,-1):
                    board[i][c]=0
        
        return board if stable else self.candyCrush(board)
                    

                    
