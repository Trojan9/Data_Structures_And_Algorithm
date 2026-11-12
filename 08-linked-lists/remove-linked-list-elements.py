# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #create dummy node add to beginning of list
        dummy=ListNode(next=head)
        #create pointers prev,current
        prev,current=dummy,head
        while current:
            if current.val==val:
                #bypass the current..no need to change prev since prev remains prev when we remove the current
                prev.next=current.next
            else:
                #current becomes prev if we find no value of val
                prev=current
            #here current will always move to next ode
            current=current.next
            #return list excluding the dummy node
        return dummy.next

# ---------------------------------------------------------------------------------------------
# Dry run of the prev/current solution above: 7(a) -> 7(b) -> 1 -> 7(c), val = 7
# ---------------------------------------------------------------------------------------------
#   start: dummy -> 7(a) -> 7(b) -> 1 -> 7(c)        prev=dummy, current=7(a)
#
#   current=7(a): match -> prev.next = 7(b)  (unlink a, prev stays dummy)
#                 list: dummy -> 7(b) -> 1 -> 7(c)
#   current=7(b): match -> prev.next = 1     (unlink b, prev stays dummy)
#                 list: dummy -> 1 -> 7(c)
#   current=1:    keep  -> prev = 1
#   current=7(c): match -> prev.next = None  (unlink c, prev stays 1)
#                 list: dummy -> 1
#   current=None: loop ends
#   return dummy.next = 1
#
# Note: prev only moves when we KEEP a node. current always moves.


# ==================== Why the dummy node is NEEDED here ====================
# In Remove Duplicates from Sorted List the head is never deleted (it's the first of its value),
# so no dummy is needed. Here the head itself can match val:
#
#   head = 7 -> 7 -> 1, val = 7   ->  answer is 1  (the head is gone)
#
# Without a dummy you'd need special code to strip 7s off the front first. With a dummy, the head
# is just "another node with something in front of it", so one loop handles every case.
#
#                          | Remove Duplicates (sorted) | Remove Elements
#   -----------------------+----------------------------+----------------
#   Can head be deleted?   | No                         | YES
#   Dummy needed?          | No                         | YES
#   Rule                   | unlink, DON'T move         | unlink, DON'T move


# ==================== One-pointer version (no prev) ====================
# Same idea as the sorted-list solution: stand on the node BEFORE the one you're checking and
# look at current.next. Then current itself plays the role of prev.

class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(next=head)                 # needed: the head itself might be removed
        current = dummy                             # stand on the node BEFORE the one we check

        while current.next:                         # check the node after me
            if current.next.val == val:             # it must go
                current.next = current.next.next    # unlink it
                                                    # DON'T move: the new next might match too
            else:
                current = current.next              # keep it, move on

        return dummy.next                           # skip the dummy

# Complexity (both versions): Time O(n), Space O(1).
#
# ---------------------------------------------------------------------------------------------
# Dry run: 7(a) -> 7(b) -> 1 -> 7(c), val = 7
# ---------------------------------------------------------------------------------------------
#   dummy -> 7(a) -> 7(b) -> 1 -> 7(c)
#
#   current=dummy, next=7(a)  match -> unlink   dummy -> 7(b) -> 1 -> 7(c)   (stay)
#   current=dummy, next=7(b)  match -> unlink   dummy -> 1 -> 7(c)           (stay)
#   current=dummy, next=1     keep  -> move
#   current=1,     next=7(c)  match -> unlink   dummy -> 1                   (stay)
#   current=1,     next=None  loop ends
#   return dummy.next = 1
#
# The trap: if you moved after unlinking 7(a), current would jump onto 7(b) and you'd never
# check it, so 7(b) would stay in the list. That's why the move is only in the else.
