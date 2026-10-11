class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #so if interval is empty the there is no need
        if not intervals:
            return []
        #first of all we need to sort this guys out
        intervals.sort(key=lambda x:x[0])
        #just intervals.sort() will do this
        #hold our result
        res=[]
        #so we need to have two pointers at first..min and max initialized to first integer
        minima,maxima=intervals[0][0],intervals[0][1]
        #so we start our loop from 2nd index
        for i in range(1,len(intervals)):
            #now if the next starting time is bigger than the present max..then there is no overlapping..add this min and max to the res
            if intervals[i][0]>maxima:
                res.append([minima,maxima])
                #then make our min and max initialized to this new index
                minima=intervals[i][0]
                maxima=intervals[i][1]
            else:
                #else they over lap...find the max between present max and and new ending time..cuz the new ending time might be smaller than the previous index ending time...doing this..in the next loop, if the starting time still overlaps..the maxima will also be updated,until we see a starting time value that doesn't overlap..then we add the min and max to our result array..and update new max and min value as above
                maxima=max(intervals[i][1],maxima)
        #after this..there would be the last values in thismin and max..we just append it..don't forget this
        res.append([minima,maxima])
        return res
                






class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #so if interval is empty the there is no need
        if not intervals:
            return []
        #first of all we need to sort this guys out
        intervals.sort(key=lambda x:x[0])
        #hold our result...and initialize the first index
        res=[intervals[0]]
        #so we take the start and end time to compare
        for start,end in intervals:
            #if start is > the [1] of the last value tuple..it doesn't overlap..add to res
            if start>res[-1][1]:
                res.append([start,end])
            #else it overlap,,now we check if end is greater than the end of last value in res..if yes..we update it
            elif end>res[-1][1]:
                res[-1][1]=end
        return res
                
