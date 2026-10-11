# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #merge 2 binary trees solution idea..
        if not root:
            return None
        
        #get left and right nodes
        root.left=self.invertTree(root.left)
        root.right=self.invertTree(root.right)
        
        #the same trick we use to invert in linked list
        #invert the nodes
        temp=root.left
        root.left=root.right
        root.right=temp
        return root
    