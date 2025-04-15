# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #so the idea is to use inequality equations so for it to be valid we must have
        #left< val < right....so we are using 2 pointers of lower and higher....when we move left, we update the right pointer to present node val,and leave the left pointer val....when we move right we update the left pointer to present node value and leave the right pointer val
        def dfs(p,left,right):
            #i.e it did not see any defaulting node not adhering to these rule
            if not p:
                return True
            #then we check if any node doesn't adhere left< val < right
            if not (left<p.val and p.val<right):
                return False
            #return the and operator for both node.left and node.right
            #when we move left, we update the right pointer to present node val,and leave the left pointer val....when we move right we update the left pointer to present node value and leave the right pointer val
            return (dfs(p.left,left,p.val)and dfs(p.right,p.val,right))
        #start from -infinity to infinity....since we don't know whats at the root
        return dfs(root,float('-inf'),float('inf'))




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque()
        # Each item: (node, min_val, max_val)
        queue.append((root, float('-inf'), float('inf')))
        
        while queue:
            node,minval,maxval = queue.popleft()

            if not (minval< node.val< maxval):
                return False

            if node.left:
                queue.append((node.left,minval,node.val))
            if node.right:
                queue.append((node.right,node.val,maxval))
            
        return True

            
First iteration:
Node: 5

Allowed range: (-∞, ∞)

✅ 5 is valid

Then:
Left child 4 → range (-∞, 5)

Right child 6 → range (5, ∞)

✅ So far, all good.

Now visit 6:
Left child 3 → range (5, 6)

❌ 3 is not greater than 5, so the tree is invalid.


Each node’s value must be:

python
Copy
Edit
min_val < node.val < max_val
Left child: max becomes node.val

Right child: min becomes node.val

