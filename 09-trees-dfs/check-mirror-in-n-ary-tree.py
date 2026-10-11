Given two n-ary trees. Check if they are mirror images of each other or not. You are also given e denoting the number of edges in both trees, and two arrays, A[] and B[]. Each array has 2*e space separated values u,v denoting an edge from u to v for the both trees.


Example 1:

Input:
n = 3, e = 2
A[] = {1, 2, 1, 3}
B[] = {1, 3, 1, 2}
Output:
1
Explanation:
   1          1
 / \        /  \
2   3      3    2 
As we can clearly see, the second tree
is mirror image of the first.
Example 2:

Input:
n = 3, e = 2
A[] = {1, 2, 1, 3}
B[] = {1, 2, 1, 3}
Output:
0
Explanation:
   1          1
 / \        /  \
2   3      2    3 
As we can clearly see, the second tree
isn't mirror image of the first.

Your Task:
You don't need to read input or print anything. Your task is to complete the function checkMirrorTree() which takes 2 Integers n, and e;  and two arrays A[] and B[] of size 2*e as input and returns 1 if the trees are mirror images of each other and 0 if not.


Expected Time Complexity: O(e)
Expected Auxiliary Space: O(e)


Constraints:
1 <= n,e <= 105







from collections import deque
class Solution:
    def checkMirrorTree(self, n, e, A, B):
        # code here
        #i am gonna have 2 maps
        
        res1 = {}
        res2 = {}
        
        #i know the array is in 2 * e, looking at the array, each parent is beside its child
        # {1, 2, 1, 3} means 1 has left as 2 and right as 3
        #so i just move in steps of 2, adding the child to each parent key in the map
        #now if they are mirrored the left will be the right in the other and vice versa
        #so what i need to do is for each parent key in the map...i check if their values are mirrored
        #that is we chec one from index 1 and check the other from index -1(last)
        #incrementing and decrementing, the values must be same , else it's not mirrored
        #so i need a stack and a deque for popleft
        
        for i in range(0,len(A),2):
            if A[i] in res1:
                res1[A[i]].append(A[i+1])
            else:
                res1[A[i]] = [A[i+1]]
            if B[i] in res2:
               res2[B[i]].append(B[i+1])
            else:
                res2[B[i]] = deque()
                res2[B[i]].append(B[i+1])
            
        
        if len(res1) != len(res2):
            return 0
        
        for val in res1:
            #for each val
            #take one from front, and the other from back
            #if they are mirrord, they sould be the same
            while res1[val] or res2[val]:
                node1 = res1[val].pop()
                node2 = res2[val].popleft()
                if node1 != node2:
                    return 0
                
        return 1
