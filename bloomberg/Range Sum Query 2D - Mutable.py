# https://www.youtube.com/watch?v=KE8MQuwE2yA&t=12s


2D Prefix Sum Formula (Summed-Area Table)
To compute the sum of elements inside a submatrix from (row1, col1) to (row2, col2), use the following formula:

---(notice we only -1 from either r1 or c1)--something to help you cram
sumRegion(row1, col1, row2, col2) = 
    sumMat[r2][c2]
  - sumMat[r1 - 1][c2]
  - sumMat[r2][c1 - 1]
  + sumMat[r1 - 1][c1 - 1]
Where:

sumMat is the precomputed 2D prefix sum matrix.

The indices are 1-based in sumMat to simplify boundary checks.

# for this we are goa get the prefix sum of the matrix
# so we we need to find the sum we just take the difference between diagonals, 
#                                 0  0  0   0   0    0             
#  1 2 3 4 5                      0  1  3   6   10   15         1+0  1+2+0   1+2+3+0   1+2+3+4+0   1+2+3+4+5+0
#  6 7 8 9 0                      0  7  16  27  40   45         6+1  6+7+3   6+7+8+6   6+7+8+9+10  6+7+8+9+0+15
#  3 4 5 6 3                      0  10 23  39  58   66         3+7  3+4+16  3+4+5+27  3+4+5+6+40  3+4+5+6+3+45
#  3 4 6 8 3      when we prefix  0  13 30  52  79   90         3+10 3+4+23  3+4+6+39  3+4+6+8+58  3+4+6+8+3+66

i.e  matrix [r][c] + (top of  sumMat[r+1][c+1]) + (left of  sumMat[r+1][c+1]) - (diagonal of sumMat[r+1][c+1] to the left)
remember we have [r+1][c+1] because we added 0's to surrond our matrix, we loop through original matrix tp create sumMat

maths equation:

self.sumMat[r+1][c+1] = matrix[r][c] + 
                        self.sumMat[r][c+1] + 
                        self.sumMat[r+1][c] - 
                        self.sumMat[r][c]

we can make it easy to remember
  self.sumMat[r+1][c+1] = matrix[r][c] -
                        self.sumMat[r][c] + 
                        self.sumMat[r][c+1] + 
                        self.sumMat[r+1][c] 
                        
                        

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



##### another approach ##########
### just create cummulative of the 2 D #######
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))  # Output: 8
print(obj.sumRegion(1, 1, 2, 2))  # Output: 11
print(obj.sumRegion(1, 2, 2, 4))  # Output: 12

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.map = {}
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        for r in range(self.rows):
            for c in range(self.cols):
                top = self.map.get((r - 1, c), 0)
                left = self.map.get((r, c - 1), 0)
                diagonal = self.map.get((r - 1, c - 1), 0)
                #so we add the 2d - the diagonal
                self.map[(r, c)] = matrix[r][c] + top + left - diagonal
        print(self.map)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.map[(row2, col2)]
        #so basically we do the exact opposite, minus the 2 D outside the bracket
        # and add the diagonal just outside the bracket
        top = self.map.get((row1 - 1, col2), 0)
        left = self.map.get((row2, col1 - 1), 0)
        overlap = self.map.get((row1 - 1, col1 - 1), 0)
        return total - top - left + overlap    

