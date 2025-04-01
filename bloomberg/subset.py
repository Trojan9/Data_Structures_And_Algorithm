# looking at this solution to the question
# we start with an empty list of list as res [[]]
# then loop through the array  arr given in question
# every element from arr is interated with the elements in res to form a new array  
# e.g [[]] elemet=3   = [[],[]+[3]] = [[],[3]]
# [[],[3]] elemrnt=4  = [[],[3],[]+4,[3]+[4] ] = [[],[3],[4],[3,4]]
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub=[[]]
        for element in nums:
            #javascript way
            # sub=[...sub,[...k, element]for k in sub]
            sub=sub + [ k + [element] for k in sub]
        return sub

