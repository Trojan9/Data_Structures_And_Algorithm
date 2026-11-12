# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


##### Original:   1 → 2 → 3 → 4 → 5 → None

###using 3 pointers window


             <--
       <--         <--
     <--               <--
   <--                     <--
 <--                           <--
--> prev    current .    next--->
    null ->    1    ->    2

1. so reverse by first keeping copy of next
    prev = None
    current = head
    next = current.next
2. then follow the allow one by one ..start from next, equate to other point in the arrow
    
    current.next = prev  ---first oint
    prev = current ----second point
    current = Next(the one stored) ---third point

3. keep on with that...then return prev at the end



##reverse it...that arrow is the front, move to point to back...prev..instead of next

....current.next= prev

##then move the sliding window pointers forward....prev becomes current....current becomes next...then next becomes the untouch value in front
prev = current 
current = next
next = current.next

##then repeat till current is null

time = 0(n)
space = 0(1)


###easiest.....this the new explanation
https://www.youtube.com/watch?v=auoTGovuo9A
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
            next =current.next
            #make current ref to be none
            current.next = prev
            #now current becomes our prev
            prev=current
            #make next value we stored above the current
            current = next

        #prev will point to new head now
        return prev
            




####### BETTER EXPLANED HERE ###############

# Original:   1 → 2 → 3 → 4 → 5 → None
# Reversed:   5 → 4 → 3 → 2 → 1 → None

# Steps:
# 1. create initial reversing node with None as first val
# 2. now transverse the original, each node you encounter needs t have the .next assigned to current reversingNode
# 3. Don't forget to store  temp next node of the original before changing the current node  .next
# normal transverse, for original it will look like we rare transversing forward, while for the reersing , will look like we are 
transversing backward

# 4 Re initialize the reverseNode to current node first, then also reinitilize currentNode to it's next value which we stoored temporarily, 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        #start reverse wih Node and current with head
        reversinNode, currNode = None, head

        while currNode:
            #first store the current node next linked list emporaily 
            tempNext = currNode.next
            #now renitalize it to the current reverse node
            currNode.next = reversinNode
            #currentNode becomes present reversenode
            reversinNode = currNode
            #equate the current node to it's .next which we stored previously
            currNode = tempNext

        return reversinNode


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #27: Reverse Linked List (Easy)  [Linked List]
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

# Brief: Reverse a singly linked list, return the new head.
#
# In plain words: flip the chain so it runs the other way. Walk along turning each node's arrow to
# point at the node behind it. Carry `prev` (the part already flipped) and `curr` (the node you're
# flipping); save `curr.next` before overwriting it or you lose the rest.
#
# Why it works: reversal means every arrow turns around. When `curr` falls off the end, `prev` is
# the last original node, now the new head.
#
# Algorithm
# 1. `prev=None`, `curr=head`. 2. Save next, flip, advance both. 3. Return `prev`.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next       # save the rest before overwriting
            curr.next = prev      # flip
            prev = curr           # reversed part grows
            curr = nxt            # advance
        return prev

# Complexity: Time O(n), Space O(1).
