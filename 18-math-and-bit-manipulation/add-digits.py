Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0



class Solution:
    def addDigits(self, num: int) -> int:
        val = str(num)
        #while the val is not single digit
        while len(val)>1:
            ori = int(val)
            remain = 0
            #get the sum
            summy = 0
            while ori > 0: #while ori is not 0, we keep on adding the remain in the division by 10
                remain = ori%10
                ori = ori // 10
                summy +=remain
            val = str(summy)
        
        return int(val)

        
