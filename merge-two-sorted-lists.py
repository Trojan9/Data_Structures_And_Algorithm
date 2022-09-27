# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #list1 and list2 are both head for two list..like we kow normally
        #create a dummy node which will reference the ew merged lists
        dummy=ListNode()#we don't need to reference to any yet
        #we do this to avoid case where list is empty..line 14 above oo
        
        prev=dummy
        
        while list1 and list2:
        #so here if any of this condition is true it adds to the listnode,then the next iteration will definately cater for the node not fit in the conditio below..for them to be on the same index..so if its index l1[0] goes first..next iteration will make l2[0] pass..so we will have l1[1] and l2[1] in 3rd iteration
            if list1.val<list2.val:
                prev.next=list1
                list1=list1.next
            else:
                prev.next=list2
                list2=list2.next
            #normal new previous will be updated
            prev=prev.next
        
        #now one of the two list will still remain uniterated..so we just add it to the end of the list since they are sorted individual list
        
        if list1:
            prev.next=list1
        else:
            prev.next=list2
            #return new list excluding dummy
        return dummy.next