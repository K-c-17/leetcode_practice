class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum=[0]*len(nums)
        right_sum=[0]*len(nums)

        prev=0

        for i in range(len(nums)):
            prev+=nums[i]
            left_sum[i]=prev
        
        prev=0
        for j in range(len(nums)-1,-1,-1):
            right_sum[j]=prev
            prev+=nums[j]
        
        # print(left_sum)
        # print(right_sum)
        
        valid=0
        for k in range(len(left_sum)-1):
            if left_sum[k]>=right_sum[k]:
                valid+=1
        return valid


        