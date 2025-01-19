class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        sor_nums=sorted(nums)
        target=0

        for i in range(len(sor_nums)-2):
            #print('number of iteration: ',i)
            if i>0 and sor_nums[i]==sor_nums[i-1]:
                continue
            else:
                residual_sum=target-sor_nums[i]
                left=i+1
                right=len(nums)-1
                while right>left:
                    comp=sor_nums[left]+sor_nums[right]
                    if comp>residual_sum:
                        right-=1
                    elif comp<residual_sum:
                        left+=1
                    else:
                        if [sor_nums[i],sor_nums[left],sor_nums[right]] not in res:
                            res.append([sor_nums[i],sor_nums[left],sor_nums[right]])
                        right-=1
                    #print('value of res:',res)
        return res



        
        