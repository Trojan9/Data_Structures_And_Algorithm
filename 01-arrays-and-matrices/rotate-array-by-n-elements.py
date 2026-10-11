Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.

Examples :

Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.
Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.
Input: arr[] = [7, 3, 9, 1], d = 9
Output: [3, 9, 1, 7]
Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.

#### i will use juggling algorithm ####

######### SOLUTION EXPLANATION ########

GCD (Greatest Common Divisor) of two numbers a and b is the largest number that divides both a and b exactly.

Example: GCD(2,5) = 1 → No bigger number divides both.

Example: GCD(4,6) = 2 → 2 divides both.

📦 Test case:
arr = [1, 2, 3, 4, 5], d = 2

We want output: [3, 4, 5, 1, 2]

📚 Step 1: Pre-calculations
n = len(arr) = 5

d = d % n = 2 % 5 = 2

gcd = math.gcd(2, 5) = 1

✅ GCD = 1 → We will have 1 cycle (because 2 and 5 are co-prime).


Since gcd = 1, we run the outer loop once (i from 0 to 0).

----- First Outer Loop (i = 0):
temp = arr[0] = 1

j = 0

🔵 Now we enter the inner while True loop.

----- First while:
k = (j + d) % n = (0 + 2) % 5 = 2

arr[j] = arr[k] → arr[0] = arr[2] → arr[0] = 3

j = k = 2

Now array looks like:
[3, 2, 3, 4, 5]

------ Second while:
k = (j + d) % n = (2 + 2) % 5 = 4

arr[j] = arr[k] → arr[2] = arr[4] → arr[2] = 5

j = k = 4

Now array looks like:
[3, 2, 5, 4, 5]

----- Third while:
k = (j + d) % n = (4 + 2) % 5 = 1

arr[j] = arr[k] → arr[4] = arr[1] → arr[4] = 2

j = k = 1

Now array looks like:
[3, 2, 5, 4, 2]

------- Fourth while:
k = (j + d) % n = (1 + 2) % 5 = 3

arr[j] = arr[k] → arr[1] = arr[3] → arr[1] = 4

j = k = 3

Now array looks like:
[3, 4, 5, 4, 2]

----- Fifth while:
k = (j + d) % n = (3 + 2) % 5 = 0

Now, k == i (0 == 0), so we break

Before breaking, place temp back:

arr[j] = temp → arr[3] = 1

Now final array is:
[3, 4, 5, 1, 2]
  
import math
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n
        gcd = math.gcd(d,n) ###get the gcp between the number of rotation and the len of array

        #now loop through the amount of gcd, which is the amount of rotation loop we will go
        for i in range(gcd):
            #store the current index item, cuz after the gcp rotation loop it's gonna get left unreplaced
            temp = arr[i]
            j = i
            while True:
                k = (j + d) % n
                #when we come back to the current index rotation is done
                if k == i:
                    break
                #if not replace
                arr[j] = arr[k]
                j = k
            # add the temp at the current j
            arr[j] = temp
        return arr



####more simpler approach to understand....


Step-by-step execution
Iteration	i	arr[i]	Array after append
Start	—	—	[7, 3, 9, 1]
1	0	7	[7, 3, 9, 1, 7]
2	1	3	[7, 3, 9, 1, 7, 3]
3	2	9	[7, 3, 9, 1, 7, 3, 9]
4	3	1	[7, 3, 9, 1, 7, 3, 9, 1]
5	4	7	[7, 3, 9, 1, 7, 3, 9, 1, 7]
6	5	3	[7, 3, 9, 1, 7, 3, 9, 1, 7, 3]
7	6	9	[7, 3, 9, 1, 7, 3, 9, 1, 7, 3, 9]
8	7	1	[7, 3, 9, 1, 7, 3, 9, 1, 7, 3, 9, 1]
9	8	7	[7, 3, 9, 1, 7, 3, 9, 1, 7, 3, 9, 1, 7]
Now your last line executes:

return arr[9:]



The result is:
Index:  0  1  2  3  4  5  6  7  8 | 9  10 11 12
Array: [7, 3, 9, 1, 7, 3, 9, 1, 7 | 3, 9, 1, 7]
                                  ↑
                              Slice starts

Result: [3, 9, 1, 7]



def rotateArr(self, arr, d):
    if len(arr) < 2:
        return arr

  ####ensures that we don't rotate the array more times than necessary.The % operator is called the modulo operator. It returns the remainder after division. 
  
    d = d % len(arr)

    for i in range(d):
        arr.append(arr[i])

    return arr[d:]









###more explanation on d= d % len(Arr)

Original:    [7, 3, 9, 1]

Rotation 1:  [3, 9, 1, 7]
Rotation 2:  [9, 1, 7, 3]
Rotation 3:  [1, 7, 3, 9]
Rotation 4:  [7, 3, 9, 1]  ← Back to original

Rotation 5:  [3, 9, 1, 7]
Rotation 6:  [9, 1, 7, 3]
Rotation 7:  [1, 7, 3, 9]
Rotation 8:  [7, 3, 9, 1]  ← Back to original

Rotation 9:  [3, 9, 1, 7]
