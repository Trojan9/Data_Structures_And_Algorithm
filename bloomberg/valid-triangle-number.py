class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        #we know in triangle , the sum of any two sides must be greater than the 3rd side
        # a+b > c....a+c>b or c+b>a..
        
        #brute force solution..o(n^3)
        #don't use for iterview oo
        res=0
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                for z in range(y+1,len(nums)):
                    if nums[x]+nums[y]>nums[z] and nums[x]+nums[z]>nums[y] and nums[z]+nums[y]>nums[x]:
                        res+=1
        return res
#better explanation
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        #so triangle rule a+b>c or a+c>b or b+c>a
        #we will use moving pointer method, with 3 pointers
        #----------------------------------------->#
        #|b                              |c      |a<- iterate backwards till index 1
        #->initially b=0, for every (a)   |
        #->move to right when b+c < a     |
        #                                 v
        #                                 move this to left when b+c>a for every iteration of a

        #so we start from the right, for each movement of a, b is initialized to 0 and c to a-1(b=0, c=a-1)
        #so while b<c, we will continually move c to the left between b and a
        #moving c to the left, we will calc b+c>a, if yes move c to the left, if No, move b to the right(forward)

        #firstly sort it , like in a pointer plot..smallest to biggest

        nums.sort()
        res=0
        for a in range(len(nums)-1,1,-1):
            b=0
            c=a-1
            while b<c:
                if nums[b]+nums[c]>nums[a]:
                    res+=c-b #just the formular to calc possible permutations of the b,c,a, i.e triangle
                    c-=1
                else:
                    b+=1
        return res

      
#same as above, this is old exolanation, i explained it better above

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        #we know in triangle , the sum of any two sides must be greater than the 3rd side
        # a+b > c....a+c>b or c+b>a..
        
        #better solution
        # watch this video youtube.com/watch?v=WSWo3ygceb4  to understand a bit
        #so first we need to sort the array..so the smallest possible value will be at index 0
        nums.sort()   #nlogn    
        #so now we will iterate from the back in
        #a will be our last index
        #b will be our 0 index
        #then c will start at index of a-1 then we keep on shiftig to the left i.e c-=1,while b < c, till num[b]+num[c] is not greater than num[a]..we only check this because we know num[a] is the largest so if it satisfy this condition it will satisfy for the other sides
        #so if num[b]+num[c] not > num[a] we will shift b to the right i.e b+=1
        res=0
        #start from len(nums)-1 to index 1 move in -1 stepsize
        for a in range(len(nums)-1,1,-1):
            b=0
            #so we start at a-1 and keep on shifting to the left,while b>c
            c=a-1
            while b<c:
                if nums[b]+nums[c]>nums[a]:
                    #this adds the number of possible triangles..its a formular..crame it
                    res+=c-b
                    #don't shift c before you calculate res oo..remember..don't fuck things up future self
                    c-=1
                else:
                    #its less than value at a..move b pointer to the right
                    b+=1
        return res
