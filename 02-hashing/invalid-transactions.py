class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        
        #so first we would make a map where we store all transactions with same time in same element or key....that is the time eill be out key..in this key we would have another map with key "name"..mapped to a hashSet of the cities
        times={}
        #array to house invalid trasactions
        invalid=[]
        for trans in  transactions:
            #we would split this string using ,
            name,time,amount,city=trans.split(",")
            
            #don't forget to convert to integer
            time = int(time)
            
            if time in times:
                #i.e same name carried out a transaction at the same time..so we just include the city to the hashSet else we create a new one
                if name in times[time]:
                    #add to set
                    times[time][name].add(city)
                else:
                    #we create a new key for the name and add the city to the set
                    times[time][name]={city}
            #else if time not in our map..we add this ew details to it
            else:
                times[time] = {name: {city}}
                
        #now we would iterate through the list again and check if any transaction was done within 60mins interval i.e -60 < t > +60....

        #so we check the maps if this time key exist , we check the name key within it to see if it exist...then we see if the hashset length is more than 1 i.e times[time][name]>1..then its invalid..remember that there is no duplicates in a hashset or set..so we can have two same element in it..all are unique....

        #then OR if timerangeValue is different from our time..i.e time =20 and present timerangeValue=30 and its present in our map times...so a nested for loop is needed....we check the name key..if its also present...we then check if our present index city is in this hashset also..if not its invalid

        for trans in transactions:
            name,time,amount,city=trans.split(",")
            #don't forget to convert this to integer
            time = int(time)
            amount = int(amount)
            #check first case
            if amount>1000:
                invalid.append(trans)
            else:
                #remember
                #so Range( starting point, ending point exclusive, step wise)
                #so start from -60 end at +60
                for tRange in range(time - 60, time + 61):
                    if tRange in times and name in times[tRange]:
                        #different cities same time or different time different cities
                        if len(times[tRange][name]) > 1 or city not in times[tRange][name]:
                            invalid.append(trans)
                            break

        return invalid
                    
            #time complexity is o(n)..the second nested loop is 0(1) because its in for loop range
        
                    
            