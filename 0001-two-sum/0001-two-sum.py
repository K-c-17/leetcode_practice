class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compCollector={}
        for i in range(len(nums)):
            if nums[i] not in compCollector:
                compCollector[target-nums[i]]=i
            else:
                return [compCollector[nums[i]],i]
                
        