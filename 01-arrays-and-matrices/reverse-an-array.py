You are given an array of integers arr[]. Your task is to reverse the given array.

Note: Modify the array in place.

Examples:

Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.
Input: arr = [4, 5, 2]
Output: [2, 5, 4]
Explanation: The elements of the array are 4 5 2. The reversed array will be 2 5 4.
Input: arr = [1]
Output: [1]
Explanation: The array has only single element, hence the reversed array is same as the original.



  class Solution:
    def reverseArray(self, arr):
        # code here
        #return if len is 1 or empty
        if not arr or len(arr) == 1:
            return arr
            
        #get the middle
        half = len(arr) // 2
        
        # loop to middle
        for i in range(half):
            #interchnage values
            temp = arr[len(arr)- i -1]
            arr[len(arr)- i -1] = arr[i]
            arr[i] = temp
        
        return arr



####### another solution ########

Visual walkthrough: Reversing an Array

Original array:
Index:    0   1   2   3   4
Array:   [1,  2,  3,  4,  5]
          ↑               ↑
         left           right


Step 1: Swap 1 and 5
Before:  [1, 2, 3, 4, 5]
          ↑           ↑
         left        right

After:   [5, 2, 3, 4, 1]


Move both pointers inward:
         [5, 2, 3, 4, 1]
             ↑     ↑
            left  right


Step 2: Swap 2 and 4
Before:  [5, 2, 3, 4, 1]
             ↑     ↑
            left  right

After:   [5, 4, 3, 2, 1]


Move both pointers inward:
         [5, 4, 3, 2, 1]
                ↑
             left/right


Step 3: Stop

Now left = 2 and right = 2.
Since left < right is false, the loop terminates.
Final reversed array:
Original: [1, 2, 3, 4, 5]
Reversed: [5, 4, 3, 2, 1]

  
0(n)-time
0(1)-space

  
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        hold = arr[left]
        arr[left] = arr[right]
        arr[right] = hold

        left += 1
        right -= 1

    return arr

arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))
# [5, 4, 3, 2, 1]
