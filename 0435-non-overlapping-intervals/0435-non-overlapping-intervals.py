class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])

        i,to_remove=0,0

        #print(intervals)
        for j in range(1,len(intervals)):
            if intervals[j][0]<intervals[i][1]:
                #print(intervals[j][0],intervals[i][1])
                to_remove+=1
                continue
            i=j
        
        return to_remove


        