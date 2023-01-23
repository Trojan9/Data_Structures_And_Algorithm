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