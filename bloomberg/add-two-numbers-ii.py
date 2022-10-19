# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#so the idea is to convert this list to a number then do the sum..then create a new linkedList with this value
class Solution:
    def convertToNumber(self,node):
        #here we would convert our linkedList to number
        cur=node
        num=0
        while cur:
            #e.g for 728, 1.(7*10)+2=72... 2.(72*10)+8=728
            num=num*10+cur.val
            cur=cur.next
        return num
    
    # def reverse(node):
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #get numbers
        num1=self.convertToNumber(l1)
        num2=self.convertToNumber(l2)
        #do summation
        numT=num1+num2
        
        #convert to string
        styy=str(numT)
        
        #create new dummynode
        dummy=ListNode()
        cur=dummy
        
        #then add this val into a node and link them
        for i in styy:
            cur.next=ListNode(int(i))
            cur=cur.next
        return dummy.next

        #another solution is to add the modulus of this total /10 to a new node  (total%10)..so you total=total//10 for next iteration...all this while total > 0...so the value will be in reverse....then you will just reverse the linkedList