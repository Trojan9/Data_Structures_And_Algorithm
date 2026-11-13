# LeetCode 547: Number of Provinces (Medium)  [Graphs, DFS]
# Video explanation: https://www.youtube.com/watch?v=giA3v_oB9Q4
#
from typing import List

# Problem: there are n cities. isConnected[i][j] = 1 means city i and city j are directly connected.
# If a is connected to b and b is connected to c, then a is (indirectly) connected to c.
# A PROVINCE is a group of cities that are connected directly or indirectly, with nothing else.
# Return the number of provinces.
#
# =============================================================================================
# KEY IDEA: THE MATRIX IS THE GRAPH. ROW i LISTS WHO CITY i IS CONNECTED TO (1 = connected).
# START A DFS FROM ANY CITY YOU HAVEN'T VISITED -> THAT'S A NEW PROVINCE (province += 1).
# THE DFS VISITS EVERY CITY IT CAN REACH (THE WHOLE PROVINCE) AND MARKS THEM VISITED,
# SO THE OUTER LOOP SKIPS THEM. COUNT HOW MANY TIMES THE OUTER LOOP HAS TO START A NEW DFS.
# =============================================================================================
#
# How to read the matrix (cities labelled 1..n like in the video; in code they're index 0..n-1):
#
#   1 -- 2 -- 3        row 2 = [1,1,1,1,0,0]
#         \                     ^ ^ ^ ^
#          4 -- 5               | | | city 4: connected
#                               | | city 3: connected
#   6                           | city 2: itself (always 1 on the diagonal)
#                               city 1: connected
#
# So "the neighbours of city i" = every j where isConnected[i][j] == 1. Same as an adjacency
# list, just written as a row of 0s and 1s.

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            self.visited.add(i)                              # mark this city as visited
            for j in range(n):                               # look along row i (every other city)
                if isConnected[i][j] and j not in self.visited:   # connected AND not seen yet
                    dfs(j)                                   # go deeper into that city first
            return                                           # row i finished -> go back up

        province = 0
        self.visited = set()
        n = len(isConnected)
        for i in range(n):                                   # try every city as a starting point
            if i not in self.visited:                        # not reached by any earlier dfs
                province += 1                                #   -> it starts a NEW province
                dfs(i)                                       #   -> visit the whole province
        return province

# Complexity: Time O(n^2) (each city's row of n is scanned once), Space O(n) (visited + recursion).


# =============================================================================================
# Walkthrough 1 (the idea): 9 cities, 3 provinces
# =============================================================================================
#
#   1 -- 2 -- 3        7 -- 9
#         \             \  /
#          4 -- 5         8
#
#   6
#
#   isConnected = [[1,1,0,0,0,0,0,0,0],   1
#                  [1,1,1,1,0,0,0,0,0],   2
#                  [0,1,1,0,0,0,0,0,0],   3
#                  [0,1,0,1,1,0,0,0,0],   4
#                  [0,0,0,1,1,0,0,0,0],   5
#                  [0,0,0,0,0,1,0,0,0],   6
#                  [0,0,0,0,0,0,1,1,1],   7
#                  [0,0,0,0,0,0,1,1,1],   8
#                  [0,0,0,0,0,0,1,1,1]]   9
#
#   Start at 1 (not visited)  -> province = 1. DFS spreads: 1 -> 2 -> 3, back to 2 -> 4 -> 5
#                                visited = {1,2,3,4,5}
#   2, 3, 4, 5                -> already visited, skip
#   Start at 6 (not visited)  -> province = 2. 6 has no neighbours
#                                visited = {1,2,3,4,5,6}
#   Start at 7 (not visited)  -> province = 3. DFS: 7 -> 8 -> 9
#                                visited = {1,2,3,4,5,6,7,8,9}
#   8, 9                      -> already visited, skip
#
#   answer: 3
#
# The number of provinces = the number of times we had to START a new DFS.


# =============================================================================================
# Walkthrough 2 (the code, line by line): 6 cities
# =============================================================================================
#
#   1 -- 2 -- 3        6
#         \
#          4 -- 5
#
#                  j: 1 2 3 4 5 6
#   isConnected = [[1,1,0,0,0,0],   i = 1
#                  [1,1,1,1,0,0],   i = 2
#                  [0,1,1,0,0,0],   i = 3
#                  [0,1,0,1,1,0],   i = 4
#                  [0,0,0,1,1,0],   i = 5
#                  [0,0,0,0,0,1]]   i = 6
#
#   province = 0; visited = set(); n = 6
#
#   OUTER LOOP i = 1: 1 not in visited -> province = 1, call dfs(1)
#
#   dfs(1): visited = {1}
#     row 1 = [1,1,0,0,0,0]
#     j = 1: connected, but 1 is visited (itself)          -> skip
#     j = 2: connected, 2 not visited                       -> call dfs(2), dfs(1) PAUSES here
#
#       dfs(2): visited = {1,2}
#         row 2 = [1,1,1,1,0,0]
#         j = 1: visited                                    -> skip
#         j = 2: visited (itself)                           -> skip
#         j = 3: connected, 3 not visited                   -> call dfs(3), dfs(2) PAUSES at j = 3
#
#           dfs(3): visited = {1,2,3}
#             row 3 = [0,1,1,0,0,0]
#             j = 2: visited, j = 3: itself, rest are 0     -> nothing new
#             loop ends -> return to dfs(2)
#
#       dfs(2) RESUMES at j = 4:
#         j = 4: connected, 4 not visited                   -> call dfs(4), dfs(2) PAUSES at j = 4
#
#           dfs(4): visited = {1,2,3,4}
#             row 4 = [0,1,0,1,1,0]
#             j = 2: visited, j = 4: itself
#             j = 5: connected, 5 not visited               -> call dfs(5), dfs(4) PAUSES
#
#               dfs(5): visited = {1,2,3,4,5}
#                 row 5 = [0,0,0,1,1,0]
#                 j = 4: visited, j = 5: itself             -> nothing new
#                 return to dfs(4)
#
#           dfs(4) RESUMES at j = 6: 0                      -> loop ends, return to dfs(2)
#
#       dfs(2) RESUMES at j = 5, 6: both 0                  -> loop ends, return to dfs(1)
#
#   dfs(1) RESUMES at j = 3..6: all 0                       -> loop ends, return to the outer loop
#
#   province = 1; visited = {1,2,3,4,5}   <- the whole first province, from ONE call in the outer loop
#
#   OUTER LOOP i = 2, 3, 4, 5: all in visited -> skip (they belong to province 1)
#   OUTER LOOP i = 6: 6 not in visited -> province = 2, call dfs(6)
#
#   dfs(6): visited = {1,2,3,4,5,6}
#     row 6 = [0,0,0,0,0,1]: only itself                    -> return
#
#   return province = 2
#
# ---------------------------------------------------------------------------------------------
# The call stack (how DFS goes DEEP first, then comes back)
# ---------------------------------------------------------------------------------------------
#
#   dfs(1)                        <- started by the outer loop (province 1)
#   └── dfs(2)                    <- 1's row says 2 is connected
#       ├── dfs(3)                <- 2's row says 3; 3 has nothing new -> return
#       └── dfs(4)                <- back in 2's row, next is 4
#           └── dfs(5)            <- 4's row says 5; nothing new -> return
#   dfs(6)                        <- started by the outer loop (province 2)
#
#   Each call reads ITS OWN row. When it finds an unvisited neighbour it goes into that city
#   straight away (deep), and only continues its own row after that whole branch returns.
#
# Why `j not in self.visited` matters: the matrix is symmetric (if 1 knows 2, 2 knows 1). Without
# the check, dfs(2) would call dfs(1) again, which calls dfs(2) again... forever.
#
# Note: the cities are labelled 1..6 above to match the video. In the code they are index 0..5,
# so "city 1" is i = 0, "city 2" is i = 1, and so on. The steps are exactly the same.


# =============================================================================================
# Walkthrough 3 (how the video ends): the call stack as a LIST, with i and j on the matrix
# =============================================================================================
# Keep 3 things next to the matrix and update them at every step:
#   - the state line:  province = ?; visited = set(...)
#   - the STACK:       every dfs call that is still running (bottom = oldest, top = running now)
#   - i and j markers: i = the row the current dfs is reading, j = the column it's checking
#
# A new dfs call is PUSHED onto the stack. When its row is finished it RETURNS and is POPPED,
# and the call under it carries on from the j where it paused.
#
# ---- step 1 ---------------------------------------------------------------------------------
#   province = 1; visited = set(1)                  stack:
#                                                     dfs(i=1)      <- running
#        j
#      [[1,1,0,0,0,0],  1  i                        row 1, j=1: itself, skip. j=2: connected,
#       [1,1,1,1,0,0],  2                           not visited -> push dfs(2)
#       ...
#
# ---- step 2 ---------------------------------------------------------------------------------
#   province = 1; visited = set(1,2)                stack:
#                                                     dfs(i=1)      paused at j=2
#                                                     dfs(i=2)      <- running
#      [[1,1,0,0,0,0],  1
#            j
#       [1,1,1,1,0,0],  2  i                        row 2, j=1: visited. j=2: itself.
#       [0,1,1,0,0,0],  3                           j=3: connected, not visited -> push dfs(3)
#
# ---- step 3 ---------------------------------------------------------------------------------
#   province = 1; visited = set(1,2,3)              stack:
#                                                     dfs(i=1)      paused at j=2
#                                                     dfs(i=2)      paused at j=3
#                                                     dfs(i=3)      <- running
#       [1,1,1,1,0,0],  2
#              j
#       [0,1,1,0,0,0],  3  i                        row 3, j=2: visited. j=3: itself.
#                                                   j=4,5,6: 0 -> row done -> RETURN, pop dfs(3)
#
# ---- step 4 ---------------------------------------------------------------------------------
#   province = 1; visited = set(1,2,3)              stack:
#                                                     dfs(i=1)      paused at j=2
#                                                     dfs(i=2)      <- running again, from j=4
#                  j
#       [1,1,1,1,0,0],  2  i                        row 2, j=4: connected, not visited
#                                                   -> push dfs(4)
#
# ---- step 5 ---------------------------------------------------------------------------------
#   province = 1; visited = set(1,2,3,4)            stack:
#                                                     dfs(i=1)      paused at j=2
#                                                     dfs(i=2)      paused at j=4
#                                                     dfs(i=4)      <- running
#                    j
#       [0,1,0,1,1,0],  4  i                        row 4, j=2: visited. j=4: itself.
#                                                   j=5: connected, not visited -> push dfs(5)
#
# ---- step 6 ---------------------------------------------------------------------------------
#   province = 1; visited = set(1,2,3,4,5)          stack:
#                                                     dfs(i=1)      paused at j=2
#                                                     dfs(i=2)      paused at j=4
#                                                     dfs(i=4)      paused at j=5
#                                                     dfs(i=5)      <- running
#       [0,0,0,1,1,0],  5  i                        row 5, j=4: visited. j=5: itself.
#                                                   rest 0 -> RETURN, pop dfs(5)
#
# ---- step 7: unwinding -----------------------------------------------------------------------
#   dfs(4) resumes at j=6: 0           -> RETURN, pop dfs(4)
#   dfs(2) resumes at j=5, 6: 0        -> RETURN, pop dfs(2)
#   dfs(1) resumes at j=3..6: all 0    -> RETURN, pop dfs(1)
#
#   province = 1; visited = set(1,2,3,4,5)          stack: (empty)
#   -> back in the OUTER loop. One call (dfs(1)) visited the whole first province.
#
# ---- step 8 ---------------------------------------------------------------------------------
#   outer loop i = 2, 3, 4, 5: all in visited -> skip, province stays 1
#
# ---- step 9 ---------------------------------------------------------------------------------
#   outer loop i = 6: not visited -> province += 1
#   province = 2; visited = set(1,2,3,4,5,6)        stack:
#                                                     dfs(i=6)      <- running
#                        j
#       [0,0,0,0,0,1],  6  i                        row 6: only itself -> RETURN, pop dfs(6)
#
#   stack empty, outer loop done -> return province = 2
#
# What to notice: `province += 1` only ever runs in the OUTER loop, when the stack is EMPTY.
# Everything a dfs reaches while the stack is non-empty belongs to the same province.
