class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]
        n = len(nums)

        for num in nums[1:]:
            currSum = max(num,currSum+num)
            if currSum> maxSum : maxSum = currSum

        return maxSum