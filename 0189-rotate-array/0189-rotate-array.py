class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #O(n) time complexity

        def reverse_arr(arr,start,last):
            while start<last:
                nums[start],nums[last]=nums[last],nums[start]
                start+=1
                last-=1
            return arr
        
        size=len(nums)
        k=k%size

        #reverse the entire array
        reverse_arr(nums,0,size-1)
        #reverse the first k elements
        reverse_arr(nums,0,k-1)
        #reverse the last len(nums)-k elements
        reverse_arr(nums,k,size-1)

        return nums

       
        
        #O(n*k) time complexity
        '''
        for _ in range(k):
            temp=nums[0]
            for i in range(1,len(nums)):
                temp2=nums[i]
                nums[i]=temp
                temp=temp2
                if i==len(nums)-1:
                    nums[0]=temp

        return nums
        '''        
        
        #O(N) space complexity
        '''
        final=[None for _ in nums]
        size=len(nums)
        for r in range(size):
            idx=(r+k)%len(nums)
            final[idx]=nums[r]
        nums[:]=final
        
        return nums
        '''