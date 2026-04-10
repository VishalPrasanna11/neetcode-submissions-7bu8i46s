class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total%2 != 0:
            return False
        
        target = total//2

        def dfs(index,curr_sum):
            if curr_sum == target:
                return True
            if (index >= len(nums)) or curr_sum > target:
                return False
            
            return dfs(index+1, curr_sum + nums[index]) or dfs(index+1, curr_sum)


        return dfs(0,0)