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