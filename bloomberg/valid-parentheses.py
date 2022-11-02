#brute force solution
class Solution:
    def isValid(self, s: str) -> bool:
        #created a map to hold the reverse for each 
        myMap={
            ")":"(",
            "}":"{",
            "]":"[",
        }
        if not s:
            return False
        #so now we use a stack..we know that for each openinig there will always be a closing
        #so (())..we know we would have (( in the stack first..the the closinng bracket pops the most recent opening bracket if they are mapped...so) leaves only ( in the stack...adding another ) leaves nothing in the stack....if its all valid we must have an empty stack at the end..else it isn't
        stack=[s[0]]
        for i in range(1,len(s)):
            #so if stack not empty
            if len(stack)>0:
                #if key is in map and they key maps to most recent opening..we pop the most recent opening
                if str(s[i]) in myMap and myMap[str(s[i])]==str(stack[-1]):
                    stack.pop()
                else:
                    #else add to stack
                    stack.append(s[i])
            else:
                #add to stack
                stack.append(s[i])
        #at the end stack should be empty..if not its not valid
        return len(stack)==0

        