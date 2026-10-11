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
        