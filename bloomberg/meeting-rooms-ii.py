class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #make sure the list is sorted....else it would fail
        #make 2 different list of end and start times
        self.start=sorted([i[0] for i in intervals])
        self.end=sorted([i[1] for i in intervals])
        
        #then we use two pointers ..start and end pointer
        self.s,self.e=0,0
        #keep track on the counter and max value reached
        self.counter=0
        self.maxima=0
        #we know start pointer will always end first..so we use that as the threshold
        while self.s<len(intervals):
            #so if value at start array pointer is less that that at end array pointer...we move the start pointer by 1 and increase counter 
            if self.start[self.s] < self.end[self.e]:
                self.counter+=1
                self.s+=1
            else:
                #else the start time is bigger we reduces the counter by one and move the end array pointer
                self.e+=1
                self.counter-=1
            #either way we would find the maximum value reached
            self.maxima=max(self.maxima,self.counter)
        return self.maxima
            
        