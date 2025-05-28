class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        for i in range(len(intervals)):
            for j in range(len(intervals)-i-1):
                if intervals[j][0]>intervals[j+1][0]:
                    intervals[j],intervals[j+1]=intervals[j+1],intervals[j]
        
        # print(intervals)
        for k in range(len(intervals)-1):
            if intervals[k][1]>intervals[k+1][0]:
                return False
        

        return True
                
        