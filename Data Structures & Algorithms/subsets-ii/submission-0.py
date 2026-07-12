class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def helper(idx, currSet):
            result.append(currSet[:])

            seen = set()
            for i in range(idx, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                currSet.append(nums[i])
                helper(i+1, currSet)
                currSet.pop()

        helper(0, [])
        return result