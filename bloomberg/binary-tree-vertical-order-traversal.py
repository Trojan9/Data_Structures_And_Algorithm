# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def dfs(self,p,counter):
#         if p is None:
#             return None
#         print(p.val)
#         self.dict[counter].append(p.val)
#         self.minimal=min(self.minimal,counter)
#         self.maxim=max(self.maxim,counter)
        
#         self.dfs(p.left,counter-1)
#         self.dfs(p.right,counter+1)
        
#     def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         self.dict=defaultdict(list)
#         self.minimal=0
#         self.maxim=0
#         self.dfs(root,0)
#         return [self.dict[x] for x in range(self.minimal, self.maxim + 1)]

#seems like dfs cannot work for this solution
#only breadth first search will work..bfs
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #so the idea is to start from pointer 0..so when we move left we minus 1(-1) but when we move right we add 1 (+1)..so we use this pointers as the key..so every nodes with same pointer fall under same vertical line..we add the values to the list
        if root is None:
            return []
        #so our dict is a list val
        self.dict=defaultdict(list)
        self.minimal=0
        self.maxima=0
        #(node, pointer)
        q=deque()
        q.append((root,0))
        
        while q:
            #get the leftmost value...cuz its breadth first..left comes before right
            p,pointer=q.popleft()
            #add this value to list at this number key
            self.dict[pointer].append(p.val)
            #find the min and max to know our value range
            self.minimal=min(self.minimal,pointer)
            self.maxima=max(self.maxima,pointer)
            #add the next left and right if not null
            if p.left is not None:
                q.append((p.left,pointer-1))
            if p.right is not None:
                q.append((p.right,pointer+1))
        #now to get the whole list
        return [self.dict[x] for x in range(self.minimal, self.maxima + 1)]



"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
       #please watch this https://www.youtube.com/watch?v=U4hFQCa1Cq0
    #so we are gonna use  dfs kinda this but without the que...we want 0(1) solution
    # so we are gonna create two pointers at first 
    #so we just need to assign left to right then ...notice we always have current and next..our current next would have been assigned , so we assign current.next.left to right.next....watch that youtube video or draw up the tree to get it
    #from the example in description...1.left is 2..so 2.next=3...3.next=None
    #4.next=5...5.next= 2.next.left=6..you get it...curr will be 2...when we move.....nxt becomes our curr ad we change nxt...note nxt is different from next...nxt is first node on level below
    # so first curr is 1 and nxt is 2..first node below...that always .left
        cur,nxt=root,root.left if root else None
    
        while cur and nxt:
            #make next of left equals right
            cur.left.next=cur.right
            #if current has next....we make next of right node eauals to left node of our current node next
            if cur.next:
                cur.right.next=cur.next.left
            #do same for all nodes on that levl....so do for 2,3 
            cur=cur.next
            #so if all nodes is done on that level..go to the next level
            if not cur:
                cur=nxt
                nxt=cur.left
        return root

#0(1)memory space...o(n) time