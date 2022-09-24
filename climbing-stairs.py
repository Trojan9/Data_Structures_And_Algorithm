class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #for e.g n=5...we start from 5 down to 0
        #we know it takes 1 way to get to 5 from 5
        #same thing 1 way from 4 to 5...this always apply to last two ,so it will always be 1,1..thats why we made two pointers from the bottom and equate them to 1 and 1
        #i.e even if n=10..it takes 1 way from 9 to 10 and from 10 to 10
        #so at 3 we have 1+1=2 (i.e one(pointer)+two(pointer) ) way to reach 5..one(pointer) becomes 2 at 3 element and two(pointer) becomes 1 at 4 element..so we need to store former value of one (pointer) before we equate it to two(pointer) 
        #so at 2 we have 2+1=3 (i.e one(pointer)+two(pointer) ) ways to reach 5..one (pointer) becomes 3 at 2element ad two(pointer) becomes 2 at 3element
        # so at 1 we have 3+2=5(i.e one(pointer)+two(pointer) ) ways to reach 5..so one (pointer) becomes 5 at 1 element and two (pointer) becomes 3 at 2 element
        # so at 0 we have 5+3=8 (i.e one(pointer)+two(pointer) ) one(pointer) then becomes 8 which we will then return as our answer
        one=1 #pointer
        two=1 #pointer
        #bottom-up dynamic programming
        #check youtube to get the explanation well
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
        return one
        