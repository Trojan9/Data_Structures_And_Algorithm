#brute force method

class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        #if the multiplication of row and column not equals to length of original array then its not possible to transform to 2D array
        if m*n != len(original):
            return []
        row=0
        result=[]
        #the rows will represent the length of array...since the number of rows represent the number of items in our list
        while row<m:
            print(row)
            #then we pop the number of column into a list since the colum determines the number of items in the tuple or inner list
            result.append([original.pop(0) for _ in range(n)])   
            row+=1
        return result
            
            

#another angle

#brute force method

class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        #if the multiplication of row and column not equals to length of original array then its not possible to transform to 2D array
        if m*n != len(original):
            return []
        arr=[]
        row=0
        for i in range(len(original)):
            arr.append(original[i])
            if len(arr)==n:
                original[row]=arr
                arr=[]
                row+=1
        return original[0:m]
        
            
            