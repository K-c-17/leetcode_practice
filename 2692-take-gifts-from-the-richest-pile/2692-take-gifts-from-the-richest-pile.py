class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        nums=[-s for s in gifts]
        heapq.heapify(nums)

        while k>0:
            max_val=-1*heapq.heappop(nums)
            var_t=int(math.floor(max_val**0.5))
            heapq.heappush(nums,-1*var_t)
            k-=1
        
        return sum([-k for k in nums])

            
        