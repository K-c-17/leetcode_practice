class Solution(object):
    def twoSum(self, nums, target):
        res=[]
        for i in nums:
            rem=nums[:]
            rem.remove(i)
            if target-i in rem:
                res.extend([nums.index(i),rem.index(target-i)+1])
                break
            else:
                pass
        return res

        