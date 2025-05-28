class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        s_t=sorted([x[0] for x in intervals])
        e_t=sorted([y[1] for y in intervals])

        cnt,res=0,0 
        i,j=0,0

        while i<len(s_t):
            if s_t[i]<e_t[j]:
                cnt+=1
                i+=1
            else:
                j+=1
                cnt-=1
            
            res=max(res,cnt)
            # print(cnt,i,j,res)
        
        return res


        


        