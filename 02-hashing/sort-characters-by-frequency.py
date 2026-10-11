class Solution:
    def frequencySort(self, s: str) -> str:
        #map this values to their count
        hashmap=defaultdict(int)
        #this will hold our result
        res=""
        #map values to count
        for i in s:
            hashmap[i]+=1
        #for loop in range of length of hashmap
        for k in range(0,len(hashmap)):
            #gets key with maximum value
            #remember to cram this..or better stilll know this..its like what we used in sorting
            maximumkey=max(hashmap,key=lambda x:hashmap[x])
            #store value in string
            res+=maximumkey*hashmap[maximumkey]
            #delete this key..so we can get next max
            del hashmap[maximumkey]
        #return result
        return res


####### solution 2 ##############################

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        #turns to a tuple
        count = sorted(count.items(),key= lambda x: x[1])
        res = ''
        print(count)
        for value in count:
            res = (value[1] * value[0]) + res
        return res
        
