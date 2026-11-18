# Binary String Expansion: Character at an Index
# (Amazon SDE-1 2026, round 4 bar raiser. Close cousin of LeetCode 779, K-th Symbol in Grammar.)
#
# =====================================================================================
# QUESTION (as asked in the Amazon interview)
# =====================================================================================
# Given a binary string s. In one transformation, every character is replaced at once:
#
#     every 0 becomes 00
#     every 1 becomes 10
#
# After performing this transformation n times, return the character at index k
# (0-indexed) of the final string.
#
# (The interview wording used "k times" and "the i-th index"; here n = number of
#  transformations and k = the index, to match the code below.)
#
# Example:
#   s = "01", n = 1, k = 2
#   After one transformation:  "0" -> "00", "1" -> "10"   =>  "0010"
#   index 2 -> "1"
#   Answer = 1
#
# The catch: every transformation DOUBLES the length. After n transformations the
# string has len(s) * 2^n characters. n = 60 is already more characters than any
# computer can hold, so building the string is not an option.
#
# VARIANT (the one most tutorials show, LeetCode 779 style):
#     every 0 becomes 01
#     every 1 becomes 10
# Same idea, only the "odd index" rule changes. It is covered at the bottom (Version B).
#
# =====================================================================================
# KEY IDEA: work BACKWARDS from the index to the original character
# =====================================================================================
#
#   Every character produces exactly TWO characters (its two "children").
#
#       previous level:      c0        c1        c2
#                           /  \      /  \      /  \
#       next level:       [0]  [1]  [2]  [3]  [4]  [5]      <- indexes
#
#   - Index 0 and 1 come from parent index 0.
#   - Index 2 and 3 come from parent index 1.
#   - Index 4 and 5 come from parent index 2.
#   => the parent of index k is index k // 2, one level up (n - 1).
#
#   - EVEN k -> the FIRST child of its parent
#   - ODD k  -> the SECOND child of its parent
#
#   So: find the parent's character (recursion), then use the rule to decide what the
#   first or second child of that parent looks like. Keep going up until n == 0, where
#   the answer is just s[k] in the original string.
#
#   We are NOT checking whether the PARENT's index is even or odd. We check whether the
#   CURRENT index k is the first or the second child produced by that parent.


# =====================================================================================
# BRUTE FORCE (only to understand / test, way too slow for big n)
# =====================================================================================
def build_amazon(s: str, n: int) -> str:
    for _ in range(n):
        s = "".join("00" if c == "0" else "10" for c in s)
    return s
# Time O(len(s) * 2^n), Space O(len(s) * 2^n). Doubles every round -> explodes.


# =====================================================================================
# VERSION A: the Amazon rules (0 -> 00, 1 -> 10)
# =====================================================================================
#
#   What each parent turns into:
#
#   Parent   first child (EVEN k)   second child (ODD k)
#   ------   --------------------   --------------------
#   0        0                      0
#   1        1                      0
#
#   - EVEN k: the first child is always the SAME as the parent.
#   - ODD k:  the second child is always 0, whatever the parent was.

class Solution:
    def getCharacter(self, s: str, n: int, k: int) -> str:
        def solve(k, n):
            # Base case: no more expansions, read the original string
            if n == 0:
                return int(s[k])

            # Find the parent character (index k // 2, one expansion earlier)
            parent = solve(k // 2, n - 1)

            # Even index: first child, same as parent
            if k % 2 == 0:
                return parent

            # Odd index: second child, always 0 ("00" and "10" both end in 0)
            return 0

        return str(solve(k, n))

# Small speed-up you can mention: for an ODD k the answer is 0 no matter what the
# parent is, so you could return 0 straight away without recursing.
#
# WALKTHROUGH 1 (the interview example): s = "01", n = 1, k = 2
#
#   solve(2, 1): n != 0, parent = solve(2 // 2 = 1, 0)
#     solve(1, 0): n == 0 -> s[1] = "1" -> 1
#   solve(2, 1): k = 2 is EVEN -> same as parent -> 1
#   Answer: "1"   (check: "0010"[2] = "1") ✓
#
# WALKTHROUGH 2: s = "01", n = 2, k = 4
#
#   level 0:  0        1                      "01"
#   level 1:  00       10                     "0010"
#   level 2:  00 00    10 00                  "00001000"
#   index:    01 23    45 67                  -> index 4 is "1"
#
#   solve(4, 2): parent = solve(2, 1)
#     solve(2, 1): parent = solve(1, 0)
#       solve(1, 0): base case -> s[1] = 1
#     solve(2, 1): k = 2 EVEN -> 1
#   solve(4, 2): k = 4 EVEN -> 1
#   Answer: "1" ✓
#
#   And k = 5 in the same string: 5 is ODD -> 0 ("00001000"[5] = "0") ✓
#
# Bonus O(1)-style answer for Version A (say it as a follow-up):
#   Any odd step on the way up gives 0. So the answer is 1 ONLY if every step was even
#   (k's last n bits are all 0, i.e. k % 2^n == 0) AND the original character
#   s[k >> n] (= s[k // 2^n]) is "1".

class SolutionClosedForm:
    def getCharacter(self, s: str, n: int, k: int) -> str:
        low_bits_all_zero = (k & ((1 << n) - 1)) == 0      # k % 2^n == 0
        return "1" if low_bits_all_zero and s[k >> n] == "1" else "0"

# Complexity (Version A)
#   Recursion:    Time O(n), one call per expansion level.
#                 Space O(n), the recursion stack is n calls deep.
#   Closed form:  Time O(n) to build the bit mask (O(1) for normal-size numbers),
#                 Space O(1).
#   Compare: the brute force is O(len(s) * 2^n) time and space.


# =====================================================================================
# VERSION B: the variant rules (0 -> 01, 1 -> 10)
# =====================================================================================
# Yes! We can solve it using recursion without generating the expanded string.
# The idea is to work backwards from the requested index to the original character.

class SolutionVariant:
    def getCharacter(self, s: str, n: int, k: int) -> str:
        def solve(k, n):
            # Base case: no more expansions
            if n == 0:
                return int(s[k])

            # Find the parent character
            parent = solve(k // 2, n - 1)

            # Even index: same as parent
            if k % 2 == 0:
                return parent

            # Odd index: opposite of parent
            return 1 - parent

        return str(solve(k, n))

# Explanation of each line
#
# Step 1: Base case
#     if n == 0:
#         return int(s[k])
#   When there are no expansions left, we simply return the character at index k in
#   the original string.
#
# Step 2: Find the parent
#     parent = solve(k // 2, n - 1)
#   Every character produces exactly two characters. Therefore:
#     - Index 0 and 1 come from parent index 0.
#     - Index 2 and 3 come from parent index 1.
#     - Index 4 and 5 come from parent index 2.
#   That's why we use k // 2 to find the parent index.
#   We also use n - 1 because we are moving back one expansion level.
#
# Step 3: Check whether the index is even or odd
#     if k % 2 == 0:
#         return parent
#     return 1 - parent
#
#   Parent   Even child index   Odd child index
#   ------   ----------------   ---------------
#   0        0                  1
#   1        1                  0
#
#   At an even index, the character remains the same.
#   At an odd index, the character flips.
#
# Why even = same and odd = opposite?
#   Look at the rules: 0 -> 01, 1 -> 10.
#   The first character stays the same, while the second character is always the
#   opposite.
#
#     parent = 0  ->  0 1            parent = 1  ->  1 0
#                     ^ ^                            ^ ^
#                  same opposite                  same opposite
#
#   Example:
#     Parent string:    0   1   1
#                       ↓   ↓   ↓
#     Expanded string:  01  10  10
#
#     Final string:     011010
#     Index:            012345
#
#     k   char   parent (index k // 2)   explanation
#     -   ----   ---------------------   ---------------
#     0   0      0  (index 0)            even -> same
#     1   1      0  (index 0)            odd  -> opposite
#     2   1      1  (index 1)            even -> same
#     3   0      1  (index 1)            odd  -> opposite
#     4   1      1  (index 2)            even -> same
#     5   0      1  (index 2)            odd  -> opposite
#
#   Indices 0, 2, 4 are even, so their characters match their parents.
#   Indices 1, 3, 5 are odd, so their characters are opposite to their parents.
#
#   k % 2 is the remainder when dividing k by 2:  4 % 2 == 0 (even), 5 % 2 == 1 (odd).
#
# Why return 1 - parent?
#   Because parent can only be 0 or 1:
#     1 - 0 = 1
#     1 - 1 = 0
#   So 1 - parent simply flips the binary character.
#
# How does this connect to the recursion?
#   parent = solve(k // 2, n - 1) finds the character at the previous expansion level
#   that produced our current character. For k = 5: k // 2 = 2, so index 5 came from
#   index 2 in the previous expansion. 5 is odd, so we return the opposite of that
#   parent.
#
#   Even k -> first child  -> same as parent.
#   Odd k  -> second child -> opposite of parent.
#   That's the entire reason this recursive solution works.
#
# RECURSIVE WALKTHROUGH: s = "0", n = 3, k = 5
#
#   level 0:  0
#   level 1:  01
#   level 2:  0110
#   level 3:  01101001        index 5 -> "0"
#             01234567
#
#   Going DOWN (asking for the parent each time):
#     solve(5, 3) -> parent = solve(5 // 2 = 2, 2)
#     solve(2, 2) -> parent = solve(2 // 2 = 1, 1)
#     solve(1, 1) -> parent = solve(1 // 2 = 0, 0)
#     solve(0, 0) -> base case: s[0] = "0" -> 0
#
#   Coming back UP (applying even/odd at each level):
#     solve(1, 1): k = 1 ODD  -> 1 - 0 = 1      (level 1 "01",       index 1 = 1) ✓
#     solve(2, 2): k = 2 EVEN -> same = 1       (level 2 "0110",     index 2 = 1) ✓
#     solve(5, 3): k = 5 ODD  -> 1 - 1 = 0      (level 3 "01101001", index 5 = 0) ✓
#
#   Answer: "0"
#
# Bonus O(1)-style answer for Version B: every odd step flips, every even step keeps.
#   The number of flips = the number of 1-bits in the last n bits of k. An even number
#   of flips gives back the original character; an odd number flips it.
#     k = 5 = 0b101, n = 3 -> two 1-bits -> even -> no change -> s[0] = "0" ✓

class SolutionVariantClosedForm:
    def getCharacter(self, s: str, n: int, k: int) -> str:
        flips = bin(k & ((1 << n) - 1)).count("1")
        return str(int(s[k >> n]) ^ (flips % 2))

# Complexity (Version B): same as Version A.
#   Recursion:    Time O(n), Space O(n) for the recursion stack.
#   Closed form:  Time O(n) to count the bits (O(1) for normal-size numbers), Space O(1).
#
# =====================================================================================
# The two versions side by side
# =====================================================================================
#
#                    Version A (Amazon)         Version B (variant)
#   rules            0 -> 00, 1 -> 10           0 -> 01, 1 -> 10
#   even k           same as parent             same as parent
#   odd k            always 0                   opposite of parent (1 - parent)
#   parent           k // 2, level n - 1        k // 2, level n - 1
#   closed form      1 only if k % 2^n == 0     s[k >> n] flipped once per
#                    and s[k >> n] == "1"       1-bit in the last n bits of k
#
#   The recursion skeleton (base case, parent = solve(k // 2, n - 1), check k % 2)
#   is the same for ANY "every character becomes 2 characters" rule. Only the last
#   step changes: write the parent -> (first child, second child) table and read it.


if __name__ == "__main__":
    import random

    def build_variant(s, n):
        for _ in range(n):
            s = "".join("01" if c == "0" else "10" for c in s)
        return s

    for _ in range(2000):
        s = "".join(random.choice("01") for _ in range(random.randint(1, 4)))
        n = random.randint(0, 6)
        k = random.randrange(len(s) << n)
        a, b = build_amazon(s, n)[k], build_variant(s, n)[k]
        assert Solution().getCharacter(s, n, k) == a == SolutionClosedForm().getCharacter(s, n, k)
        assert SolutionVariant().getCharacter(s, n, k) == b == SolutionVariantClosedForm().getCharacter(s, n, k)
    print(Solution().getCharacter("01", 1, 2), Solution().getCharacter("01", 2, 4),
          SolutionVariant().getCharacter("0", 3, 5))
