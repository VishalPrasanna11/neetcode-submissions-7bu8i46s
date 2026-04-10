class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
       
    #write code here
    #the integers in the candidates array are all non negative  
        res = []
    
        def helper(start,curSet,curSum):
            if curSum == target:
                res.append(curSet[:])
                return
        
            if curSum > target:
                return
        
            for j in range(start,len(nums)):
                curSet.append(nums[j])
                helper(j,curSet,curSum+nums[j])
                curSet.pop()
        
    
    
        helper(0,[],0)
        return res