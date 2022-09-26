# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #usig brute force solution
        arr=[]
        #convert linked list to array
        while head:
            arr.append(head.val)
            head=head.next
            
        #then we do the algo to check for palindrome
        l,r=0,len(arr)-1
        while l<=r:
            #so we start at begining and end the read towards the center
            #this is to prevent them from crossing over the middle..so they meet at the center
            if arr[l]!=arr[r]:
                #so if at all they are not same then its ot a palindrome
                
                return False
            l+=1 #increment from left to center
            r-=1 #decrement from right to center
        #if all equates the it is a palindrome..return true
        return True

#optimal solution , we use the fast and slow pointer approach(2 pointers)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #using fast ad slow pointer approach

        #get the middle element
        slow,fast=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        #reverse the second half of the liked List
        prev=None
        p=slow
        while p:
            next=p.next
            p.next=prev
            prev=p
            p=next
        #run palindrome algo
        left,right=head,prev

        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True
    
    
            
            