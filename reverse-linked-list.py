# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #focus on first iteration the rest will fall in place
        #first of all initialize prev to be None..make first element ref one
        prev=None
        #make our current head
        current=head
        while current:
            #store the next value somewhere
            temp=current.next
            #make current ref to be none
            current.next=prev
            #now current becomes our prev
            prev=current
            #make next value we stored above the current
            current=temp
        #after make the last prev our head
        head=prev
        return head
            
        