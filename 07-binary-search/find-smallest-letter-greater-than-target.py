class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        #same binary search
        l,r=0,len(letters)-1
        #if target is out of range return first element
        
        if target<letters[l] or target>=letters[r]:
            return letters[l]
        
        #if its within range
        #don't forget l<=r..here some point will meet l=0 and r=0 which will result in making l=1 after the algo..so consider that also
        
        while l<=r:
            #find middle term
            m=l+((r-l)//2)
            print("this is middle")
            print(m)
            if target<letters[m]:
                r=m-1
                print("this is r")
                print(r)
            else:
                l=m+1
                print("this is l")
                print(l)
        print("this is final l")
        print(l)
        return letters[l]
    
    
    #use example letters= ["c","f","j"]  and target= "d"
    #this is how the process will go
    
    #  this is middle
    #m= 1
    #since target is less than middle ,..this is r
    #r=m-1= 1-1 = 0
    #now l=0,r=0...this is middle
    #m=0
    #since target is greater than middle at 0.,,,this is l
    #l= m+1 = 0+1 = 1
    #since l greater than r ..loop ends...then this is final l
    #l= 1
    #which gives us "f"

            
        