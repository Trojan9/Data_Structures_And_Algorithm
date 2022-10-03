# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxdia=0
        
        def dfs(node):
            if not node:
                return -1 #watch the neetcode video to understand the concept 
            left=dfs(node.left)
            right=dfs(node.right)
            self.maxdia=max(self.maxdia,2+left+right) #diameter formular is 2+left+right
            
            return 1+max(left,right) #from 1+hr or 1+hl..this is the height
        dfs(root)
        return self.maxdia
            
        