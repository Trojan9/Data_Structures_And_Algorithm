# brute force solution..my own

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        self.myBool=False
        def dfs(node,sums):
            if not node:
                return 
    #sums+node.val because  the sums has not being updated yet till we calldfs again      
            if not node.left and not node.right and (sums+node.val)==targetSum:
                self.myBool=True
                return True
            #normal recursion thing
            dfs(node.left,sums+node.val)
            dfs(node.right,sums+node.val)
            #initialize sum to 0
        dfs(root,0)
        return self.myBool

#time complexity O(n)

#optimum solution
#its almost the samething man as what you did above

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        self.myBool=False
        def dfs(node,sums):
            if not node:
                return False
    #sums+node.val because  the sums has not being updated yet till we calldfs again      
            if not node.left and not node.right and (sums+node.val)==targetSum:
                self.myBool=True
                return True
            #normal recursion thing
            return dfs(node.left,sums+node.val) or dfs(node.right,sums+node.val)
            #initialize sum to 0
        return dfs(root,0)
        #return self.myBool
