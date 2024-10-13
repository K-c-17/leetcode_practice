class Solution(object):

    def maximumCount(self, nums):
        if nums[-1] < 0 or nums[0] > 0:
            return len(nums)
        if nums[0] == 0 and nums[-1] == 0:
            return 0

        negative_count = 0
        positive_count = 0
        left, right = 0, len(nums) - 1

        # Find positive count
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > 0:
                right = mid - 1
                positive_count = mid
            else:
                left = mid + 1

        if positive_count != 0:
            positive_count = len(nums) - positive_count

        left, right = 0, len(nums) - 1

        # Find negative count
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
                negative_count = mid
            else:
                right = mid - 1

        if negative_count != 0:
            negative_count += 1

        return max(positive_count, negative_count)
        

