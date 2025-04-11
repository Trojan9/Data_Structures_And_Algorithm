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
# so remember stack it will take the last added to explore
#now if the child is added last, it will take the last child added to explore first
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




##########another solution 0(n*n)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr= head
        stack = []
        if not curr:
            return None
        while curr.next or curr.child:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
            if curr.next:
                curr = curr.next
        
        while stack:
            remain = stack.pop()
            curr.next= remain
            curr.next.prev = curr
            while curr.next:
                curr = curr.next
        
        return head

        
