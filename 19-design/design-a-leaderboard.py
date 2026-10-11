###this is my won solution sha

class Leaderboard:

    def __init__(self):
        self.leader={}
        
    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leader:
            self.leader[playerId] = score
        else:
            self.leader[playerId] +=score
     

    def top(self, K: int) -> int:
        if not self.leader:
            return 0
        # needed to arrange from biggest to smallest, but sorted does smallest to biggest..so i neagted it
        lemesort = sorted([ -1 * self.leader[val] for val in self.leader])
        if K >len(lemesort):
            return -1* sum(lemesort[0:])
        else:
            return -1 * sum(lemesort[0:K])

    def reset(self, playerId: int) -> None:
        del self.leader[playerId]



### another solution below ###



class Leaderboard:

    def __init__(self):
        self.hash=defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        #if value in map..increment by score..else itiaalize to score
        if playerId in self.hash:
            self.hash[playerId]+=score
        else:
            self.hash[playerId]=score

    def top(self, K: int) -> int:
        #if hashmap is empty..just return 0
        if not self.hash:
            return 0
        #store values in a list
        allNum=[self.hash[keys] for keys in self.hash]
        total=0
        for i in range(0,K):
            #get the maximum val in list
            maxima=max(allNum)
            #get total
            total+=maxima
            #remove this value from list so we can get the next maximum
            allNum.remove(maxima)
        return total
            

    def reset(self, playerId: int) -> None:
        #reset
        self.hash[playerId]=0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)


#using heap

import heapq

'''
2. Heaps
Init: Initialize a dictionary (key: playerId,  val: score)
addScore: update the dictionary with the player score
top: 1. Initialize a new min - heap
     2. Iterate over the first K values(for x in scores.values) in the dict and add them to the heap 
        2a. after adding them to heap, check if len(heap) > K (if it is pop the heap)
    Doing this, helps us maintain the size of the heap to K and also remove smaller values
     3. Go through the heap (while):
     3a. pop the heap and add to res (res += heapq.heappop(heap))
     4. return res
TC: O(K)+O(NlogK) = O(NlogK)
It takes O(K) to construct the initial heap and then for the rest of the 
N-K elements, we perform the extractMin and add operations on the heap each 
of which take logK time.
SC: O(N + K) where O(N) is used by the scores dictionary and O(K) by the heap   
'''

class Leaderboard:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0
        
        self.scores[playerId] += score
        

    def top(self, K: int) -> int:
        
        heap = []
        for val in self.scores.values():
            heapq.heappush(heap, val)
            if len(heap) > K:
                heapq.heappop(heap)
            
        res = 0
        while heap:
            res += heapq.heappop(heap)
        
        return res
                
    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        

#most efficient

class Leaderboard(object):

    def __init__(self):
        self.A = collections.Counter()

    def addScore(self, playerId, score):
        self.A[playerId] += score

    def top(self, K):
        return sum(v for i,v in self.A.most_common(K))

    def reset(self, playerId):
        self.A[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
