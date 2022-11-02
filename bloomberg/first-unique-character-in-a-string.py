class Solution:
    def firstUniqChar(self, s: str) -> int:
        #so counter is just like hashMap
        
        countme=Counter(s)
        #just that it will map every lteeter it encounters to a number count
        #sorts it in respect to the count
        #Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1})
        #enumerate gets you both the index and value
        #note: index will come first
        for index,value in enumerate(s):
            if countme[value]==1:
                return index
        return -1
#so incase you were given the a testcase with capital letter and small letter "LeEtcode"...and asked to return the value instead of the index
#so we will change all to lowercase first...lower()...then use enumerate to get both index and value...then instead of returning the value from lowercase...we will return the value in s at the index