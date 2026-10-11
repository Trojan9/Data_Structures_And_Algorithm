There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 



#using math solution

#This is a combinations problem:

#To reach (m-1, n-1), the robot must take:

#(m - 1) down moves and (n - 1) right moves

#So, total steps = (m - 1 + n - 1) = (m + n - 2)
#Choose (m - 1) of them to be "down" steps → the rest will be "right" steps

#✅ Final formula:
#unique_paths = C(m + n - 2, m - 1) = (m+n-2)! / ((m-1)! * (n-1)!)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)



#another solution using dynamic programming

#         Create a 2D grid dp of size m x n

# Initialize all cells to 1

# Why? Because:

# There is only one way to reach any cell in the first row (all moves are right)

# Same for first column (all moves are down)

# So after this step:

# csharp
# Copy
# Edit
# If m = 3, n = 4 → dp =
# [
#  [1, 1, 1, 1],
#  [1, 1, 1, 1],
#  [1, 1, 1, 1]
# ]
# python
# Copy
# Edit
# for i in range(1, m):
#     for j in range(1, n):
# Now we start filling in the grid, starting from cell (1, 1)
# Why not (0, 0)? Because first row and column are already filled with 1s.

# python
# Copy
# Edit
#     dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
# 💡 The number of ways to reach cell (i, j) is:

# Ways from above → dp[i-1][j]

# Ways from left → dp[i][j-1]

# Because you can only move right or down, you could only have come from:

# the top cell or

# the left cell

# So you're just adding those two together.

# 🧠 Visual Example:
# For m = 3, n = 4, after filling:

# sql
# Copy
# Edit
# Initial dp (all 1s):
# [
#  [1, 1, 1, 1],
#  [1, 1, 1, 1],
#  [1, 1, 1, 1]
# ]

# After filling:
# [
#  [1, 1, 1, 1],
#  [1, 2, 3, 4],
#  [1, 3, 6, 10]
# ]
# dp[2][3] = 10 → there are 10 unique ways to reach the bottom-right corner.

# python
# Copy
# Edit
# return dp[-1][-1]
# This returns the value in the bottom-right corner, which is the total number of unique paths.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
