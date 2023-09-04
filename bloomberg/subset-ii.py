class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sub=[[]]
        nums = sorted(nums)
        for element in nums:
            #javascript way
            # sub=[...sub,[...k, element]for k in sub]
            sub=sub + [ k + [element] for k in sub if k+[element] not in sub]
        return sub