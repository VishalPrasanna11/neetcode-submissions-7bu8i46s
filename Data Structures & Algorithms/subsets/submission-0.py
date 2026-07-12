class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(idx, currSet):
            result.append(currSet[:])

            for i in range(idx, len(nums)):
                currSet.append(nums[i])
                helper(i+1, currSet[:])
                currSet.pop()

        helper(0,[])
        return result