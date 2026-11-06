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
