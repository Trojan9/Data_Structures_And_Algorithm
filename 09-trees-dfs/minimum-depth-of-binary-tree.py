# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #creates the highest possible number..cus we need to compare min
        self.result=float('inf')

        #using the depth first approach
        def dfs(node,h):
            if node==None:
                
                return 
            if not node.left and not node.right:
                self.result=min(self.result,h)
            dfs(node.left,h+1)
            dfs(node.right,h+1)
  #we added 1 cuz of the root level node..check the formular in your jottings ..from formular height=1+hr or 1+hl       
        dfs(root,1) 
#if tree is empty then our result is still infinity..we change it to 0
        if self.result==float('inf'):
            self.result=0
        return self.result


#using the breath first search

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
       #using breath first approach
    #so first we create a queue with a tuple in it
    #the 1 is our level..so we start from one cuz of the 1+hr..1+hl
    #so we return 0 if tree root is empty
        if not root:
            return 0

        qu=deque([(root,1)])
        while qu:
            node,num=qu.popleft()
            if not node.left and not node.right:
                return num  #minimum depth is the first node without child...immediately we encountr that, we ill return....just for bfs
            #not don't use the elif..it will perform just one of it
            if node.left:
                qu.append((node.left,num+1))#don't forget the bracket for tuple
            if node.right:
                qu.append((node.right,num+1))#don't forget the bracket for tuple
        return -1




def minDepth(root):
    # Base Case 1: Empty tree has a depth of 0
    if not root:
        return 0
        
    # Base Case 2: Leaf node has a depth of 1
    if not root.left and not root.right:
        return 1
        
    # If left child is missing, we must force traversal down the right side
    if not root.left:
        return minDepth(root.right) + 1
        
    # If right child is missing, we must force traversal down the left side
    if not root.right:
        return minDepth(root.left) + 1
        
    # If both children exist, take the minimum of both sides
    return min(minDepth(root.left), minDepth(root.right)) + 1
