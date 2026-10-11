"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#so the idea is to transverse this tree onec and store this nodes in a map of list...so every node with same counter or key will be stored together
#then we link every node stored together in same link..if not next node..equate to none
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #initialize our hashmap of list
        mymap=defaultdict(list)
        #create our dfs to transverse this nodes once
        def dfs(node,counter):
            #normal if node is ull return
            if not node:
                return
            #add to hashmap
            mymap[counter].append(node)
            dfs(node.left,counter+1)
            dfs(node.right,counter+1)
        #call it
        dfs(root,0)
        
        #then we go through each keys once
        for key in mymap:
            #loop through each nodes in the list and lik them
            for k in range(len(mymap[key])):
                #just to check if there is a node after to link to...if not link to none
                if k+1<len(mymap[key]):
                    mymap[key][k].next=mymap[key][k+1]
                else:
                    mymap[key][k].next=None
        #return root
        return root


####preferred solution 
#####this is similar to the previous one version I of it..same solution
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = collections.deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                q= queue.popleft()

                if i < size-1:
                    q.next = queue[0] 
                #make sure to add the left before the right
                #BFS only works if nodes are processed in left-to-right order, level by level.
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
        return root
        
        
