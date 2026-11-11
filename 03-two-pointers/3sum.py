# Amazon SDE-I 50, #11: 3Sum (Medium)  [Two Pointers]
# Video explanation: https://www.youtube.com/watch?v=jzZsG8n2R9A
#
from typing import List

# Brief: All unique triplets summing to zero. `[-1,0,1,2,-1,-4]` → `[[-1,-1,2],[-1,0,1]]`.
#
# In plain words: find all trios that add to zero, no duplicates. Sort the list. Fix one number,
# then use the two-pointer trick (like Two Sum II) on the rest to find pairs that cancel it out.
# Skip repeated values so you don't list the same trio twice.
#
# Why it works: fixing `nums[i]` turns it into "find two numbers after i summing to `-nums[i]`".
# Sorting puts equal values together so the skip checks remove duplicate triplets cleanly.
#
# Algorithm
# 1. Sort. 2. For each i (skip duplicate anchors), two-pointer `l,r`. 3. Adjust by the sum's sign;
#    on a hit, record and skip duplicates.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort first. Two reasons:
        #  1. Two pointers only work on sorted data: moving l right makes the sum bigger, moving r
        #     left makes it smaller, so we always know which pointer to move.
        #  2. Equal numbers end up next to each other, so skipping duplicates is just
        #     "is this the same as the one before?".
        # Sorting costs O(n log n), which is cheaper than the O(n^2) loop below, so it's free.
        nums.sort()

        # All the unique triplets we find.
        res = []

        # i is the "anchor": the first number of the triplet. Fixing it turns 3Sum into Two Sum II:
        # "find two numbers to the RIGHT of i that add up to -nums[i]".
        for i in range(len(nums)):

            # Skip an anchor we've already used. nums is sorted, so if nums[i] equals nums[i - 1],
            # every triplet starting with this value was already found in the previous round.
            # Using it again would only produce the same triplets again.
            # (i > 0 so we don't compare nums[0] with nums[-1], the LAST element.)
            if i > 0 and nums[i] == nums[i - 1]:   # skip duplicate anchor
                continue

            # Optional speed-up (not required): if nums[i] > 0, then nums[l] and nums[r] are also
            # > 0 (sorted), so no sum can be 0. You could `break` here.

            # Two pointers on the part AFTER i:
            #   l starts just right of the anchor (the smallest remaining number),
            #   r starts at the end (the largest number).
            # We only look right of i, because triplets using earlier numbers as the anchor were
            # already checked in earlier rounds.
            l, r = i + 1, len(nums) - 1

            # Keep going until the pointers meet. l < r (not <=) because l and r must be two
            # DIFFERENT positions; we can't use the same number twice.
            while l < r:
                # Sum of the three candidates.
                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    # Too big. The only way to make it smaller is a smaller number, and the
                    # smaller numbers are to the left of r. So move r left.
                    r -= 1
                elif total < 0:
                    # Too small. The only way to make it bigger is a bigger number, and the bigger
                    # numbers are to the right of l. So move l right.
                    l += 1
                else:
                    # total == 0: found a triplet. Save it.
                    res.append([nums[i], nums[l], nums[r]])

                    # Move BOTH pointers inward to look for more pairs with this same anchor.
                    # Moving only one can't find a new answer: with nums[i] and nums[r] fixed,
                    # the only l that makes 0 is a number equal to nums[l] (a duplicate).
                    l += 1
                    r -= 1

                    # Skip left values equal to the one we just used. Otherwise, e.g. with
                    # [-2, 0, 0, 2, 2], we would find [-2, 0, 2] twice.
                    # We only need to skip on the left: if l moved to a NEW value, any r that
                    # gives 0 with it must also be a new value, so r sorts itself out through
                    # the normal total > 0 / total < 0 moves.
                    # (l < r stops us walking past r.)
                    while l < r and nums[l] == nums[l - 1]:   # skip duplicate lefts
                        l += 1

        return res

# Dry run 1: nums = [-1, 0, 1, 2, -1, -4]
#
#   after sort:  nums = [-4, -1, -1, 0, 1, 2]
#                index:    0   1   2  3  4  5
#
#   i=0 (anchor -4)    l=1, r=5
#       -4 + -1 + 2 = -3   < 0  -> l += 1  (l=2)
#       -4 + -1 + 2 = -3   < 0  -> l += 1  (l=3)
#       -4 +  0 + 2 = -2   < 0  -> l += 1  (l=4)
#       -4 +  1 + 2 = -1   < 0  -> l += 1  (l=5)   l == r, stop. Nothing found with -4.
#
#   i=1 (anchor -1)    l=2, r=5
#       -1 + -1 + 2 =  0   FOUND [-1, -1, 2]   -> l=3, r=4
#                          skip check: nums[3]=0 vs nums[2]=-1, different, no skip
#       -1 +  0 + 1 =  0   FOUND [-1, 0, 1]    -> l=4, r=3   l > r, stop.
#
#   i=2 (anchor -1)    nums[2] == nums[1] (-1 == -1) -> skip duplicate anchor.
#                      (Without this skip we'd find [-1, 0, 1] again.)
#
#   i=3 (anchor 0)     l=4, r=5
#        0 +  1 + 2 =  3   > 0  -> r -= 1  (r=4)   l == r, stop.
#
#   i=4, i=5           l = i + 1 is not < r, the while loop never runs.
#
#   return [[-1, -1, 2], [-1, 0, 1]]
#
# Dry run 2 (why we skip duplicate lefts): nums = [-2, 0, 0, 2, 2]  (already sorted)
#
#   i=0 (anchor -2)    l=1, r=4
#       -2 + 0 + 2 = 0     FOUND [-2, 0, 2]    -> l=2, r=3
#                          skip check: nums[2]=0 == nums[1]=0 -> l=3. Now l == r, stop.
#   i=1 (anchor 0)     l=2, r=4:  0+0+2 = 2 > 0 -> r=3;  0+0+2 = 2 > 0 -> r=2, stop.
#   i=2, i=4           duplicate anchors, skipped.
#
#   return [[-2, 0, 2]]
#
#   WITHOUT the skip-left loop: at l=2, r=3 we'd get -2 + 0 + 2 = 0 again, and the result would
#   be [[-2, 0, 2], [-2, 0, 2]] (a duplicate triplet).

# Complexity: Time O(n²), Space O(1) (output aside).
