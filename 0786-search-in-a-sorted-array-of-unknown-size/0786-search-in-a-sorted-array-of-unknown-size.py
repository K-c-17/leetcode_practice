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

        start=0
        end=1

        #finding the length of the array
        while reader.get(end) < target:
            print(start,end)
            start=end + 1
            end= end * 2

        #initializing the pointers
        left,right=start,end
        print(left,right)

        
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
        


        