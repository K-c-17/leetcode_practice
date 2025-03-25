class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum=[0]*len(nums)
        right_sum=[0]*len(nums)

        prev=0
        for i in range(len(nums)):
            left_sum[i]=prev
            prev+=nums[i]
        
        prev=0
        for j in range(len(nums)-1,-1,-1):
            right_sum[j]=prev
            prev+=nums[j]
        
        # print(left_sum)
        # print(right_sum)
        for k in range(len(left_sum)):
            if left_sum[k]==right_sum[k]:
                return k
        return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        for i in range(len(nums)):
            if i==len(nums)-1:
                suffix=0
            else:
                suffix=sum(nums[i+1:])
            
            if i==0:
                prefix=0
            else:
                prefix=sum(nums[:i])
            
            if prefix==suffix:
                return i
        return -1
        '''
        