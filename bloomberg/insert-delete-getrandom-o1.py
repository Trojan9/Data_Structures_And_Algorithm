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