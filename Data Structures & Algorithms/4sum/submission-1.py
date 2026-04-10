class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def helper(idx, currSet, currSum):

            if currSum == target and len(currSet) == 4:
                res.append(currSet[:])
                return
            
            if  len(currSet) > 4:
                return

            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue 

                currSet.append(nums[i])
                helper(i + 1, currSet, currSum+nums[i])
                currSet.pop()

        helper(0,[],0)
        return res