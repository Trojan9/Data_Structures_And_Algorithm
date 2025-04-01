class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sub=[[]]
#Because sorting helps group duplicates together, and that makes it easier to avoid generating duplicate subsets.
#[1, 2, 2]
#Then while building subsets, you'll always encounter the duplicate 2s next to each other, so it's easier to detect and prevent duplicates like [2, 1] and [1, 2] showing up twice in different forms.
        nums = sorted(nums)
        for element in nums:
            #javascript way
            # sub=[...sub,[...k, element]for k in sub]
            sub=sub + [ k + [element] for k in sub if k+[element] not in sub]
        return sub
