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
            
        #then we compare if both are not empty and are same values
        #then we compare value of left nodes to value of right nodes
        #they must be true and true ..else it returns false
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #35: Same Tree (Easy)  [Trees]
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

# Brief: True if two trees match in structure and values.
#
# In plain words: are two trees identical? Compare the roots; if they match, recursively compare
# their left children and their right children. Both empty = match; one empty or values differ =
# not a match.
#
# Why it works: two trees are identical iff roots match and both subtrees match, a naturally
# recursive definition with clean base cases.
#
# Algorithm
# 1. Both None → True. 2. One None or values differ → False. 3. Recurse left and right.

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right))

# Complexity: Time O(n), Space O(h).
