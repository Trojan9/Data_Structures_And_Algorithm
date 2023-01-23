class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashMap=defaultdict(int)
        #sort first
        words.sort()
        #add word to map
        for i in words:
            hashMap[i]+=1
        myArr=[]
        #for max needed
        for j in range(k):
            #get max from map
            maxima=max(hashMap,key=hashMap.get)
            #delete max
            del hashMap[maxima]
            #add to array
            myArr.append(maxima)
        
        return myArr
            
        