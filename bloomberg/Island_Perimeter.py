class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
#         get row and col and create a set to store visited points
        m,n,visited = len(grid), len(grid[0]), set()
        
        def dfs(i,j):
#             if point is visited return 0
            if (i,j) in visited: return 0
#     else if its outside perimter or grid point is ==0 1.e water
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 0: return 1
#     add to set
            visited.add((i,j))
#     find dfs of surrounding
            return dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
   
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i,j)
        return 0

        # O(n*M)

#faster solution

#Loop through the grid.

#For every land cell (grid[r][c] == 1):

#Add 4 to the perimeter

#Subtract 1 for each land neighbor (right or down only to avoid double-subtracting)

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    #Because each shared edge is counted twice (once from each tile), so subtracting 2 accounts for that.
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2
        return perimeter
