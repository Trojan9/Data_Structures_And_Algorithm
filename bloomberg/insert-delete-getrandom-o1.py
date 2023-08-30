import random 
class RandomizedSet:

    def __init__(self):
        self.hashset=set()

    def insert(self, val: int) -> bool:
        #if value is already in set o need to add...return false
        if val in self.hashset:
            return False
        else:
            #it is ot in set already..add to the set this value and return false
            self.hashset.add(val)
            return True

    def remove(self, val: int) -> bool:
        #if val is in set remove it and return true
        if val in self.hashset:
            self.hashset.remove(val)
            return True
        else:
            #if not return false
            return False
        
    def getRandom(self) -> int:
        #since its sure that there will always be a value in the set when getRandom is called
        return random.sample(self.hashset,1)[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()




class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.arr = []
        self.ptr = 0
    
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        # add the value to map with mappings to the current pointer which is gonna be the index in the array
        self.dict[val] = self.ptr
        self.arr.append(val)
        self.ptr += 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        # so basically we exchange the position of our value with that of the present last index
        idx = self.dict[val]
        lastElem = self.arr[-1]
        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.dict[lastElem] = idx
        # reduce the current pointer
        self.ptr -= 1

        del self.dict[val]
        # and the pop it
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        randNum = random.choice(self.arr)
        return randNum

'''
arr = [9, 5, 7, 3, 1, 6]

dict = {9:0, 5:1, 7:2, 3:3, 1:4, 6:5}
idx = self.dict[val]
lastElem = 
steps
keep the index of 7
1. swap 7 and 6
'''
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()