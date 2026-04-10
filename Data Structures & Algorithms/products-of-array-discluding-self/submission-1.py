class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixSum = [1]*len(nums)

        left_prefix = 1

        for i in range(len(nums)):
            prefixSum[i] = left_prefix
            left_prefix *= nums[i]


        right_prefix = 1

        for i in range(len(nums)-1,-1,-1):
            prefixSum[i] *= right_prefix
            right_prefix *= nums[i]

        return prefixSum