# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
           
  ###more understanding         
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



