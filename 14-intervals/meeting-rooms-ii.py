class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # [[0,30],[5,10],[15,20]]
        #make sure the list is sorted....else it would fail
        #make 2 different list of end and start times
        self.start=sorted([i[0] for i in intervals]) #we get [0,5,15] 
        self.end=sorted([i[1] for i in intervals])  #we get [10,20,30]
        
        #then we use two pointers ..start and end pointer
        self.s,self.e=0,0
        #keep track on the counter and max value reached
        self.counter=0
        self.maxima=0

        #0-----------------30
        #  5---10 15---20
        #1. so we have our pointer on 0 and 10 ...which are first element in out sorted list
        #2. so 0 < 10 ..we increase s ,s+=1 and also increase the counter(i.e a new meeting will start or aother meeting started while the previous hasn't ended),(counter is on 0 , a new meeting just started, we have counter=1) counter+=1 and find maximum between counter and present maximum.
        # 3. pointer is on 5 and 10, 5<10, s+=1, a new meeting started while the previous is not ended, so  counter+=1, now counter=2 ...find maximum also

        #4. pointer now on 15 and 10 15>10, one of the meeting has ended then counter -=1, e+=1(end is incremented), maximum is still foud also

        #5. pointer now on 15 and 20,15<20 counter +=1 s+=1

        #6. here the algo stops cuz that's the maximum count you can have, so use s as the threshold to stop algo

        

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
            
        

        # https://www.youtube.com/watch?v=FdzJmTCVyJU