# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #using the fast and slow pointer approach also
        #if we have 2 middle node,we return the 2nd middle node which is the SLOW node when fast or fast.next becomes null or none
        #https://www.youtube.com/watch?v=_cl3O4FBZh8  check  that video to understand better
        slow=fast=head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow




#####Dry Run Examples

• Odd Length: 1 -> 2 -> 3 -> 4 -> 5
	• Step 1: slow = 2, fast = 3
	• Step 2: slow = 3, fast = 5
	• Loop ends (fast.next is null). Returns slow (node 3).
• Even Length: 1 -> 2 -> 3 -> 4 -> 5 -> 6
	• Step 1: slow = 2, fast = 3
	• Step 2: slow = 3, fast = 5
	• Step 3: slow = 4, fast = null
	• Loop ends (fast is null). Returns slow (node 4, the second middle).
