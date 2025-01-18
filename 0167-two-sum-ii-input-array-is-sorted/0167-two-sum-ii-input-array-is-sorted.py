class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=len(numbers)-1

        while right>left:
            comp=numbers[left]+numbers[right]
            if comp>target:
                right-=1
            elif comp<target:
                left+=1
            else:
                return [left+1,right+1]
        