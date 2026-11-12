# Amazon SDE-I 50, #45: Rotting Oranges (Medium)  [Graphs]
#
from typing import List
import collections

# Brief: Minutes until all fresh oranges rot, or -1. Rot spreads to 4-neighbours each minute.
#
# In plain words: rot spreads from every rotten orange at once, one ring of neighbours per minute.
# Put all rotten oranges in a queue at the start, process one full "wave" of the queue per minute
# (rotting fresh neighbours and queueing them), and count minutes. If fresh oranges remain at the
# end, some were unreachable → -1.
#
# Why it works: seeding the queue with all sources and processing a whole wave per minute models
# simultaneous spread, so the first time an orange is reached is the earliest it could rot.
#
# Algorithm
# 1. Queue all rotten; count fresh. 2. Each wave rots neighbours, decrements fresh, counts a
#    minute. 3. Return time if fresh == 0 else -1.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            for _ in range(len(q)):          # one full wave = one minute
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid)) and col in range(len(grid[0]))
                            and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

# Complexity: Time O(m·n), Space O(m·n).


# ==================== Another solution: visited set + `while q:` (no fresh counter) ====================
# Two changes from the solution above:
#   1. A `visited` set instead of writing 2 into the grid, so the input grid is NOT changed.
#   2. Loop `while q:` instead of `while fresh > 0 and q:`. When a minute rots nothing new,
#      nothing is queued, the queue empties and the loop ends by itself.
#
# But dropping `fresh` needs two fixes (see "Why the two fixes" below):
#   fix 1: return time - 1, because the last wave rots nothing but still counts a minute
#   fix 2: scan the grid at the end for any fresh orange that never got visited -> -1

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()                              # oranges that are rotten (or queued to rot)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:                  # rotten from the start
                    q.append((r, c))                 #   -> spreads from minute 1
                    visited.add((r, c))              #   -> already "visited"

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        while q:                                     # runs until no new orange rots
            for _ in range(len(q)):                  # one full wave = one minute
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols    # inside the grid
                            and grid[nr][nc] == 1            # fresh in the ORIGINAL grid
                            and (nr, nc) not in visited):    # and not rotted / queued yet
                        visited.add((nr, nc))        # mark NOW, when queued (not when popped)
                        q.append((nr, nc))           # it rots this minute, spreads next minute
            time += 1                                # this wave took one minute

        # fix 2: any fresh orange never reached -> it can never rot
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    return -1

        return max(0, time - 1)                      # fix 1: undo the wasted last wave
                                                     # max(0, ..): no rotten at all -> time is 0

# Complexity: Time O(m·n) (each cell queued at most once + one final scan), Space O(m·n) (set + queue).
#
# ---------------------------------------------------------------------------------------------
# Why mark visited when QUEUEING, not when popping
# ---------------------------------------------------------------------------------------------
#   2 1          the 1 is next to BOTH 2s
#   0 2
# If we only marked it when popped, both 2s would see it as unvisited in the same minute and
# queue it twice. Marking it the moment it's queued means the second 2 sees it's already taken.
# (The first solution does the same thing with grid[row][col] = 2 right before q.append.)
#
# ---------------------------------------------------------------------------------------------
# Why the two fixes
# ---------------------------------------------------------------------------------------------
# Fix 1, the extra minute. The last wave pops the oranges that rotted last. They have no fresh
# neighbours, so nothing rots, but `time += 1` still runs:
#
#   grid                        | while q (raw time) | correct
#   ----------------------------+--------------------+--------
#   [[2,1,1],[1,1,0],[0,1,1]]   |        5           |   4
#   [[2,2],[1,1]]               |        2           |   1
#   [[0,2]]  (nothing to rot)   |        1           |   0
#   [[0]]    (no rotten at all) |        0           |   0   <- loop never runs, hence max(0, ..)
#
# With `while fresh > 0 and q` (first solution) the loop stops as soon as the last orange rots,
# so that wasted wave never happens.
#
# Fix 2, unreachable oranges. In [[2,1,1],[0,1,1],[1,0,1]] the bottom-left 1 is walled off by
# 0s. The queue still empties normally, so the loop can't tell us; only the final scan finds it.
#
# ---------------------------------------------------------------------------------------------
# Dry run: [[2,1,1],[1,1,0],[0,1,1]]   (positions as (row, col))
# ---------------------------------------------------------------------------------------------
#   start:  q = [(0,0)]   visited = {(0,0)}   time = 0
#
#     2 1 1
#     1 1 0
#     0 1 1
#
#   wave 1: pop (0,0) -> rots (0,1), (1,0)                       q = [(0,1),(1,0)]       time = 1
#   wave 2: pop (0,1) -> rots (0,2), (1,1)
#           pop (1,0) -> (1,1) already visited, nothing new      q = [(0,2),(1,1)]       time = 2
#   wave 3: pop (0,2) -> (1,2) is 0, nothing
#           pop (1,1) -> rots (2,1)                              q = [(2,1)]             time = 3
#   wave 4: pop (2,1) -> rots (2,2)                              q = [(2,2)]             time = 4
#   wave 5: pop (2,2) -> no fresh neighbours, nothing rots       q = []                  time = 5  <- wasted wave
#   loop ends (q empty)
#
#   final scan: every 1 is in visited -> no -1
#   return max(0, 5 - 1) = 4
#
# ---------------------------------------------------------------------------------------------
# Which one to use
# ---------------------------------------------------------------------------------------------
#                       | first solution (grid = 2, fresh) | this one (visited, while q)
#   --------------------+----------------------------------+----------------------------------
#   changes the grid?   | yes                              | no
#   extra space         | queue only                       | queue + visited set
#   stops early         | yes, when fresh hits 0           | no, runs one wasted wave
#   -1 check            | fresh == 0                       | final scan of the grid
#
# The `fresh` counter does 3 jobs at once (stop on time, detect unreachable, skip when nothing
# is fresh). Use this version when you're not allowed to modify the input grid.
