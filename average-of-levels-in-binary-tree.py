# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        s=defaultdict(float)
        t=defaultdict(int)
        def dfs(node,h):
            if node==None:
                return
            s[h]+=node.val
            t[h]+=1
            dfs(node.left,h+1)
            dfs(node.right,h+1)
            
        dfs(root,0)
        
        return [s[i]/t[i] for i in range(len(s))]
        