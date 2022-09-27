# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #create a hashset
        mysets=set()
        #create a dummy node to be added at the beginning for iteration
        dummy=ListNode(next=head)
        #make prev=dummy and current=head
        prev,current=dummy,head
        
        while current:
            #if current is in set..just remove it ..its a duplicate
            if current.val in mysets:
                prev.next=current.next
            else:
                #else its not a duplicate add it to myset
                mysets.add(current.val)
                #make current the new prev
                prev=current
            #iterate the current no how
            current=current.next
         #return list excluding my dummy node   
        return dummy.next
        