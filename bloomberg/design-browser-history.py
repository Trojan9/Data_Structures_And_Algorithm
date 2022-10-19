
class BrowserHistory:
    def __init__(self, homepage: str):
        #you know in browser we deal with tabs 
        #create an hashmap...mapping the tab number to the page
        self.history={}
        #so make the pointer start at 1
        self.pointer=1
        #initialize 1 to the homepage 
        self.history[self.pointer]=homepage
        

    def visit(self, url: str) -> None:
        #so when we visit and the pointer is < than the length of map..we delete all tabs after the current created pointer tab
        self.pointer+=1
        self.history[self.pointer]=url
        #delete all tabs after pointer
        if len(self.history)>self.pointer:
            #don't forget this range...stop not inclusive..so if you want to stop at len(history) make it len(history)+1
            for i in range(self.pointer+1,len(self.history)+1):
                del self.history[i]
        

    def back(self, steps: int) -> str:
        #if pointer minus step is < 1..then return the pointer at 1
        if((self.pointer -steps) not in self.history):
            self.pointer=1
    
            return self.history[self.pointer]
        #else return the value at pointer
        else:
            self.pointer -=steps
            return self.history[self.pointer]
        

    def forward(self, steps: int) -> str:
        #if pointer plus step is > length of history
        #then we return the last value tab at len(history)
        if (self.pointer + steps)>=len(self.history):
            self.pointer=len(self.history)
            return self.history[self.pointer]
        #else return the value at pointer
        else:
            self.pointer +=steps
            return self.history[self.pointer]
            


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)