"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #add all nodes on same level to hashmap
        self.hashMaps=defaultdict(list)
        def dfs(node,i):
            if not node:
                return
            #if its not empty ..map the last node to the present incoming node  
            if(len(self.hashMaps[i])!=0):
                self.hashMaps[i][-1].next=node
            #new node becomes last ode in the list
            self.hashMaps[i].append(node)
            #never forget always check if its preset before calling it
            if node.left:dfs(node.left,i+1)
            if node.right:dfs(node.right,i+1)
        dfs(root,0)
        #just return root
        return root

########## Another SOlution , better for me ############# 

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #If the tree is empty, return None immediately (base case).
        if not root:
            return None
        #This initializes a queue (from collections.deque) with the root node.
        #We use this queue for level-order traversal (BFS).
        queue = deque([root])
        #Continue the BFS loop while there are nodes in the queue.
        while queue:
            #Get the number of nodes in the current level.
            #We use this to know where the level starts and ends.
            size = len(queue)
            #Loop through all nodes at the current level.
            #q is the current node being processed, removed from the front of the queue.
            for i in range(size):
                q= queue.popleft()
                #if it is not the end of the breath we equal next to the next in the breath line
                #If q is not the last node on the level, set its .next to the next node in the queue (i.e., its    right neighbor).

                #queue[0] is safe here because we’re still inside the level.
                if i < size -1:
                    q.next = queue[0]
                #Add the left and right children of the current node to the queue.
                #This prepares the next level for processing.
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
        #After setting all .next pointers, return the root of the updated tree.        
        return root
