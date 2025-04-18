
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

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0
        for x, v in count.items():
            group_size = x + 1
            groups = ceil(v / group_size)
            total += groups * group_size
        return total
