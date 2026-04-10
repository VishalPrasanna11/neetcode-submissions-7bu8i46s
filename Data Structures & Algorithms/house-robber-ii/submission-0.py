class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            prev1, prev2 = 0, 0  
            for num in nums:
                curr = max(num + prev2, prev1)  
                prev2 = prev1
                prev1 = curr
            return prev1

        n = len(nums)
        if n == 0:
            return
        if n == 1:
            return nums[0]  
        return max(helper(nums[1:]), helper(nums[:-1]))
