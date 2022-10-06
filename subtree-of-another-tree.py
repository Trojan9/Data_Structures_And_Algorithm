# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        #if subtree is none or null it is a subtree of both null or non null tree i.e you will see null value subtree in a leaf node of a tree always
       
        if not subRoot:
            return True
         #but a non null subtree is not a subtree of a None Tree
        if not root and subRoot:
            return False
        
        #then they are both non null..we check if its sameTree
        if self.isSameTree(root,subRoot):
            return True
        
        #note that its just the root and its branches we catered for already ..now we need to shift our root to left and right so we can cater for all nodes
        #so we use the recursive loop, note the subroot doesn't move..cuz its what we are comparing with
        #the we use or cuz we only expect the ans in just one part of the tree....if its and, then we need both side of tree to be satisfied
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
        
        #so first we would use an helper function to check if both trees are the same ...refer back to same Trees question that we solved
    def isSameTree(self,p,q):
        #if both are empty
        if not p and not q:
            return True
        #if one of them is empty or p not qual to q then its not the same now
        if not p or not q or p.val!=q.val:
            return False
        
        #else they are the same them we perform the recursive loop on it
        
        #i.e module or an entity keeps making calls to itself repeatedly,
        
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
    
    
    
    #this is solved in O(t*s)
    
    #where t and s are the nodes of tree and subtree