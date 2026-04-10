class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        prev1 , prev2 = 0,0

        for i in range(n-1,-1,-1):
            curr = max(nums[i]+prev2,prev1)
            prev2 = prev1
            prev1 = curr
        
        return prev1