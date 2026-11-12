# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Video explanation: https://www.youtube.com/watch?v=K81C31ytOZE

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxdia=0

        def dfs(node):
            if not node:
                return 0 # height of an empty tree = 0 (height counts NODES, so a leaf = 1)
                         # NOTE: this used to be -1 with left+right below, which is WRONG (gave 1
                         # instead of 3 for the tree in the dry run). See "Why 0 and not -1" below.
            left=dfs(node.left)
            right=dfs(node.right)

            # we need to calc the heighest diameter for each node..which will become the diameter for the whole tree....because of non simple trees with different diameters

            self.maxdia=max(self.maxdia,left+right) #(left+right) this is the height of left + height on right ....for each recursive point
                                                    # each child's height already includes the edge up to this node,
                                                    # so left+right = number of EDGES on the longest path through this node

            #this means height of the children node + 1(height to reach the parent)
            #     1        ##here height of children for 1 is ( 2 on left and 3 on the right) now + 1 height needed to get to parent
            #              ##1+max(2,3) = 4    diameter here: 2+3 = 5 (4-2-1-3-5-6), the answer
            #   /    \
            #  2      3     ...1+max(1,2)= 3          diameter here: 1+2 = 3        ^
            # /      /  \                                                           |
            #4       8    5....1+max(0,1) = 1+1 =2   diameter here: 0+1 = 1        |
            #1+max(0,0)    \                                                       |
            #   =1          6....1+max(0,0)= 1+0= 1  diameter here: 0+0 = 0        |  start bottom to up to understand
            #
            #(2 is 1+max(1,0) = 2, and 8 is 1+max(0,0) = 1 like 4)
            #(the None below every leaf returns 0: that's the 'one step further' level where it turns and goes up)
            #(the OLD -1 version gave: 6=0, 5=1, 4=0, 8=0, 3=2, 2=1, 1=3, one less each because it counted
            # edges. Those heights were right, but then the diameter needs left+right+2, not left+right)

            return 1+max(left,right) #from 1+hr or 1+hl..this is the height.....so each step returns this....max
        dfs(root)
        return self.maxdia


# ==================== The recursion goes ONE STEP PAST the last level ====================
# A leaf still calls dfs(leaf.left) and dfs(leaf.right). Those are None, so the recursion
# always reaches the "None level" below the leaves. That's where `if not node: return 0`
# stops it, and from there the answers flow back UP to the root.
#
#             1
#            / \
#           2   3
#          / \  / \
#         4  5 N   N        <- 3 is a leaf, but dfs still visits its None children
#        /\  /\
#       N N  N N            <- the "one step further" level: early exit, return 0
#                              everything after this flows UPWARD


# ==================== Why 0 and not -1 ====================
# The base value and the diameter formula MUST match:
#
#   return 0  -> height counts NODES (leaf = 1). A child's height already includes the edge
#                up to its parent, so diameter through a node = left + right.
#   return -1 -> height counts EDGES (leaf = 0). The two edges from the node down to its
#                children are NOT counted yet, so diameter = left + right + 2 (NeetCode's way).
#
# The old code used -1 with plain left + right. Trace on the dry-run tree (1, 2, 3, 4, 5):
#
#   node | left | right | left+right      | returns
#   -----+------+-------+-----------------+--------
#   4    |  -1  |  -1   | -2 (maxdia 0)   |   0
#   5    |  -1  |  -1   | -2 (maxdia 0)   |   0
#   3    |  -1  |  -1   | -2 (maxdia 0)   |   0
#   2    |   0  |   0   |  0 (maxdia 0)   |   1      <- path 4-2-5 is 2 edges, but we got 0
#   1    |   1  |   0   |  1 (maxdia 1)   |   2
#   answer 1, WRONG (should be 3)
#
# The return line 1+max(left,right) is right either way. Only the diameter line changes.
#
# Equivalent -1 version (NeetCode):
#
#   def dfs(node):
#       if not node:
#           return -1
#       left = dfs(node.left)
#       right = dfs(node.right)
#       self.maxdia = max(self.maxdia, left + right + 2)   # +2 = the two edges down to the children
#       return 1 + max(left, right)


# ==================== Dry run ====================
# Suppose we have the following binary tree:
#
#     1
#    / \
#   2   3
#  / \
# 4   5
#
# The maximum diameter here is 3 (the path 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3, which contains 3 edges).
#
# Step-by-Step Execution
#
# Our dfs(node) function tracks a global variable self.maxdia (initialized to 0) and returns the height of the subtree.
#
# 1. Processing Leaf Nodes (Nodes 4, 5, and 3)
#
# - Node 4:
#     - Calls dfs(None) for left and right. Both return 0.
#     - Diameter check: left (0) + right (0) = 0. self.maxdia remains 0.
#     - Returns its height: 1 + max(0, 0) = 1.
# - Node 5:
#     - Same as Node 4. Left and right return 0.
#     - self.maxdia remains 0.
#     - Returns its height: 1.
# - Node 3:
#     - Left and right return 0.
#     - self.maxdia remains 0.
#     - Returns its height: 1.
#
# 2. Processing Node 2
#
# - Node 2 receives the heights from its children:
#     - left_height = 1 (from Node 4)
#     - right_height = 1 (from Node 5)
# - Update Diameter: The path passing through Node 2 is 1 + 1 = 2. We update self.maxdia = max(0, 2) = 2.
# - Return Height: Node 2 returns its own height to its parent: 1 + max(1, 1) = 2.
#
# 3. Processing Root Node 1
#
# - Node 1 receives the heights from its children:
#     - left_height = 2 (from Node 2)
#     - right_height = 1 (from Node 3)
# - Update Diameter: The path passing through Node 1 is 2 + 1 = 3. We update self.maxdia = max(2, 3) = 3.
# - Return Height: Node 1 returns its height: 1 + max(2, 1) = 3.
#
# Answer: self.maxdia = 3
