import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sub_l=[x for x in nums[:k]]
        heapq.heapify(sub_l)
        # print(sub_l)

        for i in nums[k:]:
            if i>sub_l[0]:
                val=heapq.heappop(sub_l)
                heapq.heappush(sub_l,i)
                # print("Inside Loop: ",sub_l)
        
        return sub_l[0]
        
        