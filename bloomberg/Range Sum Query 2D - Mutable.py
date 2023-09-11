# https://www.youtube.com/watch?v=KE8MQuwE2yA&t=12s


# for this we are goa get the prefix sum of the matrix
# so we we need to find the sum we just take the difference between diagonals, 
#                                 0  0  0   0   0    0             
#  1 2 3 4 5                      0  1  3   6   10   15         1+0  1+2+0   1+2+3+0   1+2+3+4+0   1+2+3+4+5+0
#  6 7 8 9 0                      0  7  16  27  40   45         6+1  6+7+3   6+7+8+6   6+7+8+9+10  6+7+8+9+0+15
#  3 4 5 6 3                      0  10 23  39  58   66         3+7  3+4+16  3+4+5+27  3+4+5+6+40  3+4+5+6+3+45
#  3 4 6 8 3      when we prefix  0  13 30  52  79   90         3+10 3+4+23  3+4+6+39  3+4+6+8+58  3+4+6+8+3+66

#start read with col first for better reading
# taking (1,2) to (2,3) in a square...when we use in out prefix...(2,3) to (3,4)..not index starts from 0
#  bottomRight= 58     (3,4) in our prefix
# top= 10              (1,4) in our prefix
# left= 23            (3,2) in our prefix
# topLeft=3           (1,2) in our prefix

# total =28 (you can verify)

# removing the top ad left will remove the range above or towards the left side , thereby segregrating that part out




class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.row,self.col=len(matrix),len(matrix[0])
        #remember to start with col here
        self.sumMat=[[0]*(self.col+1) for r in range(self.row+1)]

        for r in range(self.row):
            prefix=0
            for c in range(self.col):
                prefix+=matrix[r][c]
                #the one above present point
                self.sumMat[r+1][c+1]=prefix+self.sumMat[r][c+1]

        
    def update(self, row: int, col: int, val: int) -> None:
        pref=self.matrix[row][col]
        self.matrix[row][col]=val
        dif=val-pref 
        #now we add this difference to all elements after the present point we changed
        for r in range(row,self.row):
            for c in range(col, self.col):
                self.sumMat[r+1][c+1]+=dif
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1,r2,c2=row1+1,col1+1,row2+1,col2+1

        bottomRight=self.sumMat[r2][c2]
        top=self.sumMat[r1-1][c2]
        left=self.sumMat[r2][c1-1]
        topLeft=self.sumMat[r1-1][c1-1]
        return bottomRight-top-left+topLeft
       
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)


