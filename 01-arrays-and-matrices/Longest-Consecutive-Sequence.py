128. Longest Consecutive Sequence
Medium
Topics
premium lock icon
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3




class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest




Intuition
To avoid repeatedly recounting the same sequences, we only want to start counting when we find the beginning of a consecutive sequence.
A number is the start of a sequence if num - 1 is not in the set.
This guarantees that each consecutive sequence is counted exactly once.

Once we identify such a starting number, we simply keep checking if num + 1, num + 2, … exist in the set and extend the streak as far as possible.
This makes the solution efficient and clean because each number contributes to the sequence only one time.

Algorithm

-Convert the list into a set numSet for O(1) lookups.
-Initialize longest to track the length of the longest consecutive sequence.
-For each number num in numSet:
  Check if num - 1 is not in the set:
  If true, num is the start of a sequence.
  Initialize length = 1.
  While num + length exists in the set, increase length.
  Update longest with the maximum length found.
-Return longest after scanning all numbers.


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #8: Longest Consecutive Sequence (Medium)  [Arrays and Hashing]
#
from typing import List

# Brief: Longest run of consecutive integers, O(n). `[100,4,200,1,3,2]` → `4` (1,2,3,4).
#
# In plain words: find the longest chain of back-to-back integers, in any order. Put everything in
# a set. Only start counting a chain from a number whose "one below" is missing (so it's a true
# start), then count upward while the next integer exists. `1` starts a chain (0 is absent), count
# 1,2,3,4 → length 4.
#
# Why it works: counting only from starts means each chain is counted once, not re-counted from
# every member, so each number is touched at most twice overall → O(n).
#
# Algorithm
# 1. Build a set. 2. For each n where `n-1` is absent, count up while `n+length` exists. 3. Track
#    the max.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if (n - 1) not in numSet:        # n is a chain's start
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

# Complexity: Time O(n), Space O(n).
