class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        max_area=float("-inf")
        
        while left<right:
            length=right-left
            width=min(height[left],height[right])
            cal_area=length*width

            if cal_area>max_area:
                max_area=cal_area
            
            if height[right]<height[left]:
                right-=1
            else:
                left+=1

        return max_area


        