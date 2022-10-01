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
        


        #using optimum solution

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
       
        
            #if both of them are empty
        if not p and not q:
            return True
            #if one of them is empty or #if two of them are not empty..we compare value
        if not p or not q or p.val!=q.val:
            return False
            
            
        #then we compare value of left nodes to value of right nodes
        #they must be true and true ..else it returns false
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        
        