# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        counter=5
        array_length=counter

        #finding the length of the array
        while reader.get(counter) <= target:
            counter+=5
            array_length=counter

        #initializing the pointers
        left,right=0,array_length

        

        while left <= right:
            
            #tracking the middle
            middle=(left+right)//2
            
            #checking the conditions over middle
            if reader.get(middle)==target:
                return middle
            elif reader.get(middle) < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1
        


        