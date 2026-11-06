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
        #create a dummy node which will reference the new merged lists
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


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #28: Merge Two Sorted Lists (Easy)  [Linked List]
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

# Brief: Merge two sorted lists into one sorted list.
#
# In plain words: zip two sorted chains into one sorted chain. Repeatedly take the smaller of the
# two front nodes, attach it, advance that list. A "dummy" starter node means you don't special-
# case the first node.
#
# Why it works: at any moment the smallest unused node is one of the two heads (each list is
# sorted). Attaching that one and advancing keeps the result sorted.
#
# Algorithm
# 1. Dummy; `node = dummy`. 2. While both non-empty, attach smaller, advance. 3. Attach the
#    remainder. Return `dummy.next`.

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 or l2       # attach whatever's left (already sorted)
        return dummy.next

# Complexity: Time O(n + m), Space O(1).
