"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #this is like level order transversing
        #if head is null..return null
        if not head:return head
        dummy=Node(0)
        cur,stack=dummy,[head]
        while stack:
            temp=stack.pop()
            if temp.next:stack.append(temp.next)
            if temp.child:stack.append(temp.child)
            cur.next=temp#double linked
            temp.prev=cur#double linked so do the prev
            temp.child=None #please dont forget to do this as its essential for double linked list
            cur=temp
        #remove the dummy..also for the prev link
        dummy.next.prev=None
        return dummy.next
            
        
        #using recursive method
        