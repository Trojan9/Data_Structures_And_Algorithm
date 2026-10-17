# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###here it reaches the last node traversely before changing
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


#using bfs ..deque
        ### make sure to invert the left and right before pushing the child nodes into the queue
##explanation
        original......1 goes in....
         1
        / \
       2   3
      / \
     4   5

           step 2   .......invert...left to right....then add the children if not none...so right is now 2 and we add the child....4 and 5
             1
            / \
           3   2
              / \
             4   5
step 3
             1
            / \
           3   2
              / \
             5   4
           
  ###more understanding  but space of 0(n)       
def invertTree(root):

    # If tree is empty
    if root is None:
        return

    q = deque()
    q.append(root)

    while len(q) > 0:

        # Get the front node
        curr = q.popleft()

        # Swap left and right child
        curr.left, curr.right = curr.right, curr.left

        # Push left child
        if curr.left is not None:
            q.append(curr.left)

        # Push right child
        if curr.right is not None:
            q.append(curr.right)





###same but straightforward


def invertTree(root):
    # Base Case
    if not root:
        return None
        
    # Swap the children
    root.left, root.right = root.right, root.left
    
    # Recurse on subtrees
    invertTree(root.left)
    invertTree(root.right)
    
    return root




The Initial Tree

Let's use a standard 3-level binary tree for our dry run:
text
       4
     /   \
    2     7
   / \   / \
  1   3 6   9
Use code with caution.

Step-by-Step Dry Run


Step 1: Start at the Root (Node 4)

• The function invertTree(Node 4) is called.
• Node 4 is not null, so it passes the base case.
• Swap Operation: The left child (Node 2) and right child (Node 7) are swapped.
• Tree State:
text
       4
     /   \
    7     2
   / \   / \
  6   9 1   3
Use code with caution.
(Notice that the entire subtrees moved with them. Now 7 is on the left, and 2 is on the right).

Step 2: Move to the New Left Child (Node 7)

• The code calls invertTree(root.left), which is now Node 7.
• Node 7 is not null.
• Swap Operation: Swap its left child (Node 6) and right child (Node 9).
• Tree State:
text
       4
     /   \
    7     2
   / \   / \
  9   6 1   3
Use code with caution.

Step 3: Dive Deeper Left (Node 9)

• The code calls invertTree(root.left), which is now Node 9.
• Node 9 is a leaf node. Its left and right children are both None.
• Swapping None with None leaves it unchanged.
• The subsequent recursive calls to its children encounter the base case (if not root: return None) and immediately return up the call stack.

Step 4: Backtrack and Check Node 7's Right Child (Node 6)

• The stack returns to Node 7 and calls invertTree(root.right), which is Node 6.
• Similar to Node 9, Node 6 is a leaf node. It swaps its None children and returns.
• Inversion for the subtree rooted at Node 7 is now completely finished.

Step 5: Backtrack to the Root and Move Right (Node 2)

• The stack returns all the way back to the main root (Node 4) and executes invertTree(root.right), which is now Node 2.
• Node 2 is not null.
• Swap Operation: Swap its left child (Node 1) and right child (Node 3).
• Tree State:
text
       4
     /   \
    7     2
   / \   / \
  9   6 3   1
Use code with caution.

Step 6: Process the Leaf Nodes (Node 3 and Node 1)

• The function recurses down to Node 3, finds no children, hits the base case, and returns.
• The function recurses down to Node 1, finds no children, hits the base case, and returns.
• Inversion for the subtree rooted at Node 2 is finished.

Step 7: Final Return

• All recursive calls are complete. The function returns the main root (Node 4).

Final Inverted Tree Output

text
       4
     /   \
    7     2
   / \   / \
  9   6 3   1
Use code with caution.

Complexity Analysis

• Time Complexity: O(N) because the algorithm must visit every single node in the tree exactly once to swap its children.
• Space Complexity: O(H) where H is the height of the tree. This space is occupied by the recursive call stack. In the worst-case scenario (a skewed tree that looks like a linked list), it becomes O(N).




