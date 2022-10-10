class UndergroundSystem(object):

    def __init__(self):
        #customerid:(t,stationName)
        self.register=defaultdict(tuple)#so this will register all passenger with their Id with the starttime and start station name
        
        #(startStaion,endStation):[timeTaken]
        self.calc=defaultdict(list)#this will get customer id start station and start time....and calulate the time difference to endstation...so all customers time with same start and end station will be added to a list

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.register[id]=(t,stationName)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        #get start time and station from the register dict for an id
        startTime,startStationName=self.register[id]
        #calc time difference
        timeDifference=t-startTime
        #add all time with same start and end station to the dict list
        self.calc[(startStationName,stationName)].append(timeDifference)
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        #return the average
        #we used the sum(map(float,val)) because using only sum() will convert to integer
        return sum(map(float,self.calc[(startStation,endStation)]))/len(self.calc[(startStation,endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


#another way but same strategy

class UndergroundSystem(object):

    def __init__(self):
        #customerid:(t,stationName)
        self.register=defaultdict(tuple)#so this will register all passenger with their Id with the starttime and start station name
        
        #(startStaion,endStation):[timeTaken]
        self.calc=defaultdict(float)#this will get customer id start station and start time....and calulate the time difference to endstation...so all customers time with same start and end station will be added to a list
        self.length=defaultdict(int)
    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.register[id]=(t,stationName)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        #get start time and station from the register dict for an id
        startTime,startStationName=self.register[id]
        #calc time difference
        timeDifference=t-startTime
        #add all time with same start and end station to the dict list
        self.calc[(startStationName,stationName)]+=timeDifference
        self.length[(startStationName,stationName)]+=1
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        #return the average
        #we used the sum(map(float,val)) because using only sum() will convert to integer
        return self.calc[(startStation,endStation)]/self.length[(startStation,endStation)]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)




#optimized solution

class UndergroundSystem(object):

    def __init__(self):
        #customerid:(t,stationName)
        self.register=defaultdict(tuple)#so this will register all passenger with their Id with the starttime and start station name
        
        #(startStaion,endStation):[timeTaken]
        self.calc=defaultdict(tuple)#this will get customer id start station and start time....and calulate the time difference to endstation...so all customers time with same start and end station will be added as tuple value will keep changing when we compute new total and frequency
    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.register[id]=(t,stationName)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        #get start time and station from the register dict for an id
        startTime,startStationName=self.register[id]
        total,freq=0,0
        if (startStationName,stationName) in self.calc:
            total,freq=self.calc[(startStationName,stationName)]
        self.calc[(startStationName,stationName)]=(float(total+(t-startTime)),freq+1)
        
        #we can go ahead and pop the id from the register dict as this will reduce time needed
        self.register.pop(id)
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        #return the average
        #so we get the total and freq from our calc tuple
        total,freq=self.calc[(startStation,endStation)]
        return total/freq
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)



#time and space complexity
# 0(1) for all functions
# Space : O(n) cos of the dictionaries