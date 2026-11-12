# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #create a hashset
        mysets=set()
        #create a dummy node to be added at the beginning for iteration
        dummy=ListNode(next=head)
        #make prev=dummy and current=head
        prev,current=dummy,head
        
        while current:
            #if current is in set..just remove it ..its a duplicate
            if current.val in mysets:
                prev.next=current.next
            else:
                #else its not a duplicate add it to myset
                mysets.add(current.val)
                #make current the new prev
                prev=current
            #iterate the current no how
            current=current.next
         #return list excluding my dummy node   
        return dummy.next
        

# ==================== Better solution: use the fact that the list is SORTED ====================
# The solution above works, but it never uses "sorted". In a sorted list, duplicates always sit
# NEXT TO EACH OTHER (1 -> 1 -> 2 -> 3 -> 3), so we only compare a node with the node right after
# it. No set, no dummy, no prev.
#
# Compared with the set version:
#   - set:        not needed, duplicates are neighbours
#   - dummy node: not needed, the head is the first of its value so it is never deleted
#   - prev:       not needed, current does the skipping itself (current.next = current.next.next)
#   - space:      O(n) -> O(1)        time: O(n) in both

class Solution(object):
    def deleteDuplicates(self, head):
        current = head                              # start at the first node

        while current and current.next:             # need a node AND a next one to compare
            if current.val == current.next.val:     # next node is a duplicate of me
                current.next = current.next.next    # skip it (unlink it)
                                                    # DON'T move: the new next might be a duplicate too
            else:
                current = current.next              # next is different, safe to move on

        return head                                 # head never changes

# Complexity: Time O(n), Space O(1).
#
# ---------------------------------------------------------------------------------------------
# Dry run: 1(a) -> 1(b) -> 1(c) -> 2 -> 3 -> 3
# ---------------------------------------------------------------------------------------------
#   current=1(a), next=1(b)  equal     -> skip b   1(a) -> 1(c) -> 2 -> 3 -> 3   (stay on a)
#   current=1(a), next=1(c)  equal     -> skip c   1(a) -> 2 -> 3 -> 3           (stay on a)
#   current=1(a), next=2     different -> move
#   current=2,    next=3     different -> move
#   current=3,    next=3     equal     -> skip     1 -> 2 -> 3
#   current=3,    next=None  loop ends
#   return 1 -> 2 -> 3
#
# The trap: after skipping, do NOT move current. If we moved after skipping b, current would jump
# to c, the next check would be c vs 2 (different), and we'd end with 1(a) -> 1(c) -> 2 -> 3: two
# 1s left. Staying on a lets us compare a with c too. That's why the move is only in the else.
#
# When the set version IS the right one: if the list is NOT sorted (3 -> 1 -> 3 -> 2), duplicates
# aren't neighbours, so you need a set to remember values already seen. Keep it for that problem.
#
# Don't mix up with LeetCode 82 (Remove Duplicates from Sorted List II): there you delete EVERY
# node whose value repeats (1 -> 1 -> 2 becomes 2), so the head can be deleted and you DO need a
# dummy node.
