# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #initialize a dummy node, a variable to hold our carry value
        dummy=ListNode()
        carry=0
        cur=dummy
        while l1 and l2:
            #so do arithmethic..the 2 val + carry...store the modulus in the ode..14/10..we write 4 carry 1
            cur.next=ListNode(((l1.val+l2.val+carry)%10))
            #we floor the division to get our carry value
            carry=(l1.val+l2.val+carry)//10
            #we next our values
            cur=cur.next
            l1=l1.next
            l2=l2.next
        #so if l1 or l2 remains ..we do same as adding the values with the carry value
        if l1:
            while l1:
                #get value with carry value
                cur.next=ListNode(((l1.val+carry)%10))
                carry=(l1.val+carry)//10
                #next our nodes
                cur=cur.next
                l1=l1.next
        if l2:
            while l2:
                #same thing here..if l2 still remains i.e l2 is longer than l1
                cur.next=ListNode(((l2.val+carry)%10))
                carry=(l2.val+carry)//10
                #next the node
                cur=cur.next
                l2=l2.next
        #now if value is > 0 that means we still need to add an extra node for this carry over
        if carry>0:
            cur.next=ListNode(carry)
        return dummy.next
        

#another solution
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        result = root
        excess = 0
        #this just packs everything into one while loop
        while l1 or l2 or excess:
            #otice the or ..so even if 1 is true it would run
            #so instead of having differet variables all of them are added to excess
            if l1:
                excess += l1.val
                l1 = l1.next
            if l2:
                excess += l2.val
                l2 = l2.next
            #if both l1 nd l2 condition are false...this will run regardless
            #this will come handy when both list are exhausted nd there is still excess umber left..it would add to the linkednode this extra value
            result.next = ListNode(excess%10)
            result = result.next
            excess = excess//10
            
        return root.next   
        