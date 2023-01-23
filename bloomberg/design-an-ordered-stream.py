'''
so initially they would give us value of n..so our arry will be a value from 1-n
our pointer will start at l=0..or first index..l=0 sha.
#..so basically when we insert value at our pointer,we will move it to the next empty index..notice that our pointer doesn't move until we fill the pointer position with something ..so we could have inserted something in some indexes after the present pointer..
#so basically when we insert and our pointer moves..we return value from the former pointer(include) to the new pointer(not inclusive)

    [ a   b   c   d   e]
      1   2   3   4   5
                            p
                            
so basically just initialize an array of value None * n
'''


class OrderedStream:

    def __init__(self, n: int):
        self.stream= [None]*n
        #start at first index
        self.pointer=0
    

    def insert(self, idKey: int, value: str) -> List[str]:
        #we first insert..cuz we will insert whatever the case
        self.stream[idKey-1]=value
        #now if we inserted at our present pointer position..we need to move to next empty position
        if (idKey-1) == self.pointer:
            #while its not out of bound and the present index is filled..keep on moving
            while self.pointer<len(self.stream) and self.stream[self.pointer]:
                self.pointer += 1
        #just return the value from index(inclusive) to the new index (not inclusive)
        return self.stream[idKey-1:self.pointer]
                
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)