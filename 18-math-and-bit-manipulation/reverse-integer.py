Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


class Solution:
    def reverse(self, x: int) -> int:
        new_X = abs(x)
        new_str = str(new_X)
        rear= ""
        for i in range(len(new_str)-1,-1,-1):
            rear+=new_str[i]
        #check the range for int 32
        if int(rear) < -2**31 or int(rear) > 2**31 - 1:
            return 0
        if x<0:
             return -1 * int(rear)
        else:
            return int(rear)


        
