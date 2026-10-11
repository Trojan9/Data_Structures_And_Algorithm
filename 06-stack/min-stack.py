
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