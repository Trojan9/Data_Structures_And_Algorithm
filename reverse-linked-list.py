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

        
