class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(idx):

            if idx == len(nums):
                result.append(nums[:])
            
            for j in range(idx, len(nums)):
                nums[j], nums[idx] = nums[idx], nums[j]
                helper(idx + 1)
                nums[j], nums[idx] = nums[idx], nums[j]

        helper(0)
        return result