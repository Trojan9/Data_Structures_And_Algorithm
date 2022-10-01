#my own brute force solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #using dfs
        self.check=""
        self.check2=""
        #check out dfs function from previous solved questions
        def dfs(node,num):
            if not node:
                if num==1:
                    self.check=self.check+"null"
                else:
                    self.check2=self.check2+"null"
                return
            if num==1:
                self.check=self.check+str(node.val)
            else:
                self.check2=self.check2+str(node.val)
            dfs(node.left,num)
            dfs(node.right,num)
        dfs(p,1)
        dfs(q,2)
        return self.check==self.check2
        