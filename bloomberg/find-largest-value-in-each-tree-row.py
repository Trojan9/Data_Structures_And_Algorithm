# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        #we are gonna add levels to each node starting from 0
        queue = deque()
        queue.append((root,0))
        mappy= {} #let all values in same level be added together
        maxi = 1 #hold the maximum level reached
        res = []
        while queue:
            node,level = queue.popleft()
            #get maximum level reached
            maxi = max(maxi, level+1)
            if level in mappy:
                mappy[level].append(node.val)
            else:
                mappy[level] = [node.val]
            
            if node.left: queue.append((node.left, level+1))
            if node.right: queue.append((node.right,level+1))
        #get max in each level
        for i in range(maxi):
            res.append(max(mappy[i]))

        return res

