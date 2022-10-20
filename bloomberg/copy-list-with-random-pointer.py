"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#so the idea is to map the old nodes to the new nodes then we link this new nodes to each other
#so we would have 2 while loop ..first to create keys of old node in the map, with the values as a new node...second loop is to link this nodes to each other
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #make all none map to node
        oldToCopy={None:None}
        cur=head
        #create copy in map
        while cur:
            #create a copy node
            copy=Node(cur.val)
            #then map the original to the copy none
            oldToCopy[cur]=copy
            #next the node
            cur=cur.next
        cur=head
        while cur:
            #then we link this copy nodes to each other
            copy=oldToCopy[cur]
            copy.next=oldToCopy[cur.next]
            copy.random=oldToCopy[cur.random]
            cur=cur.next
        #then return the duplicated list
        return oldToCopy[head]#because head is the key to the duplcate head
            
            