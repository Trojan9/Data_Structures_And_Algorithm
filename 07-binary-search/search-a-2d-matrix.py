# Amazon SDE-I 50, #23: Search a 2D Matrix (Medium)  [Binary Search]
#
from typing import List

# Brief: Row-sorted matrix, each row starts above the previous row's end. True if target present.
#
# In plain words: the grid is laid out so that reading it row by row gives one big sorted list. So
# binary search as if it's a flat list of length rows×cols, and convert a flat position back to a
# cell with `pos // cols` (row) and `pos % cols` (column).
#
# Why it works: the ordering guarantee makes the flattened grid genuinely sorted, so ordinary
# binary search applies without actually building the flat list.
#
# Algorithm
# 1. `l=0`, `r=rows*cols-1`. 2. `val = matrix[m//cols][m%cols]`. 3. Standard comparisons.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            val = matrix[m // COLS][m % COLS]
            if val > target:
                r = m - 1
            elif val < target:
                l = m + 1
            else:
                return True
        return False

# Complexity: Time O(log(m·n)), Space O(1).
