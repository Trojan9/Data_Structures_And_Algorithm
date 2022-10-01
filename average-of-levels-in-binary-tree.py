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
        

#using breath first solution DFS


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
        if not root:
            return 0
        s=defaultdict(float)
        t=defaultdict(int)
        qu=deque([(root,0)])
        while qu:
            node,num=qu.popleft()
            s[num]+=node.val
            t[num]+=1
            #not don't use the elif..it will perform just one of it
            if node.left:
                qu.append((node.left,num+1))#don't forget the bracket for tuple
            if node.right:
                qu.append((node.right,num+1))#don't forget the bracket for tuple
        
        return [s[i]/t[i] for i in range(len(s))]
        