# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #remember to always declare your variable with self.
        self.maximum=float(0)
        
        #don't forget the edge case of None root also i.e root=[]..return 0
        
        if not root:
            return 0
        
        def dfs(node,h):
            if not node:
                return
            if not node.left and not node.right:
                self.maximum=max(h,self.maximum)
            dfs(node.left,h+1)
            dfs(node.right,h+1)
        #we start from 1 because of 1+hl or 1+hr
        dfs(root,1)
        return self.maximum
        