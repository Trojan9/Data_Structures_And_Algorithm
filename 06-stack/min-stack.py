
#this has higher space complexity but faster
class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append((val,min(self.stack[-1][1],val)))
        else:
            self.stack.append((val,val))
        
#don't forget top of the stack is the one to the right
#so if told pop at the top, pop the one added last
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
    
    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


#this is slower but with lower space complexity

class MinStack:

    def __init__(self):
        self.stack=deque()
        

    def push(self, val: int) -> None:
        self.stack.append(val)
   #top is element added last     
    def pop(self) -> None:
        self.stack.pop()
 #DON'T forget top is the element added last..       
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# ==================== Amazon SDE-I 50 version (with explanation) ====================
# Amazon SDE-I 50, #18: Min Stack (Medium)  [Stack]
#
# Brief: Stack with push, pop, top, getMin all O(1).
#
# In plain words: build a stack that can also instantly tell you its smallest value. Trick:
# alongside each value you push, also store "the smallest value in the stack up to here". Then the
# current minimum is always on top, no searching.
#
# Why it works: the min of the whole stack is the min of the top value and everything below it,
# and "everything below" was already computed when those were pushed. So each push computes its
# running min in O(1), and getMin just reads the top's stored min.
#
# Algorithm
# 1. Main stack + parallel minStack. 2. Push `min(val, current min)` to minStack. 3. getMin
#    returns `minStack[-1]`.

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minStack[-1]

# Complexity: Time O(1) per op, Space O(n).
