# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #create dummy node add to beginning of list
        dummy=ListNode(next=head)
        #create pointers prev,current
        prev,current=dummy,head
        while current:
            if current.val==val:
                #bypass the current..no need to change prev since prev remains prev when we remove the current
                prev.next=current.next
            else:
                #current becomes prev if we find no value of val
                prev=current
            #here current will always move to next ode
            current=current.next
            #return list excluding the dummy node
        return dummy.next