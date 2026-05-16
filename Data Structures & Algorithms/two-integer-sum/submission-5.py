class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force approach 

        # O(n^2)
        # for i in range(len(nums)-1):
        #     for j in range(1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        hashMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[nums[i]] = i


