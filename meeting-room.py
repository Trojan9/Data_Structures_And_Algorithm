from ast import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #sort according to starting time
        intervals.sort(key = lambda x:x[0])
        
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
            
        return True