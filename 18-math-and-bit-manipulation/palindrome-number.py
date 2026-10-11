class Solution:
    def isPalindrome(self, x: int) -> bool:

        # negative numbers
        if x < 0:
            return False
        dev=x

        div=0
        while dev!=0:
            remain=dev%10
            div=div*10+remain
            dev=dev//10
        return x==div