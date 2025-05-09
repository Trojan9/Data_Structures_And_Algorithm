Given a BST, modify it so that all greater values in the given BST are added to every node.

Example 1:

Input:
           50
         /    \
        30    70
      /  \     / \  
     20  40 60 80
Output: 350 330 300 260 210 150 80
Explanation:The tree should be modified to
following:
             260
          /       \
        330      150
       /   \      /     \
    350   300 210    80
Example 2:

Input:
          2
        /   \
       1     5
            /  \
           4    7
Output: 19 18 16 12 7
Your Task:
You don't need to read input or print anything. Your task is to complete the function modify() which takes one argument: the root of the BST. The function should contain the logic to modify the BST so that in the modified BST, every node has a value equal to the sum of its value in the original BST and values of all the elements larger than it in the original BST. Return the root of the modified BST. The driver code will print the inorder traversal of the returned BST/

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(Height of the BST).

Constraints:
1<=N<=100000


Note: The Input/Output format and Example is given are used for the system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from the stdin/console. The task is to complete the function specified, and not to write the full code.





############ SOLUTION #######

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# modify the BST and return its root
def modify(root):
    #code here
    temp = root
    res = []
    queue = deque()
    queue.append(temp)
    ## firtsly get the numbers #######
    while queue:
        node = queue.popleft()
        res.append(node.data)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
        
    ### sort them ##
    res = sorted(res)
    
    ## get total sum
    summy = sum(res)
    mappy = {}

    ### now remove sum of every number before it, as this are numbers before present numbers and we just need sum of numbers greater
    ## if there are duplicates, the sum will get updated to the last one duplicated number, like if there are 3 duplicates, it will take the 3rd duplicate sum
    for i in range(len(res)):
        pre = sum(res[:i])
        mappy[res[i]] = summy -pre
    
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        node.data = mappy[node.data]
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return root
