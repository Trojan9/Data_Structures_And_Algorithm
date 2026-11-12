# Amazon SDE-I 50, #5: Top K Frequent Elements (Medium)  [Arrays and Hashing]
#
from typing import List
from collections import Counter

# Brief: Return the `k` most frequent values. `[1,1,1,2,2,3], k=2` → `[1,2]`.
#
# In plain words: which `k` values show up most? Count each value. Then make buckets where bucket
# number = "appeared this many times", and drop each value in its bucket. Read buckets from the
# busiest down until you have k values.
#
# Why it works: a value appears at most n times, so a size-(n+1) bucket array covers every
# possible count; walking it high-to-low gives descending frequency order in O(n), beating an O(n
# log n) sort.
#
# Algorithm
# 1. Count values. 2. `freq[i]` = values seen i times. 3. From the top index down, collect until
#    k.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]   # index = frequency
        for num, c in count.items():
            freq[c].append(num)
        res = []
        for i in range(len(freq) - 1, 0, -1):       # highest frequency first
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

# Complexity: Time O(n), Space O(n).

# ---------------------------------------------------------------------------------------------
# Line by line
# ---------------------------------------------------------------------------------------------
#   count = Counter(nums)                        value -> how many times it appears
#   freq = [[] for _ in range(len(nums) + 1)]    bucket i holds values that appear EXACTLY i times.
#                                                size n+1 because a value can appear 0..n times
#                                                (index 0 is never used)
#   for num, c in count.items(): freq[c].append(num)
#                                                drop each value into the bucket for its count
#   for i in range(len(freq) - 1, 0, -1):        walk buckets from the BIGGEST count down to 1
#       for num in freq[i]:                      every value in this bucket (ties share a bucket)
#           res.append(num)                      take it
#           if len(res) == k: return res         stop the moment we have k (can be mid-bucket)
#
# Why buckets and not sorting: counts are whole numbers between 1 and n, so the index of the list
# IS the sort order. Reading the list backwards = reading counts from high to low, no sort needed.

# ---------------------------------------------------------------------------------------------
# Dry run 1: nums = [1, 1, 1, 2, 2, 3], k = 2      (n = 6)
# ---------------------------------------------------------------------------------------------
#   step 1, count:
#     count = {1: 3, 2: 2, 3: 1}
#
#   step 2, buckets (size n + 1 = 7, index = how many times):
#     freq = [[], [], [], [], [], [], []]
#     1 appears 3 times -> freq[3].append(1)
#     2 appears 2 times -> freq[2].append(2)
#     3 appears 1 time  -> freq[1].append(3)
#
#     index:  0    1     2     3     4    5    6
#     freq = [[], [3],  [2],  [1],  [],  [],  []]
#
#   step 3, read from the top (i = 6 down to 1):
#     i = 6: []   nothing
#     i = 5: []   nothing
#     i = 4: []   nothing
#     i = 3: [1]  take 1 -> res = [1]       len 1, need 2, keep going
#     i = 2: [2]  take 2 -> res = [1, 2]    len 2 == k -> return [1, 2]
#     (i = 1 is never reached)
#
#   answer: [1, 2]

# ---------------------------------------------------------------------------------------------
# Dry run 2 (ties + stopping mid-bucket): nums = [5, 5, 7, 7, 9, 9, 9, 1], k = 2   (n = 8)
# ---------------------------------------------------------------------------------------------
#   count = {5: 2, 7: 2, 9: 3, 1: 1}
#
#     index:  0    1     2        3    4    5    6    7    8
#     freq = [[], [1],  [5, 7],  [9], [], [], [], [], []]
#                         ^ 5 and 7 both appear twice, so they share bucket 2
#
#     i = 8..4: all empty
#     i = 3: [9]     take 9 -> res = [9]       need 2, keep going
#     i = 2: [5, 7]  take 5 -> res = [9, 5]    len 2 == k -> return right here
#                    (7 is never looked at: we stop in the MIDDLE of the bucket)
#
#   answer: [9, 5]   ([9, 7] would also be accepted: 5 and 7 are tied)
#
# Why the return is INSIDE the inner loop: if it were after the inner loop, we'd take the whole
# bucket [5, 7] and return 3 values. Checking after every single append stops at exactly k.
