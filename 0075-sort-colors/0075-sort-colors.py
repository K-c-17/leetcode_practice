class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=defaultdict(int)
        
        for i in nums:
            count[i]+=1
        
        start,end=0,0
        for j in [0,1,2]:
            end+=count[j]
            nums[start:end]=[j]*count[j]
            start=end
            print(nums)
        
        '''
        nums[0:count[0]]=[0]*count[0]
        nums[count[0]:count[0]+count[1]]=[1]*count[1]
        nums[count[0]+count[1]:count[0]+count[1]+count[2]]=[2]*count[2]
        '''







        #Complexity= O(N**2)
        '''
        for i in range(1,len(nums)):
            curr=nums[i]
            j=i-1
            while j>=0 and nums[j]>curr:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=curr
        '''
        


        
