# 152. Maximum Product Subarray (Medium)
#
# Given an integer array nums, find a contiguous non-empty subarray with the largest
# product, and return the product.
#
# Example 1: nums = [2, 3, -2, 4]  -> 6   ([2, 3])
# Example 2: nums = [-2, 0, -1]    -> 0   ([0]; [-2, -1] is not contiguous)
#
# Two solutions below, both O(n) time and O(1) space:
#   1. Prefix and suffix product (scan from both ends)
#   2. Dynamic programming (track the max AND min product ending here)


# =====================================================================================
# SOLUTION 1: Prefix and Suffix Product
# =====================================================================================
# Idea: Traverse the array from both directions, multiplying elements as you go.
# Keep track of the largest product found.

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        result = nums[0]
        prefix = 1
        suffix = 1

        for i in range(n):
            # Reset if the previous product was zero
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            # Multiply from left to right
            prefix *= nums[i]

            # Multiply from right to left
            suffix *= nums[n - i - 1]

            # Keep the largest product
            result = max(result, prefix, suffix)

        return result

# Explanation of each line
#
# 1. Get the array length and initialise the answer.
#        n = len(nums)
#        result = nums[0]
#    We use the first element as the initial maximum because the array might contain
#    only negative numbers.
#
# 2. Initialise both products to 1.
#        prefix = 1
#        suffix = 1
#    We use 1 because multiplying by 1 doesn't change a number.
#
# 3. Loop through the array.
#        for i in range(n):
#    We visit each element once, calculating both the left-to-right and right-to-left
#    products.
#
# 4. Reset products when they become zero.
#        if prefix == 0: prefix = 1
#        if suffix == 0: suffix = 1
#    Any number multiplied by zero is zero. Resetting to 1 allows us to start
#    calculating a new product after a zero.
#
# 5. Calculate the prefix product.
#        prefix *= nums[i]
#    This multiplies elements from left to right.
#
# 6. Calculate the suffix product.
#        suffix *= nums[n - i - 1]
#    This multiplies elements from right to left.
#    For example, with nums = [2, 3, -2, 4]:
#      - i = 0: access index 3 -> 4
#      - i = 1: access index 2 -> -2
#      - i = 2: access index 1 -> 3
#      - i = 3: access index 0 -> 2
#
# 7. Update the maximum product.
#        result = max(result, prefix, suffix)
#    We compare the previous maximum with the current prefix and suffix products.
#
# Walkthrough
#   Input: nums = [2, 3, -2, 4]
#
#   i   Prefix   Suffix   Result
#   -   ------   ------   ------
#   0   2        4        4
#   1   6        -8       6
#   2   -12      -24      6
#   3   -48      -48      6
#
#   Answer: 6, from subarray [2, 3].
#
# Walkthrough with a zero: nums = [-2, 0, -1]
#
#   i   prefix before   prefix (x nums[i])   suffix before   suffix (x nums[n-1-i])   Result
#   -   -------------   ------------------   -------------   ----------------------   ------
#   0   1               -2                   1               -1                       -1
#   1   1               0                    1               0                        0
#   2   0 -> reset 1    -1                   0 -> reset 1    -2                       0
#
#   Answer: 0. The zero splits the array into [-2] and [-1]; the reset starts a fresh
#   product after it, so -2 and -1 are never multiplied together.
#
# Why do we scan in both directions?
#   Negative numbers can change the sign of a product.
#
#   When a zero-free segment has an odd number of negative numbers, the maximum
#   positive product may come from excluding the beginning through the first negative
#   number or excluding the end starting from the last negative number.
#
#   e.g. [-1, 3, 4]   one negative, at the FRONT. Best = [3, 4] = 12.
#          prefix: -1, -3, -12   (left-to-right is stuck with the -1)
#          suffix:  4, 12, -12   (right-to-left reaches 12 before hitting the -1)
#        [3, 4, -1]   one negative, at the END. Best = [3, 4] = 12.
#          prefix:  3, 12, -12   (left-to-right reaches 12 before hitting the -1)
#          suffix: -1, -4, -12   (right-to-left is stuck with the -1)
#   One direction always gets the answer, so we check both.
#
#   Scanning in both directions allows us to consider both possibilities. Zeros
#   separate the array into segments, and resetting handles them.
#
# Complexity: Time O(n), Space O(1).


# -------------------------------------------------------------------------------------
# SOLUTION 1b: Prefix and Suffix, also returning the START and END indexes
# -------------------------------------------------------------------------------------
# "With prefix and suffix there's no way to get the indexes, right?"
# Actually, yes, you can. You just need to track where each running product starts
# and ends:
#   - prefix  product covers nums[prefixStart .. i]   (starts at prefixStart, ends at i)
#   - suffix  product covers nums[j .. suffixEnd]     (starts at j, ends at suffixEnd)
#   - after a zero, the product resets to 1 AND its boundary moves to the current spot

class SolutionWithIndexes:
    def maxProduct(self, nums: list[int]):
        n = len(nums)

        prefix = 1
        suffix = 1

        result = nums[0]
        start = end = 0                   # best subarray so far: just nums[0]

        prefixStart = 0                   # where the current prefix product began
        suffixEnd = n - 1                 # where the current suffix product began (its right end)

        for i in range(n):

            # Reset prefix after zero: the new product starts here, at i
            if prefix == 0:
                prefix = 1
                prefixStart = i

            # Reset suffix after zero: the new product starts here, at n - i - 1
            if suffix == 0:
                suffix = 1
                suffixEnd = n - i - 1

            # Left to right: prefix = product of nums[prefixStart .. i]
            prefix *= nums[i]

            if prefix > result:
                result = prefix
                start = prefixStart
                end = i

            # Right to left: suffix = product of nums[j .. suffixEnd]
            j = n - i - 1
            suffix *= nums[j]

            if suffix > result:
                result = suffix
                start = j
                end = suffixEnd

        return result, start, end         # the subarray is nums[start : end + 1]

# Example: nums = [2, 3, -2, 4]   (the prefix scan finds it)
#
#   Index   Prefix product   Subarray
#   -----   --------------   --------------
#   0       2                [2]
#   1       6                [2, 3]          <- new best: start = prefixStart = 0, end = 1
#   2       -12              [2, 3, -2]
#   3       -48              [2, 3, -2, 4]
#
#   result = 6, start = 0, end = 1
#
# What about suffix? nums = [-1, 2, 3]   (the suffix scan finds it)
#
#   Index (j)   Suffix product   Subarray
#   ---------   --------------   ----------
#   2           3                [3]          <- best 3: start = j = 2, end = suffixEnd = 2
#   1           6                [2, 3]       <- best 6: start = j = 1, end = suffixEnd = 2
#   0           -6               [-1, 2, 3]
#
#   result = 6, start = 1, end = 2
#   (the prefix scan only ever sees -1, -2, -6, so it never finds 6)
#
# With a zero: nums = [3, -1, 0, 2, 5, -3]   -> 10 from [2, 5] (indexes 3..4)
#
#   i   prefix (covers)              best?            j   suffix (covers)              best?
#   -   --------------------------   --------------   -   --------------------------   -----
#   0   3      [0..0]                no (3 = 3)       5   -3     [5..5]                no
#   1   -3     [0..1]                no               4   -15    [4..5]                no
#   2   0      [0..2]                no               3   -30    [3..5]                no
#   3   reset: prefixStart = 3
#       2      [3..3]                no               2   0      [2..5]                no
#   4   10     [3..4]                YES: 10, (3, 4)      reset: suffixEnd = 1
#                                                     1   -1     [1..1]                no
#   5   -30    [3..5]                no               0   -3     [0..1]                no
#
#   result = 10, start = 3, end = 4  ->  nums[3:5] = [2, 5] ✓
#
# The key difference:
#   - For prefix, the subarray starts at prefixStart and ends at i.
#   - For suffix, the subarray starts at j and ends at suffixEnd.
#   - Both boundaries reset when a zero is encountered.
# This gives the maximum product AND the exact subarray that produced it, so you don't
# need to switch to dynamic programming to get the indexes.
#
# Complexity: Time O(n), Space O(1) (just a few extra variables).


# =====================================================================================
# SOLUTION 2: Dynamic Programming (Maximum and Minimum Products)
# =====================================================================================
# Idea: At each element, track two values:
#   - maxProd: The largest product of a subarray ending at the current position.
#   - minProd: The smallest product of a subarray ending at the current position.
#
# Why do we need the minimum? Because multiplying a negative number by another
# negative number can produce a large positive product.

class SolutionDP:
    def maxProduct(self, nums: list[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0]
        result = nums[0]

        for num in nums[1:]:
            # Save the previous maximum multiplied by num
            temp = maxProd * num

            # Find the new maximum product
            maxProd = max(num, temp, minProd * num)

            # Find the new minimum product
            minProd = min(num, temp, minProd * num)

            # Update the overall maximum
            result = max(result, maxProd)

        return result

# Explanation of each line
#
# 1. Initialise maximum, minimum and result.
#        maxProd = nums[0]
#        minProd = nums[0]
#        result = nums[0]
#    We start with the first element because every subarray must contain at least one
#    element.
#
# 2. Start looping from the second element.
#        for num in nums[1:]:
#    The first element has already been used to initialise our variables.
#
# 3. Save the previous maximum product multiplied by the current number.
#        temp = maxProd * num
#    We store this before changing maxProd, because the minimum calculation still needs
#    the previous maximum.
#
# 4. Calculate the new maximum product.
#        maxProd = max(num, temp, minProd * num)
#    We compare three possibilities:
#      - num: Start a new subarray at the current number.
#      - temp: Extend the previous maximum-product subarray.
#      - minProd * num: Extend the previous minimum-product subarray, which could
#        become the maximum when num is negative.
#
# 5. Calculate the new minimum product.
#        minProd = min(num, temp, minProd * num)
#    Similarly, we find the smallest product ending at the current position.
#    This is important because a very negative product might become a large positive
#    product later.
#    (minProd on the right side is still the OLD minProd, because it is read before
#     this line assigns it. maxProd was already overwritten, which is why we saved temp.)
#
# 6. Update the overall result.
#        result = max(result, maxProd)
#    We keep the largest product encountered anywhere in the array.
#
# Walkthrough
#   Input: nums = [-2, 3, -4]
#
#   Initially:
#     maxProd = -2
#     minProd = -2
#     result = -2
#
#   Iteration 1: num = 3
#     temp = -2 * 3                     # -6
#     maxProd = max(3, -6, -6)          # 3
#     minProd = min(3, -6, -6)          # -6
#     result = max(-2, 3)               # 3
#
#   Iteration 2: num = -4
#     temp = 3 * -4                     # -12
#     maxProd = max(-4, -12, -6 * -4)   # 24
#     minProd = min(-4, -12, -6 * -4)   # -12
#     result = max(3, 24)               # 24
#
#   Final result: 24, from subarray [-2, 3, -4].
#
# Summary table
#   Current number   maxProd   minProd   Result
#   --------------   -------   -------   ------
#   -2 (initial)     -2        -2        -2
#   3                3         -6        3
#   -4               24        -12       24
#
# Complexity: Time O(n), Space O(1).


# =====================================================================================
# Which solution should you use in an interview?
# =====================================================================================
#
#                          Prefix/Suffix         Dynamic Programming
#   Time                   O(n)                  O(n)
#   Space                  O(1)                  O(1)
#   Main idea              Scan both directions  Track maximum and minimum
#   Zero handling          Reset products        Naturally handled
#   Difficulty to explain  Relatively simple     Requires more reasoning
#
# I would recommend learning both, but start with prefix/suffix because it is
# straightforward to implement.
#
# For dynamic programming, remember this important interview explanation:
#   We track both the maximum and minimum products because multiplying two negative
#   numbers produces a positive number. A minimum product at one position could become
#   the maximum product at the next position.
#
# That is the key insight behind the problem.


if __name__ == "__main__":
    import random

    def brute(nums):
        best = nums[0]
        for i in range(len(nums)):
            p = 1
            for j in range(i, len(nums)):
                p *= nums[j]
                best = max(best, p)
        return best

    for _ in range(3000):
        nums = [random.randint(-4, 4) for _ in range(random.randint(1, 9))]
        assert Solution().maxProduct(nums) == brute(nums) == SolutionDP().maxProduct(nums), nums
        best, st, en = SolutionWithIndexes().maxProduct(nums)
        p = 1
        for v in nums[st:en + 1]:
            p *= v
        assert best == brute(nums) and p == best, nums
    print(Solution().maxProduct([2, 3, -2, 4]), Solution().maxProduct([-2, 0, -1]),
          SolutionDP().maxProduct([-2, 3, -4]))
