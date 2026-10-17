# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

https://www.youtube.com/watch?v=K81C31ytOZE 

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
            
            # we need to calc the heighest diameter for each node..which will become the diameter for the whole tree....because of non simple trees with different diameters
            
            self.maxdia=max(self.maxdia,left+right) #(left+right) this is the height of left + height on right ....for each recursive point

            #this means height of the children node + 1(height to reach the parent)
              1        ##here height of children for 1 is ( 1 on left and 2 on the right) now + 1 height needed to get to parent
            /    \
           2      3     ...1+max(0,1)= 2
          /      /  \
        4       8    5....1+max(-1,0) = 1+0 =1
           1+max(-1,-1) \
                =0       6....1+max(-1,-1)= 1-1= 0
        
            return 1+max(left,right) #from 1+hr or 1+hl..this is the height.....so each step returns this....max
        dfs(root)
        return self.maxdia






Suppose we have the following binary tree:
text
    1
   / \
  2   3
 / \
4   5
Use code with caution.
The maximum diameter here is 3 (the path 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3, which contains 3 edges).

Step-by-Step Execution

Our dfs(node) function tracks a global variable self.diameter (initialized to 0) and returns the height of the subtree.

1. Processing Leaf Nodes (Nodes 4, 5, and 3)

• Node 4:
	• Calls dfs(None) for left and right. Both return 0.
	• Diameter check: left (0) + right (0) = 0. self.diameter remains 0.
	• Returns its height: 1 + max(0, 0) = 1.
• Node 5:
	• Same as Node 4. Left and right return 0.
	• self.diameter remains 0.
	• Returns its height: 1.
• Node 3:
	• Left and right return 0.
	• self.diameter remains 0.
	• Returns its height: 1.

2. Processing Node 2

• Node 2 receives the heights from its children:
	• left_height = 1 (from Node 4)
	• right_height = 1 (from Node 5)
• Update Diameter: The path passing through Node 2 is 1 + 1 = 2. We update self.diameter = max(0, 2) = 2.
• Return Height: Node 2 returns its own height to its parent: 1 + max(1, 1) = 2.

3. Processing Root Node 1

• Node 1 receives the heights from its children:
	• left_height = 2 (from Node 2)
	• right_height = 1 (from Node 3)
• Update Diameter: The path passing through Node 1 is 2 + 1 = 3. We update self.diameter = max(2, 3) = 3.
• Return Height: Node 1 returns its height: 1 + max(2, 1) = 3.
            
        
