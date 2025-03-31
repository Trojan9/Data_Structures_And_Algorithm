#so connecting all 1's verically or horizontally...note: you can't connect diagonally.
#where you can't coect again you call that island 1
#start  from another 1 you haven't conected..strace the connection horizonatlly or vertically...where the connection stops..is another island

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
#get the length first
        rows,cols=len(grid),len(grid[0])
        island=0
#visit will hold the points we have explored  before
        visits=set()
        
        def bfs(r,c):
            q=collections.deque()
            visits.add((r,c))
            q.append((r,c))
            while q:
                rowque,colque=q.popleft()
                #i.e right,left ,up,down
                valid=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in valid:
                    row,col=rowque+dr,colque+dc
                    #we need to check if its the points are in range of rows and cols
                    if (row in range(rows) and col in range(cols) and (row,col) not in visits and grid[row][col]=="1"):
                        visits.add((row,col))
                        q.append((row,col))




        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visits:
                    bfs(r,c)
                    island+=1
        return island


#another solution same but instead of doing a range again , we just check if we are in the grid

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        island = 0
        visited = set()

        def bfs(r,c):
            q= deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                rowQue, colQue = q.popleft()
                for dr,dc in [[rowQue+1,colQue],[rowQue,colQue+1],[rowQue-1,colQue],[rowQue,colQue-1]]:
                    #make sure we are still withing grid, value is "1" and not visited yet
                    if 0<=dr<rows and 0<=dc<cols and grid[dr][dc] == "1" and (dr,dc) not in visited:
                        visited.add((dr,dc))
                        q.append((dr,dc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    island +=1
        return island

#note: if you are added to use dfs just change popleft() to pop() , so you pop at the end instead of at the front....doing this we are using dfs iteratively instead of recursively




