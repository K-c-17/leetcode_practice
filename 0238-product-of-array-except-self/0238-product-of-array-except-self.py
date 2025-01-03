class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1] * n
        right = [1] * n
        result = [1] * n

        # Compute prefix product
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # Compute suffix product
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # Combine prefix and suffix products
        for i in range(n):
            result[i] = left[i] * right[i]

        return result
        