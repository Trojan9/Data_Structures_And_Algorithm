# Amazon SDE-I 50, #21: Generate Parentheses (Medium)  [Stack]
#
from typing import List

# Brief: All well-formed combinations of `n` pairs. `n=2` → `["(())","()()"]`.
#
# In plain words: list every valid bracket string with n pairs. Build strings one character at a
# time (backtracking: choose, explore, undo). Rules: add `(` while you still have opens left
# (`open < n`); add `)` only if there's an unmatched `(` (`close < open`). Done when you've placed
# n of each.
#
# Why it works: a bracket string is valid iff no prefix ever has more closes than opens and it
# ends balanced; the two rules enforce that as you build, so you only ever create valid strings.
# The `stack.pop()` after each recursive call removes the character you just tried so the shared
# list is reset for the next option, that's the "undo".
#
# Algorithm
# 1. Recurse with open/close counts, building on a list. 2. `open==close==n` → record. 3. `open<n`
#    → append `(`, recurse, pop. 4. `close<open` → append `)`, recurse, pop.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()                    # undo '(' to try ')' in this spot
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()                    # undo ')' before returning
        backtrack(0, 0)
        return res

# Complexity: Time O(4ⁿ / √n), Space O(n) excluding output.
