# Amazon SDE-I 50, #9: Valid Palindrome (Easy)  [Two Pointers]
#
# Brief: True if it reads the same both ways, alphanumeric only, case-insensitive. `"A man, a
# plan, a canal: Panama"` → True.
#
# In plain words: does it read the same backwards, ignoring punctuation and case? Put a pointer at
# each end, skip anything that isn't a letter or digit, compare the two characters lowercased,
# step inward. If any mirrored pair differs, it's not a palindrome.
#
# Why it works: a palindrome mirrors around its centre, so the character at distance i from the
# start must equal the one at distance i from the end, exactly the pairs the two pointers compare.
#
# Algorithm
# 1. `l`, `r` at ends. 2. Skip non-alphanumerics each side. 3. Compare lowercased; mismatch →
#    False. 4. Step inward.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

# Complexity: Time O(n), Space O(1).
