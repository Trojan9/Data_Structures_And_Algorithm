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
