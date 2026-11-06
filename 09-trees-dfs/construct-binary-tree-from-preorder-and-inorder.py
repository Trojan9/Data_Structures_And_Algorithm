# Amazon SDE-I 50, #40: Construct Tree from Preorder and Inorder (Medium)  [Trees]
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

# Brief: Rebuild the tree from preorder and inorder (unique values).
#
# In plain words: preorder lists root-first; inorder lists left-root-right. So `preorder[0]` is
# the root. Find it in inorder, everything to its left is the left subtree, everything to its
# right is the right. Recurse on those pieces, taking the next root from preorder each time.
#
# Why it works: the root's position in inorder exactly separates and sizes the two subtrees, so
# the recursion reconstructs the whole tree.
#
# Algorithm
# 1. Root = `preorder[0]`. 2. `mid` = its index in inorder. 3. Left = `preorder[1:mid+1]`,
#    `inorder[:mid]`; right = the rest.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

# Complexity: Time O(n²) here (slicing + index); O(n) with an index map. Space O(n).
