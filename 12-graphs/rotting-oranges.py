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
