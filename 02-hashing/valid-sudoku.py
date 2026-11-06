# Amazon SDE-I 50, #7: Valid Sudoku (Medium)  [Arrays and Hashing]
#
from typing import List
from collections import defaultdict

# Brief: 9×9 board, True if no row/column/3×3 box repeats a digit (filled cells only).
#
# In plain words: is the board legal so far? Keep a "seen" set for each row, each column, and each
# 3×3 box. Read each filled cell; if its digit is already seen in that row, column, or box, it's
# illegal. A cell's box is `(row // 3, column // 3)` (dividing by 3 groups 0,1,2 together, etc.).
#
# Why it works: the three Sudoku rules are independent "no repeats in this group" checks; a set
# per group flags a repeat instantly. You're only checking legality so far, not solvability.
#
# Algorithm
# 1. Three dicts of sets. 2. For each filled cell, fail if its digit is in its row/col/box set. 3.
#    Else add to all three.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)       # key = (r // 3, c // 3)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]
                        or board[r][c] in cols[c]
                        or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True

# Complexity: Time O(1) (fixed 81 cells), Space O(1).
