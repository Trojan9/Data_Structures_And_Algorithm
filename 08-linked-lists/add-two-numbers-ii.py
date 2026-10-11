# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#convert both to string and int, do the math , then create the node from the result

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        #convert both to string and int, do the math , then create the node from the result
        deno=""
        nume=""
        while l1:
            nume = nume+str(l1.val)
            l1=l1.next
        while l2:
            deno = deno+str(l2.val)
            l2=l2.next


        sumeof= int(nume) + int(deno)
        numb= str(sumeof)
        res=ListNode(int(numb[0]))
        dup = res
        for i in range(1,len(numb),1):
            dup.next=ListNode(int(numb[i]))
            dup = dup.next
        
        return res


##### Another solution ################


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
