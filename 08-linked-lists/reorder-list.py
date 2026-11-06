# Amazon SDE-I 50, #31: Reorder List (Medium)  [Linked List]
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

# Brief: Reorder `L0->L1->...->Ln` to `L0->Ln->L1->Ln-1->...`. `1->2->3->4` → `1->4->2->3`.
#
# In plain words: weave the back of the list into the front. Three steps: find the middle, reverse
# the second half, then merge the two halves alternately (one from the front, one from the
# reversed back).
#
# Why it works: the target order is exactly "front, back, front, back...". Reversing the second
# half and interleaving produces that. Splitting at the middle makes the two halves the right
# sizes.
#
# Algorithm
# 1. Find middle (slow/fast). 2. Reverse second half. 3. Merge first and reversed-second
#    alternately.

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:        # slow ends at first-half tail
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None          # cut in two
        while second:                    # reverse second half
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first, second = head, prev       # merge alternately
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

# Complexity: Time O(n), Space O(1).
#
# Alternative (array, simpler to write, O(n) space). Put every node in an array, then two-point
# from both ends, relinking front-back-front-back. The order you want is just "first, last,
# second, second-last...", which is alternating between the two ends of the array, and an array
# lets you jump to either end in O(1).

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        nodes = []                       # collect every node by walking once
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        l, r = 0, len(nodes) - 1
        while l < r:
            nodes[l].next = nodes[r]     # front → back
            l += 1
            if l == r:                   # odd length: reached the middle
                break
            nodes[r].next = nodes[l]     # back → next front
            r -= 1
        nodes[l].next = None             # node we ended on becomes the tail

# Trade-off: easier to reason about, but O(n) memory instead of O(1). In an interview, offer this
# first if it's what comes to you, then mention you can do it in O(1) with the reverse-and-merge
# version above. A plain array beats a dict here because the keys are just 0-based indices.
