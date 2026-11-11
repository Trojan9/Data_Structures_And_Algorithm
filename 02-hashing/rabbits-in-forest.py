
#answers = [1, 1, 2]
#print(numRabbits(answers))  # Output: 5

#Explanation:

#Two rabbits say "1": They can be in one group of 2 rabbits.

#One rabbit says "2": Requires a group of 3 rabbits.

#Total rabbits: 2 (from the first group) + 3 (from the second group) = 5.​


#get counter for each number

#get number of groups that can fit those claims

#groups = ceil(number_of_rabbit_saying_the_same / group_size)

#group_size is just claim + 1 

#Say 5 rabbits say 2, meaning they each claim there are 3 rabbits (2 others + themselves) of the same color:

#x = 2 → group_size = 3

#v = 5 (5 rabbits saying 2)

#We can form:

#ceil(5 / 3) = 2 groups (because one group can hold 3 rabbits, we need 2 groups to fit 5)

#So total rabbits from this answer = 2 * 3 = 6

from collections import Counter
from math import ceil
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0
        for x, v in count.items():
            group_size = x + 1
            groups = ceil(v / group_size)
            total += groups * group_size
        return total


# ==================== Dry run: answers = [1, 1, 2] ====================
#
# What the input means: we asked 3 rabbits "how many OTHER rabbits share your colour?"
#   rabbit A said 1, rabbit B said 1, rabbit C said 2.
# We want the SMALLEST number of rabbits that could be in the forest (including ones we never asked).
#
#   count = Counter([1, 1, 2]) = {1: 2, 2: 1}
#           -> the answer "1" was given by 2 rabbits, the answer "2" was given by 1 rabbit
#   total = 0
#
#   x = 1, v = 2:
#       group_size = 1 + 1 = 2          (1 other + itself)
#       groups     = ceil(2 / 2) = 1    (A and B fit together in one red group of 2)
#       total     += 1 * 2  -> total = 2
#
#   x = 2, v = 1:
#       group_size = 2 + 1 = 3          (2 others + itself)
#       groups     = ceil(1 / 3) = 1    (C needs a group of 3, even though we only met C)
#       total     += 1 * 3  -> total = 5
#
#   return 5     ->  2 red (A, B) + 3 blue (C + 2 blue rabbits we never asked)
#
# Why C can't join the red group: red is already full at 2 rabbits, and C says its colour has
# 3 rabbits. Different group sizes = different colours.
#
#
# ==================== Why ceil (round UP)? ====================
#
# v / group_size tells us how many groups the v rabbits fill. It's often a fraction, and a
# fraction of a group still means a WHOLE group exists, because every rabbit in a colour group
# is real, whether we asked it or not.
#
#   - Each colour group that says x has EXACTLY x + 1 rabbits. No more, no less.
#   - So at most x + 1 of the rabbits we asked can share one colour. If more rabbits gave the same
#     answer, the extras must belong to a NEW colour group of the same size.
#   - A half-filled group is still a full group in the forest: the members we didn't ask exist.
#
# That "any leftover rabbits still need a whole group" is exactly what rounding up does:
#
#   v rabbits said 2 (group_size 3)   v / 3      ceil   floor (wrong)
#   ------------------------------   -------    ----   ------------
#   1 rabbit                          0.33        1      0   <- floor says no group at all, but C exists!
#   3 rabbits                         1.00        1      1   <- exactly one full group
#   4 rabbits                         1.33        2      1   <- 3 fill one group, the 4th needs another
#   5 rabbits                         1.67        2      1
#   6 rabbits                         2.00        2      2
#
#   e.g. 4 rabbits say "2": 3 of them can be blue (blue is now full). The 4th also says "2", so it
#   is a different colour, say green, and green has 3 rabbits too -> 2 groups * 3 = 6 rabbits.
#
# int(v / group_size) or v // group_size would round DOWN and drop those leftover rabbits.
#
# Same thing without math.ceil (integer-only trick you'll see a lot):
#   groups = (v + group_size - 1) // group_size
#   e.g. v=4, size=3: (4 + 2) // 3 = 2    v=3, size=3: (3 + 2) // 3 = 1

