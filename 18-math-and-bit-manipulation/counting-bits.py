class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr=[0]
#we would use formular 1+bit of (x/2) for odd number and bit of (x/2) for even number
        
        for i in range(1,n+1):
            if i%2==0:
                arr.append(arr[int(i/2)])
            else:
                arr.append(1+arr[int(i/2)])
        return arr



#brute force solution

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr=[]
        for i in range(n+1):
            binary=bin(i).replace("0b", "")#converts to binary
            sumOne=0
            print(binary)
            for i in str(binary):
                if i=="1":
                    sumOne+=1
            arr.append(sumOne)
        return arr