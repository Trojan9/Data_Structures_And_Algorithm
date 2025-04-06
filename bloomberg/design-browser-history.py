
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"


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
            
##########################################################
######## solution 2 similar but just improvements

class BrowserHistory:

    def __init__(self, homepage: str):
        self.pointer = 1
        self.hashmap = {}
        self.hashmap[self.pointer] = homepage
        

    def visit(self, url: str) -> None:
        self.pointer +=1
        self.hashmap[self.pointer] = url

        if len(self.hashmap) > self.pointer:
            for i in range(self.pointer+1,len(self.hashmap)+1,1):
                del self.hashmap[i]
        

    def back(self, steps: int) -> str:
        if(self.pointer - steps) not in self.hashmap:
            self.pointer = 1
        else:
            self.pointer -=steps
        
        return self.hashmap[self.pointer]

        
    def forward(self, steps: int) -> str:
        if(self.pointer + steps) not in self.hashmap:
            self.pointer = len(self.hashmap)
        else:
            self.pointer +=steps

        return self.hashmap[self.pointer]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
            
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
