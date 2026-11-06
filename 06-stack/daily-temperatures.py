# Amazon SDE-I 50, #20: Daily Temperatures (Medium)  [Stack]
#
from typing import List

# Brief: Days until a warmer day for each day. `[73,74,75,71,69,72,76,73]` → `[1,1,4,2,1,1,0,0]`.
#
# In plain words: for each day, how many days until it gets warmer (0 if never)? Keep a stack of
# days still waiting for a warmer day. When today is warmer than the day on top of the stack,
# today answers that day, pop it and record the gap in days. Keep popping while today beats the
# new top.
#
# Why it works: the stack only ever holds days in decreasing temperature (a warmer later day would
# have resolved earlier ones). So today resolves exactly the colder days waiting on top, and the
# answer is the index difference. Each day is pushed and popped once → O(n).
#
# Algorithm
# 1. Stack of `(temp, index)`. 2. While today beats the top, pop and set its answer to the gap. 3.
#    Push today.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []                              # (temp, index), temps decreasing down the stack
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd    # days waited = index gap
            stack.append((t, i))
        return res

# Complexity: Time O(n), Space O(n).
