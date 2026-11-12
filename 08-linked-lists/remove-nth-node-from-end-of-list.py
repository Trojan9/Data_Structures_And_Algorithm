# Amazon SDE-I 50, #30: Remove Nth Node From End (Medium)  [Linked List]
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

# Brief: Remove the nth node from the end. `1->2->3->4->5, n=2` → `1->2->3->5`.
#
# In plain words: delete the nth node counting from the back. Give a `fast` pointer an n-node head
# start, then move `fast` and `slow` together until fast hits the end; `slow` then sits just
# before the node to remove. (This is the one-pass version of "the node is at position length −
# n".)
#
# Why it works: keeping a fixed gap of n, when fast reaches the end slow is n nodes behind it.
# Starting slow at a `dummy` (one before the head) leaves it exactly one before the target, which
# is the predecessor you need to unlink a node. The dummy also makes removing the head itself a
# non-special case.
#
# Algorithm
# 1. Dummy before head; `l=dummy`, `r=head`. 2. Advance `r` n times. 3. Advance both until `r` is
#    None. 4. `l.next = l.next.next`.

NOte: we are trying to remove just one node...from the nth to the end

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head
        while n > 0:                # open a gap of n
            r = r.next
            n -= 1
        while r:                    # slide both; l lands one before the target
            l = l.next
            r = r.next
        l.next = l.next.next        # unlink it
        return dummy.next

# Complexity: Time O(n), Space O(1).
