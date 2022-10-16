class Solution:
    def decodeString(self, s: str) -> str:
              #so we are going to use a stack..the idea is to keep on adding this char to the stack if value is ot "]"..moment we see a "]" we don add to stack..but we pop the values in the stack till we see a "["..notice the while loop stops when it sees "["...so "[" is still in it...we pop the last value from the stack which is "[" we don't need it...
        #then we use a while lop to pop the integers after "["..so we check which last value in stack is an integer we pop in..so we could have 132 as the number to multiply..so once it sees an alphabet it stops..
        #we then multiply this number and the popped character..num*poppedChar..so 3*"a" becomes "aaa"..always put the number before the character and endeavour to convert number to int() before multiplying
        #we then add this multiplied string back into the stack...
        #this process is repeated until the whole given string is completed ..by then al the "[" and "]" will be gone
        
        # we then convert the stack back to string as our result...."".join(stack)
        stack=[]
        for i in range(len(s)):
            #add until we see a "]"
            if s[i] != "]":
                stack.append(s[i])
            else:
                res=''
                #check if last value is not "["
                while stack[-1] != "[":
                    #add to the front because we are popping from the back
                    res = stack.pop() + res
                #last "[" is still there i.e example  ["r","t","[" ]. so we remove it becomes ["r","t"]
                stack.pop()
                
                #now we need to get the multiplier integer
                k=""
                while stack and stack[-1].isnumeric():
                    k = stack.pop() + k
                
                #we add the multiplied string back to the stack..in case of nested []..e.g 5[a[3b]]
                stack.append(int(k) * res)
                print(stack)
            
        return "".join(stack)