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
                
        

You need to:

Create a stream (like a list) that can hold n items.

Receive items using a function insert(id, value).

Return a list of values starting from the current position, only if they are available in the correct order.

📦 Example
If you create a stream of size 5:

stream = OrderedStream(5)
And then call:

stream.insert(3, "ccccc") → []
stream.insert(1, "aaaaa") → ["aaaaa"]
stream.insert(2, "bbbbb") → ["bbbbb", "ccccc"]
Here’s why:

The pointer starts at position 1

You inserted item 3 → can't use it yet (waiting for 1)

Then you inserted 1 → now we can return 1

Then 2 → now we can return 2 and also 3 since both are filled

✅ Step-by-Step Plan
We’ll:

-Use a list to hold the values (like [None, None, ..., None])

-Use a pointer to track the current usable position

-Each time insert(id, value) is called:

-Put the value in the list at id - 1

-If the pointer is ready, collect values until there's a gap


###READ READ READ READ########
##explanation so basicly, pointer won't move until there is a value at current pointer position
stream = OrderedStream(5)---5 indexs
And then call:
---pointer is at index 0
stream.insert(3, "ccccc") → [] ---insert in position 3, which is index 2, but nothing is at index 0, so pointer doesn't move..we return []
stream.insert(1, "aaaaa") → ["aaaaa"]--insert index 0 (position 1), now index 0 has value, pointer moves to 1, but index 1 is empty, we return only value at index 0
stream.insert(2, "bbbbb") → ["bbbbb", "ccccc"]-insert index 1(position 2), now remember pointer is at index 1, index 1 has value, store the value for return; we move pointer to index 2, index 2(position3) also have value ,we store the vaalue for return, we move index pointer to index 3,which is empty, so we return only value at index 1 and 2.

from typing import List

class OrderedStream:
    def __init__(self, n: int):
        # Create a list of size n to store values (initially empty)
        self.stream = [None] * n
        self.ptr = 0  # This points to where we are currently "reading" from

    def insert(self, id: int, value: str) -> List[str]:
        # Place the value at position id - 1 (because list is 0-indexed)
        self.stream[id - 1] = value
        result = []

        # If the pointer is at a filled position, start collecting values
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])
            self.ptr += 1  # move pointer forward

        return result

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
