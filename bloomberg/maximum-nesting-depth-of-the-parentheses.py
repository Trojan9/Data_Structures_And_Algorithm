class Solution:
    def maxDepth(self, s: str) -> int:
        #so we have max and couter
        self.maxOut=0
        self.counter=0
        if not s:
            return 0
        for i in s:
            #if we see "(" we increament..cuz it opens a new nest
            if i=="(":
                self.counter+=1
                self.maxOut=max(self.maxOut,self.counter)
            elif i==")":
                #but if we see ")"..we reduce..cuz we closed the nest
                self.counter-=1
        return self.maxOut