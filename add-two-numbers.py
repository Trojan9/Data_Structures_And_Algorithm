# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #create dummynode from index -1, so our head will start from index 0, all we gat to do is use the next
        l3=ListNode(-1)
        #create dummy list
        temp = l3
        #create holder for carryover
        holder=0
        #if l1 has val or l2 has val
        while l1 != None or l2 != None:
            currentl1 = 0 if l1 == None else l1.val
            currentl2 = 0 if l2 == None else l2.val
            linkedval=currentl1+currentl2+holder
            holder=0
            if linkedval>=10:
                holder=linkedval//10
                linkedval=linkedval%10
                
                temp.next=ListNode(linkedval)
                #make current temp temp.next
                temp=temp.next
                #make current l1,l2 next
                if l1: l1=l1.next
                if l2: l2=l2.next
            else:
            
                temp.next=ListNode(linkedval)
                #make current temp temp.next
                temp=temp.next
                #make current l1,l2 next
                if l1: l1=l1.next
                if l2: l2=l2.next
        if holder>0:
            
	        temp.next=ListNode(holder)
	
        return l3.next
        