class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixSum = [1]*len(nums)

        left_prefix = 1

        for i in range(n):
            prefixSum[i] = left_prefix
            left_prefix *= nums[i]

        right_prefix = 1

        for i in range(n-1, -1, -1):
            prefixSum[i] *=right_prefix
            right_prefix *= nums[i]


        return prefixSum