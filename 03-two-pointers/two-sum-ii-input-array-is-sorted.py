# Amazon SDE-I 50, #10: Two Sum II, Sorted (Medium)  [Two Pointers]
#
from typing import List

# Brief: Sorted array, return the 1-indexed pair summing to target, O(1) space.
#
# In plain words: same as Two Sum but the array is sorted, so use a pointer at each end. If their
# sum is too small, move the left pointer right (bigger number); too big, move the right pointer
# left (smaller number). You converge on the pair.
#
# Why it works: sorted order means moving left up only increases the sum and moving right down
# only decreases it, so each comparison tells you unambiguously which way to go, and you never
# skip a valid pair.
#
# Algorithm
# 1. `l`, `r` at ends. 2. Sum == target → return. 3. Sum < target → `l += 1`; else `r -= 1`.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            cur = numbers[l] + numbers[r]
            if cur == target:
                return [l + 1, r + 1]
            elif cur < target:
                l += 1
            else:
                r -= 1
        return []

# Complexity: Time O(n), Space O(1).
