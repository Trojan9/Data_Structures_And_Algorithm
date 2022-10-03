# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, node1, node2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        
        if not node1 and not node2:
            return None
        t1=node1.val if node1 else 0
        t2=node2.val if node2 else 0
           
        root=TreeNode(t1+t2)
            
        root.left=self.mergeTrees(node1.left if node1 else None,node2.left if node2 else None)
        root.right=self.mergeTrees(node1.right if node1 else None,node2.right if node2 else None)
        return root
            
        
        