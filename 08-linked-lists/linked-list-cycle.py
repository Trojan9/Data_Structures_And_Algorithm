# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #fast and slow pointer approach
        
        fast=slow=head
        while fast and slow and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False





#Floyd's Tortoise and Hare algorithm

If the fast pointer reconnects to a node 5 steps back, the behavior of  does not change.
Because a cycle is formed, the fast pointer will still get trapped in the loop. Since it moves faster than the slow pointer, it will eventually catch up to the slow pointer from behind and meet at the exact same node inside the loop.

Why It Still Works (The Math)

• The Gap Closes: Every time both pointers move, the gap between the fast pointer and the slow pointer decreases by 1 step (since fast moves 2 steps and slow moves 1 step).
• Guaranteed Catch-up: If the cycle length is 5, the relative distance between them shrinks by 1 on every iteration until the distance becomes 0.

Trace Example (5-Node Cycle)

Imagine a list where the 5th node points back to the 1st node (1 -> 2 -> 3 -> 4 -> 5 -> 1):
• Start: Both slow and fast start at node 1.
• Step 1: slow goes to 2, fast goes to 3. (Distance apart: 1)
• Step 2: slow goes to 3, fast goes to 5. (Distance apart: 2)
• Step 3: slow goes to 4, fast loops around to 2. (Distance apart: 3)
• Step 4: slow goes to 5, fast goes to 4. (Distance apart: 4)
• Step 5: slow goes to 1, fast loops around to 1. They meet!
No matter how large the loop is or how far back it connects, the pointers will always meet as long as a cycle exists.

                                                                                                                            
                                                                                                                            
                                                                                                                            
#Alternative Approach: Hash Set (O(n) Time, O(n) Space)
                                                                                                                            
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #29: Linked List Cycle (Easy)  [Linked List]
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

# Brief: True if the list has a cycle.
#
# In plain words: does the chain loop back on itself? Two walkers, slow (1 step) and fast (2
# steps). If the chain ends, fast reaches the end, no loop. If there's a loop, fast keeps circling
# and eventually catches slow, they land on the same node.
#
# Why it works: inside a loop, fast gains one step on slow each move, so the gap shrinks to zero
# and they meet. No extra memory needed, unlike a visited-set.
#
# Algorithm
# 1. `slow=fast=head`. 2. While fast and fast.next: slow+1, fast+2. 3. Equal → True.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Complexity: Time O(n), Space O(1).
